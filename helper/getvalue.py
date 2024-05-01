import winreg

reg_key = winreg.OpenKey(winreg.HKEY_CURRENT_USER, "Software\Microsoft\Windows\CurrentVersion\Explorer\Shell Folders")

config_path_value = winreg.QueryValueEx(reg_key, "AppData")
DataPath = config_path_value[0]
configpath = "{}\\AZMusicDownload\\config.json".format(DataPath)
apipath = "{}\\AZMusicDownload\\api.json".format(DataPath)
download_log = "{}\\AZMusicDownload\\download_log.json".format(DataPath)
search_log = "{}\\AZMusicDownload\\search_log.json".format(DataPath)
playlist_download_log = "{}\\AZMusicDownload\\playlist_download_log.json".format(DataPath)
playlist_search_log = "{}\\AZMusicDownload\\playlist_search_log.json".format(DataPath)

music_path_value = winreg.QueryValueEx(reg_key, "My Music")
personalmusicpath = music_path_value[0]
autopath = "{}\\AZMusicDownload".format(personalmusicpath)