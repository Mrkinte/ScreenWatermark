from PySide6.QtCore import QPoint
from PySide6.QtGui import QTextOption, Qt, QColor, QPixmap, QPainter, QPainterPath
from PySide6.QtWidgets import QTextBrowser, QApplication, QWidget, QLabel, QHBoxLayout, QGraphicsOpacityEffect

from utils.app_config import cfg


class TextWatermarkWidget(QTextBrowser):
    def __init__(self):
        super().__init__()
        self.offset = QPoint()
        self.previewing = False
        self.dragging = False
        self.activated = False
        self.param = {}

        # Init widget
        self.setWindowFlag(Qt.FramelessWindowHint)
        self.setAttribute(Qt.WA_TranslucentBackground)
        self.setAttribute(Qt.WA_TransparentForMouseEvents)
        self.setWindowFlag(Qt.Tool)

        self.setWordWrapMode(QTextOption.NoWrap)
        self.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.setStyleSheet("background-color: transparent; border: None;")
        self.setContextMenuPolicy(Qt.ContextMenuPolicy.NoContextMenu)

        self.document().setDocumentMargin(10)
        self.move(cfg.get(cfg.watermarkPosX), cfg.get(cfg.watermarkPosY))

    def setOneParam(self, key, value):
        self.param[key] = value

    def setAllParam(self, param: dict):
        self.param = param
        bgColor = QColor(param["bgColor"])
        self.viewport().setStyleSheet(f"""
            background-color: rgba({bgColor.red()}, {bgColor.green()}, {bgColor.blue()}, {param["bgOpacity"]});
            border-radius: {param["bgRadius"]}px;
        """)
        self.setWindowOpacity(param["watermarkOpacity"])
        self.setWindowFlag(Qt.WindowStaysOnTopHint, param["topLayer"])

    def setActivated(self):
        self.previewing = False
        self.activated = True
        self.setAttribute(Qt.WA_TransparentForMouseEvents, True)
        self.setWindowFlag(Qt.WindowTransparentForInput, True)
        self.show()

    def setPreviewing(self):
        self.previewing = True
        self.activated = False
        self.setAttribute(Qt.WA_TransparentForMouseEvents, False)
        self.setWindowFlag(Qt.WindowTransparentForInput, False)
        self.show()

    def _updateWidgetSize(self, ):
        # 计算文档的理想大小
        doc = self.document()
        doc.adjustSize()  # 确保文档已布局完成

        ideal_width = doc.idealWidth()
        ideal_height = doc.size().height()
        self.setFixedSize(int(ideal_width), int(ideal_height))

    ###################
    # Event rewriting #
    ###################
    def showEvent(self, event):
        super().showEvent(event)
        self._updateWidgetSize()

    def mousePressEvent(self, event):
        if event.button() == Qt.LeftButton and self.previewing:
            self.dragging = True
            self.offset = event.globalPosition().toPoint() - self.frameGeometry().topLeft()

    def mouseMoveEvent(self, event):
        if self.dragging:
            self.move(event.globalPosition().toPoint() - self.offset)

    def mouseReleaseEvent(self, event):
        if event.button() == Qt.LeftButton:
            self.dragging = False
            if self.param["snapToEdge"]:
                snapToEdge(self)

    def enterEvent(self, event):
        if self.previewing:
            QApplication.setOverrideCursor(Qt.SizeAllCursor)
            super().enterEvent(event)

    def leaveEvent(self, event):
        QApplication.restoreOverrideCursor()
        super().leaveEvent(event)

    def closeEvent(self, event):
        if self.activated:
            event.ignore()
        else:
            super().closeEvent(event)


class ImageWatermarkWidget(QWidget):
    def __init__(self):
        super().__init__()
        self.offset = QPoint()
        self.previewing = False
        self.dragging = False
        self.activated = False
        self.param = {}

        # Init widget
        self.imageLabel = RoundedImageLabel()
        self.layout = QHBoxLayout()
        self.layout.setContentsMargins(0, 0, 0, 0)
        self.layout.addWidget(self.imageLabel)
        self.setLayout(self.layout)

        self.setWindowFlag(Qt.FramelessWindowHint)
        self.setAttribute(Qt.WA_TranslucentBackground)
        self.setAttribute(Qt.WA_TransparentForMouseEvents)
        self.setWindowFlag(Qt.Tool)

        self.move(cfg.get(cfg.watermarkPosX), cfg.get(cfg.watermarkPosY))

    def setOneParam(self, key, value):
        self.param[key] = value

    def setAllParam(self, param: dict):
        self.param = param
        self.setWindowFlag(Qt.WindowStaysOnTopHint, param["topLayer"])
        self.imageLabel.setOpacity(param["watermarkOpacity"])

    def setImage(self, pixmap, radius):
        self.imageLabel.setRoundedPixmap(pixmap, radius)
        self.adjustSize()

    def setActivated(self):
        self.previewing = False
        self.activated = True
        self.setAttribute(Qt.WA_TransparentForMouseEvents, True)
        self.setWindowFlag(Qt.WindowTransparentForInput, True)
        self.show()

    def setPreviewing(self):
        self.previewing = True
        self.activated = False
        self.setAttribute(Qt.WA_TransparentForMouseEvents, False)
        self.setWindowFlag(Qt.WindowTransparentForInput, False)
        self.show()

    ###################
    # Event rewriting #
    ###################
    def mousePressEvent(self, event):
        if event.button() == Qt.LeftButton and self.previewing:
            self.dragging = True
            self.offset = event.globalPosition().toPoint() - self.frameGeometry().topLeft()

    def mouseMoveEvent(self, event):
        if self.dragging:
            self.move(event.globalPosition().toPoint() - self.offset)

    def mouseReleaseEvent(self, event):
        if event.button() == Qt.LeftButton:
            self.dragging = False
            if self.param["snapToEdge"]:
                snapToEdge(self)

    def enterEvent(self, event):
        if self.previewing:
            QApplication.setOverrideCursor(Qt.SizeAllCursor)
            super().enterEvent(event)

    def leaveEvent(self, event):
        QApplication.restoreOverrideCursor()
        super().leaveEvent(event)

    def closeEvent(self, event):
        if self.activated:
            event.ignore()
        else:
            super().closeEvent(event)


class RoundedImageLabel(QLabel):
    def __init__(self):
        super().__init__()
        self.radius = 0
        self.opacity = 1.0  # 默认完全不透明
        self.setAlignment(Qt.AlignmentFlag.AlignCenter)

        # 创建透明度效果对象
        self.opacity_effect = QGraphicsOpacityEffect(self)
        self.setGraphicsEffect(self.opacity_effect)

    def setRoundedPixmap(self, pixmap, radius=None):
        if radius is not None:
            self.radius = radius

        rounded_pixmap = self.createRoundedPixmap(pixmap, self.radius)
        self.opacity_effect.setOpacity(self.opacity)
        self.setPixmap(rounded_pixmap)

    def setOpacity(self, opacity):
        """设置透明度 (0.0-1.0)"""
        self.opacity = max(0.0, min(opacity, 1.0))

    @staticmethod
    def createRoundedPixmap(pixmap, radius):
        """创建圆角图片"""
        if pixmap.isNull():
            return QPixmap()

        # 创建目标图片（透明背景）
        rounded = QPixmap(pixmap.size())
        rounded.fill(Qt.GlobalColor.transparent)

        # 使用QPainter绘制圆角图片
        painter = QPainter(rounded)
        painter.setRenderHints(QPainter.RenderHint.Antialiasing |
                               QPainter.RenderHint.SmoothPixmapTransform)

        # 创建圆角矩形路径
        path = QPainterPath()
        path.addRoundedRect(0, 0, pixmap.width(), pixmap.height(), radius, radius)
        painter.setClipPath(path)

        # 绘制原始图片
        painter.drawPixmap(0, 0, pixmap)
        painter.end()

        return rounded

    def sizeHint(self):
        if self.pixmap() and not self.pixmap().isNull():
            return self.pixmap().size()
        return super().sizeHint()


# Staticmethod
def snapToEdge(widget):
    """吸附到屏幕边缘"""
    snapThreshold = 15
    # 获取屏幕的几何信息
    screenGeometry = QApplication.primaryScreen().availableGeometry()
    # 获取窗口的几何信息
    windowGeometry = widget.frameGeometry()
    # 计算窗口到屏幕各边的距离
    leftDistance = windowGeometry.left() - screenGeometry.left()
    rightDistance = screenGeometry.right() - windowGeometry.right()
    topDistance = windowGeometry.top() - screenGeometry.top()
    bottomDistance = screenGeometry.bottom() - windowGeometry.bottom()
    # 初始化新位置
    newX = windowGeometry.x()
    newY = windowGeometry.y()

    # 左边缘
    if leftDistance < snapThreshold:
        newX = screenGeometry.left()

    # 右边缘
    elif rightDistance < snapThreshold:
        newX = screenGeometry.right() - windowGeometry.width() + 1

    # 上边缘
    if topDistance < snapThreshold:
        newY = screenGeometry.top()

    # 下边缘
    elif bottomDistance < snapThreshold:
        newY = screenGeometry.bottom() - windowGeometry.height() + 1

    # 检查角落吸附情况
    # 左上角
    if (leftDistance < snapThreshold and
            topDistance < snapThreshold):
        newX = screenGeometry.left()
        newY = screenGeometry.top()

    # 右上角
    elif (rightDistance < snapThreshold and
          topDistance < snapThreshold):
        newX = screenGeometry.right() - windowGeometry.width() + 1
        newY = screenGeometry.top()

    # 左下角
    elif (leftDistance < snapThreshold and
          bottomDistance < snapThreshold):
        newX = screenGeometry.left()
        newY = screenGeometry.bottom() - windowGeometry.height() + 1

    # 右下角
    elif (rightDistance < snapThreshold and
          bottomDistance < snapThreshold):
        newX = screenGeometry.right() - windowGeometry.width() + 1
        newY = screenGeometry.bottom() - windowGeometry.height() + 1

    widget.move(newX, newY)
