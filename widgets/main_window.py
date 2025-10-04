from PySide6.QtGui import QIcon, Qt
from qfluentwidgets import FluentIcon, NavigationItemPosition, SplitFluentWindow, setTheme

from utils.app_config import cfg, AppConfig
from widgets.full_watermark_edit_widget import FullWatermarkEditWidget
from widgets.settings_widget import SettingsWidget
from widgets.watermark_edit_widget import WatermarkEditWidget


class MainWindow(SplitFluentWindow):
    deletedFlag = True

    def __init__(self):
        super().__init__()
        setTheme(cfg.get(cfg.themeMode))
        MainWindow.deletedFlag = False

        self.setWindowIcon(QIcon(':/icons/favicon.png'))
        self.setWindowTitle("屏幕水印")
        self.resize(960, 720)
        self.navigationInterface.setExpandWidth(200)

        self.waterMarkInterface = WatermarkEditWidget()
        self.addSubInterface(self.waterMarkInterface,
                             FluentIcon.TILES,
                             "局部水印")

        self.fullWaterMarkInterface = FullWatermarkEditWidget()
        self.addSubInterface(self.fullWaterMarkInterface,
                             FluentIcon.FIT_PAGE,
                             "全屏水印")

        self.settingsInterface = SettingsWidget()
        self.addSubInterface(self.settingsInterface,
                             FluentIcon.SETTING,
                             "设置",
                             NavigationItemPosition.BOTTOM)

        # 重启云母特效，消除添加WebEngineView导致的显示异常。
        self.setAttribute(Qt.WidgetAttribute.WA_TranslucentBackground)
        self.updateFrameless()
        self.setMicaEffectEnabled(True)

    def closeEvent(self, event):
        super().closeEvent(event)
        MainWindow.deletedFlag = True
        AppConfig.globalMainWindow = None
        self.deleteLater()
