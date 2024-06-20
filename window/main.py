# coding:utf-8
import json, sys
import os

from Interface.searchmusic import searchmusic
from Interface.settings import SettingInterface

from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QMessageBox, QApplication

from qfluentwidgets import NavigationItemPosition, MSFluentWindow, NavigationItemPosition
from qfluentwidgets import FluentIcon as FIF
from Interface.localmusics import localmusics
from Interface.playlist import playlist
from Interface.plugin import plugins
from helper.config import cfg,pfg
from helper.getvalue import apipath, autoapi
from helper.pluginHelper import run_plugins, load_plugins

try:
    u = open(apipath, "r")
    data = json.loads(u.read())
    api = data["api"]
    q_api = data["q_api"]
    u.close()
except:
    api = autoapi
    q_api = ""

# Print logs | 日志输出
if cfg.debug_card.value:
    print("————————日志信息————————")
    if cfg.beta.value:
        print("Beta实验功能：启用")
    else:
        print("Beta实验功能：禁用")
    if cfg.debug_card.value:
        print("Debug模式：启用")
    else:
        print("Debug模式：禁用")
    print("使用的NeteaseCloudMusicApi：" + api)
    print("使用的QQMusicApi：" + q_api)
    print("选择的API："+pfg.apicard.value)
    print(f"显示语言：{cfg.language.value}")

class Window(MSFluentWindow):

    def __init__(self):
        super().__init__()
        self.setObjectName("MainWindow")

        self.initNavigation()
        self.initWindow()

    def initNavigation(self):
        self.addSubInterface(searchmusic(), FIF.SEARCH, '搜索下载')
        self.addSubInterface(localmusics(), FIF.MUSIC_FOLDER, '我的音乐库')
        if cfg.beta.value:
            self.addSubInterface(playlist(), FIF.EXPRESSIVE_INPUT_ENTRY, '歌单')
        if cfg.PluginEnable.value:
            self.addSubInterface(plugins(), FIF.TILES, '插件', position=NavigationItemPosition.BOTTOM)
            load_plugins(parent=self)
            run_plugins(parent=self)
        self.addSubInterface(SettingInterface(), FIF.SETTING, '设置', position=NavigationItemPosition.BOTTOM)
    def initWindow(self):
        self.resize(900, 700)
        self.setWindowIcon(QIcon('resource/logo.png'))
        self.setWindowTitle('AZMusicDownloader')

        desktop = QApplication.desktop().availableGeometry()
        w, h = desktop.width(), desktop.height()
        self.move(w // 2 - self.width() // 2, h // 2 - self.height() // 2)
        
    def closeEvent(self, event):
        sys.exit(0)
