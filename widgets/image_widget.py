import os

from PySide6.QtCore import Qt
from PySide6.QtGui import QPixmap, QTransform
from PySide6.QtWidgets import QWidget, QFileDialog

from design.Ui_ImageWidget import Ui_ImageWidget
from utils.app_config import AppConfig
from widgets.info_bar import showError, showTips


class ImageWidget(QWidget):
    def __init__(self):
        super().__init__()
        self.ui = Ui_ImageWidget()
        self.ui.setupUi(self)

        self.currentImagePath = None
        self.originalPixmap = None
        self.scaledPixmap = None
        self.rotatedPixmap = None  # 添加旋转后的图片缓存
        self.maxDisplaySize = 300  # 最大显示尺寸
        self.rotationAngle = 0  # 当前旋转角度

        self.ui.zoomSlider.setOrientation(Qt.Vertical)
        self.ui.loadImageBtn.clicked.connect(self._loadImageBtnClicked)
        self.ui.deleteImageBtn.clicked.connect(self._deleteImageBtnClicked)
        self.ui.zoomSlider.valueChanged.connect(self._zoomSliderValueChanged)
        self.ui.rotateLeftBtn.clicked.connect(self._rotateLeft)
        self.ui.rotateRightBtn.clicked.connect(self._rotateRight)

    def _loadImageBtnClicked(self):
        filePath, _ = QFileDialog.getOpenFileName(
            self, "选择图片", "",
            "图片文件 (*.png *.jpg *.jpeg *.bmp)"
        )

        if not filePath:
            return

        try:
            self.currentImagePath = filePath
            self.originalPixmap = QPixmap(filePath)
            if self.originalPixmap.isNull():
                showError("无法加载图片")
                return

            # 重置旋转角度
            self.rotationAngle = 0

            # 获取原始尺寸
            originalWidth = self.originalPixmap.width()
            originalHeight = self.originalPixmap.height()

            # 计算缩放比例以适应最大显示尺寸
            scaleFactor = 1.0
            if originalWidth > self.maxDisplaySize or originalHeight > self.maxDisplaySize:
                if originalWidth > originalHeight:
                    scaleFactor = self.maxDisplaySize / originalWidth
                else:
                    scaleFactor = self.maxDisplaySize / originalHeight

            # 应用初始缩放
            scaled_width = int(originalWidth * scaleFactor)
            scaled_height = int(originalHeight * scaleFactor)

            # 创建缩放后的图片
            self.scaledPixmap = self.originalPixmap.scaled(
                scaled_width, scaled_height,
                Qt.KeepAspectRatio, Qt.SmoothTransformation
            )

            # 初始化旋转后的图片
            self.rotatedPixmap = self.scaledPixmap.copy()

            # 显示图片
            self.ui.imageLabel.setPixmap(self.rotatedPixmap)

            # 更新UI状态
            self.ui.zoomSlider.setEnabled(True)
            self.ui.deleteImageBtn.setEnabled(True)
            self.ui.rotateLeftBtn.setEnabled(True)
            self.ui.rotateRightBtn.setEnabled(True)

            # 计算滑块初始值（基于原始尺寸）
            slider_value = int(scaleFactor * 100)
            self.ui.zoomSlider.setValue(slider_value)
            # self.ui.zoomLabel.setText(f"{slider_value}%")

            # 显示状态信息
            filename = os.path.basename(filePath)
            showTips(f"{filename} （原始尺寸:{originalWidth}x{originalHeight}）")

        except Exception as e:
            showError(str(e))

    def _deleteImageBtnClicked(self):
        self.currentImagePath = None
        self.originalPixmap = None
        self.scaledPixmap = None
        self.rotatedPixmap = None
        self.rotationAngle = 0
        self.ui.imageLabel.clear()
        self.ui.imageLabel.setText("请加载图片")
        self.ui.zoomSlider.setMaximum(100)
        self.ui.zoomSlider.setValue(100)
        self.ui.zoomSlider.setEnabled(False)
        self.ui.deleteImageBtn.setEnabled(False)
        self.ui.rotateLeftBtn.setEnabled(False)
        self.ui.rotateRightBtn.setEnabled(False)

    def _zoomSliderValueChanged(self, value):
        if not self.originalPixmap:
            return

        # self.zoomLabel.setText(f"{value}%")
        # 计算缩放比例
        scaleFactor = value / 100.0
        # 计算缩放后的尺寸
        originalSize = self.originalPixmap.size()
        scaledWidth = int(originalSize.width() * scaleFactor)
        scaledHeight = int(originalSize.height() * scaleFactor)
        # 缩放图片
        self.scaledPixmap = self.originalPixmap.scaled(
            scaledWidth, scaledHeight,
            Qt.KeepAspectRatio, Qt.SmoothTransformation
        )

        # 应用旋转
        self._applyRotation()
        self.ui.imageLabel.setPixmap(self.rotatedPixmap)

    def _rotateLeft(self):
        self._rotateImage(-90)

    def _rotateRight(self):
        self._rotateImage(90)

    def _rotateImage(self, angle):
        if not self.originalPixmap:
            return

        # 更新旋转角度（0-360度范围内）
        self.rotationAngle = (self.rotationAngle + angle) % 360
        if self.rotationAngle < 0:
            self.rotationAngle += 360

        self._applyRotation()
        self.ui.imageLabel.setPixmap(self.rotatedPixmap)

    def _applyRotation(self):
        if not self.scaledPixmap:
            return

        if self.rotationAngle != 0:
            transform = QTransform().rotate(self.rotationAngle)
            self.rotatedPixmap = self.scaledPixmap.transformed(transform, Qt.SmoothTransformation)
        else:
            self.rotatedPixmap = self.scaledPixmap.copy()

    def saveImage(self, fileName: str):
        if not self.rotatedPixmap or not self.currentImagePath:
            return

        try:
            savePath = os.path.join(AppConfig.configDir, fileName)
            if not os.path.exists(AppConfig.configDir):
                os.makedirs(AppConfig.configDir)
            self.rotatedPixmap.save(savePath)

        except Exception as e:
            showError(str(e))

    def getImage(self):
        # 返回旋转后的图片
        return self.rotatedPixmap
