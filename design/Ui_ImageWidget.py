# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ImageWidget.ui'
##
## Created by: Qt User Interface Compiler version 6.9.3
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QHBoxLayout, QSizePolicy, QSpacerItem,
    QVBoxLayout, QWidget)

from qfluentwidgets import (BodyLabel, PrimaryPushButton, Slider)
import assets_rc

class Ui_ImageWidget(object):
    def setupUi(self, ImageWidget):
        if not ImageWidget.objectName():
            ImageWidget.setObjectName(u"ImageWidget")
        ImageWidget.resize(700, 400)
        self.horizontalLayout = QHBoxLayout(ImageWidget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer_2)

        self.imageLabel = BodyLabel(ImageWidget)
        self.imageLabel.setObjectName(u"imageLabel")
        self.imageLabel.setMinimumSize(QSize(300, 300))
        self.imageLabel.setMaximumSize(QSize(300, 300))
        self.imageLabel.setStyleSheet(u"QLabel {\n"
"	border: 2px dashed #ced4da;\n"
"	border-radius: 5px;\n"
"}")
        self.imageLabel.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.horizontalLayout.addWidget(self.imageLabel)

        self.widget_2 = QWidget(ImageWidget)
        self.widget_2.setObjectName(u"widget_2")
        self.widget_2.setMinimumSize(QSize(20, 300))
        self.widget_2.setMaximumSize(QSize(60, 300))
        self.verticalLayout_5 = QVBoxLayout(self.widget_2)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_5.setContentsMargins(-1, 0, -1, 0)
        self.zoomSlider = Slider(self.widget_2)
        self.zoomSlider.setObjectName(u"zoomSlider")
        self.zoomSlider.setEnabled(False)
        self.zoomSlider.setMinimum(10)
        self.zoomSlider.setMaximum(100)
        self.zoomSlider.setValue(100)
        self.zoomSlider.setOrientation(Qt.Orientation.Vertical)

        self.verticalLayout_5.addWidget(self.zoomSlider)

        self.bodyLabel = BodyLabel(self.widget_2)
        self.bodyLabel.setObjectName(u"bodyLabel")
        self.bodyLabel.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_5.addWidget(self.bodyLabel)


        self.horizontalLayout.addWidget(self.widget_2)

        self.widget = QWidget(ImageWidget)
        self.widget.setObjectName(u"widget")
        self.verticalLayout_4 = QVBoxLayout(self.widget)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.loadImageBtn = PrimaryPushButton(self.widget)
        self.loadImageBtn.setObjectName(u"loadImageBtn")
        self.loadImageBtn.setMinimumSize(QSize(100, 32))
        self.loadImageBtn.setMaximumSize(QSize(100, 32))

        self.verticalLayout_4.addWidget(self.loadImageBtn)

        self.rotateRightBtn = PrimaryPushButton(self.widget)
        self.rotateRightBtn.setObjectName(u"rotateRightBtn")
        self.rotateRightBtn.setEnabled(False)
        self.rotateRightBtn.setMinimumSize(QSize(100, 32))
        self.rotateRightBtn.setMaximumSize(QSize(100, 32))

        self.verticalLayout_4.addWidget(self.rotateRightBtn)

        self.rotateLeftBtn = PrimaryPushButton(self.widget)
        self.rotateLeftBtn.setObjectName(u"rotateLeftBtn")
        self.rotateLeftBtn.setEnabled(False)
        self.rotateLeftBtn.setMinimumSize(QSize(100, 32))
        self.rotateLeftBtn.setMaximumSize(QSize(100, 32))

        self.verticalLayout_4.addWidget(self.rotateLeftBtn)

        self.deleteImageBtn = PrimaryPushButton(self.widget)
        self.deleteImageBtn.setObjectName(u"deleteImageBtn")
        self.deleteImageBtn.setEnabled(False)
        self.deleteImageBtn.setMinimumSize(QSize(100, 32))
        self.deleteImageBtn.setMaximumSize(QSize(100, 32))

        self.verticalLayout_4.addWidget(self.deleteImageBtn)


        self.horizontalLayout.addWidget(self.widget)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)


        self.retranslateUi(ImageWidget)

        QMetaObject.connectSlotsByName(ImageWidget)
    # setupUi

    def retranslateUi(self, ImageWidget):
        self.imageLabel.setText(QCoreApplication.translate("ImageWidget", u"\u8bf7\u52a0\u8f7d\u56fe\u7247", None))
        self.bodyLabel.setText(QCoreApplication.translate("ImageWidget", u"\u7f29\u653e", None))
        self.loadImageBtn.setText(QCoreApplication.translate("ImageWidget", u"\u52a0\u8f7d\u56fe\u7247", None))
        self.rotateRightBtn.setText(QCoreApplication.translate("ImageWidget", u"\u987a\u65f6\u948890\u00b0", None))
        self.rotateLeftBtn.setText(QCoreApplication.translate("ImageWidget", u"\u9006\u65f6\u948890\u00b0", None))
        self.deleteImageBtn.setText(QCoreApplication.translate("ImageWidget", u"\u5220\u9664\u56fe\u7247", None))
        pass
    # retranslateUi

