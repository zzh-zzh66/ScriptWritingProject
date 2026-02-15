# 状态跟踪器
# 负责跟踪人物状态、势力状态、事件状态，确保前后文一致性

import json
import os


class StateTracker:
    """
    状态跟踪器
    
    负责跟踪人物状态、势力状态、事件状态，确保前后文一致性
    """
    
    def __init__(self, data_manager):
        """
        初始化状态跟踪器
        
        Args:
            data_manager (DataManager): 数据管理器
        """
        self.data_manager = data_manager
        self.state_file = "data/state.json"
        self.state = {
            "characters": {},
            "forces": {},
            "abilities": {},
            "items": {},
            "events": [],
            "current_episode": 0
        }
        self._load_state()
    
    def _load_state(self):
        """加载状态文件"""
        if os.path.exists(self.state_file):
            try:
                with open(self.state_file, 'r', encoding='utf-8') as f:
                    self.state = json.load(f)
            except Exception as e:
                print(f"加载状态文件失败: {e}")
    
    def _save_state(self):
        """保存状态文件"""
        try:
            os.makedirs(os.path.dirname(self.state_file), exist_ok=True)
            with open(self.state_file, 'w', encoding='utf-8') as f:
                json.dump(self.state, f, ensure_ascii=False, indent=2)
        except Exception as e:
            print(f"保存状态文件失败: {e}")
    
    def get_character_stage(self, character_name, episode):
        """
        获取人物在指定集数的阶段
        
        Args:
            character_name (str): 人物名称
            episode (int): 集数
            
        Returns:
            str: 阶段名称（前期/中期/后期）
        """
        if episode <= 20:
            return "前期"
        elif episode <= 50:
            return "中期"
        else:
            return "后期"
    
    def get_character_state(self, character_name, episode):
        """
        获取人物在指定集数的状态
        
        Args:
            character_name (str): 人物名称
            episode (int): 集数
            
        Returns:
            dict: 人物状态信息
        """
        characters = self.data_manager.get_characters()
        if character_name not in characters:
            return None
        
        character = characters[character_name]
        stage = self.get_character_stage(character_name, episode)
        
        if "stages" in character and stage in character["stages"]:
            return character["stages"][stage]
        return None
    
    def get_character_appearance(self, character_name, episode):
        """
        获取人物在指定集数的外貌描写
        
        Args:
            character_name (str): 人物名称
            episode (int): 集数
            
        Returns:
            str: 外貌描写
        """
        state = self.get_character_state(character_name, episode)
        if state and "appearance" in state:
            return state["appearance"]
        return ""
    
    def get_character_identity(self, character_name, episode):
        """
        获取人物在指定集数的身份
        
        Args:
            character_name (str): 人物名称
            episode (int): 集数
            
        Returns:
            str: 身份
        """
        state = self.get_character_state(character_name, episode)
        if state and "identity" in state:
            return state["identity"]
        return ""
    
    def update_episode_state(self, episode, events):
        """
        更新剧集状态
        
        Args:
            episode (int): 集数
            events (list): 事件列表
        """
        self.state["current_episode"] = episode
        for event in events:
            if event not in self.state["events"]:
                self.state["events"].append({
                    "episode": episode,
                    "event": event
                })
        self._save_state()
    
    def is_ability_unlocked(self, ability_name, episode):
        """
        检查能力是否已解锁
        
        Args:
            ability_name (str): 能力名称
            episode (int): 集数
            
        Returns:
            bool: 是否已解锁
        """
        ability_unlock_rules = {
            "苍生笔": 1,
            "修罗剑意": 1,
            "六剑奴": 1,
            "百晓堂": 2,
            "血咒检测": 4,
            "气运画技": 5,
            "酒道通神": 21,
            "白泽": 31,
            "乾坤画轴": 31,
            "镇魔画道": 41
        }
        
        unlock_episode = ability_unlock_rules.get(ability_name, 0)
        return episode >= unlock_episode
    
    def is_item_unlocked(self, item_name, episode):
        """
        检查道具是否已解锁
        
        Args:
            item_name (str): 道具名称
            episode (int): 集数
            
        Returns:
            bool: 是否已解锁
        """
        item_unlock_rules = {
            "苍生笔": 1,
            "玉画筒": 1,
            "乾坤画轴雏形": 11,
            "乾坤画轴": 31,
            "镇魔苍生笔": 41
        }
        
        unlock_episode = item_unlock_rules.get(item_name, 0)
        return episode >= unlock_episode
    
    def is_force_unlocked(self, force_name, episode):
        """
        检查势力是否已解锁
        
        Args:
            force_name (str): 势力名称
            episode (int): 集数
            
        Returns:
            bool: 是否已解锁
        """
        force_unlock_rules = {
            "六剑奴": 1,
            "百晓堂": 2,
            "七杀楼": 11,
            "大雪龙骑": 11,
            "白泽": 31
        }
        
        unlock_episode = force_unlock_rules.get(force_name, 0)
        return episode >= unlock_episode
    
    def get_current_plot_stage(self, episode):
        """
        获取当前剧情阶段
        
        Args:
            episode (int): 集数
            
        Returns:
            dict: 剧情阶段信息
        """
        plot_stages = [
            {"stage": 1, "name": "朝堂生存战", "range": (1, 10), "description": "主角vs太子+皇后+外戚，核心：保命、护姐、夺权"},
            {"stage": 2, "name": "东土统一战", "range": (11, 20), "description": "主角vs太子残党+大明+暗黑势力，核心：整合势力、平定东土"},
            {"stage": 3, "name": "北荒边患战", "range": (21, 30), "description": "主角vs兽化人+蛮族+暗黑血咒，核心：解除诅咒、收复北荒"},
            {"stage": 4, "name": "百朝争霸战", "range": (31, 40), "description": "主角vs南林/西沼/大明联军，核心：一统天下版图"},
            {"stage": 5, "name": "盛世肃清战", "range": (41, 50), "description": "主角vs魔神残魂+叛乱势力，核心：守护太平、清除内患"},
            {"stage": 6, "name": "神魔终极战", "range": (51, 60), "description": "主角vs上古暗黑魔神，核心：世界存亡、三界安危"},
            {"stage": 7, "name": "本心抉择战", "range": (61, 70), "description": "主角vs权位束缚，核心：拒绝仙帝之位，坚守摆烂初心"}
        ]
        
        for stage_info in plot_stages:
            if stage_info["range"][0] <= episode <= stage_info["range"][1]:
                return stage_info
        return None
    
    def check_consistency(self, episode, content):
        """
        检查内容一致性
        
        Args:
            episode (int): 集数
            content (str): 剧本内容
            
        Returns:
            list: 问题列表
        """
        issues = []
        
        ability_keywords = {
            "苍生笔": 1,
            "修罗剑意": 1,
            "六剑奴": 1,
            "百晓堂": 2,
            "血咒检测": 4,
            "酒道通神": 21,
            "白泽": 31,
            "乾坤画轴": 31
        }
        
        for ability, unlock_episode in ability_keywords.items():
            if ability in content and episode < unlock_episode:
                issues.append(f"能力【{ability}】在第{episode}集出现，但应在第{unlock_episode}集后才解锁")
        
        return issues
