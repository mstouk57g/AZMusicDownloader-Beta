# coding: utf-8
import sys

from PyQt5.QtCore import Qt
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QApplication, QListWidgetItem, QListWidget, QWidget, QHBoxLayout, QLabel, QVBoxLayout

from qfluentwidgets import ListView, setTheme, Theme, ListWidget
import os
from qfluentwidgets import ToolButton, PrimaryToolButton
from qfluentwidgets import FluentIcon as FIF
import subprocess
import shlex
from helper.config import cfg

path = cfg.get(cfg.downloadFolder)
if not os.path.exists(path):
    os.makedirs(path)
def getallmusic():
    allmusic=[]
    path=cfg.get(cfg.downloadFolder)
    for file_name in os.listdir(path):
        allmusic.append(file_name)
    return allmusic

class Demo(QWidget):

    def __init__(self):
        super().__init__()
        # setTheme(Theme.DARK)
        self.setObjectName("Demo")
        self.hBoxLayout = QHBoxLayout(self)
        self.vBoxLayout = QVBoxLayout(self)
        self.listWidget = ListWidget(self)

        # self.listWidget.setAlternatingRowColors(True)
        self.data = getallmusic()
        stands = self.data
        for stand in stands:
            item = QListWidgetItem(stand)
            # item.setIcon(QIcon(':/qfluentwidgets/images/logo.png'))
            # item.setCheckState(Qt.Unchecked)
            self.listWidget.addItem(item)
            
        self.setStyleSheet("Demo{background: rgb(249, 249, 249)} ")
        self.hBoxLayout.setContentsMargins(0, 0, 0, 0)
        self.listWidget.clicked.connect(self.openbutton)
        self.resize(300, 400)
        self.openmusic = PrimaryToolButton(FIF.EMBED,self)
        self.openmusic.setEnabled(False)
        self.openmusic.released.connect(self.openthemusic)
        self.refmusics = ToolButton(FIF.MUSIC_FOLDER, self)
        self.refmusics.setEnabled(True)
        self.refmusics.released.connect(self.__refmusics)
        self.opendir = ToolButton(FIF.SYNC, self)
        self.opendir.setEnabled(True)
        self.opendir.released.connect(self.__opendir)
        
        self.vBoxLayout.addStretch(1)  
        self.vBoxLayout.addWidget(self.openmusic)
        self.vBoxLayout.addStretch(1) 
        self.vBoxLayout.addWidget(self.refmusics)
        self.vBoxLayout.addStretch(1) 
        self.vBoxLayout.addWidget(self.opendir)
        self.vBoxLayout.addStretch(20) 
        self.hBoxLayout.addWidget(self.listWidget)
        self.hBoxLayout.addStretch(20)  
        self.hBoxLayout.addLayout(self.vBoxLayout)
        self.hBoxLayout.addStretch(1)  
        
        
    def openbutton(self):
        self.openmusic.setEnabled(True)
        
    def openthemusic(self):
        row = self.listWidget.currentIndex().row() 
        name = self.data[row]
        file_path = os.path.join(cfg.get(cfg.downloadFolder), name)
        cmd = f'start "" "{file_path}"'
        subprocess.Popen(cmd, shell=True)
        
    def __refmusics(self):
        #刷新列表
        pass
    
    def __opendir(self):
        #打开音乐文件夹
        pass
        
if __name__ == "__main__":
    # enable dpi scale
    QApplication.setHighDpiScaleFactorRoundingPolicy(
        Qt.HighDpiScaleFactorRoundingPolicy.PassThrough)
    QApplication.setAttribute(Qt.AA_EnableHighDpiScaling)
    QApplication.setAttribute(Qt.AA_UseHighDpiPixmaps)

    app = QApplication(sys.argv)
    w = Demo()
    w.show()
    app.exec()
