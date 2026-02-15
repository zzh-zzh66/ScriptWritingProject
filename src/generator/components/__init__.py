# 组件模块
# 包含剧本生成的各种组件

from .character_intro import CharacterIntroComponent
from .scene_description import SceneDescriptionComponent
from .action_chain import ActionChainComponent
from .dialogue import DialogueComponent
from .system_panel import SystemPanelComponent
from .color_marker import ColorMarkerComponent

__all__ = [
    'CharacterIntroComponent',
    'SceneDescriptionComponent',
    'ActionChainComponent',
    'DialogueComponent',
    'SystemPanelComponent',
    'ColorMarkerComponent'
]
