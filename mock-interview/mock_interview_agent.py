#!/usr/bin/env python3
"""
模拟面试 Agent
Mock Interview Agent

功能：模拟技术面试，提供面试题、评估回答、给出建议
"""

import random
import json
from datetime import datetime
from typing import List, Dict, Optional

class MockInterviewAgent:
    """模拟面试智能助手"""
    
    def __init__(self):
        self.name = "模拟面试官"
        self.current_question = None
        self.question_index = 0
        self.questions = []
        self.answers = []
        self.score = 0
        self.interview_type = None
        self.difficulty = None
        
        # 面试题库
        self.question_bank = self._load_question_bank()
        
    def _load_question_bank(self) -> Dict:
        """加载面试题库"""
        return {
            "前端开发": {
                "easy": [
                    {
                        "question": "请解释 HTML5 的新特性有哪些？",
                        "key_points": ["语义化标签", "Canvas", "LocalStorage", "WebSocket", "音视频支持"],
                        "sample_answer": "HTML5引入了语义化标签如header、nav、article等；Canvas用于绘图；LocalStorage和SessionStorage用于本地存储；WebSocket实现实时通信；以及原生的音视频支持。"
                    },
                    {
                        "question": "CSS 选择器的优先级是如何计算的？",
                        "key_points": ["内联样式", "ID选择器", "类选择器", "标签选择器", "!important"],
                        "sample_answer": "CSS优先级计算：内联样式(1000) > ID选择器(100) > 类/属性/伪类选择器(10) > 标签/伪元素选择器(1)。!important可以覆盖其他所有规则。"
                    },
                    {
                        "question": "请解释 JavaScript 中的 var、let 和 const 的区别？",
                        "key_points": ["作用域", "变量提升", "重复声明", "可变性"],
                        "sample_answer": "var是函数作用域，存在变量提升，可以重复声明；let和const是块级作用域，不存在变量提升，不能重复声明；const声明的变量不能重新赋值。"
                    }
                ],
                "medium": [
                    {
                        "question": "请解释 JavaScript 中的闭包(Closure)是什么？",
                        "key_points": ["函数嵌套", "作用域链", "变量保持", "实际应用"],
                        "sample_answer": "闭包是指有权访问另一个函数作用域中变量的函数。创建方式：在一个函数内部创建另一个函数。应用：数据私有化、柯里化、防抖节流等。"
                    },
                    {
                        "question": "什么是事件委托(Event Delegation)？它的优点是什么？",
                        "key_points": ["事件冒泡", "父元素监听", "动态元素", "性能优化"],
                        "sample_answer": "事件委托是利用事件冒泡机制，在父元素上统一监听子元素的事件。优点：减少事件处理器数量、支持动态添加的元素、内存占用更少。"
                    },
                    {
                        "question": "请解释 React 中的 Virtual DOM 工作原理？",
                        "key_points": ["虚拟DOM树", "Diff算法", "批量更新", "性能优化"],
                        "sample_answer": "Virtual DOM是真实DOM的内存表示。当状态变化时，React创建新的虚拟DOM树，与旧树进行Diff比较，计算出最小变更集，然后批量更新真实DOM。"
                    }
                ],
                "hard": [
                    {
                        "question": "请详细说明浏览器渲染页面的完整过程？",
                        "key_points": ["DOM树构建", "CSSOM构建", "渲染树", "布局", "绘制", "合成"],
                        "sample_answer": "1.解析HTML构建DOM树；2.解析CSS构建CSSOM树；3.合并DOM和CSSOM构建渲染树；4.布局计算元素位置和大小；5.绘制像素到屏幕；6.合成图层。优化：减少重排重绘、使用CSS动画、图片懒加载等。"
                    },
                    {
                        "question": "如何实现一个前端路由系统？",
                        "key_points": ["Hash模式", "History模式", "路由匹配", "组件渲染", "前进后退"],
                        "sample_answer": "Hash模式：监听hashchange事件，通过location.hash获取路由。History模式：使用pushState/replaceState改变URL，监听popstate事件。实现路由表匹配，动态渲染对应组件，管理浏览器历史记录。"
                    }
                ]
            },
            "后端开发": {
                "easy": [
                    {
                        "question": "HTTP 和 HTTPS 的区别是什么？",
                        "key_points": ["安全性", "SSL/TLS", "端口", "加密传输", "证书"],
                        "sample_answer": "HTTP是明文传输，端口80；HTTPS在HTTP基础上加入SSL/TLS加密，端口443，需要数字证书，数据传输更安全。"
                    },
                    {
                        "question": "什么是 RESTful API？",
                        "key_points": ["资源", "HTTP方法", "无状态", "URL设计", "JSON"],
                        "sample_answer": "RESTful是一种API设计风格，使用HTTP方法(GET/POST/PUT/DELETE)操作资源，URL表示资源路径，无状态通信，通常使用JSON格式传输数据。"
                    }
                ],
                "medium": [
                    {
                        "question": "请解释数据库索引的工作原理？",
                        "key_points": ["B+树", "查询优化", "空间换时间", "索引类型", "最左前缀"],
                        "sample_answer": "索引是帮助数据库快速查询的数据结构，通常使用B+树实现。优点：加快查询速度；缺点：占用额外空间、降低写入速度。使用原则：在WHERE、JOIN、ORDER BY字段上建索引，避免过多索引。"
                    },
                    {
                        "question": "什么是 Redis？它有哪些使用场景？",
                        "key_points": ["内存数据库", "缓存", "持久化", "数据结构", "高并发"],
                        "sample_answer": "Redis是内存中的数据结构存储系统，支持String、Hash、List、Set、Sorted Set等。使用场景：缓存、会话存储、排行榜、计数器、消息队列、分布式锁等。"
                    }
                ],
                "hard": [
                    {
                        "question": "如何设计一个高并发系统？",
                        "key_points": ["负载均衡", "缓存", "数据库优化", "异步处理", "限流降级", "分布式"],
                        "sample_answer": "1.负载均衡分散请求；2.多级缓存减少数据库压力；3.数据库读写分离、分库分表；4.消息队列异步处理；5.限流防止系统过载；6.服务降级保证核心功能；7.无状态设计便于扩展。"
                    }
                ]
            },
            "通用": {
                "easy": [
                    {
                        "question": "请做一个自我介绍",
                        "key_points": ["基本信息", "工作经验", "项目经历", "技术栈", "个人优势"],
                        "sample_answer": "您好，我叫XXX，X年开发经验，主要技术栈是XXX。在上一家公司负责XXX项目，解决了XXX问题，取得了XXX成果。我的优势是XXX，希望能加入贵公司。"
                    },
                    {
                        "question": "你为什么离开上一家公司？",
                        "key_points": ["职业发展", "技术成长", "正面表达", "不抱怨"],
                        "sample_answer": "我在上一家公司学到了很多，但随着个人发展，我希望能在更大的平台接触更复杂的技术挑战，获得更快的成长。"
                    }
                ],
                "medium": [
                    {
                        "question": "你遇到过最大的技术挑战是什么？如何解决的？",
                        "key_points": ["具体场景", "问题分析", "解决方案", "结果量化", "经验总结"],
                        "sample_answer": "使用STAR法则：Situation(背景)、Task(任务)、Action(行动)、Result(结果)。重点描述解决过程和你的贡献。"
                    }
                ],
                "hard": [
                    {
                        "question": "如果项目 deadline 临近但进度落后，你会怎么做？",
                        "key_points": ["风险评估", "优先级排序", "沟通协调", "加班态度", "质量保证"],
                        "sample_answer": "1.评估剩余工作量和技术风险；2.与团队沟通，调整优先级，先完成核心功能；3.及时向上级汇报风险；4.必要时加班，但保证代码质量；5.总结经验避免再次发生。"
                    }
                ]
            }
        }
    
    def start_interview(self, interview_type: str = "前端开发", difficulty: str = "medium", num_questions: int = 5):
        """开始面试"""
        self.interview_type = interview_type
        self.difficulty = difficulty
        self.question_index = 0
        self.answers = []
        self.score = 0
        
        # 生成面试题
        self.questions = self._generate_questions(interview_type, difficulty, num_questions)
        
        print("=" * 60)
        print(f"🎯 模拟面试开始")
        print("=" * 60)
        print(f"面试类型: {interview_type}")
        print(f"难度级别: {difficulty}")
        print(f"题目数量: {num_questions}")
        print("=" * 60)
        print()
        
        return self.questions[0] if self.questions else None
    
    def _generate_questions(self, interview_type: str, difficulty: str, num: int) -> List[Dict]:
        """生成面试题"""
        questions = []
        
        # 获取指定类型的题目
        type_questions = self.question_bank.get(interview_type, self.question_bank["通用"])
        
        # 获取指定难度的题目
        diff_questions = type_questions.get(difficulty, type_questions["medium"])
        
        # 随机选择题目
        if len(diff_questions) >= num:
            questions = random.sample(diff_questions, num)
        else:
            questions = diff_questions
            # 如果题目不够，从其他难度补充
            for diff in ["easy", "medium", "hard"]:
                if diff != difficulty and len(questions) < num:
                    extra = type_questions.get(diff, [])
                    needed = num - len(questions)
                    questions.extend(random.sample(extra, min(needed, len(extra))))
        
        # 打乱顺序
        random.shuffle(questions)
        
        return questions[:num]
    
    def get_next_question(self) -> Optional[Dict]:
        """获取下一题"""
        if self.question_index < len(self.questions) - 1:
            self.question_index += 1
            return self.questions[self.question_index]
        return None
    
    def evaluate_answer(self, user_answer: str) -> Dict:
        """评估回答"""
        if not self.current_question:
            return {"error": "没有当前问题"}
        
        question = self.current_question
        key_points = question.get("key_points", [])
        sample_answer = question.get("sample_answer", "")
        
        # 计算得分
        score = self._calculate_score(user_answer, key_points, sample_answer)
        
        # 生成反馈
        feedback = self._generate_feedback(user_answer, key_points, sample_answer, score)
        
        # 保存答案
        self.answers.append({
            "question": question["question"],
            "user_answer": user_answer,
            "score": score,
            "feedback": feedback
        })
        
        self.score += score
        
        return {
            "score": score,
            "max_score": 100,
            "feedback": feedback,
            "key_points_missed": self._find_missed_points(user_answer, key_points),
            "sample_answer": sample_answer
        }
    
    def _calculate_score(self, user_answer: str, key_points: List[str], sample_answer: str) -> int:
        """计算得分"""
        if not user_answer or len(user_answer) < 10:
            return 20
        
        score = 40  # 基础分
        
        # 检查关键词
        user_answer_lower = user_answer.lower()
        for point in key_points:
            if any(keyword in user_answer_lower for keyword in point.lower().split()):
                score += 10
        
        # 根据回答长度调整
        if len(user_answer) > 100:
            score += 10
        
        return min(score, 100)
    
    def _generate_feedback(self, user_answer: str, key_points: List[str], sample_answer: str, score: int) -> str:
        """生成反馈"""
        if score >= 80:
            return "🌟 优秀！回答非常全面，覆盖了主要知识点。"
        elif score >= 60:
            return "👍 良好！回答基本正确，但可以补充更多细节。"
        elif score >= 40:
            return "📚 及格！回答有基础，建议深入学习相关知识点。"
        else:
            return "💪 需要加强！建议参考示例答案，系统学习这个概念。"
    
    def _find_missed_points(self, user_answer: str, key_points: List[str]) -> List[str]:
        """找出遗漏的要点"""
        missed = []
        user_answer_lower = user_answer.lower()
        for point in key_points:
            if not any(keyword in user_answer_lower for keyword in point.lower().split()):
                missed.append(point)
        return missed
    
    def get_interview_summary(self) -> Dict:
        """获取面试总结"""
        if not self.answers:
            return {"error": "面试尚未开始"}
        
        total_score = sum(a["score"] for a in self.answers)
        avg_score = total_score / len(self.answers) if self.answers else 0
        
        # 评级
        if avg_score >= 80:
            level = "优秀"
            suggestion = "你的表现非常出色！继续保持，可以挑战更高难度的题目。"
        elif avg_score >= 60:
            level = "良好"
            suggestion = "基础扎实，建议针对薄弱环节加强学习。"
        elif avg_score >= 40:
            level = "及格"
            suggestion = "需要系统学习相关知识，多做练习。"
        else:
            level = "待提高"
            suggestion = "建议从基础开始，逐步建立知识体系。"
        
        return {
            "total_questions": len(self.answers),
            "total_score": total_score,
            "average_score": round(avg_score, 1),
            "level": level,
            "suggestion": suggestion,
            "answers_detail": self.answers
        }
    
    def chat(self, user_input: str) -> str:
        """主对话函数"""
        user_input = user_input.strip()
        
        # 开始面试
        if any(keyword in user_input for keyword in ["开始", "面试", "start"]):
            return self._handle_start_interview(user_input)
        
        # 回答问题
        elif self.current_question and self.question_index < len(self.questions):
            return self._handle_answer(user_input)
        
        # 查看总结
        elif any(keyword in user_input for keyword in ["总结", "结束", "结果", "summary"]):
            return self._handle_summary()
        
        # 帮助
        else:
            return self._handle_help()
    
    def _handle_start_interview(self, user_input: str) -> str:
        """处理开始面试"""
        # 解析参数
        interview_type = "前端开发"
        if "后端" in user_input:
            interview_type = "后端开发"
        elif "通用" in user_input:
            interview_type = "通用"
        
        difficulty = "medium"
        if "简单" in user_input or "easy" in user_input:
            difficulty = "easy"
        elif "困难" in user_input or "hard" in user_input:
            difficulty = "hard"
        
        num = 5
        import re
        numbers = re.findall(r'\d+', user_input)
        if numbers:
            num = int(numbers[0])
        
        # 开始面试
        question = self.start_interview(interview_type, difficulty, num)
        self.current_question = question
        
        if question:
            return f"第 1 题 / 共 {len(self.questions)} 题\n\n{question['question']}"
        else:
            return "抱歉，无法生成面试题。"
    
    def _handle_answer(self, user_input: str) -> str:
        """处理回答"""
        # 评估回答
        result = self.evaluate_answer(user_input)
        
        response = f"\n📊 得分: {result['score']}/100\n"
        response += f"💬 评价: {result['feedback']}\n"
        
        if result['key_points_missed']:
            response += f"\n📌 遗漏要点: {', '.join(result['key_points_missed'])}\n"
        
        response += f"\n✅ 参考答案:\n{result['sample_answer'][:200]}...\n"
        
        # 获取下一题
        next_question = self.get_next_question()
        if next_question:
            self.current_question = next_question
            response += f"\n{'='*40}\n"
            response += f"第 {self.question_index + 1} 题 / 共 {len(self.questions)} 题\n\n"
            response += next_question['question']
        else:
            response += f"\n{'='*40}\n"
            response += "🎉 面试结束！输入「总结」查看面试报告。"
            self.current_question = None
        
        return response
    
    def _handle_summary(self) -> str:
        """处理总结"""
        summary = self.get_interview_summary()
        
        if "error" in summary:
            return summary["error"]
        
        response = "=" * 60 + "\n"
        response += "📋 面试总结报告\n"
        response += "=" * 60 + "\n\n"
        response += f"📊 总题数: {summary['total_questions']}\n"
        response += f"⭐ 总得分: {summary['total_score']}\n"
        response += f"📈 平均分: {summary['average_score']}\n"
        response += f"🏆 评级: {summary['level']}\n\n"
        response += f"💡 建议:\n{summary['suggestion']}\n\n"
        response += "=" * 60 + "\n"
        response += "输入「开始面试」可以进行新的面试\n"
        
        return response
    
    def _handle_help(self) -> str:
        """处理帮助"""
        return """🎯 模拟面试助手

使用方法：
1. 开始面试 - 输入："开始面试" 或 "开始前端面试 5题"
2. 回答问题 - 直接输入你的回答
3. 查看总结 - 输入："总结" 或 "结束"

可选参数：
- 面试类型：前端开发、后端开发、通用
- 难度：简单、中等、困难
- 题数：1-10题

示例：
- "开始前端面试 5题"
- "开始后端困难面试 3题"
- "开始通用简单面试"
"""

def main():
    """主程序"""
    print("=" * 60)
    print("🎯 欢迎使用模拟面试助手！")
    print("=" * 60)
    print()
    
    agent = MockInterviewAgent()
    print(agent._handle_help())
    print("-" * 60)
    
    # 交互模式
    while True:
        try:
            user_input = input("\n您: ").strip()
            if not user_input:
                continue
            if user_input.lower() in ["exit", "quit", "退出", "再见"]:
                print("\n👋 祝您面试顺利！再见！")
                break
            
            response = agent.chat(user_input)
            print(f"\n🤖 面试官: {response}")
            
        except KeyboardInterrupt:
            print("\n\n👋 再见！")
            break
        except EOFError:
            break

if __name__ == "__main__":
    main()
