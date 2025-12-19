import os

from PySide6.QtCore import QFile, QIODevice, QTextStream, QObject, QEventLoop, QTimer
from PySide6.QtWebEngineWidgets import QWebEngineView
from loguru import logger

from utils.app_config import AppConfig


class Bridge(QObject):
    def __init__(self):
        super().__init__()


class WebChannel:
    @staticmethod
    def loadHtmlFromFile(path):
        file = QFile(path)
        if not file.open(QIODevice.ReadOnly | QIODevice.Text):
            return ""
        stream = QTextStream(file)
        html = stream.readAll()
        file.close()
        return html

    @staticmethod
    def getEditorHtml(webView: QWebEngineView):
        loop = QEventLoop()
        timeoutTimer = QTimer()
        timeoutTimer.setSingleShot(True)
        timeoutTimer.timeout.connect(loop.quit)
        timeoutTimer.start(3000)
        result = ""

        def handleResult(html):
            nonlocal result
            result = html
            loop.quit()

        # 执行JavaScript代码
        webView.page().runJavaScript(
            "window.getContent();",
            handleResult
        )
        loop.exec()
        if timeoutTimer.isActive():
            timeoutTimer.stop()
        else:
            logger.error("获取Html内容超时。")

        if result == "<p style=\"line-height: 1;\"><br></p>":
            return ""
        else:
            return result

    @staticmethod
    def getEditorStatus(webView: QWebEngineView):
        loop = QEventLoop()
        timeoutTimer = QTimer()
        timeoutTimer.setSingleShot(True)
        timeoutTimer.timeout.connect(loop.quit)
        timeoutTimer.start(3000)
        result = False

        def handleResult(status):
            nonlocal result
            result = status
            loop.quit()

        # 执行JavaScript代码
        webView.page().runJavaScript(
            "window.getWangEditorStatus();",
            handleResult
        )
        loop.exec()
        if timeoutTimer.isActive():
            timeoutTimer.stop()
        else:
            logger.error("获取Editor状态超时。")

        return result

    @staticmethod
    def setEditorHtml(webView: QWebEngineView, html):
        js_code = f"window.setContent({repr(html)});"
        webView.page().runJavaScript(js_code)

    @staticmethod
    def saveHtmlToFile(fileName, htmlContent):
        # 确保目录存在，不存在则创建
        os.makedirs(AppConfig.configDir, exist_ok=True)
        filePath = os.path.join(AppConfig.configDir, fileName)

        # 写入文件（使用UTF-8编码）
        try:
            with open(filePath, 'w', encoding='utf-8') as file:
                file.write(htmlContent)
            logger.info(f"HTML文件已成功保存至: {filePath}")
            return True
        except Exception as e:
            logger.error(f"保存文件时出错: {str(e)}")
            return False
