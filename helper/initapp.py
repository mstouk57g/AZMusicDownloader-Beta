from helper.config import cfg
import winreg

def initapp(todo):
    setter = cfg.get(cfg.ifinitapp) #判断条件
    if todo == "start":
        if setter is True: #判断是否要初始化
            #设置音乐下载路径
            reg_key = winreg.OpenKey(winreg.HKEY_CURRENT_USER, "Software\Microsoft\Windows\CurrentVersion\Explorer\Shell Folders")
            documents_path_value = winreg.QueryValueEx(reg_key, "My Music")
            personalmusicpath = documents_path_value[0]
            autopath = "{}\\AZMusicDownload".format(personalmusicpath)
            cfg.set(cfg.downloadFolder, autopath) #将路径设置为默认路径
        
            #将广告改为开启
            cfg.set(cfg.adcard, False)
            
            #关闭beta功能
            cfg.set(cfg.beta, False)
            
            #关闭预选项
            cfg.set(cfg.twitcard, False)
            cfg.set(cfg.hotcard, False)
            
            #将判断改为False
            cfg.set(cfg.ifinitapp, False)
    if todo == "settings":
        cfg.set(cfg.ifinitapp, True)