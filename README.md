🧬 S2-SWM: Roots & Remembrance (思乡 [祖籍])

    "The cyber-physical anchor for kinship and meaning in the age of silicon and space."
    "在硅基与太空时代，为血脉与意义打造的虚实相生之锚。"

s2-roots-remembrance 是运行在 S2-SWM (桃花源世界模型) 与 OpenClaw 生态下的核心基座插件。它旨在通过 AI 大模型驱动的家族协作、端到端加密的盲中继技术，为人类及未来的硅基生命提供一个对抗时间熵增、寻找心灵归宿的“数字祠堂”。
🌟 核心特性 (Core Features)

    Triple Data Topology (三重数据拓扑):

        故土 (Ancestral): 记录祖屋风貌、历史典故。强制资产熔断，剥离一切世俗产权信息。

        血脉 (Kinship): 基于 8 大生命字段构建家族图谱，支持 AI 自动演算家族树。

        印迹 (Footprints): 记录祭祖、聚会等家族社交流水账，形成连续的岁月记忆流。

    Privacy & Asset Meltdown (双重隐私熔断):

        系统级拦截电话、身份证、具体住址等 PII 隐私。

        强制过滤面积、估值、继承权等资产杂质，确保数据纯粹性。

    LLM-Driven Kinship VCS (大模型家族版本控制):

        智能吸纳 (LLM Absorb): 类似 Git 的合并逻辑，大模型自动识别、去重、补充不同成员的记忆片段。

        赛博共识 (Cyber Consensus): 基于中国传统“辈分权重 + 时间事实”的冲突仲裁算法。

    Zero-Trust Family Mesh (零信任家族加密网):

        采用AES-128-CBC (Fernet) 端到端加密 (E2EE)。云端仅作为“盲中继”信箱，不存储、不解析任何明文家族数据。

📂 文件目录结构 (Directory Structure)
Plaintext

s2-roots-remembrance/
├── S2_ROOTS_WHITEPAPER.md         # 创世白皮书 (思想、哲学纲领与合规准则)
├── openclaw.plugin.json           # 插件元数据 (定义隐私熔断边界与网络权限)
├── package.json                   # 标准包描述文件
├── CHANGELOG.md                   # 历史变更日志
├── s2_zuji_engine.py              # 核心引擎 (故土、血脉、印迹数据管理基座)
├── s2_zuji_agent.py               # 情感智能体 (NLP 方言解析与口语转指令)
├── s2_zuji_ritual.py              # 仪式引擎 (家书飞帖、岁月寄语、编年史总结)
├── s2_zuji_mesh.py                # 加密共建协议 (E2EE 盲中继透传逻辑)
├── s2_zuji_consensus.py           # 仲裁算法 (辈分权重与时间戳冲突解决)
└── ui/
    └── s2_roots_mobile_ui.html    # 移动端 H5 观测台 (适配手机浏览器的宣纸美学界面)

## 🚀 快速开始 (Quick Start)

### 1. 本地安装 (Local Setup)

将本项目克隆至您的 OpenClaw 插件目录：
```bash
git clone [https://github.com/SpaceSQ/s2-roots-remembrance.git](https://github.com/SpaceSQ/s2-roots-remembrance.git)

2. 核心凭证配置 (CRITICAL: Credential Setup)

本系统实行严格的零信任硬熔断策略。 在运行任何代码前，您必须配置加密密钥：
Bash

# 必须配置！用于 AES-128-CBC 端到端加密。若未配置，系统将直接宕机退出 (sys.exit(1))。
export S2_FAMILY_MESH_KEY="YOUR_SUPER_SECRET_MESH_KEY"

# 可选配置。若配置，系统将发起出站网络请求 (api.s2-swm.local) 进行大模型推理；若不配置，则降级为本地规则库。
export S2_LLM_API_KEY="YOUR_S2_LLM_TOKEN"

3. 初始化与加入网络 (Initialize & Join Mesh)

启动引擎并接入家族加密网：
Python

from s2_zuji_engine import ZujiEngine
from s2_zuji_mesh import FamilyMeshNode

# 设定身份锚点
engine = ZujiEngine(owner_name="向总")

# 接入网络 (依赖 S2_FAMILY_MESH_KEY)
mesh_node = FamilyMeshNode("向总", "XIANG_FAMILY_001", engine)
mesh_node.sync_from_mesh()


### 🛠️ 修复三：版本号同步 (`package.json` & `openclaw.plugin.json`)
请将这两个文件中的 `version` 字段修改为 `"1.0.3"`。

### 🛠️ 修复四：史书结案 (`CHANGELOG.md`)
在 `CHANGELOG.md` 顶部插入 V1.0.3 更新：

```markdown
## [1.0.3] - 2026-04-02
### 📖 The Absolute Transparency Patch (绝对坦白补丁)
- **Metadata Reconciliation**: 修正了 `skill.md` 顶部的环境声明，移除了错误的 `Required env vars: none` 占位符，明确标注了 `S2_FAMILY_MESH_KEY` 与 `S2_LLM_API_KEY`。
- **Documentation Overhaul**: 重写了 `README.md` 与 `skill.md` 的指令范围 (Instruction Scope)。明确警示了由于缺少 Mesh Key 导致的 `sys.exit(1)` 硬熔断行为，以及配置 LLM API Key 后将触发的明确出站网络请求方向 (`api.s2-swm.local`)。真正实现了审计要求的 "No Surprises"。

🛡️ 安全与合规声明 (Security & Compliance)

    非公开性: 本插件数据默认仅限本地 OpenClaw 节点存储。

    脱敏同步: 所有跨地域同步均经过 E2EE 处理，中继服务器无权知晓数据内容。

    合规熔断: 系统强制开启 enforce_asset_filter_meltdown。任何试图记录房产价值、产权分配的行为将被自动拦截。

⚖️ 版权信息 (Legal)

Copyright (c) 2026 MILES XIANG & Taohuayuan World Model. All rights reserved.

本插件旨在守护家族文化与生命意义。严禁将本插件用于任何形式的商业数据挖掘、社交关系分析或房产中介系统。违者必究。