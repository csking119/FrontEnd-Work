#!/usr/bin/env python3
"""
智能旅游规划 Agent
Travel Planner Agent
"""

import json
import random
from datetime import datetime, timedelta
from typing import List, Dict, Optional

class TravelPlannerAgent:
    """旅游规划智能助手"""
    
    def __init__(self):
        self.name = "旅游规划小助手"
        self.destinations_db = self._load_destinations()
        
    def _load_destinations(self) -> Dict:
        """加载旅游目的地数据库"""
        return {
            "日本": {
                "cities": ["东京", "京都", "大阪", "北海道", "冲绳"],
                "budget_range": {"low": 5000, "mid": 10000, "high": 20000},
                "best_seasons": ["春季", "秋季"],
                "visa_required": True,
                "currency": "日元",
                "exchange_rate": 0.048,  # 1日元 = 0.048人民币
                "highlights": ["樱花", "温泉", "美食", "购物", "文化"]
            },
            "泰国": {
                "cities": ["曼谷", "清迈", "普吉岛", "芭提雅"],
                "budget_range": {"low": 3000, "mid": 6000, "high": 12000},
                "best_seasons": ["冬季", "春季"],
                "visa_required": False,
                "currency": "泰铢",
                "exchange_rate": 0.20,
                "highlights": ["海滩", "寺庙", "美食", "按摩", "夜生活"]
            },
            "新加坡": {
                "cities": ["新加坡"],
                "budget_range": {"low": 6000, "mid": 10000, "high": 18000},
                "best_seasons": ["全年"],
                "visa_required": False,
                "currency": "新元",
                "exchange_rate": 5.35,
                "highlights": ["花园城市", "美食", "购物", "亲子"]
            },
            "韩国": {
                "cities": ["首尔", "釜山", "济州岛"],
                "budget_range": {"low": 4000, "mid": 8000, "high": 15000},
                "best_seasons": ["春季", "秋季"],
                "visa_required": False,
                "currency": "韩元",
                "exchange_rate": 0.0054,
                "highlights": ["购物", "美食", "K-pop", "护肤", "历史"]
            },
            "欧洲": {
                "cities": ["巴黎", "伦敦", "罗马", "巴塞罗那", "阿姆斯特丹"],
                "budget_range": {"low": 15000, "mid": 25000, "high": 40000},
                "best_seasons": ["夏季", "秋季"],
                "visa_required": True,
                "currency": "欧元",
                "exchange_rate": 7.8,
                "highlights": ["艺术", "历史", "建筑", "美食", "购物"]
            },
            "国内": {
                "cities": ["北京", "上海", "西安", "成都", "云南", "新疆", "西藏"],
                "budget_range": {"low": 2000, "mid": 5000, "high": 10000},
                "best_seasons": ["全年"],
                "visa_required": False,
                "currency": "人民币",
                "exchange_rate": 1.0,
                "highlights": ["历史文化", "自然风光", "美食", "民族风情"]
            }
        }
    
    def recommend_destinations(self, budget: int, days: int, interests: List[str] = None) -> List[Dict]:
        """根据预算和天数推荐目的地"""
        recommendations = []
        
        for country, info in self.destinations_db.items():
            budget_level = self._get_budget_level(budget, info["budget_range"])
            if budget_level:
                match_score = self._calculate_match_score(info, interests)
                recommendations.append({
                    "country": country,
                    "cities": info["cities"],
                    "budget_level": budget_level,
                    "estimated_cost": self._estimate_cost(budget, days, info),
                    "visa_required": info["visa_required"],
                    "highlights": info["highlights"],
                    "match_score": match_score
                })
        
        # 按匹配度排序
        recommendations.sort(key=lambda x: x["match_score"], reverse=True)
        return recommendations[:3]  # 返回前3个推荐
    
    def _get_budget_level(self, budget: int, budget_range: Dict) -> Optional[str]:
        """判断预算等级"""
        if budget >= budget_range["low"] * 0.8:
            if budget >= budget_range["high"]:
                return "豪华"
            elif budget >= budget_range["mid"]:
                return "舒适"
            else:
                return "经济"
        return None
    
    def _calculate_match_score(self, info: Dict, interests: List[str]) -> int:
        """计算兴趣匹配度"""
        if not interests:
            return 50
        score = 50
        for interest in interests:
            if interest in info["highlights"]:
                score += 15
        return min(score, 100)
    
    def _estimate_cost(self, budget: int, days: int, info: Dict) -> Dict:
        """估算费用"""
        daily_budget = budget / days
        return {
            "flight": int(budget * 0.3),  # 机票占30%
            "hotel": int(budget * 0.25),  # 住宿占25%
            "food": int(budget * 0.2),    # 餐饮占20%
            "transport": int(budget * 0.1),  # 交通占10%
            "tickets": int(budget * 0.1),    # 门票占10%
            "shopping": int(budget * 0.05)   # 购物占5%
        }
    
    def create_itinerary(self, destination: str, days: int, interests: List[str] = None) -> List[Dict]:
        """创建详细行程"""
        itinerary = []
        
        # 模拟景点数据
        attractions = self._get_attractions(destination, interests)
        
        for day in range(1, days + 1):
            daily_plan = {
                "day": day,
                "date": (datetime.now() + timedelta(days=day)).strftime("%Y-%m-%d"),
                "theme": self._get_day_theme(day, interests),
                "activities": []
            }
            
            # 上午活动
            if day == 1:
                daily_plan["activities"].append({
                    "time": "09:00-12:00",
                    "type": "抵达/入住",
                    "description": f"抵达{destination}，办理酒店入住，休息调整"
                })
            else:
                daily_plan["activities"].append({
                    "time": "09:00-12:00",
                    "type": "景点游览",
                    "description": random.choice(attractions) if attractions else "市区观光"
                })
            
            # 午餐
            daily_plan["activities"].append({
                "time": "12:00-13:30",
                "type": "午餐",
                "description": "品尝当地特色美食"
            })
            
            # 下午活动
            daily_plan["activities"].append({
                "time": "14:00-17:00",
                "type": "景点游览",
                "description": random.choice(attractions) if attractions else "文化体验"
            })
            
            # 晚餐
            daily_plan["activities"].append({
                "time": "18:00-19:30",
                "type": "晚餐",
                "description": "推荐当地知名餐厅"
            })
            
            # 晚上活动
            if day < days:
                daily_plan["activities"].append({
                    "time": "20:00-21:30",
                    "type": "休闲活动",
                    "description": "夜市漫步/夜景欣赏/休息"
                })
            else:
                daily_plan["activities"].append({
                    "time": "20:00-21:30",
                    "type": "返程准备",
                    "description": "整理行李，准备返程"
                })
            
            itinerary.append(daily_plan)
        
        return itinerary
    
    def _get_attractions(self, destination: str, interests: List[str]) -> List[str]:
        """获取景点列表"""
        default_attractions = [
            "著名地标建筑",
            "历史文化街区",
            "当地博物馆",
            "特色公园",
            "购物中心",
            "传统市场"
        ]
        return default_attractions
    
    def _get_day_theme(self, day: int, interests: List[str]) -> str:
        """获取每日主题"""
        themes = ["城市探索", "文化体验", "自然风光", "美食之旅", "购物休闲", "历史寻访"]
        if interests:
            return interests[(day - 1) % len(interests)] if day <= len(interests) else random.choice(themes)
        return themes[(day - 1) % len(themes)]
    
    def generate_packing_list(self, destination: str, days: int, season: str = None) -> Dict:
        """生成行李清单"""
        return {
            "证件": ["身份证/护照", "签证", "机票/酒店预订单", "保险单"],
            "衣物": [f"{days}套换洗衣物", "舒适的步行鞋", "外套", "睡衣"],
            "电子设备": ["手机", "充电器", "充电宝", "相机", "转换插头"],
            "洗漱用品": ["牙刷", "牙膏", "洗发水", "沐浴露", "护肤品"],
            "药品": ["感冒药", "肠胃药", "创可贴", "个人常用药"],
            "其他": ["雨伞", "水壶", "零食", "现金/银行卡"]
        }
    
    def chat(self, user_input: str) -> str:
        """主对话函数"""
        user_input = user_input.lower()
        
        # 解析用户意图
        if "推荐" in user_input or "去哪" in user_input:
            return self._handle_recommendation(user_input)
        elif "行程" in user_input or "计划" in user_input:
            return self._handle_itinerary(user_input)
        elif "预算" in user_input or "多少钱" in user_input:
            return self._handle_budget(user_input)
        elif "清单" in user_input or "行李" in user_input:
            return self._handle_packing_list(user_input)
        else:
            return self._handle_general(user_input)
    
    def _handle_recommendation(self, user_input: str) -> str:
        """处理目的地推荐"""
        # 提取预算和天数
        budget = self._extract_number(user_input, default=10000)
        days = self._extract_days(user_input, default=5)
        
        recommendations = self.recommend_destinations(budget, days)
        
        response = f"🎯 根据您的预算¥{budget}和{days}天行程，为您推荐以下目的地：\n\n"
        for i, rec in enumerate(recommendations, 1):
            response += f"{i}. 【{rec['country']}】- {rec['budget_level']}游\n"
            response += f"   推荐城市: {', '.join(rec['cities'][:3])}\n"
            response += f"   预估费用: ¥{sum(rec['estimated_cost'].values())}\n"
            response += f"   签证: {'需要' if rec['visa_required'] else '免签/落地签'}\n"
            response += f"   亮点: {', '.join(rec['highlights'])}\n\n"
        
        return response
    
    def _handle_itinerary(self, user_input: str) -> str:
        """处理行程规划"""
        days = self._extract_days(user_input, default=5)
        destination = self._extract_destination(user_input) or "目的地"
        
        itinerary = self.create_itinerary(destination, days)
        
        response = f"🗺️ 【{destination}】{days}天行程规划：\n\n"
        for day in itinerary:
            response += f"📅 第{day['day']}天 - {day['theme']}\n"
            for activity in day['activities']:
                response += f"   {activity['time']} | {activity['type']}: {activity['description']}\n"
            response += "\n"
        
        return response
    
    def _handle_budget(self, user_input: str) -> str:
        """处理预算规划"""
        budget = self._extract_number(user_input, default=10000)
        days = self._extract_days(user_input, default=5)
        
        breakdown = {
            "✈️ 机票": int(budget * 0.3),
            "🏨 住宿": int(budget * 0.25),
            "🍽️ 餐饮": int(budget * 0.2),
            "🚗 交通": int(budget * 0.1),
            "🎫 门票": int(budget * 0.1),
            "🛍️ 购物": int(budget * 0.05)
        }
        
        response = f"💰 ¥{budget} 预算分配建议（{days}天）：\n\n"
        for item, cost in breakdown.items():
            response += f"{item}: ¥{cost}\n"
        response += f"\n日均消费: ¥{budget // days}\n"
        
        return response
    
    def _handle_packing_list(self, user_input: str) -> str:
        """处理行李清单"""
        days = self._extract_days(user_input, default=5)
        destination = self._extract_destination(user_input) or "目的地"
        
        packing_list = self.generate_packing_list(destination, days)
        
        response = f"🎒 【{destination}】{days}天旅行行李清单：\n\n"
        for category, items in packing_list.items():
            response += f"{category}:\n"
            for item in items:
                response += f"  □ {item}\n"
            response += "\n"
        
        return response
    
    def _handle_general(self, user_input: str) -> str:
        """处理一般询问"""
        return """您好！我是您的旅游规划小助手 🌍

我可以帮您：
1. 🎯 推荐旅游目的地 - 说"推荐旅游目的地"
2. 🗺️ 制定详细行程 - 说"帮我规划X天行程"
3. 💰 预算规划 - 说"预算X元怎么分配"
4. 🎒 生成行李清单 - 说"生成行李清单"

请告诉我您的需求，例如：
- "我想去日本旅游5天，预算1万元"
- "推荐适合亲子游的目的地"
- "帮我规划3天行程"""
    
    def _extract_number(self, text: str, default: int = 0) -> int:
        """提取数字"""
        import re
        numbers = re.findall(r'\d+', text)
        if numbers:
            return int(numbers[0])
        return default
    
    def _extract_days(self, text: str, default: int = 5) -> int:
        """提取天数"""
        import re
        match = re.search(r'(\d+)\s*天', text)
        if match:
            return int(match.group(1))
        return default
    
    def _extract_destination(self, text: str) -> Optional[str]:
        """提取目的地"""
        for country in self.destinations_db.keys():
            if country in text:
                return country
        return None

def main():
    """主程序"""
    print("=" * 60)
    print("🌍 欢迎使用旅游规划小助手！")
    print("=" * 60)
    print()
    
    agent = TravelPlannerAgent()
    
    # 显示欢迎信息
    print(agent._handle_general(""))
    print("-" * 60)
    
    # 交互模式
    while True:
        try:
            user_input = input("\n您: ").strip()
            if not user_input:
                continue
            if user_input.lower() in ["exit", "quit", "退出", "再见"]:
                print("\n👋 祝您旅途愉快！再见！")
                break
            
            response = agent.chat(user_input)
            print(f"\n🤖 小助手: {response}")
            
        except KeyboardInterrupt:
            print("\n\n👋 再见！")
            break
        except EOFError:
            break

if __name__ == "__main__":
    main()
