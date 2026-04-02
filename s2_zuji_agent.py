#!/usr/bin/env python3
import json
import logging
from s2_zuji_engine import ZujiEngine

logging.basicConfig(level=logging.INFO, format='%(message)s')

# =====================================================================
# 🧠 S2-SWM: 思乡[祖籍] 情感解析智能体 (Roots & Remembrance NLP Agent)
# 作用：将人类口语化的倾诉、方言、流水账，静默解析为底层结构化指令
# =====================================================================

class RootsAgent:
    def __init__(self, engine: ZujiEngine):
        self.engine = engine
        
        # 核心灵魂：赋予大模型中国家族文化底蕴与数据契约的指令集
        self.SYSTEM_PROMPT = """
        你是一个运行在 S2-SWM 桃花源世界模型中的「思乡[祖籍]」情感解析智能体。
        你的任务是将用户随口说出的家常话、方言、倾诉，静默转化为家族数据库的结构化操作。

        【解析规则与底线】
        1. 文化共情：理解中国家族伦理词汇（如“走了”代表离世，“二大爷”代表父亲的二哥）。
        2. 八大字段对齐：必须努力提取 1-姓名、2-称呼(基于说话人的相对称呼)、3-常住地、4-是否在世、5-父母、6-兄妹、7-子女、8-备注。
        3. 隐私与资产过滤：即使你听到了用户的资产和隐私(如电话/存款/面积)，也绝对不输出到 JSON 中！

        【输出格式要求】
        严格输出 JSON，包含以下可能的操作列表：
        {
          "actions": [
            {"type": "add_kinship", "data": {"1_name": "...", "2_title": "...", "4_is_alive": false, ...}},
            {"type": "add_footprint", "data": {"date": "...", "purpose": "...", "description": "..."}},
            {"type": "add_ancestral", "data": {"location": "...", "history_story": "..."}}
          ]
        }
        """

    def _mock_llm_call(self, natural_language_input: str) -> dict:
        """
        [架构师桩代码] 模拟 LLM 接收 System Prompt 和用户输入后，返回的解析结果。
        真实环境中将对接 S2 的多模态大模型 API。
        """
        logging.info("🧠 [大模型思考中...] 分析语义、提取辈分关系与时空印迹...")
        
        # 针对测试语句的精准模拟返回
        if "建军二哥" in natural_language_input and "桃源" in natural_language_input:
            return {
                "actions": [
                    {
                        "type": "add_kinship",
                        "data": {
                            "1_name": "向建军", "2_title": "二哥", "4_is_alive": False,
                            "7_children": ["向小飞"], "8_notes": "上个月离世，令人惋惜。"
                        }
                    },
                    {
                        "type": "add_kinship",
                        "data": {
                            "1_name": "向小飞", "2_title": "侄子", "3_location": "国外",
                            "4_is_alive": True, "5_parents": ["向建军"]
                        }
                    },
                    {
                        "type": "add_footprint",
                        "data": {
                            "date": "上个月", "purpose": "二哥离世", "participants": ["向小飞(缺席)"],
                            "description": "建军二哥离世，小飞在国外未及赶回见最后一面。"
                        }
                    },
                    {
                        "type": "add_ancestral",
                        "data": {
                            "location": "桃源老家",
                            "architecture": "院子里有一棵桂花树",
                            "history_story": "承载着二哥与我们的回忆，桂花树依旧开花。"
                        }
                    }
                ]
            }
        return {"actions": []}

    def process_voice_or_text(self, natural_language_input: str):
        """主入口：处理自然语言并驱动引擎"""
        print(f"\n🗣️ [接收到语音/文本]: '{natural_language_input}'")
        
        # 1. 调用大模型获取结构化操作
        llm_response = self._mock_llm_call(natural_language_input)
        
        # 2. 静默执行数据库路由
        for action in llm_response.get("actions", []):
            action_type = action.get("type")
            data = action.get("data", {})
            
            if action_type == "add_kinship":
                self.engine.add_kinship_node(
                    name=data.get("1_name", ""),
                    title=data.get("2_title", ""),
                    location=data.get("3_location", ""),
                    is_alive=data.get("4_is_alive", True),
                    parents=data.get("5_parents", []),
                    siblings=data.get("6_siblings", []),
                    children=data.get("7_children", []),
                    notes=data.get("8_notes", "")
                )
            elif action_type == "add_footprint":
                self.engine.add_footprint_event(
                    date=data.get("date", "未知"),
                    purpose=data.get("purpose", "家常"),
                    participants=data.get("participants", []),
                    description=data.get("description", "")
                )
            elif action_type == "add_ancestral":
                self.engine.add_ancestral_node(
                    location=data.get("location", ""),
                    architecture=data.get("architecture", ""),
                    history_story=data.get("history_story", "")
                )
        print("✨ [智能解析完毕] 底层数据已静默更新，触发双重熔断器巡检。")


# =====================================================================
# 🚀 场景演练：从一句带伤感的家常话到结构化数据
# =====================================================================
if __name__ == "__main__":
    print("="*60)
    print("🏮 S2 思乡[祖籍] 智能体交互测试台")
    print("="*60)

    # 初始化引擎与智能体 (假设当前使用者为向总)
    my_engine = ZujiEngine(owner_name="向总")
    zuji_agent = RootsAgent(engine=my_engine)

    # 模拟用户随口录入的一段语音
    raw_voice_input = "哎，建军二哥上个月走了，他那个在国外念书的儿子向小飞也没赶回来见最后一面。咱们桃源老家院子里的那棵桂花树，今年应该开得挺好吧。"
    
    # 智能体开始处理
    zuji_agent.process_voice_or_text(raw_voice_input)

    # 核查引擎底层沉淀的数据
    print("\n👀 [底层数据核查] AI 解析后生成的向小飞数据：")
    print(json.dumps(my_engine.db["Kinship_Nodes"].get("向小飞", {}), ensure_ascii=False, indent=2))
    
    print("\n👀 [底层数据核查] AI 解析后生成的岁月印迹：")
    print(json.dumps(my_engine.db["Footprint_Events"], ensure_ascii=False, indent=2))
    
    # 自动重构家族树
    my_engine.generate_kinship_dag()