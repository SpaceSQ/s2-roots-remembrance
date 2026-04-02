#!/usr/bin/env python3
import json
import base64
import hashlib
import logging
import os
import sys
from datetime import datetime
from cryptography.fernet import Fernet

logging.basicConfig(level=logging.INFO, format='%(message)s')

# =====================================================================
# 🔐 S2-SWM: 思乡[祖籍] 宗祠加密通讯协议 (TRUE Zero-Trust Mesh)
# 修复 V1.0.2：移除所有弱密钥兜底，强制实施硬熔断机制
# =====================================================================

class BlindRelayServer:
    def __init__(self):
        self.encrypted_mailboxes = {}

    def push_blob(self, family_id: str, encrypted_blob: bytes):
        if family_id not in self.encrypted_mailboxes:
            self.encrypted_mailboxes[family_id] = []
        self.encrypted_mailboxes[family_id].append(encrypted_blob)
        logging.info(f"☁️ [云端中继] 收到加密数据，大小: {len(encrypted_blob)} bytes。")

    def pull_blobs(self, family_id: str):
        blobs = self.encrypted_mailboxes.get(family_id, [])
        self.encrypted_mailboxes[family_id] = []
        return blobs

global_relay = BlindRelayServer()

class FamilyMeshNode:
    def __init__(self, member_name: str, family_id: str, local_engine):
        self.member_name = member_name
        self.family_id = family_id
        self.local_engine = local_engine
        
        # [核心安全修复] 强制读取环境变量，彻底移除 DEFAULT_SALT
        raw_secret = os.environ.get("S2_FAMILY_MESH_KEY")
        if not raw_secret:
            logging.error("FATAL: S2_FAMILY_MESH_KEY is missing. Zero-Trust policy prohibits default or derived weak keys. Aborting execution.")
            sys.exit(1)
            
        self._aes_key = base64.urlsafe_b64encode(hashlib.sha256(raw_secret.encode()).digest())
        self._cipher = Fernet(self._aes_key)

    def _encrypt(self, payload: dict) -> bytes:
        raw_str = json.dumps(payload, ensure_ascii=False)
        return self._cipher.encrypt(raw_str.encode('utf-8'))

    def _decrypt(self, encrypted_blob: bytes) -> dict:
        raw_str = self._cipher.decrypt(encrypted_blob).decode('utf-8')
        return json.loads(raw_str)

    def broadcast_update(self, update_type: str, data: dict):
        payload = {
            "sender": self.member_name,
            "timestamp": datetime.now().isoformat(),
            "type": update_type,
            "data": data
        }
        encrypted_blob = self._encrypt(payload)
        global_relay.push_blob(self.family_id, encrypted_blob)
        logging.info(f"📡 [{self.member_name}] 已通过 AES-128-CBC 加密推送至家族隧道。")

    def sync_from_mesh(self):
        blobs = global_relay.pull_blobs(self.family_id)
        if not blobs:
            return

        for blob in blobs:
            try:
                decrypted_payload = self._decrypt(blob)
                sender = decrypted_payload["sender"]
                update_type = decrypted_payload["type"]
                logging.info(f"🔓 [AES解密成功] 收到来自 '{sender}' 的更新: {update_type}")
            except Exception as e:
                logging.error(f"❌ [解密拦截] 数据包损坏或密钥不匹配！")