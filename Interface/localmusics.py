# coding: utf-8
import os

from PyQt5.QtWidgets import QTableWidgetItem, QWidget, QHBoxLayout, QVBoxLayout, QHeaderView

from qfluentwidgets import TableWidget
from qfluentwidgets import ToolButton, PrimaryToolButton
from qfluentwidgets import FluentIcon as FIF

from mutagen.easyid3 import EasyID3
from mutagen.id3 import ID3NoHeaderError
import subprocess

from helper.localmusicsHelper import get_all_music
from helper.config import cfg
from helper.inital import mkf


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

        self.ref()

        self.hBoxLayout.setContentsMargins(0, 0, 0, 0)
        self.local_view.clicked.connect(self.openbutton)
        self.resize(300, 400)
        self.openmusic = PrimaryToolButton(FIF.EMBED, self)
        self.openmusic.setEnabled(False)
        self.openmusic.released.connect(self.openthemusic)

        self.refmusics = ToolButton(FIF.SYNC, self)
        self.refmusics.setEnabled(True)
        self.refmusics.clicked.connect(self.ref)

        self.vBoxLayout.addStretch(1)
        self.vBoxLayout.addWidget(self.openmusic)
        self.vBoxLayout.addStretch(1)
        self.vBoxLayout.addWidget(self.refmusics)
        self.vBoxLayout.addStretch(20)

        self.hBoxLayout.addWidget(self.local_view)
        self.hBoxLayout.addLayout(self.vBoxLayout)

    def openbutton(self):
        self.openmusic.setEnabled(True)

    def openthemusic(self):
        row = self.local_view.currentIndex().row()
        name = self.data[row]
        file_path = os.path.join(cfg.get(cfg.downloadFolder), name)
        cmd = f'start "" "{file_path}"'
        subprocess.Popen(cmd, shell=True)

    def ref(self):
        self.local_view.clear()
        self.local_view.setHorizontalHeaderLabels(['路径', '歌曲名', '艺术家', '专辑'])

        self.data = get_all_music()
        songInfos = []
        for stand in self.data:
            path = os.path.join(cfg.get(cfg.downloadFolder), stand)
            try:
                audio = EasyID3(path)
            except ID3NoHeaderError:
                continue
            songinfo = [path]
            try:
                songinfo.append(audio['title'][0])
            except KeyError:
                songinfo.append("Unknown")
            try:
                songinfo.append(audio['artist'][0])
            except KeyError:
                songinfo.append("Unknown")
            try:
                songinfo.append(audio['album'][0])
            except KeyError:
                songinfo.append("Unknown")
            songInfos.append(songinfo)

        self.local_view.setRowCount(len(songInfos))

        for i, songInfo in enumerate(songInfos):
            for j, info in enumerate(songInfo):
                self.local_view.setItem(i, j, QTableWidgetItem(info))

