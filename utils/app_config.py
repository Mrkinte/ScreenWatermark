import os
import sys

from PySide6.QtCore import Qt
from PySide6.QtWidgets import QApplication
from qfluentwidgets import QConfig, BoolValidator, ConfigItem, RangeValidator, qconfig, ConfigValidator, \
    RangeConfigItem, OptionsConfigItem, OptionsValidator, Theme, setTheme


class StringValidator(ConfigValidator):
    def validate(self, value):
        return isinstance(value, str)

    def correct(self, value):
        return str(value)


class AppConfig(QConfig):
    globalMainWindow = None  # 全局可访问主窗口

    # 配置文件所在目录
    if getattr(sys, 'frozen', False):
        configDir = os.path.dirname(sys.executable) + "\\config"
        logDir = os.path.dirname(sys.executable) + "\\log"
    else:
        configDir = os.getcwd() + "\\config"
        logDir = os.getcwd() + "\\log"

    # 开机自启动
    enableAutoBoot = ConfigItem("MainWindow", "EnableAutoBoot", False, BoolValidator())
    dpiScale = OptionsConfigItem(
        "MainWindow", "DpiScale", "Auto", OptionsValidator([1, 1.25, 1.5, 1.75, 2, "Auto"]), restart=True)

    # 局部水印 参数
    watermarkActivated = ConfigItem("Watermark", "Activated", False, BoolValidator())
    watermarkPosX = RangeConfigItem("Watermark", "PosX", 0, RangeValidator(0, 65535))
    watermarkPosY = RangeConfigItem("Watermark", "PosY", 0, RangeValidator(0, 65535))
    watermarkType = ConfigItem("Watermark", "Type", "TEXT")
    watermarkBgColor = ConfigItem("Watermark", "BgColor", "#7F7F7F")
    watermarkBgOpacity = RangeConfigItem("Watermark", "BgOpa", 1, RangeValidator(0, 1.0))
    watermarkBgRadius = RangeConfigItem("Watermark", "BgRadius", 10, RangeValidator(0, 100))
    watermarkOpacity = RangeConfigItem("Watermark", "Opa", 1, RangeValidator(0, 1.0))
    watermarkTopLayer = ConfigItem("Watermark", "TopLayer", True, BoolValidator())
    watermarkSnapToEdge = ConfigItem("Watermark", "SnapToEdge", True, BoolValidator())

    # 全屏水印 参数
    fullWatermarkActivated = ConfigItem("FullWatermark", "Activated", False, BoolValidator())
    fullWatermarkType = ConfigItem("FullWatermark", "Type", "TEXT")
    fullWatermarkTopLayer = ConfigItem("FullWatermark", "TopLayer", True, BoolValidator())
    fullWatermarkOpacity = RangeConfigItem("FullWatermark", "Opa", 255, RangeValidator(0, 255))
    fullWatermarkVSpacing = RangeConfigItem("FullWatermark", "VSpacing", 100, RangeValidator(0, 255))
    fullWatermarkHSpacing = RangeConfigItem("FullWatermark", "HSpacing", 100, RangeValidator(0, 255))
    fullWatermarkAngle = RangeConfigItem("FullWatermark", "Angle", 30, RangeValidator(0, 360))


VERSION = "1.0.0"
AUTHOR = "Mrkinte"
YEAR = 2025

cfg = AppConfig()
qconfig.load(AppConfig.configDir + "\\config.json", cfg)
