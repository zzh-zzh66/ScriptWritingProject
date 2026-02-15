# 剧情摘要解析器
# 负责解析剧情摘要.md文件，提取各阶段摘要信息

from parser.markdown_parser import MarkdownParser


class PlotSummaryParser:
    """
    剧情摘要解析器
    
    负责解析剧情摘要.md文件，提取各阶段摘要信息
    """
    
    def __init__(self):
        self.md_parser = MarkdownParser()
    
    def parse_file(self, file_path):
        """
        解析剧情摘要.md文件
        
        Args:
            file_path (str): 文件路径
            
        Returns:
            dict: 摘要字典，键为阶段名称，值为摘要信息
        """
        try:
            content = self.md_parser.parse_file(file_path)
            summaries = self.parse_content(content)
            return summaries
        except Exception as e:
            print(f"解析剧情摘要文件失败: {e}")
            return {}
    
    def parse_content(self, content):
        """
        解析剧情摘要文本内容
        
        Args:
            content (str): 剧情摘要文本内容
            
        Returns:
            dict: 摘要字典
        """
        summaries = {}
        lines = content.split('\n')
        current_stage = None
        current_content = []
        in_block = False
        
        for line in lines:
            line = line.strip()
            
            if line.startswith('## 第') and '集摘要' in line:
                if current_stage and current_content:
                    summaries[current_stage] = self.parse_stage_content('\n'.join(current_content))
                current_stage = line.replace('## ', '').replace('摘要', '').strip()
                current_content = []
                in_block = False
            elif line.startswith('```'):
                in_block = not in_block
            elif current_stage and in_block and line:
                current_content.append(line)
        
        if current_stage and current_content:
            summaries[current_stage] = self.parse_stage_content('\n'.join(current_content))
        
        return summaries
    
    def parse_stage_content(self, content):
        """
        解析单个阶段摘要内容
        
        Args:
            content (str): 阶段摘要内容
            
        Returns:
            dict: 阶段摘要信息
        """
        stage_info = {
            "core_plot": "",
            "key_characters": "",
            "important_events": "",
            "current_status": "",
            "key_settings": ""
        }
        
        lines = content.split('\n')
        for line in lines:
            line = line.strip()
            if line.startswith('【核心剧情推进】'):
                stage_info["core_plot"] = line.replace('【核心剧情推进】', '').strip()
            elif line.startswith('【关键人物状态】'):
                stage_info["key_characters"] = line.replace('【关键人物状态】', '').strip()
            elif line.startswith('【重要事件】'):
                stage_info["important_events"] = line.replace('【重要事件】', '').strip()
            elif line.startswith('【当前状态】'):
                stage_info["current_status"] = line.replace('【当前状态】', '').strip()
            elif line.startswith('【关键设定】'):
                stage_info["key_settings"] = line.replace('【关键设定】', '').strip()
        
        return stage_info
    
    def get_summary(self, summaries, episode):
        """
        获取指定集数的摘要
        
        Args:
            summaries (dict): 摘要字典
            episode (int): 集数
            
        Returns:
            dict: 摘要信息或None
        """
        if episode <= 10:
            key = "1-10集"
        elif episode <= 20:
            key = "11-20集"
        elif episode <= 30:
            key = "21-30集"
        elif episode <= 40:
            key = "31-40集"
        elif episode <= 50:
            key = "41-50集"
        elif episode <= 60:
            key = "51-60集"
        else:
            key = "61-70集"
        
        return summaries.get(key)
    
    def get_stage_range(self, episode):
        """
        获取指定集数所属的阶段范围
        
        Args:
            episode (int): 集数
            
        Returns:
            tuple: (起始集, 结束集)
        """
        if episode <= 10:
            return (1, 10)
        elif episode <= 20:
            return (11, 20)
        elif episode <= 30:
            return (21, 30)
        elif episode <= 40:
            return (31, 40)
        elif episode <= 50:
            return (41, 50)
        elif episode <= 60:
            return (51, 60)
        else:
            return (61, 70)
