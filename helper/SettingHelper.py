import json, os
from helper.getvalue import apilists, verdetail, VERSION, RELEASE_URL, AZ_URL
from qfluentwidgets import MessageBoxBase, SubtitleLabel, CheckBox, PushButton, PrimaryPushButton, FlyoutView, Flyout
from PyQt5.QtWidgets import QLabel
from PyQt5.QtCore import Qt, QUrl
from qfluentwidgets import FluentIcon as FIF
from PyQt5.QtGui import QDesktopServices

def get_all_api(folders_arg):
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
    return apilists

class DeleteAllData(MessageBoxBase):
    """ Custom message box """

    def __init__(self, parent=None):
        super().__init__(parent)
        self.titleLabel = SubtitleLabel('重置应用', self)
        self.contentLabel = QLabel("""你确定要重置应用吗？\n重置应用将会删除你的设置等数据，\n同时你将会回到初始化时的状态。\n重置后将会直接关闭应用，\n请确保没有任何正在执行的下载任务。""", self)
        self.contentLabel.setStyleSheet("QLabel{color:rgb(225,0,0);font-size:17px;font-weight:normal;font-family:SimHei;}")

        self.PrimiseCheckBox = CheckBox('我已悉知以上影响', self)
        self.DataCheckBox = CheckBox('同时删除下载的音乐', self)
        self.DataCheckBox.setDisabled(True)

        # add widget to view layout
        self.viewLayout.addWidget(self.titleLabel)
        self.viewLayout.addWidget(self.contentLabel)
        self.viewLayout.addWidget(self.PrimiseCheckBox)
        self.viewLayout.addWidget(self.DataCheckBox)

        # change the text of button
        self.yesButton.setText('取消')
        self.cancelButton.setText('重置')

        self.widget.setMinimumWidth(350)
        self.cancelButton.setDisabled(True)
        #self.urlLineEdit.textChanged.connect(self._validateUrl)
        self.PrimiseCheckBox.stateChanged.connect(self.IfPrimise)
    
    def IfPrimise(self):
        self.cancelButton.setEnabled(self.PrimiseCheckBox.isChecked())

def changelog(parent):
    view = FlyoutView(
        title=f'AZMusicDownloader {VERSION}更新日志 ',
        content=verdetail,
        #image='resource/splash.png',
        isClosable=True
    )
        
    # add button to view
    button1 = PushButton(FIF.GITHUB, 'GitHub')
    button1.setFixedWidth(120)
    button1.clicked.connect(lambda: QDesktopServices.openUrl(QUrl(RELEASE_URL)))
    view.addWidget(button1, align=Qt.AlignRight)

    button2 = PushButton('AZ Studio')
    button2.setFixedWidth(120)
    button2.clicked.connect(lambda: QDesktopServices.openUrl(QUrl(AZ_URL)))
    view.addWidget(button2, align=Qt.AlignRight)

    button3 = PrimaryPushButton('检查更新')
    button3.setFixedWidth(120)
    button3.clicked.connect(parent.upworker.start)
    view.addWidget(button3, align=Qt.AlignRight)

    # adjust layout (optional)
    view.widgetLayout.insertSpacing(1, 5)
    view.widgetLayout.addSpacing(5)

    # show view
    w = Flyout.make(view, parent.aboutCard, parent)
    view.closed.connect(w.close)
