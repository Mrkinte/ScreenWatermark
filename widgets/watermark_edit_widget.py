import os

from PySide6.QtCore import QTimer
from PySide6.QtGui import QColor
from PySide6.QtWebChannel import QWebChannel
from PySide6.QtWidgets import QWidget
from qfluentwidgets import ColorDialog

from design.Ui_WatermarkEditWidget import Ui_WatermarkEditWidget
from utils.app_config import cfg, AppConfig
from utils.web_channel import Bridge, WebChannel
from widgets.image_widget import ImageWidget
from widgets.info_bar import showTips
from widgets.watermark_widget import TextWatermarkWidget, ImageWatermarkWidget


class WatermarkEditWidget(QWidget):
    textWatermarkWidget = None
    imageWatermarkWidget = None

    def __init__(self):
        super().__init__()
        self.ui = Ui_WatermarkEditWidget()
        self.ui.setupUi(self)
        self.watermarkType = cfg.get(cfg.watermarkType)
        self.htmlContent = ""
        self.param = {
            "bgColor": cfg.get(cfg.watermarkBgColor),
            "bgOpacity": cfg.get(cfg.watermarkBgOpacity),
            "bgRadius": cfg.get(cfg.watermarkBgRadius),
            "watermarkOpacity": cfg.get(cfg.watermarkOpacity),
            "topLayer": cfg.get(cfg.watermarkTopLayer),
            "snapToEdge": cfg.get(cfg.watermarkSnapToEdge)
        }

        # Init widgets
        self.imageWidget = ImageWidget()
        self.ui.stackedWidget.addWidget(self.imageWidget)
        if self.watermarkType == "TEXT":
            self.ui.textBtn.setEnabled(False)
            self.ui.stackedWidget.setCurrentIndex(0)
            if cfg.get(cfg.watermarkActivated):
                self.ui.watermarkStatus.setText("水印状态：文字水印已启用")
        else:
            self.ui.imageBtn.setEnabled(False)
            self.ui.stackedWidget.setCurrentIndex(1)
            self.ui.bgWidget.setVisible(False)
            if cfg.get(cfg.watermarkActivated):
                self.ui.watermarkStatus.setText("水印状态：图片水印已启用")
        self.ui.bgColorBtn.setStyleSheet(f"background-color:{self.param['bgColor']}; border: none; border-radius: 5px;")
        self.ui.bgOpacitySlider.setValue(self.param["bgOpacity"] * 100)
        self.ui.bgRadiusSpinBox.setValue(self.param["bgRadius"])
        self.ui.watermarkOpacitySlider.setValue(self.param["watermarkOpacity"] * 100)
        self.ui.topLayerCheckBox.setChecked(self.param["topLayer"])
        self.ui.snapToEdgeCheckBox.setChecked(self.param["snapToEdge"])

        # Connect to slot
        self.ui.textBtn.clicked.connect(self._textBtnClicked)
        self.ui.imageBtn.clicked.connect(self._imageBtnClicked)
        self.ui.bgColorBtn.clicked.connect(self._bgColorBtnClicked)
        self.ui.bgOpacitySlider.valueChanged.connect(self._bgOpacitySliderValueChanged)
        self.ui.bgRadiusSpinBox.valueChanged.connect(self._bgRadiusSpinBoxValueChanged)
        self.ui.watermarkOpacitySlider.valueChanged.connect(self._watermarkOpacitySliderValueChanged)
        self.ui.topLayerCheckBox.stateChanged.connect(self._topLayerCheckBoxStateChanged)
        self.ui.snapToEdgeCheckBox.stateChanged.connect(self._snapToEdgeCheckBoxStateChanged)
        self.ui.previewBtn.clicked.connect(self._previewBtnClicked)
        self.ui.applyBtn.clicked.connect(self._applyBtnClicked)
        self.ui.closeBtn.clicked.connect(self._closeBtnClicked)

        # WebEngineView
        self.channel = QWebChannel()
        self.bridge = Bridge()
        self.channel.registerObject("pyBridge", self.bridge)
        self.ui.webView.page().setWebChannel(self.channel)
        self.timeoutTimer = QTimer()
        self.timeoutTimer.timeout.connect(self._initWebView)
        self.timeoutTimer.start(500)

    def _initWebView(self):
        if WebChannel.getEditorStatus(self.ui.webView):
            if os.path.exists(AppConfig.configDir + "\\watermark.html"):
                self.htmlContent = WebChannel.loadHtmlFromFile(AppConfig.configDir + "\\watermark.html")
                WebChannel.setEditorHtml(self.ui.webView, self.htmlContent)
            else:
                self.htmlContent = WebChannel.loadHtmlFromFile(":/html/textWatermark.html")
                WebChannel.setEditorHtml(self.ui.webView, self.htmlContent)
            self.timeoutTimer.stop()
            self.timeoutTimer = None

    ################
    # Slot methods #
    ################
    def _textBtnClicked(self):
        self.ui.imageBtn.setEnabled(True)
        self.ui.textBtn.setDisabled(True)
        self.ui.stackedWidget.setCurrentIndex(0)
        self.ui.bgWidget.setVisible(True)
        self.watermarkType = "TEXT"

    def _imageBtnClicked(self):
        self.ui.textBtn.setEnabled(True)
        self.ui.imageBtn.setDisabled(True)
        self.ui.stackedWidget.setCurrentIndex(1)
        self.ui.bgWidget.setVisible(False)
        self.watermarkType = "IMAGE"

    def _bgColorBtnClicked(self):
        colorDialog = ColorDialog(QColor(self.param["bgColor"]), "设置背景颜色", AppConfig.globalMainWindow, False)
        colorDialog.colorChanged.connect(self._bgColorChanged)
        colorDialog.exec()

    def _bgColorChanged(self, color):
        self.param["bgColor"] = color.name()
        self.ui.bgColorBtn.setStyleSheet(f"background-color:{color.name()}; border: none; border-radius: 5px;")

    def _bgOpacitySliderValueChanged(self, value):
        self.param["bgOpacity"] = value / 100.0

    def _bgRadiusSpinBoxValueChanged(self, value):
        self.param["bgRadius"] = value

    def _watermarkOpacitySliderValueChanged(self, value):
        self.param["watermarkOpacity"] = value / 100.0

    def _topLayerCheckBoxStateChanged(self, value):
        self.param["topLayer"] = True if value == 2 else False

    def _snapToEdgeCheckBoxStateChanged(self, value):
        self.param["snapToEdge"] = True if value == 2 else False
        if self.textWatermarkWidget:
            self.textWatermarkWidget.setOneParam("snapToEdge", self.param["snapToEdge"])

    def _previewBtnClicked(self):
        """
        :return: True=正常启用预览模式
        """
        if self.watermarkType == "TEXT":
            self.htmlContent = WebChannel.getEditorHtml(self.ui.webView)
            if self.htmlContent:
                if WatermarkEditWidget.imageWatermarkWidget:  # 关闭图片水印
                    WatermarkEditWidget.imageWatermarkWidget.close()
                    WatermarkEditWidget.imageWatermarkWidget = None

                if not WatermarkEditWidget.textWatermarkWidget:
                    WatermarkEditWidget.textWatermarkWidget = TextWatermarkWidget()
                WatermarkEditWidget.textWatermarkWidget.setAllParam(self.param)
                WatermarkEditWidget.textWatermarkWidget.setHtml(self.htmlContent)
                WatermarkEditWidget.textWatermarkWidget.setPreviewing()
                WatermarkEditWidget.textWatermarkWidget.show()
                return True
            else:
                showTips("请输入文本")

        elif self.watermarkType == "IMAGE":
            image = self.imageWidget.getImage()
            if image:
                if WatermarkEditWidget.textWatermarkWidget:  # 关闭文本水印
                    WatermarkEditWidget.textWatermarkWidget.close()
                    WatermarkEditWidget.textWatermarkWidget = None

                if not WatermarkEditWidget.imageWatermarkWidget:
                    WatermarkEditWidget.imageWatermarkWidget = ImageWatermarkWidget()
                WatermarkEditWidget.imageWatermarkWidget.setAllParam(self.param)
                WatermarkEditWidget.imageWatermarkWidget.setImage(self.imageWidget.getImage(), self.param["bgRadius"])
                WatermarkEditWidget.imageWatermarkWidget.setPreviewing()
                WatermarkEditWidget.imageWatermarkWidget.show()
                return True
            else:
                showTips("请加载图片")
        return False

    def _applyBtnClicked(self):
        if self._previewBtnClicked():
            if self.watermarkType == "TEXT":
                WatermarkEditWidget.textWatermarkWidget.setActivated()
                cfg.set(cfg.watermarkActivated, True)
                x = WatermarkEditWidget.textWatermarkWidget.pos().x()
                y = WatermarkEditWidget.textWatermarkWidget.pos().y()
                cfg.set(cfg.watermarkPosX, x)
                cfg.set(cfg.watermarkPosY, y)
                cfg.set(cfg.watermarkType, "TEXT")
                self.ui.watermarkStatus.setText("水印状态：文字水印已启用")
                WebChannel.saveHtmlToFile("watermark.html", self.htmlContent)

            elif self.watermarkType == "IMAGE":
                WatermarkEditWidget.imageWatermarkWidget.setActivated()
                cfg.set(cfg.watermarkActivated, True)
                x = WatermarkEditWidget.imageWatermarkWidget.pos().x()
                y = WatermarkEditWidget.imageWatermarkWidget.pos().y()
                cfg.set(cfg.watermarkPosX, x)
                cfg.set(cfg.watermarkPosY, y)
                cfg.set(cfg.watermarkType, "IMAGE")
                self.ui.watermarkStatus.setText("水印状态：图片水印已启用")
                self.imageWidget.saveImage("watermark.png")

            cfg.set(cfg.watermarkBgColor, self.param["bgColor"])
            cfg.set(cfg.watermarkBgOpacity, self.param["bgOpacity"])
            cfg.set(cfg.watermarkBgRadius, self.param["bgRadius"])
            cfg.set(cfg.watermarkOpacity, self.param["watermarkOpacity"])
            cfg.set(cfg.watermarkTopLayer, self.param["topLayer"])
            cfg.set(cfg.watermarkSnapToEdge, self.param["snapToEdge"])

    def _closeBtnClicked(self):
        if WatermarkEditWidget.textWatermarkWidget:
            WatermarkEditWidget.textWatermarkWidget.close()
            WatermarkEditWidget.textWatermarkWidget = None

        if WatermarkEditWidget.imageWatermarkWidget:
            WatermarkEditWidget.imageWatermarkWidget.close()
            WatermarkEditWidget.imageWatermarkWidget = None

        cfg.set(cfg.watermarkActivated, False)
        self.ui.watermarkStatus.setText("水印状态：未启用")
