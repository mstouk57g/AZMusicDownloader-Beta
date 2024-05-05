from PyQt5.QtWidgets import QApplication, QSplashScreen
from qfluentwidgets import FluentTranslator
from helper.config import cfg
from window.main import Window
import sys
from PyQt5.QtCore import Qt, QTranslator
from PyQt5.QtGui import QPixmap
import win32api, win32con
from helper.inital import mkf

def global_exception_handler(exc_type, exc_value, exc_traceback):
    msesg = str(exc_type + exc_value + exc_traceback)
    win32api.MessageBox(0, msesg, "Error", win32con.MB_ICONHAND)
sys.excepthook = global_exception_handler

if __name__ == '__main__':
    QApplication.setHighDpiScaleFactorRoundingPolicy(
        Qt.HighDpiScaleFactorRoundingPolicy.PassThrough)
    QApplication.setAttribute(Qt.AA_EnableHighDpiScaling)
    QApplication.setAttribute(Qt.AA_UseHighDpiPixmaps)
    app = QApplication(sys.argv)
    mkf()
    
    splash_pix = QPixmap('resource/splash.png')
    splash = QSplashScreen(splash_pix, Qt.WindowStaysOnTopHint)
    splash.setAttribute(Qt.WA_TranslucentBackground)
    splash.show()
    screen_resolution = app.desktop().screenGeometry()
    screen_width, screen_height = screen_resolution.width(), screen_resolution.height()
    splash_width = 283
    splash_height = 276
    splash.setFixedSize(splash_width, splash_height)
    splash.move((screen_width - splash_width) // 2, (screen_height - splash_height) // 2)
    
    locale = cfg.get(cfg.language).value
    fluentTranslator = FluentTranslator(locale)
    settingTranslator = QTranslator()
    settingTranslator.load(locale, "settings", ".", "resource/i18n")

    app.installTranslator(fluentTranslator)
    app.installTranslator(settingTranslator)
    app.processEvents()
    
    w = Window()
    w.show()
    splash.finish(w)
    app.exec_()
