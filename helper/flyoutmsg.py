from PyQt5.QtCore import Qt
from qfluentwidgets import InfoBar, InfoBarPosition
from helper.getvalue import outputlist


def getoutputvalue(outid):
    try:
        out=outputlist[int(outid)]
    except:
        out=outid
    return out



def dlsuc(parent, content, title="", show_time=3000):
    # convenient class mothod
    InfoBar.success(
        title=title,
        content=content,
        orient=Qt.Horizontal,
        isClosable=True,
        position=InfoBarPosition.TOP,
        duration=show_time,
        parent=parent)


def dlerr(outid, parent, title="错误", show_time=3000):
    InfoBar.error(
        title=title,
        content=getoutputvalue(outid=outid),
        orient=Qt.Horizontal,
        isClosable=True,
        position=InfoBarPosition.TOP,
        duration=show_time,
        parent=parent)


def dlwar(outid, parent, title="警告", show_time=3000):
    InfoBar.warning(
        title=title,
        content=getoutputvalue(outid=outid),
        orient=Qt.Horizontal,
        isClosable=True,
        position=InfoBarPosition.TOP,
        duration=show_time,
        parent=parent)
