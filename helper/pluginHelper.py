# coding:utf-8
import importlib, sys, json, os
from qfluentwidgets import FluentIcon as FIF
from qfluentwidgets import SwitchSettingCard, PushSettingCard
from helper.config import cfg

plugins_items = {}


def get_folders(directory):
    folders = []
    for item in os.listdir(directory):
        item_path = os.path.join(directory, item)
        if os.path.isdir(item_path):
            folders.append(item)
    return folders


folders = cfg.PluginFolders.value


def load_plugins(parent):
    # 遍历插件目录中的文件
    global plugins_items
    plugins_items = {}
    num = 0
    if cfg.debug_card.value:
        print("————————插件导入————————")
    for dirname in folders:
        sys.path.append(dirname)
        for filename in os.listdir(dirname):
            last_path = os.path.basename(dirname)
            if filename.endswith('.py') and os.path.exists(dirname) and os.path.exists(dirname + "/index.json") and filename.replace(".py", "") == last_path:
                plugin_name = filename[:-3]
                module_name = f"{plugin_name}"
                try:
                    module = importlib.import_module(module_name)
                    plugin_class = getattr(module, plugin_name)
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
    num = 0
    for plugin_name, plugin_instance in plugins_items.items():
        folder = folders[num]
        num = num + 1
        get_v = open(f"{folder}/index.json", "r", encoding="utf-8")
        data = json.loads(get_v.read())
        get_v.close()
        if data["type"] == "Bar":
            #icon = f'plugins/{plugin_name}/{data["icon"]}'
            icon = data["show_icon"]
            #icon = "resource/logo.png"
            name = data["name"]
            if cfg.debug_card.value:
                print(f"将插件添加至导航栏: {plugin_name}")
            exec(f"parent.addSubInterface(plugin_instance, {icon}, '{name}')")


def run_plugins_plugin(parent, PluginsGroup):
    for folder in folders:
        get_json = open(f"{folder}/index.json", "r", encoding="utf-8")
        data = json.loads(get_json.read())
        get_json.close()
        addCard(parent, PluginsGroup, data["icon"], data["name"], data["desc"], data["type"], folder)


def addCard(parent, PluginsGroup, icon, title, content, type, uuid):
    if type == "Bar":
        PluginCard = SwitchSettingCard(
            icon,
            title,
            content,
            cfg.micaEnabled,
            PluginsGroup
        )
    elif type == "api":
        PluginCard = SwitchSettingCard(
            icon,
            title,
            content,
            None,
            PluginsGroup
        )
    elif type == "Window":
        PluginCard = PushSettingCard(
            '打开',
            icon,
            title,
            content,
            PluginsGroup
        )

    PluginCard.setObjectName(uuid)
    parent.PluginsGroup.addSettingCard(PluginCard)
