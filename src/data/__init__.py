# data模块初始化文件
# 数据管理模块，负责管理解析后的数据

"""
data模块

负责管理解析后的数据，包括：
- 存储解析后的数据
- 提供数据访问接口
- 确保数据一致性
"""

from .data_manager import DataManager

__all__ = [
    "DataManager"
]
