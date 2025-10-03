from PySide6.QtCore import Qt
from PySide6.QtWidgets import QWidget
from qfluentwidgets import InfoBar, InfoBarIcon, InfoBarPosition

from utils.app_config import AppConfig


def showTips(text: str, parent: QWidget = None):
    _parent = None
    if parent is not None:
        _parent = parent
    elif AppConfig.globalMainWindow:
        _parent = AppConfig.globalMainWindow
    else:
        return

    w = InfoBar(
        icon=InfoBarIcon.INFORMATION,
        title="提示",
        content=text,
        orient=Qt.Horizontal,
        isClosable=True,
        position=InfoBarPosition.TOP,
        duration=3000,
        parent=_parent
    )
    w.show()


def showError(text: str, parent: QWidget = None):
    _parent = None
    if parent is not None:
        _parent = parent
    elif AppConfig.globalMainWindow is not None:
        _parent = AppConfig.globalMainWindow
    else:
        return

    w = InfoBar(
        icon=InfoBarIcon.ERROR,
        title="错误",
        content=text,
        orient=Qt.Horizontal,
        isClosable=True,
        position=InfoBarPosition.TOP,
        duration=3000,
        parent=_parent
    )
    w.show()
