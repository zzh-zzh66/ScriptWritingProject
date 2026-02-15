# 一致性验证器
# 负责验证剧本内容的一致性，确保前后文不矛盾

import re


class ConsistencyValidator:
    """
    一致性验证器
    
    负责验证剧本内容的一致性，确保前后文不矛盾
    """
    
    def __init__(self, state_tracker):
        """
        初始化一致性验证器
        
        Args:
            state_tracker (StateTracker): 状态跟踪器
        """
        self.state_tracker = state_tracker
        
        self.forbidden_patterns = [
            r'眼神.*',
            r'声音(?!提示：).*',
            r'心里.*',
            r'气氛.*',
            r'像.*',
            r'如.*',
            r'冷冷地.*',
            r'狠狠地.*',
            r'轻轻.*',
            r'快速.*'
        ]
        
        self.ability_unlock_rules = {
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
        
        self.force_unlock_rules = {
            "六剑奴": 1,
            "百晓堂": 2,
            "七杀楼": 11,
            "大雪龙骑": 11,
            "白泽": 31
        }
        
        self.character_stage_rules = {
            "陆念离": {
                "前期": (1, 20),
                "中期": (21, 50),
                "后期": (51, 70)
            },
            "陆长乐": {
                "前期": (1, 20),
                "中期": (21, 50),
                "后期": (51, 70)
            }
        }
    
    def validate(self, episode, content):
        """
        验证剧本内容
        
        Args:
            episode (int): 集数
            content (str): 剧本内容
            
        Returns:
            dict: 验证结果
        """
        results = {
            "is_valid": True,
            "issues": [],
            "warnings": []
        }
        
        issues = []
        issues.extend(self._check_forbidden_patterns(content))
        issues.extend(self._check_ability_consistency(episode, content))
        issues.extend(self._check_force_consistency(episode, content))
        issues.extend(self._check_character_consistency(episode, content))
        issues.extend(self._check_description_length(content))
        issues.extend(self._check_consecutive_deltas(content))
        
        results["issues"] = issues
        results["is_valid"] = len(issues) == 0
        
        return results
    
    def _check_forbidden_patterns(self, content):
        """
        检查禁止模式
        
        Args:
            content (str): 剧本内容
            
        Returns:
            list: 问题列表
        """
        issues = []
        lines = content.split('\n')
        
        for i, line in enumerate(lines, 1):
            for pattern in self.forbidden_patterns:
                if re.search(pattern, line):
                    issues.append(f"第{i}行：发现禁止模式【{pattern}】：{line.strip()}")
        
        return issues
    
    def _check_ability_consistency(self, episode, content):
        """
        检查能力一致性
        
        Args:
            episode (int): 集数
            content (str): 剧本内容
            
        Returns:
            list: 问题列表
        """
        issues = []
        
        for ability, unlock_episode in self.ability_unlock_rules.items():
            if ability in content and episode < unlock_episode:
                issues.append(f"能力【{ability}】在第{episode}集出现，但应在第{unlock_episode}集后才解锁")
        
        return issues
    
    def _check_force_consistency(self, episode, content):
        """
        检查势力一致性
        
        Args:
            episode (int): 集数
            content (str): 剧本内容
            
        Returns:
            list: 问题列表
        """
        issues = []
        
        for force, unlock_episode in self.force_unlock_rules.items():
            if force in content and episode < unlock_episode:
                issues.append(f"势力【{force}】在第{episode}集出现，但应在第{unlock_episode}集后才解锁")
        
        return issues
    
    def _check_character_consistency(self, episode, content):
        """
        检查人物一致性
        
        Args:
            episode (int): 集数
            content (str): 剧本内容
            
        Returns:
            list: 问题列表
        """
        issues = []
        
        if "女帝" in content and episode < 31:
            issues.append(f"人物【陆长乐】在第{episode}集被称为女帝，但应在第31集后才登基")
        
        if "一字并肩王" in content and episode < 11:
            issues.append(f"人物【陆念离】在第{episode}集被称为一字并肩王，但应在第11集后才封王")
        
        return issues
    
    def _check_description_length(self, content):
        """
        检查描写长度
        
        Args:
            content (str): 剧本内容
            
        Returns:
            list: 问题列表
        """
        issues = []
        lines = content.split('\n')
        
        for i, line in enumerate(lines, 1):
            if line.startswith('△'):
                desc = line[1:].strip()
                if len(desc) > 50:
                    issues.append(f"第{i}行：描写过长（{len(desc)}字），建议拆分：{desc[:30]}...")
        
        return issues
    
    def _check_consecutive_deltas(self, content):
        """
        检查连续△数量
        
        Args:
            content (str): 剧本内容
            
        Returns:
            list: 问题列表
        """
        issues = []
        lines = content.split('\n')
        consecutive_count = 0
        start_line = 0
        
        for i, line in enumerate(lines, 1):
            if line.startswith('△'):
                if consecutive_count == 0:
                    start_line = i
                consecutive_count += 1
            else:
                if consecutive_count > 4:
                    issues.append(f"第{start_line}-{i-1}行：连续{consecutive_count}个△，建议穿插对话或声音")
                consecutive_count = 0
        
        if consecutive_count > 4:
            issues.append(f"第{start_line}-{len(lines)}行：连续{consecutive_count}个△，建议穿插对话或声音")
        
        return issues
    
    def validate_character_intro(self, content, character_name):
        """
        验证人物出场顺序
        
        Args:
            content (str): 剧本内容
            character_name (str): 人物名称
            
        Returns:
            bool: 是否符合规则
        """
        lines = content.split('\n')
        has_appearance = False
        has_floating_text = False
        appearance_line = 0
        floating_text_line = 0
        
        for i, line in enumerate(lines, 1):
            if character_name in line and line.startswith('△') and '金色字体' not in line:
                has_appearance = True
                appearance_line = i
            if character_name in line and '金色字体' in line:
                has_floating_text = True
                floating_text_line = i
        
        if has_appearance and has_floating_text:
            return appearance_line < floating_text_line
        
        return True
    
    def validate_scene_description(self, content):
        """
        验证场景描写格式
        
        Args:
            content (str): 剧本内容
            
        Returns:
            list: 问题列表
        """
        issues = []
        lines = content.split('\n')
        
        for i, line in enumerate(lines, 1):
            if line.startswith('△') and '金色字体' not in line:
                if '，' not in line and '。' not in line:
                    issues.append(f"第{i}行：场景描写格式不正确，应为'时间+地点+物品+状态'格式")
        
        return issues
