# coding:utf-8
import json
import os

from Interface.searchmusic import searchmusic
from Interface.settings import SettingInterface

from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QApplication

from qfluentwidgets import NavigationItemPosition, MSFluentWindow, NavigationItemPosition
from qfluentwidgets import FluentIcon as FIF
from Interface.localmusics import localmusics
from Interface.playlist import playlist
from helper.config import Config
from Interface.plugin import plugins
from helper.config import cfg
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
    if Config.beta.value:
        print("Beta实验功能：启用")
    else:
        print("Beta实验功能：禁用")
    if cfg.debug_card.value:
        print("Debug模式：启用")
    else:
        print("Debug模式：禁用")
    print("使用的NeteaseCloudMusicApi：" + api)
    print("使用的QQMusicApi：" + q_api)
    print("选择的API："+cfg.apicard.value)
    print(f"显示语言：{Config.language.value}")

if not os.path.exists("plugins"):
    os.mkdir("plugins")

class Window(MSFluentWindow):

    def __init__(self):
        super().__init__()
        self.setObjectName("MainWindow")

        self.initNavigation()
        self.initWindow()

    def initNavigation(self):
        self.addSubInterface(searchmusic(), FIF.CARE_RIGHT_SOLID, '搜索下载')
        self.addSubInterface(localmusics(), FIF.MUSIC_FOLDER, '我的音乐库')
        if Config.beta.value:
            self.addSubInterface(playlist(), FIF.EXPRESSIVE_INPUT_ENTRY, '歌单')
            self.addSubInterface(plugins(), FIF.BOOK_SHELF, '插件', position=NavigationItemPosition.BOTTOM)
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
