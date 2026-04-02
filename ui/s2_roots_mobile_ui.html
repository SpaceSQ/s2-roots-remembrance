#!/usr/bin/env python3
import logging
from datetime import datetime

logging.basicConfig(level=logging.INFO, format='%(message)s')

# =====================================================================
# ⚖️ S2-SWM: 思乡[祖籍] 赛博族谱共识算法 (Kinship Consensus Engine)
# 作用：在端到端加密共建时，处理不同成员带来的记忆与事实冲突
# =====================================================================

class KinshipConsensus:
    def __init__(self):
        # 辈分权重字典 (数字越小，解释权越高)
        self.GENERATION_RANKS = {
            "曾祖": 1, "祖父": 2, "祖母": 2, "太爷爷": 2,
            "伯父": 3, "大伯": 3, "叔叔": 3, "姑姑": 3, "父亲": 3, "母亲": 3,
            "哥哥": 4, "姐姐": 4, "自己": 4, "堂哥": 4,
            "侄子": 5, "外甥": 5, "儿子": 5, "女儿": 5,
            "孙子": 6, "孙女": 6
        }

    def _get_rank(self, title: str) -> int:
        """解析称谓，获取该成员在家族中的辈分权重"""
        for key, rank in self.GENERATION_RANKS.items():
            if key in title:
                return rank
        return 99  # 未知辈分，权重最低

    def resolve_kinship_conflict(self, local_node: dict, incoming_node: dict, 
                                 local_author_title: str, incoming_author_title: str) -> dict:
        """
        [核心仲裁] 解决同一个血脉节点在同步时的字段冲突
        """
        merged_node = local_node.copy()
        
        local_rank = self._get_rank(local_author_title)
        incoming_rank = self._get_rank(incoming_author_title)
        
        logging.info(f"⚖️ [仲裁启动] 本地作者权重: {local_rank}({local_author_title}) | 远端作者权重: {incoming_rank}({incoming_author_title})")

        # 1. 血脉关系维度：辈分高者赢 (Generation Wins)
        # 例如：父母、兄妹、子女名单冲突
        if incoming_rank < local_rank:
            merged_node["5_parents"] = incoming_node.get("5_parents", merged_node["5_parents"])
            merged_node["6_siblings"] = incoming_node.get("6_siblings", merged_node["6_siblings"])
            logging.info("   ↳ 📜 [血脉仲裁] 远端辈分更高，已采纳长辈提供的血脉图谱修正。")

        # 2. 事实状态维度：时间戳赢 (Timestamp Wins)
        # 简化处理：假设 incoming 永远代表最新发生的网络同步事实
        if incoming_node.get("4_is_alive") != local_node.get("4_is_alive"):
            merged_node["4_is_alive"] = incoming_node.get("4_is_alive")
            logging.info("   ↳ ⏳ [事实仲裁] 生死状态发生变更，已采纳最新时间线事实。")
            
        if incoming_node.get("3_location") != local_node.get("3_location"):
            merged_node["3_location"] = incoming_node.get("3_location")

        # 3. 情感回忆维度：大模型共情合流 (Sympathy Merge)
        local_notes = local_node.get("8_notes", "")
        incoming_notes = incoming_node.get("8_notes", "")
        
        if incoming_notes and incoming_notes not in local_notes:
            # 不抹除年轻人的记忆，而是追加为多维视角
            merged_node["8_notes"] = f"{local_notes}\n[记忆拼图·来自{incoming_author_title}]: {incoming_notes}"
            logging.info("   ↳ 🧠 [共情合流] 主观情感不设对错，已将两代人的记忆叠合保存。")

        return merged_node

# =====================================================================
# 🚀 场景演练：两代人的记忆冲突仲裁
# =====================================================================
if __name__ == "__main__":
    arbitrator = KinshipConsensus()

    # 假设本地数据库是“向阳(堂哥)”维护的
    local_data = {
        "1_name": "向建军", "2_title": "二伯", "4_is_alive": True,
        "5_parents": ["向老太爷"], "8_notes": "二伯喜欢抽烟袋。"
    }

    # 假设网络同步传来了“向建国(大伯)”修改的版本
    incoming_data = {
        "1_name": "向建军", "2_title": "二弟", "4_is_alive": False,
        "5_parents": ["向老太爷", "李老太"], # 大伯补充了母亲的名字
        "8_notes": "建军这辈子不容易，走的时候没受罪。"
    }

    # 执行仲裁 (本地作者: 堂哥，远端作者: 大伯)
    resolved_data = arbitrator.resolve_kinship_conflict(
        local_node=local_data, 
        incoming_node=incoming_data, 
        local_author_title="堂哥", 
        incoming_author_title="大伯"
    )

    print("\n" + "="*50)
    print("✨ [仲裁最终落盘结果]:")
    for k, v in resolved_data.items():
        print(f"  {k}: {v}")
    print("="*50)