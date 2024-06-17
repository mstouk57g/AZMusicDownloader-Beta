import json
import os
import sys
from helper.inital import setSettingsQss
from PyQt5.QtCore import Qt, QPoint, QSize, QUrl, QRect
from PyQt5.QtGui import QIcon, QFont, QColor, QPainter
from PyQt5.QtWidgets import QApplication, QWidget, QHBoxLayout, QVBoxLayout, QSizePolicy
from helper.config import cfg
from qfluentwidgets import (SettingCardGroup, SwitchSettingCard, CustomColorSettingCard,
                            OptionsSettingCard, PushSettingCard, setTheme, isDarkTheme,
                            HyperlinkCard, PrimaryPushSettingCard, ScrollArea, PushButton, PrimaryPushButton,
                            ComboBoxSettingCard, ExpandLayout, Theme, InfoBar, FlyoutView, Flyout)
from qfluentwidgets import FluentIcon as FIF
from qfluentwidgets.components.widgets.acrylic_label import AcrylicBrush
from helper.pluginHelper import run_plugins_plugin

class plugins(ScrollArea):

    def __init__(self, parent=None):
        super().__init__(parent=parent)
        self.scrollWidget = QWidget()
        self.expandLayout = ExpandLayout(self.scrollWidget)
        self.setObjectName('plugins')
        self.resize(1000, 800)
        self.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.setViewportMargins(0, 20, 0, 20)
        self.setWidget(self.scrollWidget)
        self.setWidgetResizable(True)
        self.scrollWidget.setObjectName('scrollWidget')

        self.PluginsGroup = SettingCardGroup(self.tr('插件列表/管理'), self.scrollWidget)
        run_plugins_plugin(parent=self)
        setSettingsQss(parent=self)

        self.expandLayout.setSpacing(28)
        self.expandLayout.setContentsMargins(60, 10, 60, 0)
        self.expandLayout.addWidget(self.PluginsGroup)
            
    def addCard(self, icon, title, content, type, uuid):
        print(type)
        if type == "Bar" or "api":
            print("1")
            self.PluginCard = SwitchSettingCard(
                icon,
                title,
                content,
                cfg.micaEnabled,
                self.PluginsGroup
            )
        elif type == "Window":
            print("2")
            self.Plugintoinit = PushSettingCard(
                self.tr('打开'),
                icon,
                title,
                content,
                self.PluginsGroup
            )
        
        self.PluginCard.setObjectName(uuid)
        self.PluginsGroup.addSettingCard(self.PluginCard)
