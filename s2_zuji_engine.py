#!/usr/bin/env python3
import json
import uuid
from datetime import datetime
import logging

logging.basicConfig(level=logging.INFO, format='%(message)s')

# =====================================================================
# 🌳 S2-SWM: 思乡[祖籍] 核心引擎 (Roots & Remembrance Engine)
# 作用：管理故土、血脉、印迹三重拓扑，执行隐私/资产熔断，调度 LLM 吸纳
# =====================================================================

class PrivacyAssetEnclave:
    """[底层铁律] 资产与隐私双重熔断器"""
    
    ASSET_KEYWORDS = ["房产证", "面积", "平米", "市值", "购买价格", "继承权", "份额", "产权"]
    PII_KEYWORDS = ["电话", "手机号", "邮箱", "身份证", "微信", "职务", "薪水", "具体门牌号"]

    @classmethod
    def filter_assets(cls, text: str) -> str:
        """资产熔断：剥离世俗产权信息"""
        for kw in cls.ASSET_KEYWORDS:
            if kw in text:
                logging.warning(f"🛡️ [资产熔断触发] 拦截敏感词: {kw}。祖屋是精神图腾，禁止资产化记录。")
                text = text.replace(kw, "[已按思乡规约熔断过滤]")
        return text

    @classmethod
    def filter_pii(cls, text: str) -> str:
        """隐私熔断：剔除个人身份信息"""
        for kw in cls.PII_KEYWORDS:
            if kw in text:
                logging.warning(f"🛡️ [隐私熔断触发] 拦截敏感词: {kw}。为保障家族群分享安全，禁止记录隐私信息。")
                text = text.replace(kw, "[已按思乡规约脱敏]")
        return text

class ZujiEngine:
    def __init__(self, owner_name: str):
        self.owner = owner_name
        self.repo_version = f"{owner_name}-Zuji-v1.0"
        
        # 三重数据拓扑数据库
        self.db = {
            "Ancestral_Nodes": [],  # 故土基石
            "Kinship_Nodes": {},    # 血脉节点 (以姓名为 Key)
            "Footprint_Events": []  # 时空交集 (流水账)
        }
        logging.info(f"🏡 [{self.owner} 的思乡[祖籍]库] 空间锚点已初始化。")

    # ================= 1. 故土基石管理 =================
    def add_ancestral_node(self, location: str, architecture: str, history: str):
        """添加祖屋/旧居信息 (强制进行资产熔断)"""
        clean_arch = PrivacyAssetEnclave.filter_assets(architecture)
        clean_hist = PrivacyAssetEnclave.filter_assets(history)
        
        node = {
            "id": str(uuid.uuid4())[:8],
            "type": "Ancestral_Node",
            "location": location,
            "architecture": clean_arch,
            "history_story": clean_hist,
            "timestamp": datetime.now().isoformat()
        }
        self.db["Ancestral_Nodes"].append(node)
        logging.info(f"✅ [故土锚定] 成功记录旧居风貌: {location}")

    # ================= 2. 血脉节点管理 =================
    def add_kinship_node(self, name: str, title: str, location: str="", 
                         is_alive: bool=True, parents: list=None, 
                         siblings: list=None, children: list=None, notes: str=""):
        """添加家族成员 (8大标准字段，强制 1-姓名, 2-称呼)"""
        if not name or not title:
            raise ValueError("❌ [校验失败] '1-姓名' 与 '2-称呼' 为强制必填项，无法创建空灵节点。")
        
        clean_notes = PrivacyAssetEnclave.filter_pii(notes)
        
        node = {
            "1_name": name,
            "2_title": title,
            "3_location": location,
            "4_is_alive": is_alive,
            "5_parents": parents or [],
            "6_siblings": siblings or [],
            "7_children": children or [],
            "8_notes": clean_notes
        }
        self.db["Kinship_Nodes"][name] = node
        logging.info(f"🧬 [血脉连接] 成功录入族人: {title} ({name})")

    # ================= 3. 时空交集管理 =================
    def add_footprint_event(self, date: str, purpose: str, participants: list, description: str):
        """添加自然语言流水账日记"""
        node = {
            "date": date,
            "purpose": purpose,
            "participants": participants,
            "description": description
        }
        self.db["Footprint_Events"].append(node)
        logging.info(f"⏳ [岁月印迹] 新增家族事件: {purpose} ({date})")

    # ================= 4. 大模型家族版本控制 (Git for Kinship) =================
    def llm_absorb_branch(self, incoming_db: dict, provider_name: str):
        """[核心算法] 模拟 LLM 吸纳合并逻辑 (非机械覆盖)"""
        logging.info(f"\n🔄 [大模型吸纳启动] 正在解析 {provider_name} 分享的思乡副本...")
        
        # 模拟大模型比对血脉节点
        for name, incoming_node in incoming_db.get("Kinship_Nodes", {}).items():
            if name not in self.db["Kinship_Nodes"]:
                # 发现本地缺失的节点，直接吸纳
                self.db["Kinship_Nodes"][name] = incoming_node
                logging.info(f"  ↳ 🧠 [LLM 增补] 发现缺失血脉: {incoming_node['2_title']} ({name})，已合并入当前图谱。")
            else:
                # 模拟 LLM 智能融合字段 (例如补充子女信息)
                local_node = self.db["Kinship_Nodes"][name]
                new_children = set(incoming_node["7_children"]) - set(local_node["7_children"])
                if new_children:
                    local_node["7_children"].extend(list(new_children))
                    logging.info(f"  ↳ 🧠 [LLM 纠偏] 补充 {name} 的分支信息: 新增子女 {list(new_children)}")

        logging.info(f"✅ [吸纳完成] 版本升级为: {self.repo_version}_merged_with_{provider_name}\n")

    # ================= 5. 族谱推理引擎 =================
    def generate_kinship_dag(self):
        """基于 5 大关系字段生成家族树 (DAG) 结构"""
        logging.info("\n🌳 [家族树演算] AI 正在重构亲属网络有向无环图...")
        # 实际开发中，这里会调用 LLM 将字典转为 Graphviz 或 D3.js JSON 结构
        # 此处仅作引擎侧的概念输出
        for name, data in self.db["Kinship_Nodes"].items():
            parent_str = ", ".join(data["5_parents"]) if data["5_parents"] else "上溯未知"
            children_str = ", ".join(data["7_children"]) if data["7_children"] else "暂无"
            print(f"  {parent_str} ━━> [ {data['2_title']}: {name} ] ━━> {children_str}")
        print("🌳 [演算完成] 随时可依据自然语言指令回滚或调优。\n")

# =====================================================================
# 🚀 场景演练：两代人的记忆合流
# =====================================================================
if __name__ == "__main__":
    print("="*60)
    print("🏮 S2 思乡[祖籍] 引擎测试台")
    print("="*60 + "\n")

    # 1. 初始化个人的思乡库
    my_engine = ZujiEngine(owner_name="我自己")

    # 2. 录入故土基石 (触发资产熔断拦截测试)
    my_engine.add_ancestral_node(
        location="湖南桃源",
        architecture="青砖黛瓦的湘西北传统老屋，木雕窗棂上刻着岁寒三友，院子里有口老井。当年爷爷买下它的购买价格是300大洋，现在面积大约150平米。",
        history_story="老屋见证了家族百年的兴衰。"
    )

    # 3. 录入自己所知的血脉信息 (触发隐私熔断拦截测试)
    my_engine.add_kinship_node(
        name="向建国", title="大伯", location="深圳",
        children=["向阳"],
        notes="脾气倔强，做的一手好腊肉。他的微信号是 XiangJG_1955，联系电话 13800138000。"
    )
    my_engine.add_kinship_node(
        name="向阳", title="堂哥", location="北京", parents=["向建国"]
    )

    # 4. 录入时空交集 (日记)
    my_engine.add_footprint_event(
        date="2026-02-17", purpose="春节祭祖", participants=["我自己", "向建国", "向阳"],
        description="大雪天，全家在青砖老屋前围炉夜话，大伯讲了老井的故事。"
    )

    # --- 模拟：收到堂哥分享的思乡库 ---
    cousin_db_mock = {
        "Kinship_Nodes": {
            "向建国": {"2_title": "父亲", "7_children": ["向阳", "向雪"]}, # 堂哥知道得更全，多了一个女儿向雪
            "向建军": {"2_title": "二叔", "3_location": "长沙"} # 堂哥记录了二叔，我本地没有
        }
    }

    # 5. 启动大模型吸纳 (LLM Absorb)
    my_engine.llm_absorb_branch(incoming_db=cousin_db_mock, provider_name="向阳堂哥")

    # 6. 推演族谱
    my_engine.generate_kinship_dag()
    
    # 查看脱敏后的底层数据
    print("👀 [底层数据核查] 最终安全落盘的向建国备注：")
    print(f"   {my_engine.db['Kinship_Nodes']['向建国']['8_notes']}")