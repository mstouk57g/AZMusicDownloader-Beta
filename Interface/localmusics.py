# coding: utf-8
import os

from PyQt5.QtWidgets import QWidget, QHBoxLayout, QVBoxLayout, QHeaderView

from qfluentwidgets import TableWidget
from qfluentwidgets import ToolButton, PrimaryToolButton
from qfluentwidgets import FluentIcon as FIF

import subprocess
from helper.config import cfg
from helper.localmusicsHelper import ref, get_all_music

musicpath = cfg.get(cfg.downloadFolder)

class localmusics(QWidget):

    def __init__(self):
        super().__init__()
        self.setObjectName("localmusics")
        self.hBoxLayout = QHBoxLayout(self)
        self.vBoxLayout = QVBoxLayout()
        self.local_view = TableWidget(self)
        self.local_view.setColumnCount(4)
        self.local_view.verticalHeader().hide()
        self.local_view.setHorizontalHeaderLabels(['路径', '歌曲名', '艺术家', '专辑'])

        ref(local_view=self.local_view, musicpath=musicpath)

        self.hBoxLayout.setContentsMargins(0, 0, 0, 0)
        self.local_view.clicked.connect(self.openbutton)
        self.resize(300, 400)
        self.openmusic = PrimaryToolButton(FIF.EMBED, self)
        self.openmusic.setEnabled(False)
        self.openmusic.released.connect(self.openthemusic)

        self.vBoxLayout.addStretch(1)
        self.vBoxLayout.addWidget(self.openmusic)
        self.vBoxLayout.addStretch(20)

        self.hBoxLayout.addWidget(self.local_view)
        self.hBoxLayout.addLayout(self.vBoxLayout)

    def openbutton(self):
        self.openmusic.setEnabled(True)

    def openthemusic(self):
        row = self.local_view.currentIndex().row()
        self.data = get_all_music(path=musicpath)
        name = self.data[row]
        file_path = os.path.join(cfg.get(cfg.downloadFolder), name)
        cmd = f'start "" "{file_path}"'
        subprocess.Popen(cmd, shell=True)

    
