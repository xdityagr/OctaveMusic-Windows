# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'octaveMusicSearchItem_changeoneXsFzov.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import *
from PySide6.QtGui import *
from PySide6.QtWidgets import *


class Ui_searchItem(object):
    def setupUi(self, searchItem):
        if not searchItem.objectName():
            searchItem.setObjectName(u"searchItem")

        searchItem.resize(530, 70)
        searchItem.setMinimumSize(QSize(400, 70))
        searchItem.setMaximumSize(QSize(530, 70))
        self.isSelected = False
        self.gridLayout = QGridLayout(searchItem)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.body = QFrame(searchItem)
        self.body.setObjectName(u"body")
        self.body.setMaximumSize(QSize(530, 70))
        self.body.setStyleSheet(u"QFrame { \n"
"background-color:rgba(0,0,0,100); border-radius:15px;\n"
"}\n"
"QFrame::hover {\n"
"background-color:rgba(255,255,255,20);\n"
" border-radius:15px;\n"
"}")
        self.body.setFrameShape(QFrame.StyledPanel)
        self.body.setFrameShadow(QFrame.Raised)
        self.gridLayout_3 = QGridLayout(self.body)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.gridLayout_3.setHorizontalSpacing(10)
        self.gridLayout_3.setContentsMargins(4, 4, 4, 4)
        self.coverArt = QLabel(self.body)
        self.coverArt.setObjectName(u"coverArt")
        self.coverArt.setMinimumSize(QSize(60, 60))
        self.coverArt.setMaximumSize(QSize(60, 60))
        self.coverArt.setStyleSheet(u"background:none;")

        self.gridLayout_3.addWidget(self.coverArt, 0, 0, 1, 1)

        self.MediaInfo_frame = QFrame(self.body)
        self.MediaInfo_frame.setObjectName(u"MediaInfo_frame")
        self.MediaInfo_frame.setStyleSheet(u"background-color:none;")
        self.MediaInfo_frame.setFrameShape(QFrame.StyledPanel)
        self.MediaInfo_frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.MediaInfo_frame)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_3.addItem(self.verticalSpacer_2)

        self.title = QLabel(self.MediaInfo_frame)
        self.title.setObjectName(u"title")
        self.title.setMaximumSize(QSize(300, 16777215))
        font = QFont()
        font.setFamily(u"Inter 18pt")
        font.setPointSize(11)
        self.title.setFont(font)
        self.title.setStyleSheet(u"color:white;")

        self.verticalLayout_3.addWidget(self.title)

        self.artist = QLabel(self.MediaInfo_frame)
        self.artist.setObjectName(u"artist")
        self.artist.setMaximumSize(QSize(300, 16777215))
        font1 = QFont()
        font1.setFamily(u"Inter 18pt")
        font1.setPointSize(9)
        self.artist.setFont(font1)
        self.artist.setStyleSheet(u"color:rgba(255,255,255,200);")

        self.verticalLayout_3.addWidget(self.artist)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_3.addItem(self.verticalSpacer)


        self.gridLayout_3.addWidget(self.MediaInfo_frame, 0, 1, 1, 1)

        self.horizontalSpacer = QSpacerItem(195, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_3.addItem(self.horizontalSpacer, 0, 2, 1, 1)

        self.frame_2 = QFrame(self.body)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setMaximumSize(QSize(16777215, 45))
        self.frame_2.setStyleSheet(u"background:none;")
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.gridLayout_2 = QGridLayout(self.frame_2)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.likeBtn = QPushButton(self.frame_2)
        self.likeBtn.setObjectName(u"likeBtn")
        self.likeBtn.setMinimumSize(QSize(28, 28))
        self.likeBtn.setMaximumSize(QSize(28, 28))
        self.likeBtn.setStyleSheet(u"QPushButton {\n"
"background-color:rgba(0,0,0,0); \n"
"color:white;\n"
"border-radius:14px;\n"
"padding:0px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"background-color:rgba(255, 255, 255,30); \n"
"color:white;\n"
"border-radius:14px;\n"
"padding:0px;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"background-color:rgba(255, 255, 255,50); \n"
"color:white;\n"
"border-radius:14px;\n"
"padding:0px;\n"
"}")
        icon = QIcon()
        icon.addFile(u"../../resources/icons/icon_like.png", QSize(), QIcon.Normal, QIcon.Off)
        self.likeBtn.setIcon(icon)
        self.likeBtn.setIconSize(QSize(26, 26))

        self.gridLayout_2.addWidget(self.likeBtn, 0, 0, 1, 1)

        self.moreOptions = QPushButton(self.frame_2)
        self.moreOptions.setObjectName(u"moreOptions")
        self.moreOptions.setMinimumSize(QSize(28, 28))
        self.moreOptions.setMaximumSize(QSize(28, 28))
        self.moreOptions.setStyleSheet(u"QPushButton {\n"
"background-color:rgba(0,0,0,0); \n"
"color:white;\n"
"border-radius:14px;\n"
"padding:0px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"background-color:rgba(255, 255, 255,30); \n"
"color:white;\n"
"border-radius:14px;\n"
"padding:0px;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"background-color:rgba(255, 255, 255,50); \n"
"color:white;\n"
"border-radius:14px;\n"
"padding:0px;\n"
"}")
        icon1 = QIcon()
        icon1.addFile(u"../../resources/icons/icon_dotMenu.png", QSize(), QIcon.Normal, QIcon.Off)
        self.moreOptions.setIcon(icon1)
        self.moreOptions.setIconSize(QSize(25, 25))

        self.gridLayout_2.addWidget(self.moreOptions, 0, 1, 1, 1)


        self.gridLayout_3.addWidget(self.frame_2, 0, 3, 1, 1)


        self.gridLayout.addWidget(self.body, 0, 0, 1, 1)

#if QT_CONFIG(shortcut)
#endif // QT_CONFIG(shortcut)

        self.retranslateUi(searchItem)

        QMetaObject.connectSlotsByName(searchItem)
    # setupUi

    def retranslateUi(self, searchItem):
        searchItem.setWindowTitle(QCoreApplication.translate("searchItem", u"Form", None))
        self.coverArt.setText("")
        self.title.setText(QCoreApplication.translate("searchItem", u"The Hills ", None))
        self.artist.setText(QCoreApplication.translate("searchItem", u"The Weeknd", None))
        self.likeBtn.setText("")
        self.moreOptions.setText("")
    # retranslateUi

#     def setSelected(self, bool):
#         self.isSelected = bool
#         if self.isSelected:
#                 self.body.setStyleSheet(u"QFrame {background-color:rgba(255,255,255,50); border-radius:15px;} QFrame::hover {background-color:rgba(255,255,255,40); border-radius:15px;}")
#         else:
#              self.body.setStyleSheet(u"QFrame {background-color:rgba(0,0,0,100); border-radius:15px;} QFrame::hover {background-color:rgba(255,255,255,20); border-radius:15px;}")