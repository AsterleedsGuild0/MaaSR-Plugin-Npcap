"""NpCap 插件主模块

插件适配层，组合 PacketCapture 实例，对外暴露统一接口。
"""

from collections.abc import Callable
from typing import Any

from maasr_plugin_npcap.logger import logger
from maasr_plugin_npcap.player_tracker import PlayerInfo, PlayerPosition
from maasr_plugin_npcap.sniffer import PacketCapture
from maasr_plugin_npcap.utils.common_util import get_runtime_config


class NpcapPlugin:
    """NpCap 插件类

    组合 PacketCapture，提供插件生命周期管理和抓包 API。
    """

    def __init__(self):
        """初始化插件"""
        plugin_info = get_runtime_config()
        self.name = plugin_info.get("display_name", "NpcapPlugin")
        self.version = plugin_info.get("version", "0.0.0")
        self.description = plugin_info.get("description", "")
        self.author = plugin_info.get("author", "")
        self._capture = PacketCapture()

    def start(self) -> bool:
        """启动插件（启动抓包）

        Returns:
            bool: 启动是否成功
        """
        try:
            self._capture.start()
            logger.info(f"{self.name} v{self.version} 已启动")
            return True
        except Exception as e:
            logger.error(f"{self.name} 启动失败: {e}")
            return False

    def stop(self) -> bool:
        """停止插件（停止抓包）

        Returns:
            bool: 停止是否成功
        """
        try:
            self._capture.stop()
            logger.info(f"{self.name} 已停止")
            return True
        except Exception as e:
            logger.error(f"{self.name} 停止失败: {e}")
            return False

    def get_info(self) -> dict[str, Any]:
        """获取插件信息

        Returns:
            dict: 插件信息字典
        """
        return {
            "name": self.name,
            "version": self.version,
            "description": self.description,
            "author": self.author,
            "is_running": self.is_running,
        }

    @property
    def is_running(self) -> bool:
        """抓包是否运行中"""
        return self._capture.is_running

    def get_position(self) -> PlayerPosition | None:
        """获取最新玩家位置

        Returns:
            PlayerPosition | None: 最新位置，无数据时返回 None
        """
        return self._capture.get_position()

    def get_player_info(self) -> PlayerInfo:
        """获取玩家信息快照

        Returns:
            PlayerInfo: 玩家信息
        """
        return self._capture.get_player_info()

    def on_position_update(self, callback: Callable[[PlayerPosition], None]) -> None:
        """注册位置更新回调

        Args:
            callback: 接收 PlayerPosition 的回调函数
        """
        self._capture.on_position_update(callback)

    def on_player_info_update(self, callback: Callable[[PlayerInfo], None]) -> None:
        """注册玩家信息更新回调

        Args:
            callback: 接收 PlayerInfo 的回调函数
        """
        self._capture.on_player_info_update(callback)

    def remove_position_callback(self, callback: Callable[[PlayerPosition], None]) -> None:
        """移除位置回调

        Args:
            callback: 要移除的回调函数
        """
        self._capture.remove_position_callback(callback)

    def remove_player_info_callback(self, callback: Callable[[PlayerInfo], None]) -> None:
        """移除玩家信息回调

        Args:
            callback: 要移除的回调函数
        """
        self._capture.remove_player_info_callback(callback)

    def reset(self) -> None:
        """重置内部状态（不停止抓包）"""
        self._capture.reset()
        logger.info(f"{self.name} 状态已重置")