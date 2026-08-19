"""NpCap 插件

提供基于 Npcap 的游戏网络抓包功能，实时提取玩家位置和信息。
"""

from maasr_plugin_npcap.npcap_plugin import NpcapPlugin
from maasr_plugin_npcap.player_tracker import PlayerInfo, PlayerPosition

# 模块级单例，供主程序通过插件加载器自动启动
_instance = NpcapPlugin()

def start() -> bool:
    """启动插件抓包（由主程序插件加载器自动调用）。"""
    return _instance.start()

def stop() -> bool:
    """停止插件抓包。"""
    return _instance.stop()

def get_position() -> PlayerPosition | None:
    """获取最新玩家位置。"""
    return _instance.get_position()

def get_player_info() -> PlayerInfo:
    """获取玩家信息快照。"""
    return _instance.get_player_info()

def on_position_update(callback) -> None:
    """注册位置更新回调。"""
    _instance.on_position_update(callback)

def on_player_info_update(callback) -> None:
    """注册玩家信息更新回调。"""
    _instance.on_player_info_update(callback)

def remove_position_callback(callback) -> None:
    """移除位置回调。"""
    _instance.remove_position_callback(callback)

def remove_player_info_callback(callback) -> None:
    """移除玩家信息回调。"""
    _instance.remove_player_info_callback(callback)

__all__ = [
    "NpcapPlugin",
    "PlayerInfo",
    "PlayerPosition",
    "start",
    "stop",
    "get_position",
    "get_player_info",
    "on_position_update",
    "on_player_info_update",
    "remove_position_callback",
    "remove_player_info_callback",
]