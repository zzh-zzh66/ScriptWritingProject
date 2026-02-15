# 场景描写组件
# 负责生成场景描写


class SceneDescriptionComponent:
    """
    场景描写组件
    
    负责生成场景描写
    """
    
    def __init__(self, data_manager):
        """
        初始化场景描写组件
        
        Args:
            data_manager (DataManager): 数据管理器
        """
        self.data_manager = data_manager
    
    def generate(self, time, location, items=None, state=None):
        """
        生成场景描写
        
        Args:
            time (str): 时间
            location (str): 地点
            items (list): 物品列表
            state (str): 状态
            
        Returns:
            str: 场景描写
        """
        content = f"△{time}，{location}"
        
        if items:
            content += f"，{', '.join(items)}"
        
        if state:
            content += f"，{state}"
        
        content += "。\n"
        return content
    
    def generate_from_scene_data(self, scene_name):
        """
        从场景数据生成场景描写
        
        Args:
            scene_name (str): 场景名称
            
        Returns:
            str: 场景描写
        """
        scenes = self.data_manager.get_scenes()
        if scene_name in scenes:
            scene = scenes[scene_name]
            return self.generate(
                time=scene.get("time", "日"),
                location=scene.get("name", scene_name),
                state=scene.get("description", "")
            )
        return f"△{scene_name}。\n"
    
    def generate_scene_header(self, scene_id, time, location_type, location_name):
        """
        生成场景标题
        
        Args:
            scene_id (str): 场景ID（如"1-1"）
            time (str): 时间（如"夜"）
            location_type (str): 地点类型（如"内"、"外"）
            location_name (str): 地点名称
            
        Returns:
            str: 场景标题
        """
        return f"{scene_id} {time} {location_type} {location_name}\n\n"
    
    def generate_scene_intro(self, location_name, episode):
        """
        生成场景介绍（金色字体）
        
        Args:
            location_name (str): 地点名称
            episode (int): 集数
            
        Returns:
            str: 场景介绍
        """
        return f"△金色字体，横向，悬浮在场景上方，显示：{location_name}\n"
