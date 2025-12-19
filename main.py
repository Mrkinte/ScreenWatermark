import os.path
import sys

import winshell
from PySide6.QtCore import QLocale, QTranslator, QTimer
from PySide6.QtGui import QIcon, QAction, QGuiApplication, QPixmap
from PySide6.QtWidgets import QApplication, QSystemTrayIcon, QMenu
from loguru import logger
from qfluentwidgets import FluentTranslator

from utils.app_config import cfg, AppConfig, VERSION
from utils.check_update import CheckUpdate
from utils.web_channel import WebChannel
from widgets.full_watermark_edit_widget import FullWatermarkEditWidget
from widgets.full_watermark_widget import FullTextWatermarkWidget, FullImageWatermarkWidget
from widgets.info_bar import showTips
from widgets.main_window import MainWindow
from widgets.watermark_edit_widget import WatermarkEditWidget
from widgets.watermark_widget import TextWatermarkWidget, ImageWatermarkWidget


class ScreenWatermark:
    def __init__(self):
        logger.add(AppConfig.logDir + "//{time:YYYY-MM-DD}.log", rotation="00:00", retention="7 days", enqueue=True)
        self.app = QApplication(sys.argv)
        self.mainWindow = None

        locale = QLocale(QLocale.Chinese, QLocale.China)
        translator = FluentTranslator(locale)
        galleryTranslator = QTranslator()
        self.app.installTranslator(translator)
        self.app.installTranslator(galleryTranslator)

        if not os.path.exists(AppConfig.configDir):
            os.makedirs(AppConfig.configDir)

        if not os.path.exists(AppConfig.logDir):
            os.makedirs(AppConfig.logDir)

        if cfg.get(cfg.enableAutoBoot):
            self._checkAutoBoot()

        self._createMenu()
        self._widgetSelection()
        self.app.exec()

    def _createMenu(self):
        self.showAction = QAction("显示主窗口")
        self.showAction.triggered.connect(self._createMainWindow)
        self.exitAction = QAction("退出")
        self.exitAction.triggered.connect(self._exitApplication)

        self.menu = QMenu()
        self.menu.addAction(self.showAction)
        self.menu.addAction(self.exitAction)

        self.trayIcon = QSystemTrayIcon()
        self.trayIcon.setIcon(QIcon(":/icons/favicon.png"))
        self.trayIcon.setContextMenu(self.menu)
        self.trayIcon.show()
        self.trayIcon.activated.connect(self._onTrayActivated)

    def _createMainWindow(self, checkUpdate=False):
        if MainWindow.deletedFlag:
            self.mainWindow = MainWindow()
            if checkUpdate:
                self.checkUpdateThread = CheckUpdate()
                self.checkUpdateThread.newVersionSignal.connect(self._tipUpdate)
                self.time = QTimer()
                self.time.setSingleShot(True)
                self.time.timeout.connect(self.checkUpdateThread.start)
                self.time.start(5000)  # 软件打开5s后自动检查是否存在更新
        if self.mainWindow is not None:
            self.mainWindow.show()
            AppConfig.globalMainWindow = self.mainWindow

    def _widgetSelection(self):
        if cfg.get(cfg.watermarkActivated) or cfg.get(cfg.fullWatermarkActivated):
            if cfg.get(cfg.watermarkActivated):
                param = {
                    "bgColor": cfg.get(cfg.watermarkBgColor),
                    "bgOpacity": cfg.get(cfg.watermarkBgOpacity),
                    "bgRadius": cfg.get(cfg.watermarkBgRadius),
                    "watermarkOpacity": cfg.get(cfg.watermarkOpacity),
                    "topLayer": cfg.get(cfg.watermarkTopLayer),
                    "snapToEdge": cfg.get(cfg.watermarkSnapToEdge)
                }
                match cfg.get(cfg.watermarkType):
                    case "TEXT":
                        WatermarkEditWidget.textWatermarkWidget = TextWatermarkWidget()
                        WatermarkEditWidget.textWatermarkWidget.setAllParam(param)
                        html = WebChannel.loadHtmlFromFile(AppConfig.configDir + "\\watermark.html")
                        if html:
                            WatermarkEditWidget.textWatermarkWidget.setHtml(html)
                            WatermarkEditWidget.textWatermarkWidget.setActivated()
                            WatermarkEditWidget.textWatermarkWidget.show()
                        else:
                            logger.error("Html加载失败")
                            cfg.set(cfg.watermarkActivated, False)
                            self._createMainWindow(True)

                    case "IMAGE":
                        image = QPixmap(AppConfig.configDir + "\\watermark.png")
                        WatermarkEditWidget.imageWatermarkWidget = ImageWatermarkWidget()
                        WatermarkEditWidget.imageWatermarkWidget.setAllParam(param)
                        if image:
                            WatermarkEditWidget.imageWatermarkWidget.setImage(image, param["bgRadius"])
                            WatermarkEditWidget.imageWatermarkWidget.setActivated()
                            WatermarkEditWidget.imageWatermarkWidget.show()
                        else:
                            logger.error("图片加载失败")
                            cfg.set(cfg.watermarkActivated, False)
                            self._createMainWindow(True)

            if cfg.get(cfg.fullWatermarkActivated):
                param = {
                    "topLayer": cfg.get(cfg.fullWatermarkTopLayer),
                    "watermarkOpacity": cfg.get(cfg.fullWatermarkOpacity),
                    "hSpacing": cfg.get(cfg.fullWatermarkHSpacing),
                    "vSpacing": cfg.get(cfg.fullWatermarkVSpacing),
                    "angle": cfg.get(cfg.fullWatermarkAngle),
                }
                screens = QGuiApplication.screens()
                match cfg.get(cfg.fullWatermarkType):
                    case "TEXT":
                        for screen in screens:
                            geom = screen.geometry()
                            FullWatermarkEditWidget.fullTextWatermarkWidget.append(FullTextWatermarkWidget(geom))
                        html = WebChannel.loadHtmlFromFile(AppConfig.configDir + "\\fullWatermark.html")
                        for widget in FullWatermarkEditWidget.fullTextWatermarkWidget:
                            if html:
                                widget.setHtml(html)
                                widget.setAllParam(param)
                                widget.setActivated()
                                widget.showFullScreen()
                            else:
                                logger.error("Html加载失败")
                                cfg.set(cfg.fullWatermarkActivated, False)
                                self._createMainWindow(True)

                    case "IMAGE":
                        for screen in screens:
                            geom = screen.geometry()
                            FullWatermarkEditWidget.fullImageWatermarkWidget.append(FullImageWatermarkWidget(geom))
                        image = QPixmap(AppConfig.configDir + "\\fullWatermark.png")
                        for widget in FullWatermarkEditWidget.fullImageWatermarkWidget:
                            if image:
                                widget.setImage(image)
                                widget.setAllParam(param)
                                widget.setActivated()
                                widget.showFullScreen()
                            else:
                                logger.error("图片加载失败")
                                self._createMainWindow(True)
                                cfg.set(cfg.fullWatermarkActivated, False)
                                break
        else:
            self._createMainWindow(True)

    def _checkAutoBoot(self):
        startupFolder = winshell.startup()
        for filename in os.listdir(startupFolder):
            if filename.lower() == "屏幕水印.lnk".lower():
                return
        cfg.set(cfg.enableAutoBoot, False)
        if self.mainWindow is not None:
            if self.mainWindow.isVisible():
                showTips("开机自启动快捷方式已失效，请重新设置。")

    ################
    # Slot methods #
    ################
    def _onTrayActivated(self, reason):
        if reason == QSystemTrayIcon.Trigger:  # 左键单击
            self._createMainWindow()

    def _exitApplication(self):
        self.trayIcon.hide()
        self.app.exit()

    def _tipUpdate(self, status, newVersion):
        if status and self.mainWindow:
            if newVersion > VERSION:
                showTips(f"发现新版本：{newVersion}")


if __name__ == "__main__":
    screenWatermark = ScreenWatermark()
