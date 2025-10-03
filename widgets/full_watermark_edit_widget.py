import os

from PySide6.QtCore import QTimer
from PySide6.QtGui import QGuiApplication
from PySide6.QtWebChannel import QWebChannel
from PySide6.QtWidgets import QWidget

from design.Ui_FullWatermarkEditWidget import Ui_FullWatermarkEditWidget
from utils.app_config import cfg, AppConfig
from utils.web_channel import Bridge, WebChannel
from widgets.full_watermark_widget import FullTextWatermarkWidget, FullImageWatermarkWidget
from widgets.image_widget import ImageWidget
from widgets.info_bar import showTips


class FullWatermarkEditWidget(QWidget):
    fullTextWatermarkWidget = []
    fullImageWatermarkWidget = []

    def __init__(self):
        super().__init__()
        self.ui = Ui_FullWatermarkEditWidget()
        self.ui.setupUi(self)
        self.watermarkType = cfg.get(cfg.fullWatermarkType)
        self.htmlContent = ""
        self.param = {
            "topLayer": cfg.get(cfg.fullWatermarkTopLayer),
            "watermarkOpacity": cfg.get(cfg.fullWatermarkOpacity),
            "hSpacing": cfg.get(cfg.fullWatermarkHSpacing),
            "vSpacing": cfg.get(cfg.fullWatermarkVSpacing),
            "angle": cfg.get(cfg.fullWatermarkAngle),
        }

        # Init widgets
        self.imageWidget = ImageWidget()
        self.ui.stackedWidget.addWidget(self.imageWidget)
        if self.watermarkType == "TEXT":
            self.ui.textBtn.setEnabled(False)
            self.ui.stackedWidget.setCurrentIndex(0)
            if cfg.get(cfg.fullWatermarkActivated):
                self.ui.watermarkStatus.setText("水印状态：文字水印已启用")
        else:
            self.ui.imageBtn.setEnabled(False)
            self.ui.stackedWidget.setCurrentIndex(1)
            if cfg.get(cfg.fullWatermarkActivated):
                self.ui.watermarkStatus.setText("水印状态：图片水印已启用")
        screens = QGuiApplication.screens()
        self.ui.screenNums.setText(f"屏幕数量：{len(screens)}")
        self.ui.opacitySlider.setValue(self.param["watermarkOpacity"])
        self.ui.topLayerCheckBox.setChecked(self.param["topLayer"])
        self.ui.hSpacingSpinBox.setValue(self.param["hSpacing"])
        self.ui.vSpacingSpinBox.setValue(self.param["vSpacing"])
        self.ui.angleSpinBox.setValue(self.param["angle"])

        # Connect to slot
        self.ui.textBtn.clicked.connect(self._textBtnClicked)
        self.ui.imageBtn.clicked.connect(self._imageBtnClicked)
        self.ui.opacitySlider.valueChanged.connect(self._opacitySliderValueChanged)
        self.ui.topLayerCheckBox.stateChanged.connect(self._topLayerCheckBoxStateChanged)
        self.ui.vSpacingSpinBox.valueChanged.connect(self._vSpacingSpinBoxValueChanged)
        self.ui.hSpacingSpinBox.valueChanged.connect(self._hSpacingSpinBoxValueChanged)
        self.ui.angleSpinBox.valueChanged.connect(self._angleSpinBoxValueChanged)
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
            if os.path.exists(AppConfig.configDir + "\\fullWatermark.html"):
                self.htmlContent = WebChannel.loadHtmlFromFile(AppConfig.configDir + "\\fullWatermark.html")
                WebChannel.setEditorHtml(self.ui.webView, self.htmlContent)
            else:
                self.htmlContent = WebChannel.loadHtmlFromFile(":/html/fullTextWatermark.html")
                WebChannel.setEditorHtml(self.ui.webView, self.htmlContent)
            self.timeoutTimer.stop()
            self.timeoutTimer = None

    # Slot
    def _textBtnClicked(self):
        self.ui.imageBtn.setEnabled(True)
        self.ui.textBtn.setDisabled(True)
        self.ui.stackedWidget.setCurrentIndex(0)
        self.watermarkType = "TEXT"

    def _imageBtnClicked(self):
        self.ui.textBtn.setEnabled(True)
        self.ui.imageBtn.setDisabled(True)
        self.ui.stackedWidget.setCurrentIndex(1)
        self.watermarkType = "IMAGE"

    def _opacitySliderValueChanged(self, value):
        self.param["watermarkOpacity"] = value

    def _topLayerCheckBoxStateChanged(self, value):
        self.param["topLayer"] = True if value == 2 else False

    def _vSpacingSpinBoxValueChanged(self, value):
        self.param["vSpacing"] = value

    def _hSpacingSpinBoxValueChanged(self, value):
        self.param["hSpacing"] = value

    def _angleSpinBoxValueChanged(self, value):
        self.param["angle"] = value

    def _previewBtnClicked(self):
        """
        :return: True=正常启用预览模式
        """
        screens = QGuiApplication.screens()
        if self.watermarkType == "TEXT":
            self.htmlContent = WebChannel.getEditorHtml(self.ui.webView)
            if self.htmlContent:
                if FullWatermarkEditWidget.fullImageWatermarkWidget:
                    for widget in FullWatermarkEditWidget.fullImageWatermarkWidget:
                        widget.close()
                    FullWatermarkEditWidget.fullImageWatermarkWidget = []

                if not FullWatermarkEditWidget.fullTextWatermarkWidget:
                    for screen in screens:
                        geom = screen.geometry()
                        FullWatermarkEditWidget.fullTextWatermarkWidget.append(FullTextWatermarkWidget(geom))

                for widget in FullWatermarkEditWidget.fullTextWatermarkWidget:
                    widget.setHtml(self.htmlContent)
                    widget.setAllParam(self.param)
                    widget.setPreviewing()
                    widget.showFullScreen()
                return True
            else:
                showTips("请输入文本")

        elif self.watermarkType == "IMAGE":
            image = self.imageWidget.getImage()
            if image:
                if FullWatermarkEditWidget.fullTextWatermarkWidget:
                    for widget in FullWatermarkEditWidget.fullTextWatermarkWidget:
                        widget.close()
                    FullWatermarkEditWidget.fullTextWatermarkWidget = []

                if not FullWatermarkEditWidget.fullImageWatermarkWidget:
                    for screen in screens:
                        geom = screen.geometry()
                        FullWatermarkEditWidget.fullImageWatermarkWidget.append(FullImageWatermarkWidget(geom))

                for widget in FullWatermarkEditWidget.fullImageWatermarkWidget:
                    widget.setImage(self.imageWidget.getImage())
                    widget.setAllParam(self.param)
                    widget.setPreviewing()
                    widget.showFullScreen()
                return True
            else:
                showTips("请加载图片")
        return False

    def _applyBtnClicked(self):
        if self._previewBtnClicked():
            if self.watermarkType == "TEXT":
                for widget in FullWatermarkEditWidget.fullTextWatermarkWidget:
                    widget.setActivated()
                cfg.set(cfg.fullWatermarkType, "TEXT")
                self.ui.watermarkStatus.setText("水印状态：文字水印已启用")
                WebChannel.saveHtmlToFile("fullWatermark.html", self.htmlContent)

            elif self.watermarkType == "IMAGE":
                for widget in FullWatermarkEditWidget.fullImageWatermarkWidget:
                    widget.setActivated()
                cfg.set(cfg.fullWatermarkType, "IMAGE")
                self.ui.watermarkStatus.setText("水印状态：图片水印已启用")
                self.imageWidget.saveImage("fullWatermark.png")

            cfg.set(cfg.fullWatermarkActivated, True)
            cfg.set(cfg.fullWatermarkTopLayer, self.param["topLayer"])
            cfg.set(cfg.fullWatermarkOpacity, self.param["watermarkOpacity"])
            cfg.set(cfg.fullWatermarkVSpacing, self.param["vSpacing"])
            cfg.set(cfg.fullWatermarkHSpacing, self.param["hSpacing"])
            cfg.set(cfg.fullWatermarkAngle, self.param["angle"])

    def _closeBtnClicked(self):
        if FullWatermarkEditWidget.fullTextWatermarkWidget:
            for widget in FullWatermarkEditWidget.fullTextWatermarkWidget:
                widget.close()
            FullWatermarkEditWidget.fullTextWatermarkWidget = []

        if FullWatermarkEditWidget.fullImageWatermarkWidget:
            for widget in FullWatermarkEditWidget.fullImageWatermarkWidget:
                widget.close()
            FullWatermarkEditWidget.fullImageWatermarkWidget = []

        cfg.set(cfg.fullWatermarkActivated, False)
        self.ui.watermarkStatus.setText("水印状态：未启用")
