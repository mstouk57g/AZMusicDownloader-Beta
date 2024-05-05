import os, json
from helper.config import cfg
from helper.getvalue import apipath, download_log, search_log, autoapi, playlistpath, logpath


def mkf():
    path = cfg.get(cfg.downloadFolder)
    if not os.path.exists(logpath):
        os.makedirs(logpath)
    if not os.path.exists(download_log):
        d = open(download_log, "w")
        d.close()
    if not os.path.exists(search_log):
        d = open(search_log, "w")
        d.close()
    if not os.path.exists(apipath):
        u = open(apipath, "w")
        u.write(json.dumps({"api": autoapi}))
        u.close()
    if not os.path.exists(path):
        os.makedirs(path)
    if not os.path.exists(playlistpath):
        os.makedirs(playlistpath)