# 系统面板组件
# 负责生成系统面板描写


class SystemPanelComponent:
    """
    系统面板组件
    
    负责生成系统面板描写
    """
    
    def __init__(self):
        """
        初始化系统面板组件
        """
        pass
    
    def generate(self, content, color="green"):
        """
        生成系统面板
        
        Args:
            content (str): 面板内容
            color (str): 颜色标记
            
        Returns:
            str: 系统面板内容
        """
        return f"【{color.upper()}】△系统面板：半空中浮现淡蓝色透明面板，上面写着\"{content}\"\n"
    
    def generate_binding_success(self, rewards):
        """
        生成系统绑定成功面板
        
        Args:
            rewards (list): 奖励列表
            
        Returns:
            str: 系统面板内容
        """
        content = f"系统绑定成功！新手大礼包激活：{', '.join(rewards)}！"
        return self.generate(content)
    
    def generate_task(self, task_name, description, reward, penalty=None):
        """
        生成任务面板
        
        Args:
            task_name (str): 任务名称
            description (str): 任务描述
            reward (str): 奖励
            penalty (str): 惩罚
            
        Returns:
            str: 任务面板内容
        """
        content = f"{task_name}：{description}，奖励{reward}"
        if penalty:
            content += f"！{penalty}"
        else:
            content += "！"
        return self.generate(content)
    
    def generate_task_complete(self, time_used, reward):
        """
        生成任务完成面板
        
        Args:
            time_used (str): 用时
            reward (str): 奖励
            
        Returns:
            str: 任务完成面板内容
        """
        content = f"任务完成（耗时{time_used}）！{reward}到账！"
        return self.generate(content)
    
    def generate_main_quest(self, description, progress, reward):
        """
        生成主线任务面板
        
        Args:
            description (str): 任务描述
            progress (str): 进度
            reward (str): 奖励
            
        Returns:
            str: 主线任务面板内容
        """
        content = f"主线任务已激活：{description}。当前进度：{progress}。奖励：{reward}。"
        return self.generate(content)
    
    def generate_warning(self, content, danger_level=1):
        """
        生成警告面板
        
        Args:
            content (str): 警告内容
            danger_level (int): 危险等级（1-5）
            
        Returns:
            str: 警告面板内容
        """
        stars = "★" * danger_level
        return f"【BLUE】△系统面板：半空中浮现淡蓝色透明面板，上面显示\"{content}，危险等级：{stars}\"\n"
