#!/usr/bin/env python3
"""
雅思口语练习 Agent
IELTS Speaking Practice Agent

功能：模拟雅思口语考试，提供话题、评分、改进建议
"""

import random
import json
import re
from datetime import datetime
from typing import List, Dict, Optional, Tuple

class IELTSSpeakingAgent:
    """雅思口语练习智能助手"""
    
    def __init__(self):
        self.name = "雅思口语教练"
        self.current_part = 1
        self.current_question = None
        self.question_index = 0
        self.questions = []
        self.responses = []
        self.scores = {"fluency": 0, "vocabulary": 0, "grammar": 0, "pronunciation": 0}
        self.part_scores = []
        
        # 话题库
        self.topic_bank = self._load_topic_bank()
        
    def _load_topic_bank(self) -> Dict:
        """加载雅思口语话题库"""
        return {
            "Part1": {
                "个人信息": [
                    "Can you tell me about your hometown?",
                    "What do you like about your hometown?",
                    "Would you like to live in your hometown in the future?",
                    "Do you work or are you a student?",
                    "What do you like about your job/studies?",
                    "What do you do in your free time?"
                ],
                "兴趣爱好": [
                    "Do you like reading? What kind of books do you read?",
                    "What sports do you like to watch or play?",
                    "Do you prefer to spend time indoors or outdoors?",
                    "What kind of music do you like?",
                    "Do you like cooking? Why or why not?",
                    "What hobbies would you like to try in the future?"
                ],
                "日常生活": [
                    "What time do you usually get up?",
                    "Do you prefer to study in the morning or at night?",
                    "How do you usually travel to work/school?",
                    "What do you usually do on weekends?",
                    "Do you prefer to eat at home or eat out?",
                    "How do you like to relax after a busy day?"
                ],
                "科技媒体": [
                    "How often do you use the Internet?",
                    "Do you prefer to use a computer or a smartphone?",
                    "What social media platforms do you use?",
                    "Do you like watching TV? What programs do you watch?",
                    "How has technology changed your life?",
                    "Do you prefer to read news online or in newspapers?"
                ]
            },
            "Part2": {
                "人物": [
                    {
                        "topic": "Describe a person who has influenced you.",
                        "prompts": ["Who this person is", "How you met this person", "What this person does", "Why this person has influenced you"]
                    },
                    {
                        "topic": "Describe a famous person you admire.",
                        "prompts": ["Who this person is", "What this person is famous for", "Why you admire this person", "How this person has influenced others"]
                    },
                    {
                        "topic": "Describe a good friend.",
                        "prompts": ["Who this person is", "How you met", "What you do together", "Why you are good friends"]
                    }
                ],
                "地点": [
                    {
                        "topic": "Describe a place you have visited that had a lot of noise.",
                        "prompts": ["Where this place was", "Why you went there", "Why it was noisy", "How you felt about the noise"]
                    },
                    {
                        "topic": "Describe a beautiful place you have visited.",
                        "prompts": ["Where this place is", "When you visited it", "What you did there", "Why you think it is beautiful"]
                    },
                    {
                        "topic": "Describe your ideal house or apartment.",
                        "prompts": ["Where it would be", "What it would look like", "What facilities it would have", "Why it would be ideal for you"]
                    }
                ],
                "经历": [
                    {
                        "topic": "Describe a difficult decision you made.",
                        "prompts": ["What the decision was", "When you made it", "Why it was difficult", "How you felt after making it"]
                    },
                    {
                        "topic": "Describe a time when you helped someone.",
                        "prompts": ["Who you helped", "How you helped them", "Why you helped them", "How you felt about it"]
                    },
                    {
                        "topic": "Describe a memorable journey you have taken.",
                        "prompts": ["Where you went", "Who you went with", "What you did", "Why it was memorable"]
                    }
                ],
                "物品": [
                    {
                        "topic": "Describe something you own that is important to you.",
                        "prompts": ["What it is", "How long you have had it", "How you got it", "Why it is important"]
                    },
                    {
                        "topic": "Describe a gift you received that made you happy.",
                        "prompts": ["What the gift was", "Who gave it to you", "When you received it", "Why it made you happy"]
                    },
                    {
                        "topic": "Describe a book you have read recently.",
                        "prompts": ["What the book is about", "When you read it", "Why you chose to read it", "What you learned from it"]
                    }
                ]
            },
            "Part3": {
                "教育": [
                    "What are the advantages and disadvantages of online learning?",
                    "Do you think traditional schools will disappear in the future?",
                    "What skills do you think are most important for young people to learn today?",
                    "How has education changed in your country over the past few decades?",
                    "Do you think teachers will be replaced by technology in the future?"
                ],
                "科技": [
                    "How has technology changed the way people communicate?",
                    "Do you think people rely too much on technology?",
                    "What are the benefits and drawbacks of artificial intelligence?",
                    "How do you think technology will change our lives in the future?",
                    "Should children be allowed to use smartphones and tablets?"
                ],
                "环境": [
                    "What are the main environmental problems in your country?",
                    "Do you think individuals or governments should take more responsibility for protecting the environment?",
                    "What can ordinary people do to help protect the environment?",
                    "How has climate change affected your country?",
                    "Do you think renewable energy is the solution to environmental problems?"
                ],
                "社会": [
                    "What are the advantages and disadvantages of living in a big city?",
                    "How has family life changed in your country over the past few decades?",
                    "Do you think people today are too materialistic?",
                    "What role should the government play in helping poor people?",
                    "How important is it to preserve traditional culture in modern society?"
                ],
                "工作": [
                    "What qualities make a good leader?",
                    "Do you think people should stay in one job for their whole career?",
                    "How has the nature of work changed in recent years?",
                    "What are the advantages and disadvantages of working from home?",
                    "Do you think money is the most important factor when choosing a job?"
                ]
            }
        }
    
    def start_practice(self, part: int = 1, topic: str = None) -> Dict:
        """开始练习"""
        self.current_part = part
        self.question_index = 0
        self.responses = []
        self.part_scores = []
        
        # 生成题目
        self.questions = self._generate_questions(part, topic)
        
        print("=" * 60)
        print(f"🎯 雅思口语练习 - Part {part}")
        print("=" * 60)
        
        if part == 1:
            print("📋 Part 1: 自我介绍和一般问题 (4-5分钟)")
            print("💡 提示：回答要简洁，通常2-3句话")
        elif part == 2:
            print("📋 Part 2: 个人陈述 (3-4分钟)")
            print("💡 提示：准备1分钟，陈述1-2分钟")
        else:
            print("📋 Part 3: 深入讨论 (4-5分钟)")
            print("💡 提示：给出观点并解释，适当举例")
        
        print("=" * 60)
        print()
        
        self.current_question = self.questions[0] if self.questions else None
        return self.current_question
    
    def _generate_questions(self, part: int, topic: str = None) -> List[Dict]:
        """生成题目"""
        questions = []
        
        if part == 1:
            # Part 1: 随机选择3-4个话题，每个话题1-2题
            topics = list(self.topic_bank["Part1"].keys())
            selected_topics = random.sample(topics, min(3, len(topics)))
            for t in selected_topics:
                topic_questions = self.topic_bank["Part1"][t]
                num = random.randint(1, 2)
                questions.extend(random.sample(topic_questions, min(num, len(topic_questions))))
        
        elif part == 2:
            # Part 2: 随机选择一个话题卡片
            all_topics = []
            for category, topics in self.topic_bank["Part2"].items():
                all_topics.extend(topics)
            
            if topic and topic in self.topic_bank["Part2"]:
                selected = random.choice(self.topic_bank["Part2"][topic])
            else:
                selected = random.choice(all_topics)
            
            questions.append({
                "topic": selected["topic"],
                "prompts": selected["prompts"],
                "type": "cue_card"
            })
        
        else:  # Part 3
            # Part 3: 基于Part 2的话题选择相关问题，或随机选择
            topics = list(self.topic_bank["Part3"].keys())
            selected_topic = random.choice(topics)
            topic_questions = self.topic_bank["Part3"][selected_topic]
            questions.extend(random.sample(topic_questions, min(4, len(topic_questions))))
        
        return questions
    
    def get_next_question(self) -> Optional[Dict]:
        """获取下一题"""
        if self.question_index < len(self.questions) - 1:
            self.question_index += 1
            self.current_question = self.questions[self.question_index]
            return self.current_question
        return None
    
    def evaluate_response(self, user_response: str) -> Dict:
        """评估回答"""
        if not self.current_question:
            return {"error": "没有当前问题"}
        
        # 计算各项得分
        fluency_score = self._evaluate_fluency(user_response)
        vocab_score = self._evaluate_vocabulary(user_response)
        grammar_score = self._evaluate_grammar(user_response)
        pronunciation_guide = self._evaluate_pronunciation(user_response)
        
        # 总分
        total_score = (fluency_score + vocab_score + grammar_score) / 3
        
        # 生成反馈
        feedback = self._generate_detailed_feedback(
            user_response, fluency_score, vocab_score, grammar_score
        )
        
        # 保存回答
        self.responses.append({
            "part": self.current_part,
            "question": self.current_question if isinstance(self.current_question, str) else self.current_question.get("topic", ""),
            "response": user_response,
            "scores": {
                "fluency": fluency_score,
                "vocabulary": vocab_score,
                "grammar": grammar_score
            },
            "total": round(total_score, 1)
        })
        
        # 累加分数
        self.scores["fluency"] += fluency_score
        self.scores["vocabulary"] += vocab_score
        self.scores["grammar"] += grammar_score
        
        return {
            "scores": {
                "fluency": fluency_score,
                "vocabulary": vocab_score,
                "grammar": grammar_score,
                "total": round(total_score, 1)
            },
            "feedback": feedback,
            "improvements": self._suggest_improvements(user_response),
            "better_response": self._generate_better_response()
        }
    
    def _evaluate_fluency(self, response: str) -> int:
        """评估流利度"""
        score = 5
        word_count = len(response.split())
        
        # 根据回答长度评分
        if word_count > 50:
            score += 1
        if word_count > 100:
            score += 1
        
        # 检查连接词使用
        connectors = ["however", "therefore", "moreover", "in addition", "on the other hand", "for example"]
        connector_count = sum(1 for c in connectors if c.lower() in response.lower())
        score += min(connector_count, 2)
        
        return min(score, 9)
    
    def _evaluate_vocabulary(self, response: str) -> int:
        """评估词汇"""
        score = 5
        
        # 检查高级词汇
        advanced_words = ["significant", "essential", "consequently", "nevertheless", "approximately", "furthermore"]
        advanced_count = sum(1 for w in advanced_words if w.lower() in response.lower())
        score += min(advanced_count * 0.5, 2)
        
        # 检查同义词替换
        synonyms = ["happy", "glad", "pleased", "delighted"]
        synonym_used = any(s in response.lower() for s in synonyms)
        if synonym_used:
            score += 0.5
        
        # 词汇多样性
        words = response.lower().split()
        unique_words = set(words)
        if len(unique_words) / len(words) > 0.6:
            score += 1
        
        return min(int(score), 9)
    
    def _evaluate_grammar(self, response: str) -> int:
        """评估语法"""
        score = 5
        
        # 检查复杂句型
        complex_patterns = [
            r"\bif\b.*\bwould\b",
            r"\bbecause\b.*\bso\b",
            r"\balthough\b.*\b",
            r"\bwhich\b.*\b",
            r"\bwho\b.*\b"
        ]
        complex_count = sum(1 for pattern in complex_patterns if re.search(pattern, response, re.IGNORECASE))
        score += min(complex_count, 2)
        
        # 检查时态多样性
        tenses = ["have been", "had been", "will be", "would be", "is being"]
        tense_count = sum(1 for t in tenses if t in response.lower())
        score += min(tense_count * 0.5, 1.5)
        
        return min(int(score), 9)
    
    def _evaluate_pronunciation(self, response: str) -> str:
        """发音指导"""
        difficult_words = []
        words = response.split()
        for word in words:
            if len(word) > 8:
                difficult_words.append(word)
        
        if difficult_words:
            return f"注意这些词的发音: {', '.join(difficult_words[:3])}"
        return "发音良好，继续保持"
    
    def _generate_detailed_feedback(self, response: str, fluency: int, vocab: int, grammar: int) -> str:
        """生成详细反馈"""
        feedback_parts = []
        
        # 流利度反馈
        if fluency >= 7:
            feedback_parts.append("✅ 流利度：表达流畅，语速适中")
        elif fluency >= 5:
            feedback_parts.append("📚 流利度：基本流畅，可以适当放慢语速")
        else:
            feedback_parts.append("💪 流利度：需要多练习，建议先写再说")
        
        # 词汇反馈
        if vocab >= 7:
            feedback_parts.append("✅ 词汇：用词准确，有高级词汇")
        elif vocab >= 5:
            feedback_parts.append("📚 词汇：词汇量尚可，尝试使用更多同义词")
        else:
            feedback_parts.append("💪 词汇：需要扩充词汇量，多积累话题词汇")
        
        # 语法反馈
        if grammar >= 7:
            feedback_parts.append("✅ 语法：句式多样，语法准确")
        elif grammar >= 5:
            feedback_parts.append("📚 语法：基本正确，可以尝试更复杂的句型")
        else:
            feedback_parts.append("💪 语法：注意基础语法，多练习从句")
        
        return "\n".join(feedback_parts)
    
    def _suggest_improvements(self, response: str) -> List[str]:
        """建议改进点"""
        suggestions = []
        
        word_count = len(response.split())
        if word_count < 30:
            suggestions.append("回答较短，尝试扩展观点并举例说明")
        
        if not any(c in response.lower() for c in ["because", "since", "as"]):
            suggestions.append("多使用连接词解释原因，如 because, since")
        
        if not any(c in response.lower() for c in ["for example", "such as", "like"]):
            suggestions.append("适当举例会使回答更有说服力")
        
        if response.count(".") < 2:
            suggestions.append("尝试使用复合句，增加句子复杂度")
        
        return suggestions if suggestions else ["回答不错，继续保持！"]
    
    def _generate_better_response(self) -> str:
        """生成更好的回答示例"""
        return """参考回答结构：
1. 直接回答问题
2. 给出理由/解释
3. 举例说明
4. 总结或延伸

示例：
"I think... because... For example,... So,..."""
    
    def get_practice_summary(self) -> Dict:
        """获取练习总结"""
        if not self.responses:
            return {"error": "还没有练习记录"}
        
        num_responses = len(self.responses)
        avg_fluency = self.scores["fluency"] / num_responses if num_responses else 0
        avg_vocab = self.scores["vocabulary"] / num_responses if num_responses else 0
        avg_grammar = self.scores["grammar"] / num_responses if num_responses else 0
        overall = (avg_fluency + avg_vocab + avg_grammar) / 3
        
        # 评级
        if overall >= 7:
            band = "7.0-9.0 (Good-Expert)"
            advice = "表现优秀！继续保持，注意细节提升"
        elif overall >= 5:
            band = "5.0-6.5 (Modest-Competent)"
            advice = "基础良好，重点提升词汇和流利度"
        else:
            band = "4.0-4.5 (Limited)"
            advice = "需要系统学习，建议从基础句型和词汇开始"
        
        return {
            "part": self.current_part,
            "total_questions": num_responses,
            "average_scores": {
                "fluency": round(avg_fluency, 1),
                "vocabulary": round(avg_vocab, 1),
                "grammar": round(avg_grammar, 1),
                "overall": round(overall, 1)
            },
            "estimated_band": band,
            "advice": advice,
            "responses": self.responses
        }
    
    def chat(self, user_input: str) -> str:
        """主对话函数"""
        user_input = user_input.strip()
        
        # 开始练习
        if any(keyword in user_input for keyword in ["开始", "练习", "start", "part"]):
            return self._handle_start(user_input)
        
        # 回答问题
        elif self.current_question and len(self.responses) < len(self.questions):
            return self._handle_response(user_input)
        
        # 查看总结
        elif any(keyword in user_input for keyword in ["总结", "结束", "结果", "summary", "score"]):
            return self._handle_summary()
        
        # 帮助
        else:
            return self._handle_help()
    
    def _handle_start(self, user_input: str) -> str:
        """处理开始练习"""
        # 解析Part
        part = 1
        if "part 2" in user_input.lower() or "part2" in user_input.lower():
            part = 2
        elif "part 3" in user_input.lower() or "part3" in user_input.lower():
            part = 3
        
        question = self.start_practice(part)
        
        if question:
            if isinstance(question, dict) and question.get("type") == "cue_card":
                # Part 2 话题卡
                response = f"📝 话题卡：\n\n{question['topic']}\n\n"
                response += "提示要点：\n"
                for i, prompt in enumerate(question['prompts'], 1):
                    response += f"  {i}. {prompt}\n"
                response += "\n⏱️ 你有1分钟准备时间，然后请开始陈述（1-2分钟）"
                return response
            else:
                return f"🎤 问题 {self.question_index + 1}/{len(self.questions)}:\n\n{question}"
        else:
            return "抱歉，无法生成题目。"
    
    def _handle_response(self, user_input: str) -> str:
        """处理回答"""
        # 评估回答
        result = self.evaluate_response(user_input)
        
        response = f"\n📊 评分结果:\n"
        response += f"  流利度: {result['scores']['fluency']}/9\n"
        response += f"  词汇: {result['scores']['vocabulary']}/9\n"
        response += f"  语法: {result['scores']['grammar']}/9\n"
        response += f"  总分: {result['scores']['total']}/9\n\n"
        
        response += f"💬 反馈:\n{result['feedback']}\n\n"
        
        response += f"💡 改进建议:\n"
        for suggestion in result['improvements']:
            response += f"  • {suggestion}\n"
        
        # 获取下一题
        next_question = self.get_next_question()
        if next_question:
            response += f"\n{'='*50}\n"
            if isinstance(next_question, dict) and next_question.get("type") == "cue_card":
                response += f"📝 话题卡：\n\n{next_question['topic']}\n"
            else:
                response += f"🎤 问题 {self.question_index + 1}/{len(self.questions)}:\n\n{next_question}"
        else:
            response += f"\n{'='*50}\n"
            response += "🎉 本部分练习结束！输入「总结」查看完整报告。"
        
        return response
    
    def _handle_summary(self) -> str:
        """处理总结"""
        summary = self.get_practice_summary()
        
        if "error" in summary:
            return summary["error"]
        
        response = "=" * 60 + "\n"
        response += "📋 雅思口语练习报告\n"
        response += "=" * 60 + "\n\n"
        response += f"📚 Part {summary['part']} 练习总结\n\n"
        response += f"📝 答题数量: {summary['total_questions']}\n\n"
        response += "📊 平均得分:\n"
        response += f"  流利度: {summary['average_scores']['fluency']}/9\n"
        response += f"  词汇: {summary['average_scores']['vocabulary']}/9\n"
        response += f"  语法: {summary['average_scores']['grammar']}/9\n"
        response += f"  总分: {summary['average_scores']['overall']}/9\n\n"
        response += f"🎯 预估分数段: {summary['estimated_band']}\n\n"
        response += f"💡 建议:\n{summary['advice']}\n\n"
        response += "=" * 60 + "\n"
        response += "输入「开始 Part 1/2/3」继续练习\n"
        
        return response
    
    def _handle_help(self) -> str:
        """处理帮助"""
        return """🎯 雅思口语练习助手

使用方法：
1. 开始练习 - 输入："开始 Part 1" 或 "开始 Part 2"
2. 回答问题 - 直接输入你的回答
3. 查看总结 - 输入："总结" 或 "结束"

雅思口语三部分：
• Part 1: 自我介绍和一般问题 (4-5分钟)
• Part 2: 个人陈述 (3-4分钟)  
• Part 3: 深入讨论 (4-5分钟)

评分标准：
• 流利度和连贯性 (Fluency & Coherence)
• 词汇资源 (Lexical Resource)
• 语法范围和准确性 (Grammatical Range & Accuracy)
• 发音 (Pronunciation)

示例：
- "开始 Part 1" - 开始第一部分练习
- "开始 Part 2" - 开始第二部分练习
- "开始 Part 3" - 开始第三部分练习
"""

def main():
    """主程序"""
    print("=" * 60)
    print("🎯 欢迎使用雅思口语练习助手！")
    print("=" * 60)
    print()
    
    agent = IELTSSpeakingAgent()
    print(agent._handle_help())
    print("-" * 60)
    
    # 交互模式
    while True:
        try:
            user_input = input("\n您: ").strip()
            if not user_input:
                continue
            if user_input.lower() in ["exit", "quit", "退出", "再见"]:
                print("\n👋 Good luck with your IELTS! See you!")
                break
            
            response = agent.chat(user_input)
            print(f"\n🤖 教练: {response}")
            
        except KeyboardInterrupt:
            print("\n\n👋 Goodbye!")
            break
        except EOFError:
            break

if __name__ == "__main__":
    main()
