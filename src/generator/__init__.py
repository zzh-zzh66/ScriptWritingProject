# generator模块初始化文件
# 剧本生成模块，负责生成符合要求的剧本

"""
generator模块

负责生成符合要求的剧本，包括：
- 剧本生成核心逻辑
- 第一集特殊处理
- 第二集特殊处理
- 正常集数处理
"""

from .script_generator import ScriptGenerator
from .first_episode import FirstEpisodeGenerator
from .second_episode import SecondEpisodeGenerator
from .normal_episode import NormalEpisodeGenerator

__all__ = [
    "ScriptGenerator",
    "FirstEpisodeGenerator",
    "SecondEpisodeGenerator",
    "NormalEpisodeGenerator"
]
