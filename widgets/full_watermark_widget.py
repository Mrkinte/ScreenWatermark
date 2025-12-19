from PySide6.QtCore import Qt, QRectF, QPointF
from PySide6.QtGui import QPainter, QTextDocument, QPixmap, QColor, QTransform, QPolygonF, QTextOption
from PySide6.QtWidgets import QWidget


# ---全屏文字水印---
class FullTextWatermarkWidget(QWidget):
    def __init__(self, screenGeometry):
        super().__init__()
        self.previewing = False
        self.activated = False
        self.color = QColor()
        self.param = {}

        self.setWindowFlag(Qt.FramelessWindowHint)
        self.setWindowFlag(Qt.WindowStaysOnTopHint)
        self.setAttribute(Qt.WA_TranslucentBackground)
        self.setAttribute(Qt.WA_TransparentForMouseEvents)
        self.setAttribute(Qt.WA_ShowWithoutActivating)
        self.setWindowFlag(Qt.Tool, True)
        self.setGeometry(screenGeometry)

        self.doc = QTextDocument()
        self.doc.setDocumentMargin(0)
        # 禁止自动换行
        self.doc.setDefaultStyleSheet("""
            body, p, div, span {
                white-space: nowrap;
                }
            """)

    def showFullScreen(self):
        super().show()
        self.update()

    def setHtml(self, html: str):
        self.doc.setHtml(html)
        self.doc.setDefaultTextOption(QTextOption(Qt.AlignLeft | Qt.AlignVCenter))
        self.doc.adjustSize()
        self.doc.setTextWidth(self.doc.idealWidth())
        self.doc.adjustSize()

    def setAllParam(self, param: dict):
        self.param = param
        # watermarkOpacity 0 - 255
        self.color.setAlpha(param["watermarkOpacity"])
        self.setWindowFlag(Qt.WindowStaysOnTopHint, param["topLayer"])

    def setActivated(self):
        self.previewing = False
        self.activated = True

    def setPreviewing(self):
        self.previewing = True
        self.activated = False

    ###################
    # Event rewriting #
    ###################
    def paintEvent(self, event):
        painter = QPainter(self)
        painter.setRenderHint(QPainter.Antialiasing)
        painter.setRenderHint(QPainter.TextAntialiasing)

        rect = self.rect()
        w, h = rect.width(), rect.height()
        itemW = self.doc.idealWidth()
        itemH = self.doc.size().height()

        # 计算旋转后的实际占用尺寸
        angle = self.param["angle"]
        if angle % 360 != 0:  # 需要旋转时才计算
            # 创建变换矩阵计算旋转后的边界
            transform = QTransform()
            transform.rotate(angle)
            polygon = QPolygonF([
                QPointF(0, 0),
                QPointF(itemW, 0),
                QPointF(itemW, itemH),
                QPointF(0, itemH)
            ])
            rotated_poly = transform.map(polygon)
            rotated_rect = rotated_poly.boundingRect()
            rotatedW = rotated_rect.width()
            rotatedH = rotated_rect.height()
        else:
            rotatedW = itemW
            rotatedH = itemH

        # 使用旋转后的尺寸计算间距
        stepX = rotatedW + max(1, int(self.param["hSpacing"]))
        stepY = rotatedH + max(1, int(self.param["vSpacing"]))

        # 计算需要的行列数（考虑旋转后尺寸）
        cols = int(w / stepX) + 4
        rows = int(h / stepY) + 4
        rowShift = stepX // 2

        # 计算初始偏移使水印居中
        offsetX = (w - (cols - 1) * stepX) / 2
        offsetY = (h - (rows - 1) * stepY) / 2

        painter.setOpacity(self.color.alphaF())
        for row in range(rows):
            y = row * stepY + offsetY
            shift = (row % 2) * rowShift
            for col in range(cols):
                x = col * stepX + shift + offsetX
                # 直接使用水印单元中心作为旋转中心
                cx = x + itemW / 2
                cy = y + itemH / 2
                painter.save()
                painter.translate(cx, cy)
                painter.rotate(angle)
                # 绘制时以中心点为基准
                targetRect = QRectF(0, 0, itemW, itemH)
                self.doc.drawContents(painter, targetRect)
                painter.restore()

    def closeEvent(self, event):
        if self.activated:
            event.ignore()
        else:
            super().closeEvent(event)


# ---全屏照片水印---
class FullImageWatermarkWidget(QWidget):
    def __init__(self, screenGeometry):
        super().__init__()
        self.previewing = False
        self.activated = False
        self.color = QColor()
        self.param = {}

        self.setWindowFlag(Qt.FramelessWindowHint)
        self.setWindowFlag(Qt.WindowStaysOnTopHint)
        self.setAttribute(Qt.WA_TranslucentBackground)
        self.setAttribute(Qt.WA_TransparentForMouseEvents)
        self.setAttribute(Qt.WA_ShowWithoutActivating)
        self.setWindowFlag(Qt.Tool, True)
        self.setGeometry(screenGeometry)

        self.pixmap = QPixmap()

    def showFullScreen(self):
        super().show()
        self.update()

    def setImage(self, image):
        self.pixmap = image

    def setAllParam(self, param: dict):
        self.param = param
        # watermarkOpacity 0 - 255
        self.color.setAlpha(param["watermarkOpacity"])
        self.setWindowFlag(Qt.WindowStaysOnTopHint, param["topLayer"])

    def setActivated(self):
        self.previewing = False
        self.activated = True

    def setPreviewing(self):
        self.previewing = True
        self.activated = False

    ###################
    # Event rewriting #
    ###################
    def paintEvent(self, event):
        painter = QPainter(self)
        painter.setRenderHint(QPainter.Antialiasing)
        painter.setRenderHint(QPainter.SmoothPixmapTransform)

        rect = self.rect()
        w, h = rect.width(), rect.height()
        imgW = self.pixmap.width()
        imgH = self.pixmap.height()
        if imgW <= 0 or imgH <= 0:
            return

        # 计算旋转后的实际占用尺寸
        angle = self.param["angle"]
        if angle % 360 != 0:  # 需要旋转时才计算
            # 创建变换矩阵计算旋转后的边界
            transform = QTransform()
            transform.rotate(angle)
            polygon = QPolygonF([
                QPointF(0, 0),
                QPointF(imgW, 0),
                QPointF(imgW, imgH),
                QPointF(0, imgH)
            ])
            rotated_poly = transform.map(polygon)
            rotated_rect = rotated_poly.boundingRect()
            rotatedW = rotated_rect.width()
            rotatedH = rotated_rect.height()
        else:
            rotatedW = imgW
            rotatedH = imgH

        # 使用旋转后的尺寸计算间距
        stepX = rotatedW + max(1, int(self.param["hSpacing"]))
        stepY = rotatedH + max(1, int(self.param["vSpacing"]))

        # 计算需要的行列数（考虑旋转后尺寸）
        cols = int(w / stepX) + 4
        rows = int(h / stepY) + 4
        rowShift = stepX // 2

        # 计算初始偏移使水印居中
        offsetX = (w - (cols - 1) * stepX) / 2
        offsetY = (h - (rows - 1) * stepY) / 2

        painter.setOpacity(self.color.alphaF())
        for row in range(rows):
            y = row * stepY + offsetY
            shift = (row % 2) * rowShift
            for col in range(cols):
                x = col * stepX + shift + offsetX
                # 直接使用图片中心作为旋转中心
                cx = x + imgW / 2
                cy = y + imgH / 2
                painter.save()
                painter.translate(cx, cy)
                painter.rotate(angle)
                # 绘制时以中心点为基准
                painter.drawPixmap(0, 0, self.pixmap)
                painter.restore()

    def closeEvent(self, event):
        if self.activated:
            event.ignore()
        else:
            super().closeEvent(event)
