import json
import os
from helper.config import cfg

folders = cfg.PluginFolders.value


def get_all_api():
    texts = ['NCMA', 'QQMA']
    for folder in folders:
        for filename in os.listdir(folder):
            last_path = os.path.basename(folder)
            if filename.endswith('.py') and os.path.exists(folder) and os.path.exists(
                    folder + "/index.json") and filename.replace(".py", "") == last_path and not os.path.exists(
                folder + "/plugin.lock"):
                u = open(folder + "/index.json", "r", encoding="utf-8")
                data = json.loads(u.read())
                u.close()
                if data["type"] == "api":
                    texts.append(filename.replace(".py", ""))
    return texts
