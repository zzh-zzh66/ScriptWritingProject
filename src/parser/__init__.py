# parser模块初始化文件
# 文档解析模块，负责解析各种文档并提取关键信息

"""
parser模块

负责解析各种文档并提取关键信息，包括：
- Markdown文件解析
- 人物信息提取
- 场景信息提取
- 剧情大纲提取
- 设定信息提取
"""

from .markdown_parser import MarkdownParser
from .character_parser import CharacterParser
from .scene_parser import SceneParser
from .outline_parser import OutlineParser
from .setting_parser import SettingParser

__all__ = [
    "MarkdownParser",
    "CharacterParser",
    "SceneParser",
    "OutlineParser",
    "SettingParser"
]
