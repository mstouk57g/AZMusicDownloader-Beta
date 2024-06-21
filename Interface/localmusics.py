# coding: utf-8
import os

from PyQt5.QtWidgets import QTableWidgetItem, QWidget, QHBoxLayout, QVBoxLayout

from qfluentwidgets import TableWidget
from qfluentwidgets import ToolButton, PrimaryToolButton
from qfluentwidgets import FluentIcon as FIF

from mutagen.easyid3 import EasyID3
import subprocess

from helper.localmusicsHelper import get_all_music
from helper.config import cfg
from helper.inital import mkf


class localmusics(QWidget):

    def __init__(self):
        super().__init__()
        # setTheme(Theme.DARK)
        self.setObjectName("localmusics")
        self.hBoxLayout = QHBoxLayout(self)
        self.vBoxLayout = QVBoxLayout(self)
        self.TableWidget = TableWidget(self)

        self.TableWidget.verticalHeader().hide()
        self.TableWidget.setHorizontalHeaderLabels(['路径', '歌曲名', '艺术家', '专辑'])
        self.TableWidget.resizeColumnsToContents()
        self.ref()
        
        self.hBoxLayout.setContentsMargins(0, 0, 0, 0)
        self.TableWidget.clicked.connect(self.openbutton)
        self.resize(300, 400)
        self.openmusic = PrimaryToolButton(FIF.EMBED,self)
        self.openmusic.setEnabled(False)
        self.openmusic.released.connect(self.openthemusic)
        # self.open_dir = ToolButton(FIF.MUSIC_FOLDER, self)
        # self.open_dir.setEnabled(True)
        # self.open_dir.clicked.connect(self.openfolder)
        self.refmusics = ToolButton(FIF.SYNC, self)
        self.refmusics.setEnabled(True)
        self.refmusics.clicked.connect(self.ref)
        
        self.vBoxLayout.addStretch(1)  
        self.vBoxLayout.addWidget(self.openmusic)
        self.vBoxLayout.addStretch(1) 
        # self.vBoxLayout.addWidget(self.open_dir)
        # self.vBoxLayout.addStretch(1)
        self.vBoxLayout.addWidget(self.refmusics)
        self.vBoxLayout.addStretch(20) 
        self.hBoxLayout.addWidget(self.TableWidget)
        self.hBoxLayout.addStretch(20)  
        self.hBoxLayout.addLayout(self.vBoxLayout)
        self.hBoxLayout.addStretch(1)  
        
        
    def openbutton(self):
        self.openmusic.setEnabled(True)
        
    def openthemusic(self):
        row = self.TableWidget.currentIndex().row() 
        name = self.data[row]
        file_path = os.path.join(cfg.get(cfg.downloadFolder), name)
        cmd = f'start "" "{file_path}"'
        subprocess.Popen(cmd, shell=True)

    # def openfolder(self):
    #     f_path = cfg.get(cfg.downloadFolder)
    #     cmd = f'start {f_path}'
    #     print(cmd)
    #     subprocess.Popen(cmd, shell=True)

    def ref(self):
        self.TableWidget.clear()
        self.data = get_all_music()
        stands = self.data
        songInfos = []
        for stand in stands:
            path = os.path.join(cfg.get(cfg.downloadFolder), stand)
            print(path)
            audio = EasyID3(path)
            songinfo = []
            songinfo.append(path)
            try:
                song = audio['title'] 
                songinfo.append(song[0])
            except:
                songinfo.append(None)
            try:
                album = audio['album']
                songinfo.append(album[0])
            except:
                songinfo.append(None)
            try:
                singer = audio["artist"]
                songinfo.append(singer[0])
            except:
                songinfo.append(None)
            songInfos.append(songinfo)

        print(songInfos)
        songInfos += songInfos
        for i, songInfo in enumerate(songInfos):
            for j in range(4):
                self.TableWidget.setItem(i, j, QTableWidgetItem(songInfo[j]))