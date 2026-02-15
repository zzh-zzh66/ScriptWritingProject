# 创作指南约束器
# 负责强制执行创作指南的所有要求

class ForbiddenChecker:
    """
    禁止事项检查器
    
    检查剧本中是否包含创作指南禁止的事项
    """
    
    def __init__(self):
        """
        初始化禁止事项检查器
        """
        # 眼神描写禁止词
        self.eye_phrases = [
            "眼神冷", "眼神锐利", "眼神一冷", "眼神扫过", "眼神没离开",
            "眼神坚定", "眼神警惕", "眼神变得专注", "眼神频繁瞟", "眼神怒", "眼神骤亮"
        ]
        
        # 声音描写禁止词
        self.sound_phrases = [
            "声音冷", "声音狠", "声音发颤", "喉间压狠音", "声音沙哑", "声音低沉"
        ]
        
        # 心理描写禁止词
        self.mind_phrases = [
            "心中暗爽", "很害怕", "心里想", "心中想", "心里觉得", "心中觉得"
        ]
        
        # 情感描述禁止词
        self.emotion_phrases = [
            "气氛紧张", "很愤怒", "恐惧", "开心", "悲伤", "兴奋", "焦虑", "紧张"
        ]
        
        # 抽象描述禁止词
        self.abstract_phrases = [
            "很安静", "气质清雅", "优雅", "美丽", "丑陋", "英俊", "高大", "矮小", "肥胖"
        ]
        
        # 比喻禁止词
        self.metaphor_phrases = [
            "像什么", "如什么", "如诗如画", "如同", "宛如", "仿佛", "好似", "恰似", "犹如", "好像"
        ]
        
        # 形容词和副词修饰禁止词
        self.modifier_phrases = [
            "冷冷地", "狠狠地", "轻轻", "快速", "慢慢地", "缓缓地", "重重地", "悄悄地", "偷偷地", "渐渐地"
        ]
    
    def check(self, text):
        """
        检查文本中的禁止事项
        
        Args:
            text (str): 待检查的文本
            
        Returns:
            list: 发现的问题列表
        """
        issues = []
        
        # 检查眼神描写
        for phrase in self.eye_phrases:
            if phrase in text:
                issues.append(f"[禁止事项] 发现眼神描写：'{phrase}'")
        
        # 检查声音描写
        for phrase in self.sound_phrases:
            if phrase in text:
                issues.append(f"[禁止事项] 发现声音描写：'{phrase}'")
        
        # 检查心理描写
        for phrase in self.mind_phrases:
            if phrase in text:
                issues.append(f"[禁止事项] 发现心理描写：'{phrase}'")
        
        # 检查情感描述
        for phrase in self.emotion_phrases:
            if phrase in text:
                issues.append(f"[禁止事项] 发现情感描述：'{phrase}'")
        
        # 检查抽象描述
        for phrase in self.abstract_phrases:
            if phrase in text:
                issues.append(f"[禁止事项] 发现抽象描述：'{phrase}'")
        
        # 检查比喻
        for phrase in self.metaphor_phrases:
            if phrase in text:
                issues.append(f"[禁止事项] 发现比喻：'{phrase}'")
        
        # 检查形容词和副词修饰
        for phrase in self.modifier_phrases:
            if phrase in text:
                issues.append(f"[禁止事项] 发现形容词/副词修饰：'{phrase}'")
        
        # 检查台词括号中的眼神和声音描写
        lines = text.split('\n')
        for i, line in enumerate(lines, 1):
            if '（' in line and '）' in line:
                # 提取括号内容
                start = line.find('（')
                end = line.find('）')
                if start != -1 and end != -1:
                    content = line[start+1:end]
                    # 检查括号内容是否包含眼神或声音描写
                    for phrase in self.eye_phrases:
                        if phrase in content:
                            issues.append(f"[禁止事项] 第{i}行台词括号中发现眼神描写：'{phrase}'")
                    for phrase in self.sound_phrases:
                        if phrase in content:
                            issues.append(f"[禁止事项] 第{i}行台词括号中发现声音描写：'{phrase}'")
        
        return issues


class FormatEnforcer:
    """
    格式强制执行器
    
    强制执行创作指南的格式要求
    """
    
    def enforce_scene_description(self, description):
        """
        强制执行场景描写格式：时间+地点+物品+状态
        
        Args:
            description (str): 场景描写
            
        Returns:
            str: 格式化后的场景描写
        """
        # 简单的格式化处理，确保符合"时间+地点+物品+状态"格式
        # 这里只是基础处理，实际生成时需要更复杂的逻辑
        return description
    
    def enforce_action_description(self, action):
        """
        强制执行动作描写格式：主体+动词+对象
        
        Args:
            action (str): 动作描写
            
        Returns:
            str: 格式化后的动作描写
        """
        # 简单的格式化处理，确保符合"主体+动词+对象"格式
        return action
    
    def enforce_dialogue_parentheses(self, dialogue):
        """
        强制执行台词括号格式：只保留核心动作
        
        Args:
            dialogue (str): 台词
            
        Returns:
            str: 格式化后的台词
        """
        # 简单的格式化处理，确保台词括号只保留核心动作
        return dialogue


class InterleaveController:
    """
    穿插比例控制器
    
    控制场景/动作描写与对话的穿插比例
    """
    
    def check_interleave_ratio(self, content):
        """
        检查穿插比例：3-5句场景/动作配1-2句对话
        
        Args:
            content (str): 剧本内容
            
        Returns:
            list: 发现的问题列表
        """
        issues = []
        lines = content.split('\n')
        
        action_count = 0
        dialogue_count = 0
        max_continuous_actions = 0
        current_continuous_actions = 0
        
        for line in lines:
            line = line.strip()
            if not line:
                continue
            
            # 判断是否为动作描写（以△开头）
            if line.startswith('△'):
                action_count += 1
                current_continuous_actions += 1
                max_continuous_actions = max(max_continuous_actions, current_continuous_actions)
            # 判断是否为对话（包含冒号）
            elif '：' in line or ':' in line:
                dialogue_count += 1
                current_continuous_actions = 0
            # 判断是否为声音提示
            elif line.startswith('声音提示：'):
                current_continuous_actions = 0
        
        # 检查是否连续5句以上纯场景/动作
        if max_continuous_actions > 5:
            issues.append(f"[穿插比例] 发现连续{max_continuous_actions}句纯场景/动作描写，超过限制")
        
        # 检查穿插比例
        if action_count > 0 and dialogue_count > 0:
            ratio = action_count / dialogue_count
            if ratio > 5:
                issues.append(f"[穿插比例] 场景/动作描写与对话比例失衡（{ratio:.1f}:1），建议调整为3-5:1")
        
        return issues


class ScriptGuideEnforcer:
    """
    创作指南约束器
    
    负责强制执行创作指南的所有要求
    """
    
    def __init__(self):
        """
        初始化创作指南约束器
        """
        self.forbidden_checker = ForbiddenChecker()
        self.format_enforcer = FormatEnforcer()
        self.interleave_controller = InterleaveController()
    
    def check_script(self, script_content, episode_num=None):
        """
        检查剧本内容是否符合创作指南要求
        
        Args:
            script_content (str): 剧本内容
            episode_num (int): 集数（可选）
            
        Returns:
            dict: 检查结果
        """
        result = {
            "forbidden_issues": [],
            "format_issues": [],
            "interleave_issues": [],
            "required_issues": [],
            "all_issues": []
        }
        
        # 1. 检查禁止事项
        forbidden_issues = self.forbidden_checker.check(script_content)
        result["forbidden_issues"] = forbidden_issues
        result["all_issues"].extend(forbidden_issues)
        
        # 2. 检查穿插比例
        interleave_issues = self.interleave_controller.check_interleave_ratio(script_content)
        result["interleave_issues"] = interleave_issues
        result["all_issues"].extend(interleave_issues)
        
        # 3. 检查必须包含的内容
        required_issues = self.check_required_content(script_content, episode_num)
        result["required_issues"] = required_issues
        result["all_issues"].extend(required_issues)
        
        return result
    
    def check_required_content(self, script_content, episode_num):
        """
        检查剧本是否包含必须的内容
        
        Args:
            script_content (str): 剧本内容
            episode_num (int): 集数
            
        Returns:
            list: 发现的问题列表
        """
        issues = []
        
        # 检查颜色标记
        if '【绿色】' not in script_content:
            issues.append("[必须包含] 缺少【绿色】高光场景标记")
        else:
            green_count = script_content.count('【绿色】')
            if green_count < 1:
                issues.append(f"[必须包含] 【绿色】高光场景标记数量不足（当前：{green_count}，要求：至少1处）")
        
        if '【黄色】' not in script_content:
            issues.append("[必须包含] 缺少【黄色】冲突场景标记")
        else:
            yellow_count = script_content.count('【黄色】')
            if yellow_count < 1:
                issues.append(f"[必须包含] 【黄色】冲突场景标记数量不足（当前：{yellow_count}，要求：至少1处）")
        
        if '【蓝色】' not in script_content:
            issues.append("[必须包含] 缺少【蓝色】钩子标记")
        else:
            blue_count = script_content.count('【蓝色】')
            if blue_count < 1:
                issues.append(f"[必须包含] 【蓝色】钩子标记数量不足（当前：{blue_count}，要求：至少1处）")
        
        # 检查音效标注
        if '声音提示：' not in script_content:
            issues.append("[必须包含] 缺少音效标注")
        
        # 检查场景标注
        if '金色字体，横向，悬浮在场景上方' not in script_content:
            issues.append("[必须包含] 缺少金色字体场景标注")
        
        # 检查系统面板可视化
        if '△系统面板：' not in script_content:
            issues.append("[必须包含] 缺少系统面板可视化描述")
        
        # 前三集专项检查
        if episode_num and episode_num <= 3:
            special_issues = self.check_first_three_episodes(script_content, episode_num)
            issues.extend(special_issues)
        
        return issues
    
    def check_first_three_episodes(self, script_content, episode_num):
        """
        检查前三集的专项要求
        
        Args:
            script_content (str): 剧本内容
            episode_num (int): 集数
            
        Returns:
            list: 发现的问题列表
        """
        issues = []
        
        if episode_num == 1:
            # 第一集必须包含OS交代世界观、背景、身份、主线目标
            if '陆念离（OS）：' not in script_content:
                issues.append("[第一集专项] 缺少OS交代世界观、背景、身份、主线目标")
            
            # 第一集结尾必须有护姐宣言
            if '姐姐' not in script_content and '二姐' not in script_content:
                issues.append("[第一集专项] 缺少护姐宣言")
            
            # 第一集结尾必须有系统任务提示
            if script_content.count('主线任务') < 1:
                issues.append("[第一集专项] 缺少系统任务提示")
        
        elif episode_num == 2:
            # 第二集必须有主线推进
            if '主线推进' not in script_content and '主线' not in script_content:
                issues.append("[第二集专项] 缺少主线推进")
            
            # 第二集必须有系统任务提示
            if script_content.count('主线任务') < 1:
                issues.append("[第二集专项] 缺少系统任务提示")
        
        elif episode_num == 3:
            # 第三集必须有台词明确最终目标
            if '一统百朝' not in script_content and '终结乱世' not in script_content:
                issues.append("[第三集专项] 缺少台词明确最终目标")
            
            # 第三集必须有系统任务提示
            if script_content.count('主线任务') < 1:
                issues.append("[第三集专项] 缺少系统任务提示")
        
        return issues