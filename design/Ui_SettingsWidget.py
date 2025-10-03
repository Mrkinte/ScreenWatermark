# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'SettingsWidget.ui'
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
from PySide6.QtWidgets import (QApplication, QSizePolicy, QVBoxLayout, QWidget)

from qfluentwidgets import ScrollArea

class Ui_SettingsWidget(object):
    def setupUi(self, SettingsWidget):
        if not SettingsWidget.objectName():
            SettingsWidget.setObjectName(u"SettingsWidget")
        SettingsWidget.resize(1143, 902)
        self.layout = QVBoxLayout(SettingsWidget)
        self.layout.setSpacing(0)
        self.layout.setObjectName(u"layout")
        self.layout.setContentsMargins(0, 48, 0, 0)
        self.scrollArea = ScrollArea(SettingsWidget)
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
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 1143, 854))
        self.settingsLayout = QVBoxLayout(self.scrollAreaWidgetContents)
        self.settingsLayout.setObjectName(u"settingsLayout")
        self.settingsLayout.setContentsMargins(-1, 0, -1, -1)
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)

        self.layout.addWidget(self.scrollArea)


        self.retranslateUi(SettingsWidget)

        QMetaObject.connectSlotsByName(SettingsWidget)
    # setupUi

    def retranslateUi(self, SettingsWidget):
        pass
    # retranslateUi

