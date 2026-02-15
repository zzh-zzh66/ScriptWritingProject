# 剧情大纲解析器
# 负责解析剧情大纲目录下的所有文件，提取每集的剧情大纲

import os
import re
from .markdown_parser import MarkdownParser

class OutlineParser:
    """
    剧情大纲解析器
    
    负责解析剧情大纲目录下的所有文件，提取每集的剧情大纲
    """
    
    def __init__(self):
        """
        初始化剧情大纲解析器
        """
        self.md_parser = MarkdownParser()
    
    def parse_directory(self, directory_path):
        """
        解析剧情大纲目录
        
        Args:
            directory_path (str): 目录路径
            
        Returns:
            dict: 剧情大纲字典，键为集数，值为剧情大纲
        """
        outlines = {}
        
        try:
            # 遍历目录下的所有文件
            for filename in os.listdir(directory_path):
                if filename.endswith('.md') and filename != '剧情摘要.md':
                    file_path = os.path.join(directory_path, filename)
                    # 解析单个文件
                    file_outlines = self.parse_file(file_path)
                    # 合并剧情大纲
                    outlines.update(file_outlines)
            
            # 解析剧情摘要
            summary_path = os.path.join(directory_path, '剧情摘要.md')
            if os.path.exists(summary_path):
                summary = self.parse_summary(summary_path)
                outlines['summary'] = summary
            
            return outlines
        except Exception as e:
            print(f"解析剧情大纲目录失败: {e}")
            return {}
    
    def parse_file(self, file_path):
        """
        解析单个剧情大纲文件
        
        Args:
            file_path (str): 文件路径
            
        Returns:
            dict: 剧情大纲字典
        """
        outlines = {}
        
        try:
            # 读取文件内容
            content = self.md_parser.parse_file(file_path)
            # 提取文件名中的集数范围
            filename = os.path.basename(file_path)
            
            # 解析集数范围（如「剧情大纲1-10.md」）
            if '剧情大纲' in filename:
                # 提取数字部分
                match = re.search(r'剧情大纲(\d+)-(\d+)\.md', filename)
                if match:
                    start_episode = int(match.group(1))
                    end_episode = int(match.group(2))
                    
                    # 解析每集的剧情大纲
                    for i in range(start_episode, end_episode + 1):
                        # 查找对应集数的剧情大纲
                        episode_outline = self.extract_episode_outline(content, i)
                        if episode_outline:
                            outlines[i] = episode_outline
        except Exception as e:
            print(f"解析剧情大纲文件失败: {e}")
        
        return outlines
    
    def extract_episode_outline(self, content, episode):
        """
        提取指定集数的剧情大纲
        
        Args:
            content (str): 文件内容
            episode (int): 集数
            
        Returns:
            dict: 剧情大纲字典
        """
        outline = {
            "episode": episode,
            "title": "",
            "main_progress": "",
            "event_logic": {
                "cause": "",
                "process": "",
                "result": ""
            },
            "goals": [],
            "utilize": [],
            "hook": "",
            "climax": "",
            "highlights": [],
            "conflicts": [],
            "connections": []
        }
        
        # 查找对应集数的标题
        episode_pattern = rf'# 第{episode}集：([^\n]+)'
        episode_match = re.search(episode_pattern, content)
        
        if not episode_match:
            return None
        
        outline["title"] = f"第{episode}集：{episode_match.group(1)}"
        
        # 提取该集的内容（到下一集标题或文件结束）
        start_pos = episode_match.end()
        next_episode_pattern = rf'# 第{episode + 1}集：'
        next_episode_match = re.search(next_episode_pattern, content[start_pos:])
        
        if next_episode_match:
            episode_content = content[start_pos:start_pos + next_episode_match.start()]
        else:
            episode_content = content[start_pos:]
        
        # 提取各个字段
        outline["main_progress"] = self.extract_field(episode_content, "主线推进")
        
        # 提取事件逻辑
        event_logic = self.extract_field(episode_content, "事件逻辑")
        if event_logic:
            outline["event_logic"]["cause"] = self.extract_event_part(event_logic, "起因")
            outline["event_logic"]["process"] = self.extract_event_part(event_logic, "经过")
            outline["event_logic"]["result"] = self.extract_event_part(event_logic, "结果")
        
        # 提取目的必须达成
        goals_text = self.extract_field(episode_content, "目的必须达成")
        if goals_text:
            outline["goals"] = [line.strip() for line in goals_text.split('\n') if line.strip()]
        
        # 提取利用
        utilize_text = self.extract_field(episode_content, "利用")
        if utilize_text:
            outline["utilize"] = [line.strip() for line in utilize_text.split('\n') if line.strip()]
        
        # 提取悬念/钩子
        outline["hook"] = self.extract_field(episode_content, "悬念/钩子")
        
        # 提取爽点
        outline["climax"] = self.extract_field(episode_content, "爽点")
        
        # 提取亮点
        highlights_text = self.extract_field(episode_content, "亮点")
        if highlights_text:
            outline["highlights"] = [line.strip() for line in highlights_text.split('\n') if line.strip()]
        
        # 提取矛盾冲突
        conflicts_text = self.extract_field(episode_content, "矛盾冲突")
        if conflicts_text:
            outline["conflicts"] = [line.strip() for line in conflicts_text.split('\n') if line.strip()]
        
        # 提取环环相扣
        connections_text = self.extract_field(episode_content, "环环相扣")
        if connections_text:
            outline["connections"] = [line.strip() for line in connections_text.split('\n') if line.strip()]
        
        return outline
    
    def extract_field(self, content, field_name):
        """
        提取指定字段的内容
        
        Args:
            content (str): 内容
            field_name (str): 字段名
            
        Returns:
            str: 字段内容
        """
        pattern = rf'{field_name}[：:（][^：:\n]*[）]?\s*'
        match = re.search(pattern, content)
        if match:
            lines = content[match.end():].split('\n')
            field_lines = []
            for line in lines:
                stripped = line.strip()
                if stripped and (stripped.startswith('-') or stripped.startswith('•')):
                    field_lines.append(stripped)
                elif stripped and not stripped.startswith('#') and not any(kw in stripped for kw in ['主线推进', '事件逻辑', '目的必须达成', '利用', '悬念', '爽点', '亮点', '矛盾冲突', '环环相扣']):
                    if field_lines:
                        field_lines.append(stripped)
                elif stripped.startswith('#'):
                    break
                elif not stripped and field_lines:
                    break
            return '\n'.join(field_lines)
        return ""
    
    def extract_event_part(self, event_logic, part_name):
        """
        提取事件逻辑的指定部分
        
        Args:
            event_logic (str): 事件逻辑内容
            part_name (str): 部分名（起因、经过、结果）
            
        Returns:
            str: 部分内容
        """
        pattern = rf'- {part_name}：([^\n]+)'
        match = re.search(pattern, event_logic)
        if match:
            return match.group(1).strip()
        return ""
    
    def parse_summary(self, file_path):
        """
        解析剧情摘要文件
        
        Args:
            file_path (str): 文件路径
            
        Returns:
            dict: 剧情摘要字典
        """
        summary = {}
        
        try:
            # 读取文件内容
            content = self.md_parser.parse_file(file_path)
            # 提取章节
            sections = self.md_parser.extract_sections(content)
            
            for section_title, section_content in sections.items():
                if '摘要' in section_title:
                    # 提取集数范围
                    match = re.search(r'第(\d+)-(\d+)集摘要', section_title)
                    if match:
                        start_episode = int(match.group(1))
                        end_episode = int(match.group(2))
                        summary[(start_episode, end_episode)] = {
                            "range": f"{start_episode}-{end_episode}",
                            "content": section_content.strip()
                        }
        except Exception as e:
            print(f"解析剧情摘要文件失败: {e}")
        
        return summary
    
    def get_outline(self, outlines, episode):
        """
        获取指定集数的剧情大纲
        
        Args:
            outlines (dict): 剧情大纲字典
            episode (int): 集数
            
        Returns:
            dict: 剧情大纲或None
        """
        return outlines.get(episode)
    
    def get_summary(self, outlines, start_episode, end_episode):
        """
        获取指定集数范围的剧情摘要
        
        Args:
            outlines (dict): 剧情大纲字典
            start_episode (int): 开始集数
            end_episode (int): 结束集数
            
        Returns:
            dict: 剧情摘要或None
        """
        if 'summary' in outlines:
            return outlines['summary'].get((start_episode, end_episode))
        return None