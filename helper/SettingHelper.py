import json, os
from helper.getvalue import apilists

def get_all_api(folders_arg):
    print(folders_arg)
    global apilists
    for folder in folders_arg:
        for filename in os.listdir(folder):
            last_path = os.path.basename(folder)
            if filename.endswith('.py') and os.path.exists(folder) and os.path.exists(
                    folder + "/index.json") and filename.replace(".py", "") == last_path and not os.path.exists(
                folder + "/plugin.lock"):
                u = open(folder + "/index.json", "r", encoding="utf-8")
                data = json.loads(u.read())
                u.close()
                if data["type"] == "api":
                    apilists.append(filename.replace(".py", ""))
    print(apilists)
    return apilists