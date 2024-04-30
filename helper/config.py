# coding:utf-8
from enum import Enum
import datetime
import winreg

from PyQt5.QtCore import Qt, QLocale
from PyQt5.QtGui import QGuiApplication, QFont
from qfluentwidgets import (qconfig, QConfig, ConfigItem, OptionsConfigItem, BoolValidator,
                            ColorConfigItem, OptionsValidator, RangeConfigItem, RangeValidator,
                            FolderListValidator, EnumSerializer, FolderValidator, ConfigSerializer)


class SongQuality(Enum):
    """ Online song quality enumeration class """

    STANDARD = "Standard quality"
    HIGH = "High quality"
    SUPER = "Super quality"
    LOSSLESS = "Lossless quality"


class MvQuality(Enum):
    """ MV quality enumeration class """

    FULL_HD = "Full HD"
    HD = "HD"
    SD = "SD"
    LD = "LD"


class Language(Enum):
    """ Language enumeration """

    CHINESE_SIMPLIFIED = QLocale(QLocale.Chinese, QLocale.China)
    CHINESE_TRADITIONAL = QLocale(QLocale.Chinese, QLocale.HongKong)
    ENGLISH = QLocale(QLocale.English)
    AUTO = QLocale()


class LanguageSerializer(ConfigSerializer):
    """ Language serializer """

    def serialize(self, language):
        return language.value.name() if language != Language.AUTO else "Auto"

    def deserialize(self, value: str):
        return Language(QLocale(value)) if value != "Auto" else Language.AUTO


class Config(QConfig):
    # Folders
    reg_key = winreg.OpenKey(winreg.HKEY_CURRENT_USER, "Software\Microsoft\Windows\CurrentVersion\Explorer\Shell Folders")
    music_path_value = winreg.QueryValueEx(reg_key, "My Music")
    personalmusicpath = music_path_value[0]
    autopath = "{}\\AZMusicDownload".format(personalmusicpath)
    downloadFolder = ConfigItem(
        "Folders", "Download", autopath, FolderValidator())

    # Application
    beta = ConfigItem(
        "Application", "beta", False, BoolValidator(), restart=True)
    adcard = ConfigItem(
        "Application", "adcard", False, BoolValidator(), restart=True)
    
    #Search
    twitcard = ConfigItem(
        "Search", "twitcard", False, BoolValidator(), restart=True)
    hotcard = ConfigItem(
        "Search", "hotcard", False, BoolValidator(), restart=True)
    
    #Personalize
    language = OptionsConfigItem(
        "Personalize", "Language", Language.AUTO, OptionsValidator(Language), LanguageSerializer(), restart=True)
    

YEAR = int(datetime.date.today().year)
AUTHOR = "AZ Studio"
VERSION = "2.2.0"
HELP_URL = "https://azstudio.net.cn/"
FEEDBACK_URL = "https://azstudio.net.cn/"
RELEASE_URL = "https://azstudio.net.cn/"


cfg = Config()
reg_key = winreg.OpenKey(winreg.HKEY_CURRENT_USER, "Software\Microsoft\Windows\CurrentVersion\Explorer\Shell Folders")
config_path_value = winreg.QueryValueEx(reg_key, "AppData")
DataPath = config_path_value[0]
configpath = "{}\\AZMusicDownload\\config.json".format(DataPath)
qconfig.load(configpath, cfg)