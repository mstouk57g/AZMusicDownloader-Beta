# coding:utf-8
import importlib
import json
import os
from qfluentwidgets import FluentIcon as FIF
from helper.config import cfg

plugins_items = {}

def get_folders(directory):
    folders = []
    for item in os.listdir(directory):
        item_path = os.path.join(directory, item)
        if os.path.isdir(item_path):
            folders.append(item)
    return folders

def load_plugins(parent):
        # 遍历插件目录中的文件
        global plugins_items
        plugin_dir = "plugins"
        plugins_items = {}
        num = 0
        if cfg.debug_card.value:
            print("————————插件导入————————")
        for dirname in get_folders(plugin_dir):
            for filename in os.listdir(f'plugins\\{dirname}'):
                if filename.endswith('.py'):
                    plugin_name = filename[:-3]
                    module_name = f"{plugin_dir}.{dirname}.{plugin_name}"
                    try:
                        module = importlib.import_module(module_name)
                        plugin_class = getattr(module, plugin_name.capitalize())
                        plugins_items[plugin_name] = plugin_class()
                        if cfg.debug_card.value:
                            print(f"导入插件: {plugin_name}")
                        num = num + 1
                    except Exception as e:
                        if cfg.debug_card.value:
                            print(f"导入{plugin_name}插件错误: {e}")
        if cfg.debug_card.value:
            print(f"成功导入了{str(num)}个插件")

def run_plugins(parent):
    global plugins_items
    for plugin_name, plugin_instance in plugins_items.items():
        get_v = open(f"plugins/{plugin_name}/index.json", "r", encoding="utf-8")
        data = json.loads(get_v.read())
        get_v.close()
        icon = data["show_icon"]
        name = data["name"]
        if cfg.debug_card.value:
            print(f"将插件添加至导航栏: {plugin_name}")
        exec(f"parent.addSubInterface(plugin_instance, {icon}, '{name}')")