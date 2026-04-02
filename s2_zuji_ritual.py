#!/usr/bin/env python3
import json
import logging
from datetime import datetime

logging.basicConfig(level=logging.INFO, format='%(message)s')

# =====================================================================
# 🏮 S2-SWM: 思乡[祖籍] 仪式与情感共鸣引擎 (Ritual & Emotion Engine)
# 作用：处理家书起草、跨越生死的岁华寄语、以及家族大事件的史诗级总结
# =====================================================================

class RitualEngine:
    def __init__(self, db_engine):
        self.db_engine = db_engine  # 传入底层的 ZujiEngine

    # ---------------------------------------------------------
    # 交互 1：家书飞帖 (生成充满共情的仪式通知)
    # ---------------------------------------------------------
    def craft_ancestral_call(self, event_type: str, date: str, initiator_name: str, core_message: str):
        """基于大模型，将干瘪的指令转化为充满底蕴的家族飞帖"""
        logging.info(f"📜 [家书起草中...] 正在为大事件 '{event_type}' 研墨撰文...")
        
        # 提取发起人辈分与故土信息
        kinship_db = self.db_engine.db.get("Kinship_Nodes", {})
        ancestral_db = self.db_engine.db.get("Ancestral_Nodes", [])
        
        hometown = ancestral_db[0]["location"] if ancestral_db else "老家"
        initiator = kinship_db.get(initiator_name, {"2_title": initiator_name})
        
        # [模拟 LLM 生成] 结合中国时令与家族文化的文本生成
        draft = ""
        if "清明" in event_type or "祭祖" in event_type:
            draft = (f"【家书飞帖：清明集结号】\n"
                     f"草木蔓发，春山可望。又是一年清明将至。\n"
                     f"咱们 {hometown} 的老树应该又发了新枝。经 {initiator['2_title']} ({initiator_name}) 提议：\n"
                     f"暂定于 {date}，家族同辈尽量拨冗回乡。不拘礼数，只为在祖屋老井旁聚一聚，\n"
                     f"给先人们扫扫墓，拢一拢咱们血脉的火种。\n"
                     f"附言：{core_message}")
        elif "春节" in event_type or "过年" in event_type:
            draft = (f"【家书飞帖：岁首团圆】\n"
                     f"爆竹声中一岁除。无论今年在外漂泊多远，风雨多大，\n"
                     f"{initiator['2_title']} ({initiator_name}) 喊大家 {date} 回 {hometown} 围炉吃顿热乎饭！\n"
                     f"附言：{core_message}")
            
        print("\n" + "="*40 + "\n" + draft + "\n" + "="*40)
        return draft

    # ---------------------------------------------------------
    # 交互 2：岁华寄语 (跨越生死的数字倾诉)
    # ---------------------------------------------------------
    def send_time_echo(self, sender: str, target_name: str, message: str):
        """向特定家族节点发送情感寄语 (生者为祝福，逝者为祭奠)"""
        kinship_db = self.db_engine.db.get("Kinship_Nodes", {})
        if target_name not in kinship_db:
            logging.error(f"❌ 未找到族人：{target_name}")
            return
            
        target_node = kinship_db[target_name]
        is_alive = target_node.get("4_is_alive", True)
        title = target_node.get("2_title", "")
        
        echo_record = {
            "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M"),
            "sender": sender,
            "message": message,
            "type": "blessing" if is_alive else "memorial"
        }
        
        # 将寄语静默附加到备注/隐藏的时间轴字段中
        current_notes = target_node.get("8_notes", "")
        prefix = "💌 [岁华寄语]" if is_alive else "🕯️ [跨时空祭奠]"
        target_node["8_notes"] = current_notes + f"\n{prefix} {echo_record['timestamp']} 来自 {sender}: '{message}'"
        
        if not is_alive:
            logging.info(f"🕯️ [星空回响] 已将您的思念化作数字星光，刻入 {title} ({target_name}) 的生命节点。")
        else:
            logging.info(f"💌 [岁月传书] 寄语已妥善保存至 {title} ({target_name}) 的家族档案中。")

    # ---------------------------------------------------------
    # 交互 3：岁月成碑 (将杂乱的流水账提炼为家族史诗)
    # ---------------------------------------------------------
    def summarize_ritual_chronicle(self, event_title: str, raw_footprints: list):
        """[核心算法] 大模型提炼零散的记录，生成有温度的编年史总结"""
        logging.info(f"\n📚 [岁月成碑] AI 正在将 {len(raw_footprints)} 条零散日记熔炼为《{event_title}》...")
        
        # [模拟 LLM 归纳总结]
        # 实际逻辑：提取所有参与人、关键事件（修族谱、大扫除、聚餐）、情感走向
        participants = set()
        for f in raw_footprints:
            participants.update(f.get("participants", []))
            
        chronicle = (
            f"《家族编年史：{event_title}》\n"
            f"【参与血脉】: {', '.join(participants)}\n"
            f"【史记正文】:\n"
            f"  是日也，天朗气清。家族老少同聚故土。众人齐心修缮了院落，席间谈及往事，笑语晏晏。\n"
            f"  大伯提及了先人创业之艰辛，晚辈们亦汇报了各自在外之成绩。虽有岁月更迭，但血脉之情，\n"
            f"  如老屋前的那口古井，源远流长，生生不息。\n"
            f"【数字封存】: 包含 12 张合影，3 段视频，已作为底层印迹永久加密固化。"
        )
        print("\n" + "*"*50 + "\n" + chronicle + "\n" + "*"*50 + "\n")
        return chronicle

# =====================================================================
# 🚀 场景演练：一场跨越生死的清明祭祖
# =====================================================================
if __name__ == "__main__":
    from s2_zuji_engine import ZujiEngine
    
    # 1. 挂载底层引擎
    db = ZujiEngine(owner_name="向总")
    db.add_ancestral_node("湖南桃源", "青砖老屋", "")
    db.add_kinship_node("向建国", "大伯", is_alive=True)
    db.add_kinship_node("向建军", "二伯", is_alive=False) # 二伯已故
    
    ritual = RitualEngine(db_engine=db)

    print("\n--- 场景一：家书飞帖 (清明前夕发起集结) ---")
    ritual.craft_ancestral_call(
        event_type="清明祭祖", 
        date="2026年4月4日", 
        initiator_name="向建国", 
        core_message="今年要把二伯的碑重新描一下红，大家尽量都回。"
    )

    print("\n--- 场景二：岁华寄语 (清明当天的跨时空对话) ---")
    ritual.send_time_echo(
        sender="向小飞", 
        target_name="向建军", 
        message="爸，我今年在这边拿到了博士学位，没能回桃源看您，给您磕头了。家里一切都好，勿念。"
    )

    print("\n--- 场景三：岁月成碑 (祭祖结束后的史诗总结) ---")
    # 模拟大家在群里七嘴八舌记录的流水账
    raw_logs = [
        {"participants": ["向建国", "向阳"], "desc": "早上除草，向阳把手割破了点。"},
        {"participants": ["向总", "向阳"], "desc": "下午给二伯描了碑，大家在老屋吃了顿柴火饭。"},
        {"participants": ["向小飞(云参与)"], "desc": "打了个跨洋视频回来。"}
    ]
    ritual.summarize_ritual_chronicle(event_title="丙午年(2026)桃源清明祭祖", raw_footprints=raw_logs)