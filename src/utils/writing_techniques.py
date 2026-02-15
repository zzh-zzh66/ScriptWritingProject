# 新写作技巧模块
# 实现创作指南中的新写作技巧：金色字体、系统面板、旁白、俯视图

class GoldenTextGenerator:
    """
    金色字体生成器
    
    生成金色字体浮动描写，用于人物介绍和场景标注
    """
    
    def generate_character_intro(self, character_name, background):
        """
        生成金色字体人物介绍
        
        Args:
            character_name (str): 人物名
            background (str): 身份背景
            
        Returns:
            str: 金色字体人物介绍
        """
        # 格式：△金色字体，竖向，悬浮在人物旁边，显示：人物名：身份背景
        return f"△金色字体，竖向，悬浮在人物旁边，显示：{character_name}：{background}"
    
    def generate_scene_label(self, location_name):
        """
        生成金色字体场景标注
        
        Args:
            location_name (str): 地点名
            
        Returns:
            str: 金色字体场景标注
        """
        # 格式：△金色字体，横向，悬浮在场景上方，显示：地点名
        return f"△金色字体，横向，悬浮在场景上方，显示：{location_name}"


class SystemPanelGenerator:
    """
    系统面板生成器
    
    生成系统面板可视化描述
    """
    
    def generate_system_panel(self, content):
        """
        生成系统面板可视化描述
        
        Args:
            content (str): 面板内容
            
        Returns:
            str: 系统面板可视化描述
        """
        # 格式：△系统面板：可视化描述
        return f"△系统面板：{content}"
    
    def generate_task_panel(self, task_name, progress, description):
        """
        生成任务面板
        
        Args:
            task_name (str): 任务名
            progress (str): 进度
            description (str): 任务描述
            
        Returns:
            str: 任务面板描述
        """
        content = f"{task_name}，当前进度{progress}"
        if description:
            content += f"，{description}"
        return self.generate_system_panel(content)
    
    def generate_reward_panel(self, reward_description):
        """
        生成奖励面板
        
        Args:
            reward_description (str): 奖励描述
            
        Returns:
            str: 奖励面板描述
        """
        return self.generate_system_panel(reward_description)
    
    def generate_warning_panel(self, warning_message, danger_level):
        """
        生成警告面板
        
        Args:
            warning_message (str): 警告信息
            danger_level (str): 危险等级
            
        Returns:
            str: 警告面板描述
        """
        content = f"{warning_message}，危险等级：{danger_level}"
        return self.generate_system_panel(content)


class NarratorGenerator:
    """
    旁白生成器
    
    生成简单直白的旁白
    """
    
    def generate_narrator(self, world_info):
        """
        生成旁白
        
        Args:
            world_info (str): 世界观信息
            
        Returns:
            str: 旁白
        """
        # 格式：旁白：简单直白，清楚交代信息
        return f"旁白：{world_info}"
    
    def generate_world_view_narrator(self, world_name, power_structure, main_conflict):
        """
        生成世界观旁白
        
        Args:
            world_name (str): 世界名称
            power_structure (str): 势力结构
            main_conflict (str): 主要冲突
            
        Returns:
            str: 世界观旁白
        """
        world_info = f"{world_name}，{power_structure}，{main_conflict}"
        return self.generate_narrator(world_info)


class TopViewGenerator:
    """
    俯视图生成器
    
    生成俯视图描述
    """
    
    def generate_top_view(self, scene_description):
        """
        生成俯视图
        
        Args:
            scene_description (str): 场景描述
            
        Returns:
            str: 俯视图描述
        """
        # 格式：△俯视图：场景描述
        return f"△俯视图：{scene_description}"
    
    def generate_location_top_view(self, location_name, key_positions):
        """
        生成地点俯视图
        
        Args:
            location_name (str): 地点名称
            key_positions (str): 关键位置描述
            
        Returns:
            str: 地点俯视图描述
        """
        scene_description = f"{location_name}，{key_positions}"
        return self.generate_top_view(scene_description)


class WritingTechniques:
    """
    写作技巧集合
    
    整合所有新写作技巧
    """
    
    def __init__(self):
        """
        初始化写作技巧集合
        """
        self.golden_text = GoldenTextGenerator()
        self.system_panel = SystemPanelGenerator()
        self.narrator = NarratorGenerator()
        self.top_view = TopViewGenerator()
    
    def generate_opening_scene(self, location_name, world_info, key_positions=None):
        """
        生成开场场景（包含金色字体标注、俯视图、旁白）
        
        Args:
            location_name (str): 地点名称
            world_info (str): 世界观信息
            key_positions (str): 关键位置描述（可选）
            
        Returns:
            str: 开场场景描述
        """
        content = ""
        
        # 1. 金色字体场景标注
        content += self.golden_text.generate_scene_label(location_name) + "\n"
        
        # 2. 俯视图
        if key_positions:
            content += self.top_view.generate_location_top_view(location_name, key_positions) + "\n"
        
        # 3. 旁白
        content += self.narrator.generate_narrator(world_info) + "\n"
        
        return content
    
    def generate_character_introduction(self, character_name, background):
        """
        生成人物介绍（包含金色字体人物介绍）
        
        Args:
            character_name (str): 人物名
            background (str): 身份背景
            
        Returns:
            str: 人物介绍描述
        """
        return self.golden_text.generate_character_intro(character_name, background)
    
    def generate_system_activation(self, system_name, abilities, rewards):
        """
        生成系统激活描述（包含系统面板可视化）
        
        Args:
            system_name (str): 系统名称
            abilities (list): 能力列表
            rewards (list): 奖励列表
            
        Returns:
            str: 系统激活描述
        """
        content = ""
        
        # 生成系统面板内容
        panel_content = f"{system_name}绑定成功！"
        if abilities:
            abilities_str = "、".join(abilities)
            panel_content += f"激活能力：{abilities_str}"
        if rewards:
            rewards_str = "、".join(rewards)
            panel_content += f"，奖励：{rewards_str}"
        
        content += self.system_panel.generate_system_panel(panel_content) + "\n"
        content += "声音提示：叮（系统提示音）\n"
        content += f"系统：{panel_content}\n"
        
        return content
    
    def generate_task_assignment(self, task_name, progress, description, deadline=None):
        """
        生成任务分配描述（包含系统面板可视化）
        
        Args:
            task_name (str): 任务名称
            progress (str): 进度
            description (str): 任务描述
            deadline (str): 截止时间（可选）
            
        Returns:
            str: 任务分配描述
        """
        content = ""
        
        # 生成任务面板
        panel_content = f"{task_name}，当前进度{progress}，{description}"
        if deadline:
            panel_content += f"，截止时间：{deadline}"
        
        content += self.system_panel.generate_task_panel(task_name, progress, panel_content) + "\n"
        content += "声音提示：叮（系统提示音）\n"
        content += f"系统：{task_name}已发布！\n"
        
        return content
    
    def generate_reward_notification(self, reward_type, amount, description):
        """
        生成奖励通知描述（包含系统面板可视化）
        
        Args:
            reward_type (str): 奖励类型
            amount (str): 数量
            description (str): 描述
            
        Returns:
            str: 奖励通知描述
        """
        content = ""
        
        # 生成奖励面板
        panel_content = f"{reward_type}+{amount}，{description}"
        
        content += self.system_panel.generate_reward_panel(panel_content) + "\n"
        content += "声音提示：叮（系统提示音）\n"
        content += f"系统：{reward_type}到账！\n"
        
        return content
    
    def generate_warning_notification(self, warning_message, danger_level):
        """
        生成警告通知描述（包含系统面板可视化）
        
        Args:
            warning_message (str): 警告信息
            danger_level (str): 危险等级
            
        Returns:
            str: 警告通知描述
        """
        content = ""
        
        # 生成警告面板
        content += self.system_panel.generate_warning_panel(warning_message, danger_level) + "\n"
        content += "声音提示：警告（系统提示音）\n"
        content += f"系统：检测到{warning_message}！\n"
        
        return content