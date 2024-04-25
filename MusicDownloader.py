from PyQt5.QtWidgets import QApplication, QSplashScreen
from window.main import Window
from sys import argv
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPixmap
from os import path, remove
import winreg
from helper.config import cfg

def initapp():
    condition_file = "./requirements.txt" #判断的文件
    if path.exists(condition_file) is True: #判断是否要初始化
        #设置音乐下载路径
        reg_key = winreg.OpenKey(winreg.HKEY_CURRENT_USER, "Software\Microsoft\Windows\CurrentVersion\Explorer\Shell Folders")
        documents_path_value = winreg.QueryValueEx(reg_key, "My Music")
        personalmusicpath = documents_path_value[0]
        autopath = "{}\\AZMusicDownload".format(personalmusicpath)
        cfg.set(cfg.downloadFolder, autopath) #将路径设置为默认路径
        
        #删除判断文件，以后不再初始化
        remove(condition_file) 


if __name__ == '__main__':
    initapp()
    QApplication.setHighDpiScaleFactorRoundingPolicy(
        Qt.HighDpiScaleFactorRoundingPolicy.PassThrough)
    QApplication.setAttribute(Qt.AA_EnableHighDpiScaling)
    QApplication.setAttribute(Qt.AA_UseHighDpiPixmaps)
    app = QApplication(argv)
    splash_pix = QPixmap('resource/MusicDownloader.png')
    splash = QSplashScreen(splash_pix, Qt.WindowStaysOnTopHint)
    splash.setAttribute(Qt.WA_TranslucentBackground)
    splash.show()
    screen_resolution = app.desktop().screenGeometry()
    screen_width, screen_height = screen_resolution.width(), screen_resolution.height()
    splash_width = 1313
    splash_height = 736
    splash.setFixedSize(splash_width, splash_height)
    splash.move((screen_width - splash_width) // 2, (screen_height - splash_height) // 2)
    app.processEvents()
    w = Window()
    w.show()
    splash.finish(w)
    app.exec_()
