# coding:utf-8
import sys
from ctypes import c_bool, cdll
from ctypes.wintypes import DWORD, HWND,LPARAM

from win32 import win32gui
from win32.lib import win32con

from Interface.playlist_tip import playlist_tip
from Interface.searchmusic import searchmusic
from Interface.settings import SettingInterface

from PyQt5.QtCore import Qt, pyqtSignal, QEasingCurve, QUrl, QFileInfo
from PyQt5.QtGui import QIcon, QDesktopServices
from PyQt5.QtWidgets import QLabel, QHBoxLayout, QVBoxLayout, QApplication, QFrame, QWidget

from qfluentwidgets import (NavigationItemPosition, MessageBox, setTheme, Theme, MSFluentWindow,
                            NavigationAvatarWidget, qrouter, SubtitleLabel, setFont, Action, NavigationBar, NavigationItemPosition)
from qfluentwidgets import FluentIcon as FIF
from qframelesswindow import FramelessWindow, TitleBar
#from Interface.web import web
from Interface.mymusic_beta import Demo
from Interface.note import note
from Interface.playlist import playlist
import os
import helper.config

class Window(MSFluentWindow):

    def __init__(self):
        super().__init__()

        # create sub interface
        self.searchInterface = searchmusic()
        self.localmusics = Demo()
        self.releases = note()
        self.playlist = playlist()
        self.betatip_playtip = playlist_tip()
        self.settingsInterface = SettingInterface()

        self.initNavigation()
        self.initWindow()

    def initNavigation(self):
        self.addSubInterface(self.searchInterface, FIF.CARE_RIGHT_SOLID, '搜索下载')
        self.addSubInterface(self.localmusics, FIF.MUSIC_FOLDER, '我的音乐库')
        if helper.config.Config.beta.value == True:
            self.addSubInterface(self.playlist, FIF.EXPRESSIVE_INPUT_ENTRY, '歌单')
        else:
            self.addSubInterface(self.betatip_playtip, FIF.EXPRESSIVE_INPUT_ENTRY, '歌单')
        #self.addSubInterface(web(), FIF.GLOBE, 'WEB管理', NavigationItemPosition.BOTTOM)
        self.addSubInterface(self.releases, FIF.QUICK_NOTE, '更新日志', position=NavigationItemPosition.BOTTOM)
        self.addSubInterface(self.settingsInterface, FIF.SETTING, '设置', position=NavigationItemPosition.BOTTOM)

        self.navigationInterface.setCurrentItem(self.searchInterface.objectName())

    def initWindow(self):
        self.resize(900, 700)
        self.setWindowIcon(QIcon('resource/logo.png'))
        self.setWindowTitle('AZMusicDownloader')

        desktop = QApplication.desktop().availableGeometry()
        w, h = desktop.width(), desktop.height()
        self.move(w//2 - self.width()//2, h//2 - self.height()//2)





