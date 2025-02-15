# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'musicItemZxMIbf.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import *
from PySide6.QtGui import *
from PySide6.QtWidgets import *


class Ui_musicItem(object):
    def setupUi(self, musicItem):
        if not musicItem.objectName():
            musicItem.setObjectName(u"musicItem")
        musicItem.resize(170, 210)
        musicItem.setMinimumSize(QSize(168, 210))
        musicItem.setSizeIncrement(QSize(168, 210))
        musicItem.setStyleSheet(u"background-color:rgba(0,0,0,100);\n"
" border-radius:20px;")
        self.verticalLayout_2 = QVBoxLayout(musicItem)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.coverart_fram = QFrame(musicItem)
        self.coverart_fram.setObjectName(u"coverart_fram")
        self.coverart_fram.setMinimumSize(QSize(150, 150))
        self.coverart_fram.setMaximumSize(QSize(150, 150))
        self.coverart_fram.setStyleSheet(u"background-color:rgba(0,0,0,0); border-radius:20px;")
        self.coverart_fram.setFrameShape(QFrame.StyledPanel)
        self.coverart_fram.setFrameShadow(QFrame.Raised)
        self.verticalLayout = QVBoxLayout(self.coverart_fram)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.coverart = QLabel(self.coverart_fram)
        self.coverart.setObjectName(u"coverart")
        self.coverart.setMinimumSize(QSize(150, 150))
        self.coverart.setMaximumSize(QSize(150, 150))
        self.coverart.setStyleSheet(u"background-color:none;")

        self.verticalLayout.addWidget(self.coverart)


        self.verticalLayout_2.addWidget(self.coverart_fram)

        self.MediaInfo_frame = QFrame(musicItem)
        self.MediaInfo_frame.setObjectName(u"MediaInfo_frame")
        self.MediaInfo_frame.setStyleSheet(u"background-color:none;")
        self.MediaInfo_frame.setFrameShape(QFrame.StyledPanel)
        self.MediaInfo_frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.MediaInfo_frame)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.title = QLabel(self.MediaInfo_frame)
        self.title.setObjectName(u"title")
        self.title.setMaximumSize(QSize(152, 16777215))
        font = QFont()
        font.setFamily(u"Inter 18pt")
        font.setPointSize(10)
        self.title.setFont(font)
        self.title.setStyleSheet(u"color:white;")

        self.verticalLayout_3.addWidget(self.title)

        self.artist = QLabel(self.MediaInfo_frame)
        self.artist.setObjectName(u"artist")
        self.artist.setMaximumSize(QSize(152, 16777215))
        font1 = QFont()
        font1.setFamily(u"Inter 18pt")
        font1.setPointSize(9)
        self.artist.setFont(font1)
        self.artist.setStyleSheet(u"color:rgba(255,255,255,200);")

        self.verticalLayout_3.addWidget(self.artist)


        self.verticalLayout_2.addWidget(self.MediaInfo_frame)

#if QT_CONFIG(shortcut)
#endif // QT_CONFIG(shortcut)

        self.retranslateUi(musicItem)

        QMetaObject.connectSlotsByName(musicItem)
    # setupUi

    def retranslateUi(self, musicItem):
        musicItem.setWindowTitle(QCoreApplication.translate("musicItem", u"Frame", None))
        self.coverart.setText("")
        self.title.setText(QCoreApplication.translate("musicItem", u"The Hills ", None))
        self.artist.setText(QCoreApplication.translate("musicItem", u"The Weeknd", None))
    # retranslateUi

