from helper.config import cfg
from os import path, remove, execl, open
import winreg
from sys import argv, executable

def initapp(todo):
    condition_file = "./requirements.txt" #判断的文件
    if todo == "start":
        if path.exists(condition_file) is True: #判断是否要初始化
            #设置音乐下载路径
            reg_key = winreg.OpenKey(winreg.HKEY_CURRENT_USER, "Software\Microsoft\Windows\CurrentVersion\Explorer\Shell Folders")
            documents_path_value = winreg.QueryValueEx(reg_key, "My Music")
            personalmusicpath = documents_path_value[0]
            autopath = "{}\\AZMusicDownload".format(personalmusicpath)
            cfg.set(cfg.downloadFolder, autopath) #将路径设置为默认路径
        
            #删除判断文件，以后不再初始化
            remove(condition_file) 
    if todo == "settings":
        w = open(condition_file)  
        w.close() #添加判断文件
        execl(executable, executable, * argv) #重启