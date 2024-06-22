from helper.inital import mkf
from mutagen.easyid3 import EasyID3
from mutagen.id3 import ID3NoHeaderError
from PyQt5.QtWidgets import QTableWidgetItem
from os import listdir
from os.path import basename, join

mkf()

def get_all_music(path):
    all_music = []
    for file_name in listdir(path):
        if file_name.endswith(".mp3"):
            all_music.append(file_name)
    return all_music

def ref(local_view, musicpath):
    local_view.clear()
    local_view.setHorizontalHeaderLabels(['文件名', '歌曲名', '艺术家', '专辑'])

    data = get_all_music(path = musicpath)
    songInfos = []
    for stand in data:
        path = join(musicpath, stand)
        try:
            audio = EasyID3(path)
        except ID3NoHeaderError:
            continue
        songinfo = [stand]
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

    local_view.setRowCount(len(songInfos))

    for i, songInfo in enumerate(songInfos):
        for j, info in enumerate(songInfo):
            local_view.setItem(i, j, QTableWidgetItem(info))
