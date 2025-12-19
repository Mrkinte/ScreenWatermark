# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'FullWatermarkEditWidget.ui'
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
from PySide6.QtWebEngineWidgets import QWebEngineView
from PySide6.QtWidgets import (QApplication, QHBoxLayout, QSizePolicy, QSpacerItem,
    QStackedWidget, QVBoxLayout, QWidget)

from qfluentwidgets import (BodyLabel, CheckBox, PrimaryPushButton, ScrollArea,
    Slider, SpinBox)
import assets_rc

class Ui_FullWatermarkEditWidget(object):
    def setupUi(self, FullWatermarkEditWidget):
        if not FullWatermarkEditWidget.objectName():
            FullWatermarkEditWidget.setObjectName(u"FullWatermarkEditWidget")
        FullWatermarkEditWidget.resize(980, 721)
        FullWatermarkEditWidget.setMinimumSize(QSize(980, 720))
        self.verticalLayout = QVBoxLayout(FullWatermarkEditWidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(-1, 48, -1, -1)
        self.stackedWidget = QStackedWidget(FullWatermarkEditWidget)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.stackedWidget.setMinimumSize(QSize(0, 400))
        self.textPage = QWidget()
        self.textPage.setObjectName(u"textPage")
        self.textPage.setStyleSheet(u"QWidget {\n"
"	background-color: rgb(255, 255, 255);\n"
"    border-radius: 5px;\n"
"}")
        self.verticalLayout_3 = QVBoxLayout(self.textPage)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.webView = QWebEngineView(self.textPage)
        self.webView.setObjectName(u"webView")
        self.webView.setUrl(QUrl(u"qrc:/html/index.html"))

        self.verticalLayout_3.addWidget(self.webView)

        self.stackedWidget.addWidget(self.textPage)

        self.verticalLayout.addWidget(self.stackedWidget)

        self.scrollArea = ScrollArea(FullWatermarkEditWidget)
        self.scrollArea.setObjectName(u"scrollArea")
        self.scrollArea.setStyleSheet(u"QScrollArea {\n"
"	background-color: transparent;\n"
"	border: none;\n"
"}\n"
"\n"
"#scrollAreaWidgetContents {\n"
"	 background-color: transparent;\n"
"}")
        self.scrollArea.setWidgetResizable(True)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 950, 266))
        self.verticalLayout_2 = QVBoxLayout(self.scrollAreaWidgetContents)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.widget_8 = QWidget(self.scrollAreaWidgetContents)
        self.widget_8.setObjectName(u"widget_8")
        self.horizontalLayout_8 = QHBoxLayout(self.widget_8)
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.textBtn = PrimaryPushButton(self.widget_8)
        self.textBtn.setObjectName(u"textBtn")
        self.textBtn.setMinimumSize(QSize(100, 32))
        self.textBtn.setMaximumSize(QSize(100, 32))

        self.horizontalLayout_8.addWidget(self.textBtn)

        self.imageBtn = PrimaryPushButton(self.widget_8)
        self.imageBtn.setObjectName(u"imageBtn")
        self.imageBtn.setMinimumSize(QSize(100, 32))
        self.imageBtn.setMaximumSize(QSize(100, 32))

        self.horizontalLayout_8.addWidget(self.imageBtn)

        self.horizontalSpacer_20 = QSpacerItem(40, 20, QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_8.addItem(self.horizontalSpacer_20)

        self.watermarkStatus = BodyLabel(self.widget_8)
        self.watermarkStatus.setObjectName(u"watermarkStatus")
        self.watermarkStatus.setMinimumSize(QSize(30, 0))

        self.horizontalLayout_8.addWidget(self.watermarkStatus)

        self.horizontalSpacer_19 = QSpacerItem(40, 20, QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_8.addItem(self.horizontalSpacer_19)

        self.screenNums = BodyLabel(self.widget_8)
        self.screenNums.setObjectName(u"screenNums")

        self.horizontalLayout_8.addWidget(self.screenNums)

        self.horizontalSpacer_7 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_8.addItem(self.horizontalSpacer_7)


        self.verticalLayout_2.addWidget(self.widget_8)

        self.verticalSpacer_2 = QSpacerItem(20, 10, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)

        self.verticalLayout_2.addItem(self.verticalSpacer_2)

        self.widget_7 = QWidget(self.scrollAreaWidgetContents)
        self.widget_7.setObjectName(u"widget_7")
        self.widget_7.setMinimumSize(QSize(0, 50))
        self.horizontalLayout_6 = QHBoxLayout(self.widget_7)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.horizontalLayout_6.setContentsMargins(27, -1, 27, -1)
        self.label_5 = BodyLabel(self.widget_7)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setMinimumSize(QSize(30, 0))

        self.horizontalLayout_6.addWidget(self.label_5)

        self.horizontalSpacer_6 = QSpacerItem(44, 20, QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_6.addItem(self.horizontalSpacer_6)

        self.label_10 = BodyLabel(self.widget_7)
        self.label_10.setObjectName(u"label_10")

        self.horizontalLayout_6.addWidget(self.label_10)

        self.opacitySlider = Slider(self.widget_7)
        self.opacitySlider.setObjectName(u"opacitySlider")
        self.opacitySlider.setMinimumSize(QSize(100, 0))
        self.opacitySlider.setMaximumSize(QSize(100, 16777215))
        self.opacitySlider.setMaximum(255)
        self.opacitySlider.setOrientation(Qt.Orientation.Horizontal)

        self.horizontalLayout_6.addWidget(self.opacitySlider)

        self.horizontalSpacer_16 = QSpacerItem(40, 20, QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_6.addItem(self.horizontalSpacer_16)

        self.topLayerCheckBox = CheckBox(self.widget_7)
        self.topLayerCheckBox.setObjectName(u"topLayerCheckBox")

        self.horizontalLayout_6.addWidget(self.topLayerCheckBox)

        self.horizontalSpacer_17 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_6.addItem(self.horizontalSpacer_17)


        self.verticalLayout_2.addWidget(self.widget_7)

        self.widget_6 = QWidget(self.scrollAreaWidgetContents)
        self.widget_6.setObjectName(u"widget_6")
        self.widget_6.setMinimumSize(QSize(0, 50))
        self.horizontalLayout_5 = QHBoxLayout(self.widget_6)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout_5.setContentsMargins(27, -1, 27, -1)
        self.horizontalSpacer_14 = QSpacerItem(80, 20, QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_5.addItem(self.horizontalSpacer_14)

        self.label_7 = BodyLabel(self.widget_6)
        self.label_7.setObjectName(u"label_7")

        self.horizontalLayout_5.addWidget(self.label_7)

        self.hSpacingSpinBox = SpinBox(self.widget_6)
        self.hSpacingSpinBox.setObjectName(u"hSpacingSpinBox")
        self.hSpacingSpinBox.setMinimumSize(QSize(100, 32))
        self.hSpacingSpinBox.setMaximum(255)

        self.horizontalLayout_5.addWidget(self.hSpacingSpinBox)

        self.horizontalSpacer_13 = QSpacerItem(40, 20, QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_5.addItem(self.horizontalSpacer_13)

        self.label_8 = BodyLabel(self.widget_6)
        self.label_8.setObjectName(u"label_8")

        self.horizontalLayout_5.addWidget(self.label_8)

        self.vSpacingSpinBox = SpinBox(self.widget_6)
        self.vSpacingSpinBox.setObjectName(u"vSpacingSpinBox")
        self.vSpacingSpinBox.setMinimumSize(QSize(100, 32))
        self.vSpacingSpinBox.setMaximum(255)

        self.horizontalLayout_5.addWidget(self.vSpacingSpinBox)

        self.horizontalSpacer_18 = QSpacerItem(40, 20, QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_5.addItem(self.horizontalSpacer_18)

        self.label_9 = BodyLabel(self.widget_6)
        self.label_9.setObjectName(u"label_9")

        self.horizontalLayout_5.addWidget(self.label_9)

        self.angleSpinBox = SpinBox(self.widget_6)
        self.angleSpinBox.setObjectName(u"angleSpinBox")
        self.angleSpinBox.setMinimumSize(QSize(100, 32))
        self.angleSpinBox.setMaximum(360)

        self.horizontalLayout_5.addWidget(self.angleSpinBox)

        self.horizontalSpacer_15 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_5.addItem(self.horizontalSpacer_15)


        self.verticalLayout_2.addWidget(self.widget_6)

        self.verticalSpacer_3 = QSpacerItem(20, 20, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)

        self.verticalLayout_2.addItem(self.verticalSpacer_3)

        self.widget_4 = QWidget(self.scrollAreaWidgetContents)
        self.widget_4.setObjectName(u"widget_4")
        self.horizontalLayout_3 = QHBoxLayout(self.widget_4)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.previewBtn = PrimaryPushButton(self.widget_4)
        self.previewBtn.setObjectName(u"previewBtn")
        self.previewBtn.setMinimumSize(QSize(100, 32))
        self.previewBtn.setMaximumSize(QSize(100, 32))

        self.horizontalLayout_3.addWidget(self.previewBtn)

        self.applyBtn = PrimaryPushButton(self.widget_4)
        self.applyBtn.setObjectName(u"applyBtn")
        self.applyBtn.setMinimumSize(QSize(100, 32))
        self.applyBtn.setMaximumSize(QSize(100, 32))

        self.horizontalLayout_3.addWidget(self.applyBtn)

        self.closeBtn = PrimaryPushButton(self.widget_4)
        self.closeBtn.setObjectName(u"closeBtn")
        self.closeBtn.setMinimumSize(QSize(100, 32))
        self.closeBtn.setMaximumSize(QSize(100, 32))

        self.horizontalLayout_3.addWidget(self.closeBtn)


        self.verticalLayout_2.addWidget(self.widget_4)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_2.addItem(self.verticalSpacer)

        self.scrollArea.setWidget(self.scrollAreaWidgetContents)

        self.verticalLayout.addWidget(self.scrollArea)


        self.retranslateUi(FullWatermarkEditWidget)

        self.stackedWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(FullWatermarkEditWidget)
    # setupUi

    def retranslateUi(self, FullWatermarkEditWidget):
        self.textBtn.setText(QCoreApplication.translate("FullWatermarkEditWidget", u"\u6587\u5b57\u6c34\u5370", None))
        self.imageBtn.setText(QCoreApplication.translate("FullWatermarkEditWidget", u"\u56fe\u7247\u6c34\u5370", None))
        self.watermarkStatus.setText(QCoreApplication.translate("FullWatermarkEditWidget", u"\u6c34\u5370\u72b6\u6001\uff1a\u672a\u542f\u7528", None))
        self.screenNums.setText(QCoreApplication.translate("FullWatermarkEditWidget", u"\u5c4f\u5e55\u6570\u91cf\uff1a", None))
        self.label_5.setText(QCoreApplication.translate("FullWatermarkEditWidget", u"\u6c34\u5370", None))
        self.label_10.setText(QCoreApplication.translate("FullWatermarkEditWidget", u"\u900f\u660e\u5ea6", None))
        self.topLayerCheckBox.setText(QCoreApplication.translate("FullWatermarkEditWidget", u"\u7f6e\u9876", None))
        self.label_7.setText(QCoreApplication.translate("FullWatermarkEditWidget", u"\u6c34\u5e73\u95f4\u8ddd", None))
        self.hSpacingSpinBox.setSuffix(QCoreApplication.translate("FullWatermarkEditWidget", u"  px", None))
        self.label_8.setText(QCoreApplication.translate("FullWatermarkEditWidget", u"\u5782\u76f4\u95f4\u8ddd", None))
        self.vSpacingSpinBox.setSuffix(QCoreApplication.translate("FullWatermarkEditWidget", u"  px", None))
        self.label_9.setText(QCoreApplication.translate("FullWatermarkEditWidget", u"\u89d2\u5ea6", None))
        self.angleSpinBox.setSuffix(QCoreApplication.translate("FullWatermarkEditWidget", u"  \u00b0", None))
        self.previewBtn.setText(QCoreApplication.translate("FullWatermarkEditWidget", u"\u9884\u89c8\u6c34\u5370", None))
        self.applyBtn.setText(QCoreApplication.translate("FullWatermarkEditWidget", u"\u5e94\u7528\u8bbe\u7f6e", None))
        self.closeBtn.setText(QCoreApplication.translate("FullWatermarkEditWidget", u"\u5173\u95ed\u6c34\u5370", None))
        pass
    # retranslateUi

