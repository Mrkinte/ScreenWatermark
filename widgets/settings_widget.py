import os
import shutil
import sys

import winshell
from PySide6.QtCore import Qt
from PySide6.QtWidgets import QWidget, QSpacerItem, QSizePolicy, QApplication
from qfluentwidgets import FluentIcon, SwitchSettingCard, HyperlinkCard, PrimaryPushSettingCard, OptionsSettingCard, \
    CustomColorSettingCard, setThemeColor, setTheme, Theme, isDarkTheme
from win32com.client import Dispatch

from design.Ui_SettingsWidget import Ui_SettingsWidget
from utils.app_config import cfg, VERSION, AppConfig, YEAR, AUTHOR
from utils.check_update import CheckUpdate
from widgets.info_bar import showTips, showError
from widgets.update_widget import UpdateWidget


class SettingsWidget(QWidget):
    def __init__(self):
        super(SettingsWidget, self).__init__()
        self.ui = Ui_SettingsWidget()
        self.ui.setupUi(self)
        self.checkUpdate = None
        self.updateWidget = None

        self.autoBootCard = SwitchSettingCard(
            icon=FluentIcon.TRANSPARENT,
            title="开机自启动",
            content="Windows登录时启动软件并显示水印",
            configItem=cfg.enableAutoBoot
        )
        self.autoBootCard.checkedChanged.connect(self._autoBootCardCheckedChanged)

        self.themeCard = OptionsSettingCard(
            cfg.themeMode,
            FluentIcon.BRUSH,
            "应用主题",
            "调整应用的外观",
            texts=[
                "浅色", "深色", "跟随系统设置"
            ]
        )
        cfg.themeChanged.connect(setTheme)

        self.themeColorCard = CustomColorSettingCard(
            cfg.themeColor,
            FluentIcon.PALETTE,
            "主题色",
            "调整应用的主题色"
        )
        self.themeColorCard.colorChanged.connect(setThemeColor)

        self.openConfigCard = PrimaryPushSettingCard(
            text="打开",
            icon=FluentIcon.ROBOT,
            title="配置文件夹",
            content=AppConfig.configDir
        )
        self.openConfigCard.clicked.connect(self._openConfigCardClicked)

        self.defaultConfigCard = PrimaryPushSettingCard(
            text="恢复",
            icon=FluentIcon.HELP,
            title="恢复默认设置",
            content="删除配置文件和文本纪录"
        )
        self.defaultConfigCard.clicked.connect(self._defaultConfigCardClicked)

        self.updateCard = PrimaryPushSettingCard(
            text="检查更新",
            icon=FluentIcon.UPDATE,
            title="获取最新版本",
            content=f"© 版权所有 {YEAR}, {AUTHOR}, 当前版本 {VERSION}"
        )
        self.updateCard.clicked.connect(self._updateCardClicked)

        self.issueCard = HyperlinkCard(
            url="https://github.com/Mrkinte/ScreenWatermark/issues",
            text="跳转至Github",
            icon=FluentIcon.QUESTION,
            title="问题反馈",
            content="在Github中反馈遇到的Bug"
        )

        self.ui.settingsLayout.addWidget(self.autoBootCard)
        self.ui.settingsLayout.addWidget(self.themeCard)
        self.ui.settingsLayout.addWidget(self.themeColorCard)
        self.ui.settingsLayout.addWidget(self.openConfigCard)
        self.ui.settingsLayout.addWidget(self.defaultConfigCard)
        self.ui.settingsLayout.addWidget(self.updateCard)
        self.ui.settingsLayout.addWidget(self.issueCard)
        self.ui.settingsLayout.addItem(QSpacerItem(20, 40, QSizePolicy.Fixed, QSizePolicy.Expanding))

    def _autoBootCardCheckedChanged(self):
        appPath = os.path.abspath(os.path.basename(sys.argv[0]))
        startupFolder = winshell.startup()
        shortcutPath = os.path.join(startupFolder, "屏幕水印.lnk")
        if self.autoBootCard.isChecked():
            # 创建快捷方式
            shell = Dispatch('WScript.Shell')
            shortcut = shell.CreateShortCut(shortcutPath)
            shortcut.TargetPath = appPath
            shortcut.IconLocation = appPath
            shortcut.save()
            showTips("已创建开机自启动快捷方式。")
        else:
            if os.path.exists(shortcutPath):
                os.remove(shortcutPath)
                showTips("已删除开机自启动快捷方式。")

    def _openConfigCardClicked(self):
        try:
            os.startfile(self.openConfigCard.contentLabel.text())
        except FileNotFoundError:
            showError("找不到配置文件夹。")

    def _defaultConfigCardClicked(self):
        try:
            shutil.rmtree(AppConfig.configDir)
            showTips("已恢复默认设置，重启生效。")
        except IOError as e:
            showError("恢复默认设置失败。")
        self.defaultConfigCard.setEnabled(False)
        self.openConfigCard.setEnabled(False)

    def _updateCardClicked(self):
        if self.checkUpdate is None:
            self.checkUpdate = CheckUpdate()
            self.checkUpdate.newVersionSignal.connect(self._showUpdateInfo)
            self.checkUpdate.start()

    def _showUpdateInfo(self, status, newVersion, downloadUrl, updateContent):
        if status:
            if newVersion > VERSION:
                updateWidget = UpdateWidget(newVersion, downloadUrl, updateContent)
                if isDarkTheme():
                    updateWidget.setStyleSheet(updateWidget.property("darkCustomQss"))
                else:
                    updateWidget.setStyleSheet(updateWidget.property("lightCustomQss"))
                updateWidget.exec()
            else:
                showTips("已是最新版本")
        else:
            showError("检查更新失败")
        self.checkUpdate = None
