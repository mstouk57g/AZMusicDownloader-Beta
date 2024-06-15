import json, random, AZMusicAPI, webbrowser
from PyQt5.QtCore import QModelIndex, Qt
from PyQt5.QtCore import QThread
from PyQt5.QtGui import QPalette
from PyQt5.QtWidgets import QStyleOptionViewItem, QTableWidgetItem, QWidget, QHBoxLayout, \
    QVBoxLayout, QLabel, QCompleter, QHeaderView
from qfluentwidgets import TableWidget, isDarkTheme, TableItemDelegate, SearchLineEdit, \
    PrimaryPushButton, SpinBox, InfoBar, InfoBarPosition, InfoBarIcon, PushButton, ProgressBar
from PyQt5.QtCore import QObject, pyqtSignal, pyqtSlot
import helper.config
import requests, os
from json import loads
from mutagen.easyid3 import EasyID3
from helper.config import cfg
from helper.getvalue import apipath, download_log, search_log, autoapi, upurl, VERSION
from helper.inital import mkf
from helper.flyoutmsg import dlsuc, dlerr, dlwar

class downloading(QThread):
    finished = pyqtSignal(str)

    @pyqtSlot()
    def run(self):
        musicpath = cfg.get(cfg.downloadFolder)
        u = open(download_log, "r")
        data = json.loads(u.read())
        u.close()
        id = data["id"]
        api = data["api"]
        song = data["song"]
        singer = data["singer"]
        if cfg.apicard.value == "NCMA":
            url = AZMusicAPI.geturl(id=id, api=api)
        else:
            url = AZMusicAPI.geturl(id=id, api=api, server="qqma")
        if url == "Error 3":
            self.show_error = "Error 3"
            self.finished.emit("Error")
        elif url == "Error 4":
            self.show_error = "Error 4"
            self.finished.emit("Error")
        elif url == "NetworkError":
            self.show_error = "NetworkError"
            self.finished.emit("Error")
        if not "Error" in url:
            response = requests.get(url, stream=True)
            file_size = int(response.headers.get('content-length', 0))
            chunk_size = file_size // 100
            path = "{}\\{} - {}.mp3".format(musicpath, singer, song)
            with open(path, 'wb') as f:
                for chunk in response.iter_content(chunk_size=chunk_size):
                    f.write(chunk)
                    downloaded_bytes = f.tell()
                    progress = downloaded_bytes * 100 // file_size
                    if downloaded_bytes % chunk_size == 0:
                        self.finished.emit(str(progress))

            self.finished.emit(str(200))