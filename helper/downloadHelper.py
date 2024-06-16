import json, AZMusicAPI
from PyQt5.QtCore import QThread
from PyQt5.QtCore import pyqtSignal, pyqtSlot
import requests, os
from mutagen.easyid3 import EasyID3
from helper.config import cfg
from helper.getvalue import download_log, playlist_download_log
from helper.flyoutmsg import dlsuc, dlerr, dlwar

class downloading(QThread):
    finished = pyqtSignal(str)

    def __init__(self, howto):
        super().__init__()
        self.howto = howto
        
    @pyqtSlot()
    def run(self):
        musicpath = cfg.get(cfg.downloadFolder)
        if self.howto == "search":
            u = open(download_log, "r")
        elif self.howto == "playlist":
            u = open(playlist_download_log, "r")
            
        data = json.loads(u.read())
        u.close()
        id = data["id"]
        api = data["api"]
        song = data["song"]
        singer = data["singer"]
        
        if cfg.apicard.value == "QQMA" and self.howto == "search":
            url = AZMusicAPI.geturl(id=id, api=api, server="qqma")
        else:
            url = AZMusicAPI.geturl(id=id, api=api)
            
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
            
def download(progress, table, progressbar, songdata, dworker, button, parent, howto):
        musicpath = cfg.get(cfg.downloadFolder)
        if progress == "200":
            progressbar.setValue(100)
            
            if howto == "search":
                row = table.currentIndex().row()
                try:
                    data = songdata[row]
                except:
                    dlwar(outid=2, parent=parent)
                    return 0
                
                song_id = data["id"]
                song = data["name"]
                singer = data["artists"]
                album = data["album"]
                dworker.quit()
            elif howto == "lists":
                u = open(playlist_download_log, "r")
                data = json.loads(u.read())
                u.close()
                song = data["song"]
                singer = data["singer"]
                album = data["album"]
                                
            table.clearSelection()           
            button.setEnabled(False)
            path = "{}\\{} - {}.mp3".format(musicpath, singer, song)
            path = os.path.abspath(path)
            
            audio = EasyID3(path)
            audio['title'] = song
            audio['album'] = album
            audio["artist"] = singer
            audio.save()
            
            text = '音乐下载完成！\n歌曲名：{}\n艺术家：{}\n保存路径：{}'.format(song, singer, path)
            dlsuc(content=text, parent=parent)
            progressbar.setHidden(True)
            
        elif progress == "Error":
            error = dworker.show_error
            dworker.quit()
            progressbar.setHidden(True)
            button.setEnabled(False)
            table.clearSelection()
            
            if error == "Error 3":
                dlerr(outid=7, parent=parent)
            elif error == "Error 4":
                dlerr(outid=8, parent=parent)
            elif error == "NetworkError":
                dlerr(outid=6, parent=parent)
        else:
            progressbar.setValue(int(progress))