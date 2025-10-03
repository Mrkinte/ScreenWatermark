# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'WatermarkEditWidget.ui'
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
from PySide6.QtWidgets import (QApplication, QHBoxLayout, QLayout, QPushButton,
    QSizePolicy, QSpacerItem, QStackedWidget, QVBoxLayout,
    QWidget)

from qfluentwidgets import (BodyLabel, CheckBox, PrimaryPushButton, ScrollArea,
    Slider, SpinBox)
import assets_rc

class Ui_WatermarkEditWidget(object):
    def setupUi(self, WatermarkEditWidget):
        if not WatermarkEditWidget.objectName():
            WatermarkEditWidget.setObjectName(u"WatermarkEditWidget")
        WatermarkEditWidget.resize(960, 720)
        self.verticalLayout = QVBoxLayout(WatermarkEditWidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(-1, 48, -1, -1)
        self.stackedWidget = QStackedWidget(WatermarkEditWidget)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.stackedWidget.setMinimumSize(QSize(0, 400))
        self.textPage = QWidget()
        self.textPage.setObjectName(u"textPage")
        self.textPage.setStyleSheet(u"QWidget {\n"
"	background-color: rgb(255, 255, 255);\n"
"    border-radius: 5px;\n"
"}")
        self.verticalLayout_2 = QVBoxLayout(self.textPage)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.webView = QWebEngineView(self.textPage)
        self.webView.setObjectName(u"webView")
        self.webView.setUrl(QUrl(u"qrc:/html/index.html"))

        self.verticalLayout_2.addWidget(self.webView)

        self.stackedWidget.addWidget(self.textPage)

        self.verticalLayout.addWidget(self.stackedWidget)

        self.widget_8 = QWidget(WatermarkEditWidget)
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

        self.horizontalSpacer_5 = QSpacerItem(40, 20, QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_8.addItem(self.horizontalSpacer_5)

        self.watermarkStatus = BodyLabel(self.widget_8)
        self.watermarkStatus.setObjectName(u"watermarkStatus")
        self.watermarkStatus.setMinimumSize(QSize(30, 0))

        self.horizontalLayout_8.addWidget(self.watermarkStatus)

        self.horizontalSpacer_7 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_8.addItem(self.horizontalSpacer_7)


        self.verticalLayout.addWidget(self.widget_8)

        self.verticalSpacer_2 = QSpacerItem(20, 10, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)

        self.verticalLayout.addItem(self.verticalSpacer_2)

        self.scrollArea = ScrollArea(WatermarkEditWidget)
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
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 930, 194))
        self.verticalLayout_3 = QVBoxLayout(self.scrollAreaWidgetContents)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.widget_2 = QWidget(self.scrollAreaWidgetContents)
        self.widget_2.setObjectName(u"widget_2")
        self.horizontalLayout = QHBoxLayout(self.widget_2)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setSizeConstraint(QLayout.SizeConstraint.SetMaximumSize)
        self.horizontalLayout.setContentsMargins(27, -1, 27, -1)
        self.label = BodyLabel(self.widget_2)
        self.label.setObjectName(u"label")
        self.label.setMinimumSize(QSize(30, 0))

        self.horizontalLayout.addWidget(self.label)

        self.horizontalSpacer_2 = QSpacerItem(44, 20, QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer_2)

        self.bgWidget = QWidget(self.widget_2)
        self.bgWidget.setObjectName(u"bgWidget")
        self.bgWidget.setMaximumSize(QSize(324, 16777215))
        self.horizontalLayout_5 = QHBoxLayout(self.bgWidget)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.bgColorLabel = BodyLabel(self.bgWidget)
        self.bgColorLabel.setObjectName(u"bgColorLabel")

        self.horizontalLayout_5.addWidget(self.bgColorLabel)

        self.bgColorBtn = QPushButton(self.bgWidget)
        self.bgColorBtn.setObjectName(u"bgColorBtn")
        self.bgColorBtn.setMinimumSize(QSize(32, 32))
        self.bgColorBtn.setMaximumSize(QSize(32, 32))

        self.horizontalLayout_5.addWidget(self.bgColorBtn)

        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_5.addItem(self.horizontalSpacer_3)

        self.bgOpacityLabe = BodyLabel(self.bgWidget)
        self.bgOpacityLabe.setObjectName(u"bgOpacityLabe")

        self.horizontalLayout_5.addWidget(self.bgOpacityLabe)

        self.bgOpacitySlider = Slider(self.bgWidget)
        self.bgOpacitySlider.setObjectName(u"bgOpacitySlider")
        self.bgOpacitySlider.setMinimumSize(QSize(100, 0))
        self.bgOpacitySlider.setMaximumSize(QSize(100, 16777215))
        self.bgOpacitySlider.setMaximum(100)
        self.bgOpacitySlider.setOrientation(Qt.Orientation.Horizontal)

        self.horizontalLayout_5.addWidget(self.bgOpacitySlider)

        self.horizontalSpacer_4 = QSpacerItem(40, 20, QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_5.addItem(self.horizontalSpacer_4)


        self.horizontalLayout.addWidget(self.bgWidget)

        self.label_4 = BodyLabel(self.widget_2)
        self.label_4.setObjectName(u"label_4")

        self.horizontalLayout.addWidget(self.label_4)

        self.bgRadiusSpinBox = SpinBox(self.widget_2)
        self.bgRadiusSpinBox.setObjectName(u"bgRadiusSpinBox")
        self.bgRadiusSpinBox.setMinimumSize(QSize(100, 32))
        self.bgRadiusSpinBox.setMaximum(100)

        self.horizontalLayout.addWidget(self.bgRadiusSpinBox)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)


        self.verticalLayout_3.addWidget(self.widget_2)

        self.widget_7 = QWidget(self.scrollAreaWidgetContents)
        self.widget_7.setObjectName(u"widget_7")
        self.widget_7.setMinimumSize(QSize(0, 50))
        self.horizontalLayout_7 = QHBoxLayout(self.widget_7)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.horizontalLayout_7.setContentsMargins(27, -1, 27, -1)
        self.label_5 = BodyLabel(self.widget_7)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setMinimumSize(QSize(30, 0))

        self.horizontalLayout_7.addWidget(self.label_5)

        self.horizontalSpacer_6 = QSpacerItem(44, 20, QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_7.addItem(self.horizontalSpacer_6)

        self.label_10 = BodyLabel(self.widget_7)
        self.label_10.setObjectName(u"label_10")

        self.horizontalLayout_7.addWidget(self.label_10)

        self.watermarkOpacitySlider = Slider(self.widget_7)
        self.watermarkOpacitySlider.setObjectName(u"watermarkOpacitySlider")
        self.watermarkOpacitySlider.setMinimumSize(QSize(100, 0))
        self.watermarkOpacitySlider.setMaximumSize(QSize(100, 16777215))
        self.watermarkOpacitySlider.setOrientation(Qt.Orientation.Horizontal)

        self.horizontalLayout_7.addWidget(self.watermarkOpacitySlider)

        self.horizontalSpacer_16 = QSpacerItem(40, 20, QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_7.addItem(self.horizontalSpacer_16)

        self.topLayerCheckBox = CheckBox(self.widget_7)
        self.topLayerCheckBox.setObjectName(u"topLayerCheckBox")

        self.horizontalLayout_7.addWidget(self.topLayerCheckBox)

        self.horizontalSpacer_22 = QSpacerItem(40, 20, QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_7.addItem(self.horizontalSpacer_22)

        self.snapToEdgeCheckBox = CheckBox(self.widget_7)
        self.snapToEdgeCheckBox.setObjectName(u"snapToEdgeCheckBox")

        self.horizontalLayout_7.addWidget(self.snapToEdgeCheckBox)

        self.horizontalSpacer_17 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_7.addItem(self.horizontalSpacer_17)


        self.verticalLayout_3.addWidget(self.widget_7)

        self.verticalSpacer_4 = QSpacerItem(20, 20, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)

        self.verticalLayout_3.addItem(self.verticalSpacer_4)

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


        self.verticalLayout_3.addWidget(self.widget_4)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_3.addItem(self.verticalSpacer)

        self.scrollArea.setWidget(self.scrollAreaWidgetContents)

        self.verticalLayout.addWidget(self.scrollArea)


        self.retranslateUi(WatermarkEditWidget)

        self.stackedWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(WatermarkEditWidget)
    # setupUi

    def retranslateUi(self, WatermarkEditWidget):
        self.textBtn.setText(QCoreApplication.translate("WatermarkEditWidget", u"\u6587\u5b57\u6c34\u5370", None))
        self.imageBtn.setText(QCoreApplication.translate("WatermarkEditWidget", u"\u56fe\u7247\u6c34\u5370", None))
        self.watermarkStatus.setText(QCoreApplication.translate("WatermarkEditWidget", u"\u6c34\u5370\u72b6\u6001\uff1a\u672a\u542f\u7528", None))
        self.label.setText(QCoreApplication.translate("WatermarkEditWidget", u"\u80cc\u666f", None))
        self.bgColorLabel.setText(QCoreApplication.translate("WatermarkEditWidget", u"\u989c\u8272", None))
        self.bgColorBtn.setText("")
        self.bgOpacityLabe.setText(QCoreApplication.translate("WatermarkEditWidget", u"\u900f\u660e\u5ea6", None))
        self.label_4.setText(QCoreApplication.translate("WatermarkEditWidget", u"\u5706\u89d2", None))
        self.bgRadiusSpinBox.setSuffix(QCoreApplication.translate("WatermarkEditWidget", u"  px", None))
        self.label_5.setText(QCoreApplication.translate("WatermarkEditWidget", u"\u6c34\u5370", None))
        self.label_10.setText(QCoreApplication.translate("WatermarkEditWidget", u"\u900f\u660e\u5ea6", None))
        self.topLayerCheckBox.setText(QCoreApplication.translate("WatermarkEditWidget", u"\u7f6e\u9876", None))
        self.snapToEdgeCheckBox.setText(QCoreApplication.translate("WatermarkEditWidget", u"\u8fb9\u7f18\u5438\u9644", None))
        self.previewBtn.setText(QCoreApplication.translate("WatermarkEditWidget", u"\u9884\u89c8\u6c34\u5370", None))
        self.applyBtn.setText(QCoreApplication.translate("WatermarkEditWidget", u"\u5e94\u7528\u8bbe\u7f6e", None))
        self.closeBtn.setText(QCoreApplication.translate("WatermarkEditWidget", u"\u5173\u95ed\u6c34\u5370", None))
        pass
    # retranslateUi

