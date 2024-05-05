import winreg
from datetime import date

reg_key = winreg.OpenKey(winreg.HKEY_CURRENT_USER, "Software\Microsoft\Windows\CurrentVersion\Explorer\Shell Folders")

config_path_value = winreg.QueryValueEx(reg_key, "AppData")
DataPath = config_path_value[0]
allpath = "{}\\AZMusicDownload".format(DataPath)

configpath = "{}\\config.json".format(allpath)
apipath = "{}\\api.json".format(allpath)
download_log = "{}\\download_log.json".format(allpath)
search_log = "{}\\search_log.json".format(allpath)
playlist_download_log = "{}\\playlist_download_log.json".format(allpath)
playlist_search_log = "{}\\playlist_search_log.json".format(allpath)

music_path_value = winreg.QueryValueEx(reg_key, "My Music")
personalmusicpath = music_path_value[0]
autopath = "{}\\AZMusicDownload".format(personalmusicpath)

autoapi = "https://ncma.azprod.cn/" #API为ncma的克隆项目

YEAR = int(date.today().year)
AUTHOR = "AZ Studio"
VERSION = "2.2.0"
HELP_URL = "https://azstudio.net.cn/"
FEEDBACK_URL = "https://azstudio.net.cn/"
RELEASE_URL = "https://github.com/AZ-Studio-2023/AZMusicDownloader/releases/tag/v2.2.0"