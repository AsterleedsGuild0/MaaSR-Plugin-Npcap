"""
插件入口点

当插件作为 .pyz 文件运行时的入口。
"""

from src.maasr_plugin_npcap.npcap_plugin import NpcapPlugin

if __name__ == "__main__":
    plugin = NpcapPlugin()
    plugin.start()
