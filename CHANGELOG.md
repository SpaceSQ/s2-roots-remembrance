# Changelog - Roots & Remembrance (思乡[祖籍])

All notable changes to this project will be documented in this file.

## [1.0.4] - 2026-04-02
### 📦 The Final Sealing Patch (终极封焊补丁)
- **Dependency Pipeline**: 新增 `requirements.txt` 并声明了 `cryptography>=41.0.0` 依赖。在 `package.json` 中注入了 `"install": "pip install -r requirements.txt"` 生命周期脚本，消除了缺失依赖导致的静默运行失败风险。
- **Registry Alignment**: 新增最高级注册表清单 `skill.json`，在顶层元数据彻底抹除 "Required env vars: none" 的错误宣告，强制向生态平台声明 `S2_FAMILY_MESH_KEY` 与 `S2_LLM_API_KEY`，实现从底层代码到外层商店的 100% 声明一致性。

## [1.0.3] - 2026-04-02
### 🛡️ The Cryptographic Truth Patch (真理与硬核补丁)
- **Hard-Exit Enforcement**: 彻底移除了 `s2_zuji_mesh.py` 中的 `DEFAULT_SALT` 弱密钥派生后门。若环境未提供 `S2_FAMILY_MESH_KEY`，系统将直接触发 `sys.exit(1)` 硬熔断，拒绝不安全的降级运行。
- **Cryptographic Honesty**: 修正了 `README.md` 与文档中的加密强度声明，将 "AES-256" 更正为实际底层的 "AES-128-CBC (Fernet)"，消除安全声明误导。
- **Metadata Alignment**: 在 `package.json` 的顶层扩展中显式声明了 `secrets` 数组，消除了平台注册表与插件清单之间的环境变量声明断层。

## [1.0.1] - 2026-04-02
### 🚀 Genesis Launch (创世发布)
- **Triple Data Topology (三重数据拓扑)**: 
  - `Ancestral Nodes` (故土基石): 记录祖屋风貌、历史典故与岁月影像。
  - `Kinship Nodes` (血脉节点): 基于 8 大标准字段构建家族成员画像。
  - `Footprint Events` (时空交集): 记录探亲、祭祖等家族社交流水账。
- **Privacy Meltdown Enclave (双重隐私熔断器)**:
  - System-level asset blocking: 强制拦截面积、估值、产权等世俗资产杂质。
  - System-level PII blocking: 强制脱敏电话、身份证、社交账号等个人隐私。
- **LLM-Driven Kinship Agent (情感解析智能体)**: 
  - Added `s2_zuji_agent.py` to parse natural language, dialects, and emotional expressions into structured database operations silently.
- **Ritual & Emotion Engine (仪式与共鸣引擎)**:
  - Added `s2_zuji_ritual.py` supporting Ancestral Call (家书飞帖), Time Echoes (跨越生死的岁华寄语), and Chronicle Refiner (岁月成碑总结).
- **Zero-Trust Family Mesh (零信任宗祠加密网)**:
  - Added `s2_zuji_mesh.py` for End-to-End Encrypted (E2EE) blind relay. Cloud servers act only as encrypted mailboxes.
- **Cyber-Genealogy Consensus (赛博族谱共识算法)**:
  - Added `s2_zuji_consensus.py` to resolve sync conflicts using a 3-tier strategy: Generation Rank (辈分权重), Timestamp (时间事实), and LLM Sympathy Merge (情感多重视角叠加).
- **Hologram & Web UI (观测前端)**: 
  - Released `s2_roots_mobile_ui.html` featuring a traditional Chinese aesthetic (宣纸与青砖) for cross-generational mobile access.