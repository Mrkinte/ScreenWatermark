from xml.etree import ElementTree as ET

import requests
from PySide6.QtCore import QThread, Signal
from loguru import logger

from utils.app_config import VERSION


class CheckUpdate(QThread):
    newVersionSignal = Signal(bool, str, str, str)  # status, version, downloadLink, updateContent

    def __init__(self):
        super().__init__()
        self.setObjectName("CheckUpdateThread")
        self.currentVersion = VERSION
        self.versionUrl = "https://raw.githubusercontent.com/Mrkinte/ScreenWatermark/main/version.txt"

    def run(self):
        try:
            logger.info("检查更新...")
            response = requests.get(self.versionUrl)
            response.raise_for_status()  # 检查请求是否成功
        except requests.exceptions.RequestException as e:
            logger.warning(f"获取更新信息失败: {e}")
            self.newVersionSignal.emit(False, "", "", "")
            return

        # 解析XML内容
        try:
            root = ET.fromstring(response.content)
            # 提取版本信息
            newVersion = root.find('version').text
            githubLink = root.find('GitHub/link').text
            updateContent = root.find('update_contents/contents_zh_cn').text

            if newVersion > self.currentVersion:
                logger.info(f"发现新版本: {newVersion} (当前版本: {self.currentVersion})")
                self.newVersionSignal.emit(True, newVersion, githubLink, updateContent)
            else:
                logger.info(f"当前已是最新版本 ({self.currentVersion})")
                self.newVersionSignal.emit(True, newVersion, "", "")

        except ET.ParseError:
            logger.error("解析version.txt失败：无效的XML格式")
            self.newVersionSignal.emit(False, "", "", "")
        except AttributeError:
            logger.error("解析version.txt失败：缺少必要的XML元素")
            self.newVersionSignal.emit(False, "", "", "")
