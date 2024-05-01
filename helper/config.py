# coding:utf-8
from enum import Enum
import datetime
from sys import platform, getwindowsversion
from helper.getvalue import configpath, autopath
from PyQt5.QtCore import QLocale
from qfluentwidgets import (qconfig, QConfig, ConfigItem, OptionsConfigItem, BoolValidator,
                            OptionsValidator,  FolderValidator, ConfigSerializer)


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
    downloadFolder = ConfigItem(
        "Folders", "Download", autopath, FolderValidator())

    # Application
    beta = ConfigItem(
        "Application", "beta", False, BoolValidator(), restart=True)
    adcard = ConfigItem(
        "Application", "adcard", False, BoolValidator(), restart=True)
    
    # Search
    twitcard = ConfigItem(
        "Search", "twitcard", False, BoolValidator(), restart=True)
    hotcard = ConfigItem(
        "Search", "hotcard", False, BoolValidator(), restart=True)
    
    # Personalize
    language = OptionsConfigItem(
        "Personalize", "Language", Language.AUTO, OptionsValidator(Language), LanguageSerializer(), restart=True)
    micaEnabled = ConfigItem("Personalize", "MicaEnabled", platform == 'win32' and getwindowsversion().build >= 22000, BoolValidator())
    

YEAR = int(datetime.date.today().year)
AUTHOR = "AZ Studio"
VERSION = "2.2.0"
HELP_URL = "https://azstudio.net.cn/"
FEEDBACK_URL = "https://azstudio.net.cn/"
RELEASE_URL = "https://github.com/AZ-Studio-2023/AZMusicDownloader/releases/tag/v2.2.0"


cfg = Config()
qconfig.load(configpath, cfg)