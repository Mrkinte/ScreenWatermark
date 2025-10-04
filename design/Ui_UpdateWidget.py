# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'UpdateWidget.ui'
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
from PySide6.QtWidgets import (QApplication, QDialog, QHBoxLayout, QSizePolicy,
    QSpacerItem, QVBoxLayout, QWidget)

from qfluentwidgets import (BodyLabel, HyperlinkButton)
import assets_rc

class Ui_UpdateWidget(object):
    def setupUi(self, UpdateWidget):
        if not UpdateWidget.objectName():
            UpdateWidget.setObjectName(u"UpdateWidget")
        UpdateWidget.resize(600, 400)
        UpdateWidget.setMinimumSize(QSize(600, 400))
        UpdateWidget.setMaximumSize(QSize(600, 400))
        icon = QIcon()
        icon.addFile(u":/icons/favicon.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        UpdateWidget.setWindowIcon(icon)
        UpdateWidget.setStyleSheet(u"")
        self.verticalLayout = QVBoxLayout(UpdateWidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.versionLabel = BodyLabel(UpdateWidget)
        self.versionLabel.setObjectName(u"versionLabel")
        font = QFont()
        font.setPointSize(16)
        font.setBold(True)
        self.versionLabel.setFont(font)
        self.versionLabel.setMargin(10)

        self.verticalLayout.addWidget(self.versionLabel)

        self.contentLabel = BodyLabel(UpdateWidget)
        self.contentLabel.setObjectName(u"contentLabel")
        font1 = QFont()
        font1.setPointSize(12)
        font1.setKerning(True)
        self.contentLabel.setFont(font1)
        self.contentLabel.setTextFormat(Qt.TextFormat.MarkdownText)
        self.contentLabel.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignTop)
        self.contentLabel.setMargin(10)

        self.verticalLayout.addWidget(self.contentLabel)

        self.widget = QWidget(UpdateWidget)
        self.widget.setObjectName(u"widget")
        self.horizontalLayout = QHBoxLayout(self.widget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)

        self.getUpdateBtn = HyperlinkButton(self.widget)
        self.getUpdateBtn.setObjectName(u"getUpdateBtn")
        self.getUpdateBtn.setMinimumSize(QSize(100, 32))
        self.getUpdateBtn.setMaximumSize(QSize(100, 32))

        self.horizontalLayout.addWidget(self.getUpdateBtn)


        self.verticalLayout.addWidget(self.widget)

        self.verticalLayout.setStretch(1, 1)

        self.retranslateUi(UpdateWidget)

        QMetaObject.connectSlotsByName(UpdateWidget)
    # setupUi

    def retranslateUi(self, UpdateWidget):
        UpdateWidget.setWindowTitle(QCoreApplication.translate("UpdateWidget", u"\u68c0\u67e5\u66f4\u65b0", None))
        UpdateWidget.setProperty(u"lightCustomQss", QCoreApplication.translate("UpdateWidget", u"QDialog {\n"
"	background-color: rgb(253, 253, 253);\n"
"}", None))
        UpdateWidget.setProperty(u"darkCustomQss", QCoreApplication.translate("UpdateWidget", u"QDialog {\n"
"	background-color: rgb(51, 50, 50);\n"
"}", None))
        self.versionLabel.setText(QCoreApplication.translate("UpdateWidget", u"\u53d1\u73b0\u65b0\u7248\u672c\uff1a1.1.0 \uff08\u5f53\u524d\u7248\u672c\uff1a1.0.0\uff09", None))
        self.contentLabel.setText(QCoreApplication.translate("UpdateWidget", u"\u66f4\u65b0\u5185\u5bb9\uff1a", None))
        self.getUpdateBtn.setText(QCoreApplication.translate("UpdateWidget", u"\u83b7\u53d6\u66f4\u65b0", None))
    # retranslateUi

