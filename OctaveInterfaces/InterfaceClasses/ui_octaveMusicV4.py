# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'octaveMusicV4BQDTxu.ui'
##
## Created by: Qt User Interface Compiler version 6.8.1
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
from PySide6.QtWidgets import (QAbstractItemView, QApplication, QFrame, QGridLayout,
    QHBoxLayout, QLabel, QLineEdit, QListView,
    QListWidget, QListWidgetItem, QMainWindow, QPushButton,
    QScrollArea, QSizePolicy, QSlider, QSpacerItem,
    QStackedWidget, QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1010, 650)
        MainWindow.setStyleSheet(u"/* VERTICAL SCROLLBAR */\n"
"\n"
"\n"
"QScrollBar:vertical {\n"
"    border: none;\n"
"    background: rgba(255, 255, 255, 100); /* Slight tint of white background */\n"
"    width: 10px; /* Reduced width */\n"
"    margin: 15px 0;\n"
"    border-radius: 5px;\n"
"}\n"
"\n"
"/* HANDLE BAR VERTICAL */\n"
"QScrollBar::handle:vertical {    \n"
"    background-color: white; /* White handle */\n"
"    min-height: 30px;\n"
"    border-radius:5px;\n"
"}\n"
"QScrollBar::handle:vertical:hover {    \n"
"    background-color: rgb(255, 255, 255); /* Light gray hover color */\n"
"}\n"
"QScrollBar::handle:vertical:pressed {    \n"
"    background-color: rgba(255, 255, 255, 100); /* Semi-transparent pressed color */\n"
"}\n"
"\n"
"/* BTN TOP - SCROLLBAR */\n"
"QScrollBar::sub-line:vertical {\n"
"    border: none;\n"
"    background-color: rgba(255, 255, 255, 100); /* Slight tint of white background */\n"
"    height: 10px;\n"
"    width: 10px; /* Rounded button */\n"
"    border-radius: 5px; /* Completely rounded */\n"
"    s"
                        "ubcontrol-position: top;\n"
"    subcontrol-origin: margin;\n"
"    background-image: url('path_to_up_arrow_icon.png'); /* Icon URL */\n"
"    background-repeat: no-repeat;\n"
"    background-position: center;\n"
"}\n"
"QScrollBar::sub-line:vertical:hover {    \n"
"    background-color: rgb(255,255,255); /* Light gray hover color */\n"
"}\n"
"QScrollBar::sub-line:vertical:pressed {    \n"
"    background-color: rgb(255, 255, 255); /* Semi-transparent pressed color */\n"
"}\n"
"\n"
"/* BTN BOTTOM - SCROLLBAR */\n"
"QScrollBar::add-line:vertical {\n"
"    border: none;\n"
"    background-color: rgba(255, 255, 255, 100); /* Slight tint of white background */\n"
"    height: 10px;\n"
"    width: 10px; /* Rounded button */\n"
"    border-radius: 5px; /* Completely rounded */\n"
"    subcontrol-position: bottom;\n"
"    subcontrol-origin: margin;\n"
"    background-image: url('path_to_down_arrow_icon.png'); /* Icon URL */\n"
"    background-repeat: no-repeat;\n"
"    background-position: center;\n"
"}\n"
"QScrollBar"
                        "::add-line:vertical:hover {    \n"
"    background-color: rgb(255,255,255); /* Light gray hover color */\n"
"}\n"
"QScrollBar::add-line:vertical:pressed {    \n"
"    background-color: rgba(255, 255, 255, 100); /* Semi-transparent pressed color */\n"
"}\n"
"\n"
"/* RESET ARROW */\n"
"QScrollBar::up-arrow:vertical, QScrollBar::down-arrow:vertical {\n"
"    background: none;\n"
"}\n"
"QScrollBar::add-page:vertical, QScrollBar::sub-page:vertical {\n"
"    background: none;\n"
"}\n"
"\n"
"\n"
"\n"
"\n"
"/* HORIZONTAL SCROLLBAR */\n"
"QScrollBar:horizontal {\n"
"    border: none;\n"
"    background-color: rgba(255, 255, 255, 80); /* More transparent background */\n"
"    height: 6px; /* Reduced height */\n"
"    margin: 0 15px;\n"
"    border-radius: 3px;\n"
"}\n"
"\n"
"/* HANDLE BAR HORIZONTAL */\n"
"QScrollBar::handle:horizontal {    \n"
"    background-color: rgba(255,255,255,80); /* White handle */\n"
"    min-width: 30px;\n"
"    border-radius: 3px;\n"
"}\n"
"QScrollBar::handle:horizontal:hover {    \n"
"    b"
                        "ackground-color: rgba(255,255,255,80); /* White handle */\n"
"}\n"
"QScrollBar::handle:horizontal:pressed {    \n"
"    background-color: rgba(255,255,255,80); /* White handle */\n"
"}\n"
"\n"
"/* BTN LEFT - SCROLLBAR */\n"
"QScrollBar::sub-line:horizontal {\n"
"    border: none;\n"
"    background-color: rgba(255, 255, 255, 0); /* Slight tint of white background */\n"
"    width: 6px; /* Rounded button */\n"
"    height: 6px;\n"
"    border-radius: 3px; /* Completely rounded */\n"
"    subcontrol-position: left;\n"
"    subcontrol-origin: margin;\n"
"  /**  background-image: url('path_to_left_arrow_icon.png');  Icon URL */\n"
"    background-repeat: no-repeat;\n"
"    background-position: center;\n"
"}\n"
"QScrollBar::sub-line:horizontal:hover {    \n"
"    background-color: rgba(255,255,255, 0); /* Light gray hover color */\n"
"}\n"
"QScrollBar::sub-line:horizontal:pressed {    \n"
"    background-color: rgba(255, 255, 255, 0); /* Semi-transparent pressed color */\n"
"}\n"
"\n"
"/* BTN RIGHT - SCROLLBAR */\n"
""
                        "QScrollBar::add-line:horizontal {\n"
"    border: none;\n"
"    background-color: rgba(255, 255, 255, 0); /* Slight tint of white background */\n"
"    width: 6px; /* Rounded button */\n"
"    height: 6px;\n"
"    border-radius: 3px; /* Completely rounded */\n"
"    subcontrol-position: right;\n"
"    subcontrol-origin: margin;\n"
" /*    background-image: url('path_to_right_arrow_icon.png'); Icon URL */\n"
"    background-repeat: no-repeat;\n"
"    background-position: center;\n"
"}\n"
"QScrollBar::add-line:horizontal:hover {    \n"
"    background-color: rgba(255,255,255, 0); /* Light gray hover color */\n"
"}\n"
"QScrollBar::add-line:horizontal:pressed {    \n"
"    background-color: rgba(255, 255, 255, 0); /* Semi-transparent pressed color */\n"
"}\n"
"\n"
"/* RESET ARROW */\n"
"QScrollBar::left-arrow:horizontal, QScrollBar::right-arrow:horizontal {\n"
"    background: none;\n"
"}\n"
"QScrollBar::add-page:horizontal, QScrollBar::sub-page:horizontal {\n"
"    background: none;\n"
"}\n"
"")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setStyleSheet(u"border-radius:0px; \n"
"background-color: qlineargradient(spread:pad, x1:1, y1:0, x2:1, y2:1, stop:0 rgba(0, 0, 0, 255), stop:0.994444 rgba(26, 26, 26, 255));\n"
" color:white;")
        self.gridLayout = QGridLayout(self.centralwidget)
        self.gridLayout.setSpacing(0)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.Window = QFrame(self.centralwidget)
        self.Window.setObjectName(u"Window")
        self.Window.setStyleSheet(u"background-color: rgb(5, 4, 40);\n"
"background-color: qlineargradient(spread:pad, x1:1, y1:0, x2:1, y2:1, stop:0 rgba(0, 0, 0, 151), stop:1 rgba(0, 0, 0, 0));\n"
"")
        self.Window.setFrameShape(QFrame.Shape.StyledPanel)
        self.Window.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout = QVBoxLayout(self.Window)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.MainFrame = QFrame(self.Window)
        self.MainFrame.setObjectName(u"MainFrame")
        self.MainFrame.setStyleSheet(u"background-color: transparent;")
        self.MainFrame.setFrameShape(QFrame.Shape.StyledPanel)
        self.MainFrame.setFrameShadow(QFrame.Shadow.Raised)
        self.gridLayout_2 = QGridLayout(self.MainFrame)
        self.gridLayout_2.setSpacing(0)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.TopFrame = QFrame(self.MainFrame)
        self.TopFrame.setObjectName(u"TopFrame")
        self.TopFrame.setMinimumSize(QSize(0, 70))
        self.TopFrame.setMaximumSize(QSize(16777215, 70))
        self.TopFrame.setStyleSheet(u"/**background-color: rgba(0,0,0,100);**/\n"
"background-color: transparent;")
        self.TopFrame.setFrameShape(QFrame.Shape.StyledPanel)
        self.TopFrame.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_4 = QHBoxLayout(self.TopFrame)
        self.horizontalLayout_4.setSpacing(0)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(9, 0, 9, 0)
        self.frame_13 = QFrame(self.TopFrame)
        self.frame_13.setObjectName(u"frame_13")
        self.frame_13.setMinimumSize(QSize(64, 45))
        self.frame_13.setMaximumSize(QSize(64, 16777215))
        self.frame_13.setStyleSheet(u"background-color:transparent;")
        self.frame_13.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_13.setFrameShadow(QFrame.Shadow.Raised)
        self.gridLayout_6 = QGridLayout(self.frame_13)
        self.gridLayout_6.setObjectName(u"gridLayout_6")
        self.menuBtn = QPushButton(self.frame_13)
        self.menuBtn.setObjectName(u"menuBtn")
        self.menuBtn.setMinimumSize(QSize(46, 46))
        self.menuBtn.setMaximumSize(QSize(46, 46))
        self.menuBtn.setStyleSheet(u"QPushButton {\n"
"border-radius:23px;\n"
"background-color:rgba(0,0,0,50);\n"
"border:none;\n"
"}\n"
"\n"
"QPushButton::hover {\n"
"border-radius:23px;\n"
"background-color:rgba(255,255,255, 50);\n"
"border:none;\n"
"}\n"
"\n"
"QPushButton::pressed {\n"
"border-radius:23px;\n"
"background-color:rgba(255,255,255, 30);\n"
"border:none;\n"
"}\n"
"")
        icon = QIcon()
        icon.addFile(u"../../../../Downloads/icons8-menu-48.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.menuBtn.setIcon(icon)
        self.menuBtn.setIconSize(QSize(36, 36))

        self.gridLayout_6.addWidget(self.menuBtn, 0, 0, 1, 1)


        self.horizontalLayout_4.addWidget(self.frame_13)

        self.frame_12 = QFrame(self.TopFrame)
        self.frame_12.setObjectName(u"frame_12")
        self.frame_12.setStyleSheet(u"background-color:transparent;")
        self.frame_12.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_12.setFrameShadow(QFrame.Shadow.Raised)
        self.gridLayout_5 = QGridLayout(self.frame_12)
        self.gridLayout_5.setObjectName(u"gridLayout_5")
        self.search = QPushButton(self.frame_12)
        self.search.setObjectName(u"search")
        self.search.setMinimumSize(QSize(40, 40))
        self.search.setMaximumSize(QSize(40, 40))
        self.search.setStyleSheet(u"QPushButton {\n"
"border-radius:20px;\n"
"background-color:rgba(0,0,0,50);\n"
"border:none;\n"
"}\n"
"\n"
"QPushButton::hover {\n"
"border-radius:20px;\n"
"background-color:rgba(255,255,255, 50);\n"
"border:none;\n"
"}\n"
"\n"
"QPushButton::pressed {\n"
"border-radius:20px;\n"
"background-color:rgba(255,255,255, 30);\n"
"border:none;\n"
"}\n"
"")
        icon1 = QIcon()
        icon1.addFile(u"../../../../Downloads/icons8-search-48.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.search.setIcon(icon1)
        self.search.setIconSize(QSize(34, 34))

        self.gridLayout_5.addWidget(self.search, 0, 1, 1, 1)

        self.searchBox = QLineEdit(self.frame_12)
        self.searchBox.setObjectName(u"searchBox")
        self.searchBox.setMinimumSize(QSize(270, 40))
        self.searchBox.setMaximumSize(QSize(270, 40))
        font = QFont()
        font.setFamilies([u"Inter 18pt"])
        font.setPointSize(11)
        self.searchBox.setFont(font)
        self.searchBox.setStyleSheet(u"\n"
"\n"
"QLineEdit {\n"
"    border: 1px solid rgba(255, 255, 255, 100); /* Highlight border color */\n"
"    background-color: rgba(0, 0, 0, 150);  /* Background color (optional) */\n"
"    color: white;                          /* Text color */\n"
"/*     border: 1px solid rgba(255, 255, 255, 200); Border color */\n"
"    padding: 8px;                         /* Padding inside the line edit */\n"
"	border-radius:20px;\n"
"	background:rgba(0,0,0,50);\n"
"}\n"
"\n"
"QLineEdit:focus {\n"
"	border-radius:20px;\n"
"	padding:8px;\n"
"    border: 2px solid rgba(255, 255, 255, 255); /* Highlight border color */\n"
"    background-color: rgba(0, 0, 0, 100); /* Highlight color */\n"
"}")

        self.gridLayout_5.addWidget(self.searchBox, 0, 0, 1, 1)

        self.horizontalSpacer_5 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_5.addItem(self.horizontalSpacer_5, 0, 2, 1, 1)


        self.horizontalLayout_4.addWidget(self.frame_12)

        self.horizontalSpacer_4 = QSpacerItem(462, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_4.addItem(self.horizontalSpacer_4)

        self.frame_11 = QFrame(self.TopFrame)
        self.frame_11.setObjectName(u"frame_11")
        self.frame_11.setMinimumSize(QSize(300, 0))
        self.frame_11.setStyleSheet(u"background-color:transparent;")
        self.frame_11.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_11.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_6 = QHBoxLayout(self.frame_11)
        self.horizontalLayout_6.setSpacing(11)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.horizontalLayout_6.setContentsMargins(-1, 6, 8, 6)
        self.horizontalSpacer_10 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_6.addItem(self.horizontalSpacer_10)

        self.profileBtn = QPushButton(self.frame_11)
        self.profileBtn.setObjectName(u"profileBtn")
        self.profileBtn.setMinimumSize(QSize(40, 40))
        self.profileBtn.setMaximumSize(QSize(40, 40))
        self.profileBtn.setStyleSheet(u"QPushButton {\n"
"border-radius:20px;\n"
"background-color:rgba(0,0,0,50);\n"
"border:none;\n"
"}\n"
"\n"
"QPushButton::hover {\n"
"border-radius:20px;\n"
"background-color:rgba(255,255,255, 50);\n"
"border:none;\n"
"}\n"
"\n"
"QPushButton::pressed {\n"
"border-radius:20px;\n"
"background-color:rgba(255,255,255, 30);\n"
"border:none;\n"
"}\n"
"")
        icon2 = QIcon()
        icon2.addFile(u"../../../../Downloads/Group 1 (2).png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.profileBtn.setIcon(icon2)
        self.profileBtn.setIconSize(QSize(34, 34))

        self.horizontalLayout_6.addWidget(self.profileBtn)

        self.minimizeBtn = QPushButton(self.frame_11)
        self.minimizeBtn.setObjectName(u"minimizeBtn")
        self.minimizeBtn.setMinimumSize(QSize(40, 40))
        self.minimizeBtn.setMaximumSize(QSize(40, 40))
        self.minimizeBtn.setStyleSheet(u"QPushButton {\n"
"border-radius:20px;\n"
"background-color:rgba(0,0,0,50);\n"
"border:none;\n"
"}\n"
"\n"
"QPushButton::hover {\n"
"border-radius:20px;\n"
"background-color:rgba(255,255,255, 50);\n"
"border:none;\n"
"}\n"
"\n"
"QPushButton::pressed {\n"
"border-radius:20px;\n"
"background-color:rgba(255,255,255, 30);\n"
"border:none;\n"
"}\n"
"")
        icon3 = QIcon()
        icon3.addFile(u"../../../../Downloads/icons8-minimize-48.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.minimizeBtn.setIcon(icon3)
        self.minimizeBtn.setIconSize(QSize(18, 18))

        self.horizontalLayout_6.addWidget(self.minimizeBtn)

        self.maximiseBtn = QPushButton(self.frame_11)
        self.maximiseBtn.setObjectName(u"maximiseBtn")
        self.maximiseBtn.setMinimumSize(QSize(40, 40))
        self.maximiseBtn.setMaximumSize(QSize(40, 40))
        self.maximiseBtn.setStyleSheet(u"QPushButton {\n"
"border-radius:20px;\n"
"background-color:rgba(0,0,0,50);\n"
"border:none;\n"
"}\n"
"\n"
"QPushButton::hover {\n"
"border-radius:20px;\n"
"background-color:rgba(255,255,255, 50);\n"
"border:none;\n"
"}\n"
"\n"
"QPushButton::pressed {\n"
"border-radius:20px;\n"
"background-color:rgba(255,255,255, 30);\n"
"border:none;\n"
"}\n"
"")
        icon4 = QIcon()
        icon4.addFile(u"../../../../Downloads/icons8-maximize-button-48.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.maximiseBtn.setIcon(icon4)
        self.maximiseBtn.setIconSize(QSize(18, 18))

        self.horizontalLayout_6.addWidget(self.maximiseBtn)

        self.closeBtn = QPushButton(self.frame_11)
        self.closeBtn.setObjectName(u"closeBtn")
        self.closeBtn.setMinimumSize(QSize(40, 40))
        self.closeBtn.setMaximumSize(QSize(40, 40))
        self.closeBtn.setStyleSheet(u"\n"
"QPushButton {\n"
"border-radius:20px;\n"
"background-color:rgba(0,0,0,50);\n"
"border:none;}\n"
"\n"
"QPushButton::hover {\n"
"border-radius:20px;\n"
"background-color:rgba(255,0,0, 100);\n"
"border:none;}\n"
"\n"
"QPushButton::pressed {\n"
"border-radius:20px;\n"
"background-color:rgba(255,0,0, 150);\n"
"border:none;}\n"
"")
        icon5 = QIcon()
        icon5.addFile(u"../../../../Downloads/icons8-close-48.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.closeBtn.setIcon(icon5)
        self.closeBtn.setIconSize(QSize(18, 18))

        self.horizontalLayout_6.addWidget(self.closeBtn)


        self.horizontalLayout_4.addWidget(self.frame_11)


        self.gridLayout_2.addWidget(self.TopFrame, 0, 0, 1, 2)

        self.BodyFrame = QFrame(self.MainFrame)
        self.BodyFrame.setObjectName(u"BodyFrame")
        self.BodyFrame.setStyleSheet(u"background-color: transparent;")
        self.BodyFrame.setFrameShape(QFrame.Shape.StyledPanel)
        self.BodyFrame.setFrameShadow(QFrame.Shadow.Raised)
        self.gridLayout_3 = QGridLayout(self.BodyFrame)
        self.gridLayout_3.setSpacing(0)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.gridLayout_3.setContentsMargins(0, 0, 0, 0)
        self.viewFrame = QStackedWidget(self.BodyFrame)
        self.viewFrame.setObjectName(u"viewFrame")
        self.viewFrame.setMinimumSize(QSize(0, 480))
        self.viewFrame.setStyleSheet(u"/**background-color:rgba(0,0,0,100);**/\n"
"background-color: transparent;\n"
"border-radius:10px; margin:5px;")
        self.homePage = QWidget()
        self.homePage.setObjectName(u"homePage")
        self.homePage.setStyleSheet(u"background-color:transparent;\n"
"border-radius:10px;\n"
"margin:0px;")
        self.gridLayout_23 = QGridLayout(self.homePage)
        self.gridLayout_23.setObjectName(u"gridLayout_23")
        self.bodyArea = QScrollArea(self.homePage)
        self.bodyArea.setObjectName(u"bodyArea")
        self.bodyArea.setStyleSheet(u"background:transparent;")
        self.bodyArea.setWidgetResizable(True)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 408, 971))
        self.scrollAreaWidgetContents.setStyleSheet(u"background:transparent;")
        self.gridLayout_7 = QGridLayout(self.scrollAreaWidgetContents)
        self.gridLayout_7.setObjectName(u"gridLayout_7")
        self.gridLayout_7.setContentsMargins(-1, 0, -1, -1)
        self.frame_18 = QFrame(self.scrollAreaWidgetContents)
        self.frame_18.setObjectName(u"frame_18")
        self.frame_18.setMinimumSize(QSize(0, 300))
        self.frame_18.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_18.setFrameShadow(QFrame.Shadow.Raised)
        self.gridLayout_16 = QGridLayout(self.frame_18)
        self.gridLayout_16.setSpacing(0)
        self.gridLayout_16.setObjectName(u"gridLayout_16")
        self.gridLayout_16.setContentsMargins(0, 0, 0, 0)
        self.frame_19 = QFrame(self.frame_18)
        self.frame_19.setObjectName(u"frame_19")
        self.frame_19.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_19.setFrameShadow(QFrame.Shadow.Raised)
        self.gridLayout_14 = QGridLayout(self.frame_19)
        self.gridLayout_14.setObjectName(u"gridLayout_14")
        self.gridLayout_14.setHorizontalSpacing(0)
        self.gridLayout_14.setContentsMargins(0, 0, 0, 0)
        self.label_5 = QLabel(self.frame_19)
        self.label_5.setObjectName(u"label_5")
        font1 = QFont()
        font1.setFamilies([u"Inter 24pt SemiBold"])
        font1.setPointSize(18)
        self.label_5.setFont(font1)
        self.label_5.setStyleSheet(u"background-color:rgba(0,0,0,0); ")

        self.gridLayout_14.addWidget(self.label_5, 0, 0, 1, 1)


        self.gridLayout_16.addWidget(self.frame_19, 0, 0, 1, 1)

        self.frame_20 = QFrame(self.frame_18)
        self.frame_20.setObjectName(u"frame_20")
        self.frame_20.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_20.setFrameShadow(QFrame.Shadow.Raised)
        self.gridLayout_25 = QGridLayout(self.frame_20)
        self.gridLayout_25.setObjectName(u"gridLayout_25")
        self.label_7 = QLabel(self.frame_20)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setMaximumSize(QSize(180, 16777215))
        font2 = QFont()
        font2.setFamilies([u"Inter 18pt Light"])
        font2.setPointSize(10)
        self.label_7.setFont(font2)

        self.gridLayout_25.addWidget(self.label_7, 0, 0, 1, 1)

        self.horizontalSpacer_6 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_25.addItem(self.horizontalSpacer_6, 0, 1, 1, 1)


        self.gridLayout_16.addWidget(self.frame_20, 1, 0, 1, 1)

        self.frame_21 = QFrame(self.frame_18)
        self.frame_21.setObjectName(u"frame_21")
        self.frame_21.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_21.setFrameShadow(QFrame.Shadow.Raised)
        self.gridLayout_15 = QGridLayout(self.frame_21)
        self.gridLayout_15.setObjectName(u"gridLayout_15")
        self.favourites = QListWidget(self.frame_21)
        self.favourites.setObjectName(u"favourites")
        self.favourites.setStyleSheet(u"    QListWidget::item {\n"
"        selection-background-color: transparent; /* No background on selection */\n"
"        selection-color: transparent;            /* No text color change on selection */\n"
"        outline: none;              \n"
"	border:none;             /* Remove white selection border */\n"
"    }\n"
"\n"
"    QListWidget::item:hover {\n"
"        background-color: transparent;           /* No hover effect */                     \n"
"        outline: none;              \n"
"	border:none; /* Keep the same text color */\n"
"    }\n"
"\n"
"    QListWidget::item:selected {\n"
"        background-color: transparent;           /* No background on selection */\n"
"             /* No selection border */\n"
"        outline: none;              \n"
"	border:none;\n"
"    }")
        self.favourites.setTextElideMode(Qt.TextElideMode.ElideLeft)
        self.favourites.setVerticalScrollMode(QAbstractItemView.ScrollMode.ScrollPerPixel)
        self.favourites.setHorizontalScrollMode(QAbstractItemView.ScrollMode.ScrollPerPixel)
        self.favourites.setMovement(QListView.Movement.Static)
        self.favourites.setFlow(QListView.Flow.LeftToRight)
        self.favourites.setProperty(u"isWrapping", False)
        self.favourites.setResizeMode(QListView.ResizeMode.Fixed)
        self.favourites.setLayoutMode(QListView.LayoutMode.SinglePass)
        self.favourites.setSpacing(8)
        self.favourites.setViewMode(QListView.ViewMode.ListMode)
        self.favourites.setUniformItemSizes(True)
        self.favourites.setSelectionRectVisible(False)

        self.gridLayout_15.addWidget(self.favourites, 1, 0, 1, 1)


        self.gridLayout_16.addWidget(self.frame_21, 2, 0, 1, 1)


        self.gridLayout_7.addWidget(self.frame_18, 2, 0, 1, 1)

        self.frame_22 = QFrame(self.scrollAreaWidgetContents)
        self.frame_22.setObjectName(u"frame_22")
        self.frame_22.setMinimumSize(QSize(0, 300))
        self.frame_22.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_22.setFrameShadow(QFrame.Shadow.Raised)
        self.gridLayout_13 = QGridLayout(self.frame_22)
        self.gridLayout_13.setSpacing(0)
        self.gridLayout_13.setObjectName(u"gridLayout_13")
        self.gridLayout_13.setContentsMargins(0, 0, 0, 0)
        self.frame_23 = QFrame(self.frame_22)
        self.frame_23.setObjectName(u"frame_23")
        self.frame_23.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_23.setFrameShadow(QFrame.Shadow.Raised)
        self.gridLayout_11 = QGridLayout(self.frame_23)
        self.gridLayout_11.setSpacing(0)
        self.gridLayout_11.setObjectName(u"gridLayout_11")
        self.gridLayout_11.setContentsMargins(0, 0, 0, 0)
        self.label = QLabel(self.frame_23)
        self.label.setObjectName(u"label")
        self.label.setFont(font1)
        self.label.setStyleSheet(u"background-color:rgba(0,0,0,0); ")

        self.gridLayout_11.addWidget(self.label, 0, 0, 1, 1)


        self.gridLayout_13.addWidget(self.frame_23, 0, 0, 1, 1)

        self.frame_24 = QFrame(self.frame_22)
        self.frame_24.setObjectName(u"frame_24")
        self.frame_24.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_24.setFrameShadow(QFrame.Shadow.Raised)
        self.gridLayout_20 = QGridLayout(self.frame_24)
        self.gridLayout_20.setObjectName(u"gridLayout_20")
        self.label_6 = QLabel(self.frame_24)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setMaximumSize(QSize(180, 16777215))
        self.label_6.setFont(font2)

        self.gridLayout_20.addWidget(self.label_6, 0, 0, 1, 1)

        self.horizontalSpacer_7 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_20.addItem(self.horizontalSpacer_7, 0, 1, 1, 1)


        self.gridLayout_13.addWidget(self.frame_24, 1, 0, 1, 1)

        self.frame_25 = QFrame(self.frame_22)
        self.frame_25.setObjectName(u"frame_25")
        self.frame_25.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_25.setFrameShadow(QFrame.Shadow.Raised)
        self.gridLayout_12 = QGridLayout(self.frame_25)
        self.gridLayout_12.setObjectName(u"gridLayout_12")
        self.recentlyPlayed = QListWidget(self.frame_25)
        self.recentlyPlayed.setObjectName(u"recentlyPlayed")
        self.recentlyPlayed.setStyleSheet(u"    QListWidget::item {\n"
"        selection-background-color: transparent; /* No background on selection */\n"
"        selection-color: transparent;            /* No text color change on selection */\n"
"        outline: none;              \n"
"	border:none;             /* Remove white selection border */\n"
"    }\n"
"\n"
"    QListWidget::item:hover {\n"
"        background-color: transparent;           /* No hover effect */                     \n"
"        outline: none;              \n"
"	border:none; /* Keep the same text color */\n"
"    }\n"
"\n"
"    QListWidget::item:selected {\n"
"        background-color: transparent;           /* No background on selection */\n"
"             /* No selection border */\n"
"        outline: none;              \n"
"	border:none;\n"
"    }")
        self.recentlyPlayed.setTextElideMode(Qt.TextElideMode.ElideLeft)
        self.recentlyPlayed.setVerticalScrollMode(QAbstractItemView.ScrollMode.ScrollPerPixel)
        self.recentlyPlayed.setHorizontalScrollMode(QAbstractItemView.ScrollMode.ScrollPerPixel)
        self.recentlyPlayed.setMovement(QListView.Movement.Static)
        self.recentlyPlayed.setFlow(QListView.Flow.LeftToRight)
        self.recentlyPlayed.setProperty(u"isWrapping", False)
        self.recentlyPlayed.setResizeMode(QListView.ResizeMode.Fixed)
        self.recentlyPlayed.setLayoutMode(QListView.LayoutMode.SinglePass)
        self.recentlyPlayed.setSpacing(8)
        self.recentlyPlayed.setViewMode(QListView.ViewMode.ListMode)
        self.recentlyPlayed.setUniformItemSizes(True)
        self.recentlyPlayed.setSelectionRectVisible(False)

        self.gridLayout_12.addWidget(self.recentlyPlayed, 0, 0, 1, 1)


        self.gridLayout_13.addWidget(self.frame_25, 2, 0, 1, 1)


        self.gridLayout_7.addWidget(self.frame_22, 1, 0, 1, 1)

        self.frame_26 = QFrame(self.scrollAreaWidgetContents)
        self.frame_26.setObjectName(u"frame_26")
        self.frame_26.setMinimumSize(QSize(0, 350))
        self.frame_26.setMaximumSize(QSize(16777215, 380))
        self.frame_26.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_26.setFrameShadow(QFrame.Shadow.Raised)
        self.gridLayout_10 = QGridLayout(self.frame_26)
        self.gridLayout_10.setSpacing(0)
        self.gridLayout_10.setObjectName(u"gridLayout_10")
        self.gridLayout_10.setContentsMargins(0, 0, 0, 0)
        self.frame_27 = QFrame(self.frame_26)
        self.frame_27.setObjectName(u"frame_27")
        self.frame_27.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_27.setFrameShadow(QFrame.Shadow.Raised)
        self.gridLayout_8 = QGridLayout(self.frame_27)
        self.gridLayout_8.setObjectName(u"gridLayout_8")
        self.gridLayout_8.setHorizontalSpacing(0)
        self.gridLayout_8.setContentsMargins(0, 0, 0, 0)
        self.queueWidget = QListWidget(self.frame_27)
        self.queueWidget.setObjectName(u"queueWidget")
        self.queueWidget.setMinimumSize(QSize(0, 230))
        self.queueWidget.setMaximumSize(QSize(16777215, 230))
        self.queueWidget.setStyleSheet(u"    QListWidget::item {\n"
"        selection-background-color: transparent; /* No background on selection */\n"
"        selection-color: transparent;            /* No text color change on selection */\n"
"        outline: none;              \n"
"	border:none;             /* Remove white selection border */\n"
"    }\n"
"\n"
"    QListWidget::item:hover {\n"
"        background-color: transparent;           /* No hover effect */                     \n"
"        outline: none;              \n"
"	border:none; /* Keep the same text color */\n"
"    }\n"
"\n"
"    QListWidget::item:selected {\n"
"        background-color: transparent;           /* No background on selection */\n"
"             /* No selection border */\n"
"        outline: none;              \n"
"	border:none;\n"
"    }")
        self.queueWidget.setVerticalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        self.queueWidget.setHorizontalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAsNeeded)
        self.queueWidget.setSelectionMode(QAbstractItemView.SelectionMode.SingleSelection)
        self.queueWidget.setTextElideMode(Qt.TextElideMode.ElideLeft)
        self.queueWidget.setVerticalScrollMode(QAbstractItemView.ScrollMode.ScrollPerPixel)
        self.queueWidget.setHorizontalScrollMode(QAbstractItemView.ScrollMode.ScrollPerPixel)
        self.queueWidget.setMovement(QListView.Movement.Static)
        self.queueWidget.setFlow(QListView.Flow.LeftToRight)
        self.queueWidget.setProperty(u"isWrapping", False)
        self.queueWidget.setResizeMode(QListView.ResizeMode.Fixed)
        self.queueWidget.setLayoutMode(QListView.LayoutMode.SinglePass)
        self.queueWidget.setSpacing(8)
        self.queueWidget.setViewMode(QListView.ViewMode.ListMode)
        self.queueWidget.setUniformItemSizes(True)
        self.queueWidget.setSelectionRectVisible(False)

        self.gridLayout_8.addWidget(self.queueWidget, 0, 0, 1, 1)

        self.verticalSpacer_5 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.gridLayout_8.addItem(self.verticalSpacer_5, 1, 1, 1, 1)

        self.verticalSpacer_4 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.gridLayout_8.addItem(self.verticalSpacer_4, 1, 0, 1, 1)


        self.gridLayout_10.addWidget(self.frame_27, 1, 0, 1, 1)

        self.frame_28 = QFrame(self.frame_26)
        self.frame_28.setObjectName(u"frame_28")
        self.frame_28.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_28.setFrameShadow(QFrame.Shadow.Raised)
        self.gridLayout_9 = QGridLayout(self.frame_28)
        self.gridLayout_9.setObjectName(u"gridLayout_9")
        self.gridLayout_9.setHorizontalSpacing(0)
        self.gridLayout_9.setContentsMargins(0, 0, 0, 0)
        self.frame_29 = QFrame(self.frame_28)
        self.frame_29.setObjectName(u"frame_29")
        self.frame_29.setMinimumSize(QSize(0, 38))
        self.frame_29.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_29.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_10 = QHBoxLayout(self.frame_29)
        self.horizontalLayout_10.setSpacing(0)
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.horizontalLayout_10.setContentsMargins(0, 0, 0, 0)
        self.label_8 = QLabel(self.frame_29)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setMinimumSize(QSize(215, 0))
        self.label_8.setMaximumSize(QSize(215, 16777215))
        self.label_8.setFont(font1)
        self.label_8.setStyleSheet(u"background-color:rgba(0,0,0,0); ")

        self.horizontalLayout_10.addWidget(self.label_8)

        self.frame_30 = QFrame(self.frame_29)
        self.frame_30.setObjectName(u"frame_30")
        self.frame_30.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_30.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_11 = QHBoxLayout(self.frame_30)
        self.horizontalLayout_11.setSpacing(4)
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.horizontalLayout_11.setContentsMargins(-1, 0, 0, 0)
        self.playBtn_queue = QPushButton(self.frame_30)
        self.playBtn_queue.setObjectName(u"playBtn_queue")
        self.playBtn_queue.setMinimumSize(QSize(40, 38))
        self.playBtn_queue.setMaximumSize(QSize(40, 38))
        self.playBtn_queue.setStyleSheet(u"QPushButton {\n"
"background-color:rgba(0,0,0,0); \n"
"color:white;\n"
"border-radius:19px;\n"
"padding:0px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"background-color:rgba(255, 255, 255,30); \n"
"color:white;\n"
"border-radius:19px;\n"
"padding:0px;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"background-color:rgba(255, 255, 255,50); \n"
"color:white;\n"
"border-radius:19px;\n"
"padding:0px;\n"
"}")
        icon6 = QIcon()
        icon6.addFile(u"../../resources/icons/icon_play.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.playBtn_queue.setIcon(icon6)
        self.playBtn_queue.setIconSize(QSize(42, 42))

        self.horizontalLayout_11.addWidget(self.playBtn_queue)

        self.frame_31 = QFrame(self.frame_30)
        self.frame_31.setObjectName(u"frame_31")
        self.frame_31.setMinimumSize(QSize(118, 40))
        self.frame_31.setMaximumSize(QSize(118, 40))
        self.frame_31.setStyleSheet(u"background-color:rgba(0,0,0,20); border-radius:20;")
        self.frame_31.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_31.setFrameShadow(QFrame.Shadow.Raised)
        self.gridLayout_17 = QGridLayout(self.frame_31)
        self.gridLayout_17.setSpacing(0)
        self.gridLayout_17.setObjectName(u"gridLayout_17")
        self.gridLayout_17.setContentsMargins(0, 0, 0, 0)
        self.newQueue = QPushButton(self.frame_31)
        self.newQueue.setObjectName(u"newQueue")
        self.newQueue.setMinimumSize(QSize(32, 30))
        self.newQueue.setMaximumSize(QSize(32, 30))
        self.newQueue.setStyleSheet(u"QPushButton {\n"
"background-color:rgba(0,0,0,0); \n"
"color:white;\n"
"border-radius:15px;\n"
"padding:0px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"background-color:rgba(255, 255, 255,30); \n"
"color:white;\n"
"border-radius:15px;\n"
"padding:0px;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"background-color:rgba(255, 255, 255,50); \n"
"color:white;\n"
"border-radius:15px;\n"
"padding:0px;\n"
"}")
        icon7 = QIcon()
        icon7.addFile(u"../../resources/icons/icon_newQueue.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.newQueue.setIcon(icon7)
        self.newQueue.setIconSize(QSize(28, 28))

        self.gridLayout_17.addWidget(self.newQueue, 0, 0, 1, 1)

        self.addToQueue = QPushButton(self.frame_31)
        self.addToQueue.setObjectName(u"addToQueue")
        self.addToQueue.setMinimumSize(QSize(32, 30))
        self.addToQueue.setMaximumSize(QSize(32, 30))
        self.addToQueue.setStyleSheet(u"QPushButton {\n"
"background-color:rgba(0,0,0,0); \n"
"color:white;\n"
"border-radius:15px;\n"
"padding:0px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"background-color:rgba(255, 255, 255,30); \n"
"color:white;\n"
"border-radius:15px;\n"
"padding:0px;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"background-color:rgba(255, 255, 255,50); \n"
"color:white;\n"
"border-radius:15px;\n"
"padding:0px;\n"
"}")
        icon8 = QIcon()
        icon8.addFile(u"../../resources/icons/icon_addToQueue.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.addToQueue.setIcon(icon8)
        self.addToQueue.setIconSize(QSize(28, 28))

        self.gridLayout_17.addWidget(self.addToQueue, 0, 1, 1, 1)

        self.removeFromQueue = QPushButton(self.frame_31)
        self.removeFromQueue.setObjectName(u"removeFromQueue")
        self.removeFromQueue.setMinimumSize(QSize(32, 30))
        self.removeFromQueue.setMaximumSize(QSize(32, 30))
        self.removeFromQueue.setStyleSheet(u"QPushButton {\n"
"background-color:rgba(0,0,0,0); \n"
"color:white;\n"
"border-radius:15px;\n"
"padding:0px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"background-color:rgba(255, 255, 255,30); \n"
"color:white;\n"
"border-radius:15px;\n"
"padding:0px;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"background-color:rgba(255, 255, 255,50); \n"
"color:white;\n"
"border-radius:15px;\n"
"padding:0px;\n"
"}")
        icon9 = QIcon()
        icon9.addFile(u"../../resources/icons/icon_removeFromQueue.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.removeFromQueue.setIcon(icon9)
        self.removeFromQueue.setIconSize(QSize(28, 28))

        self.gridLayout_17.addWidget(self.removeFromQueue, 0, 2, 1, 1)


        self.horizontalLayout_11.addWidget(self.frame_31)

        self.horizontalSpacer_8 = QSpacerItem(423, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_11.addItem(self.horizontalSpacer_8)


        self.horizontalLayout_10.addWidget(self.frame_30)


        self.gridLayout_9.addWidget(self.frame_29, 0, 0, 1, 1)

        self.frame_32 = QFrame(self.frame_28)
        self.frame_32.setObjectName(u"frame_32")
        self.frame_32.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_32.setFrameShadow(QFrame.Shadow.Raised)
        self.gridLayout_19 = QGridLayout(self.frame_32)
        self.gridLayout_19.setObjectName(u"gridLayout_19")
        self.label_9 = QLabel(self.frame_32)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setMaximumSize(QSize(180, 16777215))
        self.label_9.setFont(font2)

        self.gridLayout_19.addWidget(self.label_9, 0, 0, 1, 1)

        self.loadQueue = QPushButton(self.frame_32)
        self.loadQueue.setObjectName(u"loadQueue")
        self.loadQueue.setMinimumSize(QSize(38, 38))
        self.loadQueue.setMaximumSize(QSize(100, 16777215))
        font3 = QFont()
        font3.setFamilies([u"Inter 18pt SemiBold"])
        font3.setPointSize(9)
        self.loadQueue.setFont(font3)
        self.loadQueue.setStyleSheet(u"QPushButton {\n"
"border-radius:8px;\n"
"background-color:rgba(0,0,0,0);\n"
"border:none;\n"
"\n"
"}\n"
"QPushButton::hover {\n"
"border-radius:8px;\n"
"color:rgb(200, 200, 200);\n"
"border:none;\n"
"}\n"
"\n"
"QPushButton::pressed {\n"
"border-radius:8px;\n"
"color:rgb(149, 149, 149);\n"
"border:none;\n"
"}\n"
"")
        self.loadQueue.setIconSize(QSize(34, 34))

        self.gridLayout_19.addWidget(self.loadQueue, 0, 1, 1, 1)

        self.horizontalSpacer_9 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_19.addItem(self.horizontalSpacer_9, 0, 2, 1, 1)


        self.gridLayout_9.addWidget(self.frame_32, 2, 0, 1, 1)


        self.gridLayout_10.addWidget(self.frame_28, 0, 0, 1, 1)


        self.gridLayout_7.addWidget(self.frame_26, 0, 0, 1, 1)

        self.bodyArea.setWidget(self.scrollAreaWidgetContents)

        self.gridLayout_23.addWidget(self.bodyArea, 0, 0, 1, 1)

        self.viewFrame.addWidget(self.homePage)
        self.explorePage = QWidget()
        self.explorePage.setObjectName(u"explorePage")
        self.explorePage.setMinimumSize(QSize(0, 340))
        self.explorePage.setStyleSheet(u"background-color:transparent;\n"
"border-radius:0px;\n"
"margin:0px;")
        self.verticalLayout_9 = QVBoxLayout(self.explorePage)
        self.verticalLayout_9.setSpacing(5)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.verticalLayout_9.setContentsMargins(6, 0, 4, -1)
        self.searchbarFrame_2 = QFrame(self.explorePage)
        self.searchbarFrame_2.setObjectName(u"searchbarFrame_2")
        self.searchbarFrame_2.setMinimumSize(QSize(0, 20))
        self.searchbarFrame_2.setMaximumSize(QSize(16777215, 20))
        self.searchbarFrame_2.setFrameShape(QFrame.Shape.StyledPanel)
        self.searchbarFrame_2.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_10 = QVBoxLayout(self.searchbarFrame_2)
        self.verticalLayout_10.setSpacing(0)
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.verticalLayout_10.setContentsMargins(0, 0, 0, 0)

        self.verticalLayout_9.addWidget(self.searchbarFrame_2)

        self.explorePageBody = QFrame(self.explorePage)
        self.explorePageBody.setObjectName(u"explorePageBody")
        self.explorePageBody.setMinimumSize(QSize(0, 340))
        self.explorePageBody.setMaximumSize(QSize(16777215, 16777215))
        self.explorePageBody.setFrameShape(QFrame.Shape.StyledPanel)
        self.explorePageBody.setFrameShadow(QFrame.Shadow.Raised)
        self.gridLayout_21 = QGridLayout(self.explorePageBody)
        self.gridLayout_21.setObjectName(u"gridLayout_21")
        self.gridLayout_21.setContentsMargins(0, 0, 0, 0)
        self.searchResultsBody = QFrame(self.explorePageBody)
        self.searchResultsBody.setObjectName(u"searchResultsBody")
        self.searchResultsBody.setMinimumSize(QSize(0, 340))
        self.searchResultsBody.setFrameShape(QFrame.Shape.StyledPanel)
        self.searchResultsBody.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_13 = QHBoxLayout(self.searchResultsBody)
        self.horizontalLayout_13.setObjectName(u"horizontalLayout_13")
        self.topResultFrame = QFrame(self.searchResultsBody)
        self.topResultFrame.setObjectName(u"topResultFrame")
        self.topResultFrame.setMinimumSize(QSize(325, 0))
        self.topResultFrame.setMaximumSize(QSize(325, 16777215))
        self.topResultFrame.setFrameShape(QFrame.Shape.StyledPanel)
        self.topResultFrame.setFrameShadow(QFrame.Shadow.Raised)
        self.gridLayout_29 = QGridLayout(self.topResultFrame)
        self.gridLayout_29.setObjectName(u"gridLayout_29")
        self.gridLayout_29.setContentsMargins(4, 4, -1, -1)
        self.verticalSpacer_3 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.gridLayout_29.addItem(self.verticalSpacer_3, 1, 0, 1, 1)

        self.topResultCard = QFrame(self.topResultFrame)
        self.topResultCard.setObjectName(u"topResultCard")
        self.topResultCard.setMinimumSize(QSize(310, 240))
        self.topResultCard.setMaximumSize(QSize(310, 240))
        self.topResultCard.setStyleSheet(u"background-color:rgba(0,0,0,100); \n"
"border-radius:18px;")
        self.topResultCard.setFrameShape(QFrame.Shape.StyledPanel)
        self.topResultCard.setFrameShadow(QFrame.Shadow.Raised)
        self.gridLayout_27 = QGridLayout(self.topResultCard)
        self.gridLayout_27.setSpacing(0)
        self.gridLayout_27.setObjectName(u"gridLayout_27")
        self.gridLayout_27.setContentsMargins(4, 4, 4, 4)
        self.topResultCard_coverartframe = QFrame(self.topResultCard)
        self.topResultCard_coverartframe.setObjectName(u"topResultCard_coverartframe")
        self.topResultCard_coverartframe.setMinimumSize(QSize(160, 150))
        self.topResultCard_coverartframe.setMaximumSize(QSize(16777215, 150))
        self.topResultCard_coverartframe.setStyleSheet(u"background-color:transparent;")
        self.topResultCard_coverartframe.setFrameShape(QFrame.Shape.StyledPanel)
        self.topResultCard_coverartframe.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_15 = QHBoxLayout(self.topResultCard_coverartframe)
        self.horizontalLayout_15.setSpacing(0)
        self.horizontalLayout_15.setObjectName(u"horizontalLayout_15")
        self.horizontalLayout_15.setContentsMargins(12, 0, 0, 0)
        self.topResultCoverart = QLabel(self.topResultCard_coverartframe)
        self.topResultCoverart.setObjectName(u"topResultCoverart")
        self.topResultCoverart.setMinimumSize(QSize(140, 140))
        self.topResultCoverart.setMaximumSize(QSize(140, 140))
        self.topResultCoverart.setStyleSheet(u"background-color:rgba(0,0,0,100); border-radius:24px;")

        self.horizontalLayout_15.addWidget(self.topResultCoverart)

        self.horizontalSpacer_14 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_15.addItem(self.horizontalSpacer_14)


        self.gridLayout_27.addWidget(self.topResultCard_coverartframe, 0, 0, 1, 1)

        self.topResultCard_titles = QFrame(self.topResultCard)
        self.topResultCard_titles.setObjectName(u"topResultCard_titles")
        self.topResultCard_titles.setMaximumSize(QSize(16777215, 60))
        font4 = QFont()
        font4.setPointSize(5)
        self.topResultCard_titles.setFont(font4)
        self.topResultCard_titles.setStyleSheet(u"background-color:transparent;")
        self.topResultCard_titles.setFrameShape(QFrame.Shape.StyledPanel)
        self.topResultCard_titles.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_14 = QHBoxLayout(self.topResultCard_titles)
        self.horizontalLayout_14.setSpacing(0)
        self.horizontalLayout_14.setObjectName(u"horizontalLayout_14")
        self.horizontalLayout_14.setContentsMargins(16, 0, 16, 2)
        self.frame_33 = QFrame(self.topResultCard_titles)
        self.frame_33.setObjectName(u"frame_33")
        self.frame_33.setMaximumSize(QSize(16777215, 45))
        self.frame_33.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_33.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_11 = QVBoxLayout(self.frame_33)
        self.verticalLayout_11.setSpacing(0)
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.verticalLayout_11.setContentsMargins(0, 0, 0, 0)
        self.topResult_title = QLabel(self.frame_33)
        self.topResult_title.setObjectName(u"topResult_title")
        self.topResult_title.setMinimumSize(QSize(152, 32))
        self.topResult_title.setMaximumSize(QSize(180, 32))
        font5 = QFont()
        font5.setFamilies([u"Inter 18pt ExtraBold"])
        font5.setPointSize(16)
        self.topResult_title.setFont(font5)
        self.topResult_title.setScaledContents(False)
        self.topResult_title.setWordWrap(False)

        self.verticalLayout_11.addWidget(self.topResult_title)

        self.topResult_artist = QLabel(self.frame_33)
        self.topResult_artist.setObjectName(u"topResult_artist")
        self.topResult_artist.setMinimumSize(QSize(100, 18))
        self.topResult_artist.setMaximumSize(QSize(200, 18))
        font6 = QFont()
        font6.setFamilies([u"Inter 18pt"])
        font6.setPointSize(10)
        self.topResult_artist.setFont(font6)
        self.topResult_artist.setStyleSheet(u"color:rgba(255,255,255,200);")

        self.verticalLayout_11.addWidget(self.topResult_artist)


        self.horizontalLayout_14.addWidget(self.frame_33)

        self.frame_34 = QFrame(self.topResultCard_titles)
        self.frame_34.setObjectName(u"frame_34")
        self.frame_34.setMinimumSize(QSize(60, 60))
        self.frame_34.setMaximumSize(QSize(60, 60))
        self.frame_34.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_34.setFrameShadow(QFrame.Shadow.Raised)
        self.gridLayout_28 = QGridLayout(self.frame_34)
        self.gridLayout_28.setObjectName(u"gridLayout_28")
        self.verticalSpacer_6 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.gridLayout_28.addItem(self.verticalSpacer_6, 1, 0, 1, 1)

        self.playTopResult = QPushButton(self.frame_34)
        self.playTopResult.setObjectName(u"playTopResult")
        self.playTopResult.setMinimumSize(QSize(50, 50))
        self.playTopResult.setMaximumSize(QSize(50, 50))
        self.playTopResult.setStyleSheet(u"QPushButton {\n"
"color:white;\n"
"border-radius:25px;\n"
"padding:0px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"background-color:rgba(255,255, 255,40); \n"
"color:white;\n"
"padding:0px;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"background-color:rgba(255, 255, 255,50); \n"
"color:white;\n"
"padding:0px;\n"
"}")
        icon10 = QIcon()
        icon10.addFile(u"../../../../Downloads/icons8-play-96.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.playTopResult.setIcon(icon10)
        self.playTopResult.setIconSize(QSize(46, 46))

        self.gridLayout_28.addWidget(self.playTopResult, 0, 0, 1, 1)


        self.horizontalLayout_14.addWidget(self.frame_34)


        self.gridLayout_27.addWidget(self.topResultCard_titles, 1, 0, 1, 1)


        self.gridLayout_29.addWidget(self.topResultCard, 0, 0, 1, 1)

        self.horizontalSpacer_15 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_29.addItem(self.horizontalSpacer_15, 0, 1, 1, 1)


        self.horizontalLayout_13.addWidget(self.topResultFrame)

        self.searchResultListFrame = QFrame(self.searchResultsBody)
        self.searchResultListFrame.setObjectName(u"searchResultListFrame")
        self.searchResultListFrame.setMinimumSize(QSize(560, 340))
        self.searchResultListFrame.setFrameShape(QFrame.Shape.StyledPanel)
        self.searchResultListFrame.setFrameShadow(QFrame.Shadow.Raised)
        self.gridLayout_30 = QGridLayout(self.searchResultListFrame)
        self.gridLayout_30.setObjectName(u"gridLayout_30")
        self.gridLayout_30.setHorizontalSpacing(0)
        self.gridLayout_30.setContentsMargins(2, 4, 0, 0)
        self.searchResults = QListWidget(self.searchResultListFrame)
        self.searchResults.setObjectName(u"searchResults")
        self.searchResults.setMinimumSize(QSize(550, 320))
        self.searchResults.setMaximumSize(QSize(16777215, 16777215))
        font7 = QFont()
        font7.setFamilies([u"Inter"])
        self.searchResults.setFont(font7)
        self.searchResults.setFocusPolicy(Qt.FocusPolicy.NoFocus)
        self.searchResults.setContextMenuPolicy(Qt.ContextMenuPolicy.NoContextMenu)
        self.searchResults.setStyleSheet(u"\n"
"    QListWidget::item {\n"
"        selection-background-color: transparent; /* No background on selection */\n"
"        selection-color: transparent;            /* No text color change on selection */\n"
"        outline: none;              \n"
"	border:none;             /* Remove white selection border */\n"
"border-radius:10px;\n"
"color:white;\n"
"    }\n"
"\n"
"    QListWidget::item:hover {\n"
"        background-color: transparent;           /* No hover effect */                     \n"
"        outline: none;              \n"
"	border:none; /* Keep the same text color */\n"
"    }\n"
"\n"
"    QListWidget::item:selected {\n"
"        background-color: transparent;           /* No hover effect */                     \n"
"           /* No background on selection */\n"
"             /* No selection border */\n"
"        outline: none;              \n"
"	border:none;\n"
"    }")
        self.searchResults.setFrameShape(QFrame.Shape.NoFrame)
        self.searchResults.setFrameShadow(QFrame.Shadow.Plain)
        self.searchResults.setVerticalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAsNeeded)
        self.searchResults.setHorizontalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAsNeeded)
        self.searchResults.setSelectionMode(QAbstractItemView.SelectionMode.SingleSelection)
        self.searchResults.setTextElideMode(Qt.TextElideMode.ElideNone)
        self.searchResults.setVerticalScrollMode(QAbstractItemView.ScrollMode.ScrollPerPixel)
        self.searchResults.setHorizontalScrollMode(QAbstractItemView.ScrollMode.ScrollPerPixel)
        self.searchResults.setMovement(QListView.Movement.Static)
        self.searchResults.setFlow(QListView.Flow.TopToBottom)
        self.searchResults.setProperty(u"isWrapping", False)
        self.searchResults.setResizeMode(QListView.ResizeMode.Fixed)
        self.searchResults.setLayoutMode(QListView.LayoutMode.SinglePass)
        self.searchResults.setSpacing(1)
        self.searchResults.setViewMode(QListView.ViewMode.ListMode)
        self.searchResults.setUniformItemSizes(True)
        self.searchResults.setSelectionRectVisible(False)

        self.gridLayout_30.addWidget(self.searchResults, 0, 0, 1, 1)


        self.horizontalLayout_13.addWidget(self.searchResultListFrame)


        self.gridLayout_21.addWidget(self.searchResultsBody, 1, 0, 1, 1)

        self.searchResultsTitleFrame = QFrame(self.explorePageBody)
        self.searchResultsTitleFrame.setObjectName(u"searchResultsTitleFrame")
        self.searchResultsTitleFrame.setMaximumSize(QSize(16777215, 40))
        self.searchResultsTitleFrame.setFrameShape(QFrame.Shape.StyledPanel)
        self.searchResultsTitleFrame.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_16 = QHBoxLayout(self.searchResultsTitleFrame)
        self.horizontalLayout_16.setObjectName(u"horizontalLayout_16")
        self.horizontalLayout_16.setContentsMargins(16, 0, 0, 0)
        self.searchHeading_2 = QLabel(self.searchResultsTitleFrame)
        self.searchHeading_2.setObjectName(u"searchHeading_2")
        self.searchHeading_2.setMinimumSize(QSize(314, 0))
        self.searchHeading_2.setMaximumSize(QSize(314, 16777215))
        font8 = QFont()
        font8.setFamilies([u"Inter 24pt ExtraBold"])
        font8.setPointSize(18)
        self.searchHeading_2.setFont(font8)
        self.searchHeading_2.setStyleSheet(u"background-color:rgba(0,0,0,0); ")

        self.horizontalLayout_16.addWidget(self.searchHeading_2)

        self.searchHeading_3 = QLabel(self.searchResultsTitleFrame)
        self.searchHeading_3.setObjectName(u"searchHeading_3")
        self.searchHeading_3.setMinimumSize(QSize(390, 0))
        self.searchHeading_3.setMaximumSize(QSize(390, 16777215))
        self.searchHeading_3.setFont(font8)
        self.searchHeading_3.setStyleSheet(u"background-color:rgba(0,0,0,0);")

        self.horizontalLayout_16.addWidget(self.searchHeading_3)

        self.horizontalSpacer_12 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_16.addItem(self.horizontalSpacer_12)


        self.gridLayout_21.addWidget(self.searchResultsTitleFrame, 0, 0, 1, 1)


        self.verticalLayout_9.addWidget(self.explorePageBody)

        self.viewFrame.addWidget(self.explorePage)
        self.page_2 = QWidget()
        self.page_2.setObjectName(u"page_2")
        self.page_2.setStyleSheet(u"background-color:transparent;\n"
"border-radius:10px;\n"
"margin:0px;")
        self.label_2 = QLabel(self.page_2)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(240, 70, 47, 13))
        self.viewFrame.addWidget(self.page_2)
        self.settingsPage = QWidget()
        self.settingsPage.setObjectName(u"settingsPage")
        self.settingsPage.setStyleSheet(u"background-color:transparent;\n"
"border-radius:10px;\n"
"margin:0px;")
        self.gridLayout_4 = QGridLayout(self.settingsPage)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.settingsFrame = QFrame(self.settingsPage)
        self.settingsFrame.setObjectName(u"settingsFrame")
        self.settingsFrame.setFrameShape(QFrame.Shape.StyledPanel)
        self.settingsFrame.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_12 = QVBoxLayout(self.settingsFrame)
        self.verticalLayout_12.setObjectName(u"verticalLayout_12")
        self.settingsHeading = QLabel(self.settingsFrame)
        self.settingsHeading.setObjectName(u"settingsHeading")
        self.settingsHeading.setMinimumSize(QSize(215, 0))
        self.settingsHeading.setMaximumSize(QSize(215, 16777215))
        self.settingsHeading.setFont(font1)
        self.settingsHeading.setStyleSheet(u"background-color:rgba(0,0,0,0);")

        self.verticalLayout_12.addWidget(self.settingsHeading)

        self.settingsScrollArea = QScrollArea(self.settingsFrame)
        self.settingsScrollArea.setObjectName(u"settingsScrollArea")
        self.settingsScrollArea.setWidgetResizable(True)
        self.scrollAreaWidgetContents_2 = QWidget()
        self.scrollAreaWidgetContents_2.setObjectName(u"scrollAreaWidgetContents_2")
        self.scrollAreaWidgetContents_2.setGeometry(QRect(0, 0, 883, 399))
        self.appearanceFrame = QFrame(self.scrollAreaWidgetContents_2)
        self.appearanceFrame.setObjectName(u"appearanceFrame")
        self.appearanceFrame.setGeometry(QRect(10, 0, 549, 380))
        self.appearanceFrame.setStyleSheet(u"background-color: rgba(0, 0, 0, 80);\n"
"border-radius:8px;\n"
"")
        self.appearanceFrame.setFrameShape(QFrame.Shape.StyledPanel)
        self.appearanceFrame.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_14 = QVBoxLayout(self.appearanceFrame)
        self.verticalLayout_14.setObjectName(u"verticalLayout_14")
        self.appearanceHeader = QFrame(self.appearanceFrame)
        self.appearanceHeader.setObjectName(u"appearanceHeader")
        self.appearanceHeader.setMinimumSize(QSize(0, 60))
        self.appearanceHeader.setMaximumSize(QSize(16777215, 60))
        self.appearanceHeader.setStyleSheet(u"border:none;\n"
" background:rgba(0,0,0,0);")
        self.appearanceHeader.setFrameShape(QFrame.Shape.StyledPanel)
        self.appearanceHeader.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_13 = QVBoxLayout(self.appearanceHeader)
        self.verticalLayout_13.setObjectName(u"verticalLayout_13")
        self.appearanceHead = QLabel(self.appearanceHeader)
        self.appearanceHead.setObjectName(u"appearanceHead")
        self.appearanceHead.setMinimumSize(QSize(215, 0))
        self.appearanceHead.setMaximumSize(QSize(215, 16777215))
        font9 = QFont()
        font9.setFamilies([u"Inter"])
        font9.setPointSize(14)
        self.appearanceHead.setFont(font9)
        self.appearanceHead.setStyleSheet(u"background-color:rgba(0,0,0,0);\n"
"\n"
"")

        self.verticalLayout_13.addWidget(self.appearanceHead)

        self.label_12 = QLabel(self.appearanceHeader)
        self.label_12.setObjectName(u"label_12")
        self.label_12.setMinimumSize(QSize(215, 0))
        self.label_12.setMaximumSize(QSize(215, 16777215))
        font10 = QFont()
        font10.setFamilies([u"Inter"])
        font10.setPointSize(8)
        self.label_12.setFont(font10)
        self.label_12.setStyleSheet(u"background-color:rgba(0,0,0,0); color:rgba(255,255,255,100);")

        self.verticalLayout_13.addWidget(self.label_12)


        self.verticalLayout_14.addWidget(self.appearanceHeader)

        self.appearanceOptions = QFrame(self.appearanceFrame)
        self.appearanceOptions.setObjectName(u"appearanceOptions")
        self.appearanceOptions.setMinimumSize(QSize(531, 53))
        self.appearanceOptions.setMaximumSize(QSize(16777215, 53))
        self.appearanceOptions.setStyleSheet(u"border:none;\n"
" background:rgba(0,0,0,0);")
        self.appearanceOptions.setFrameShape(QFrame.Shape.StyledPanel)
        self.appearanceOptions.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_7 = QHBoxLayout(self.appearanceOptions)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.app_auto = QPushButton(self.appearanceOptions)
        self.app_auto.setObjectName(u"app_auto")
        self.app_auto.setMinimumSize(QSize(80, 30))
        self.app_auto.setMaximumSize(QSize(80, 30))
        self.app_auto.setStyleSheet(u"QPushButton {\n"
"border:1px solid rgba(240,240,240, 255);\n"
"border-radius:8px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"background-color:rgba(255, 255, 255,50); \n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"background-color:rgba(255, 255, 255,80); \n"
"\n"
"}\n"
"\n"
"QPushButton:checked {\n"
"background-color: qlineargradient(spread:pad, x1:0, y1:0.0113636, x2:1, y2:1, stop:0 rgba(156, 12, 12, 255), stop:1 rgba(20, 39, 84, 255));\n"
"\n"
"}")
        self.app_auto.setCheckable(True)
        self.app_auto.setChecked(False)
        self.app_auto.setAutoExclusive(True)

        self.horizontalLayout_7.addWidget(self.app_auto)

        self.app_smart = QPushButton(self.appearanceOptions)
        self.app_smart.setObjectName(u"app_smart")
        self.app_smart.setMinimumSize(QSize(80, 30))
        self.app_smart.setMaximumSize(QSize(80, 30))
        self.app_smart.setStyleSheet(u"QPushButton {\n"
"border:1px solid rgba(240,240,240, 255);\n"
"border-radius:8px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"background-color:rgba(255, 255, 255,50); \n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"background-color:rgba(255, 255, 255,80); \n"
"\n"
"}\n"
"\n"
"QPushButton:checked {\n"
"background-color: qlineargradient(spread:pad, x1:0, y1:0.0113636, x2:1, y2:1, stop:0 rgba(156, 12, 12, 255), stop:1 rgba(20, 39, 84, 255));\n"
"\n"
"}")
        self.app_smart.setCheckable(True)
        self.app_smart.setChecked(False)
        self.app_smart.setAutoExclusive(True)

        self.horizontalLayout_7.addWidget(self.app_smart)

        self.app_amoled = QPushButton(self.appearanceOptions)
        self.app_amoled.setObjectName(u"app_amoled")
        self.app_amoled.setMinimumSize(QSize(80, 30))
        self.app_amoled.setMaximumSize(QSize(80, 30))
        self.app_amoled.setStyleSheet(u"QPushButton {\n"
"border:1px solid rgba(240,240,240, 255);\n"
"border-radius:8px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"background-color:rgba(255, 255, 255,50); \n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"background-color:rgba(255, 255, 255,80); \n"
"\n"
"}\n"
"\n"
"QPushButton:checked {\n"
"background-color: qlineargradient(spread:pad, x1:0, y1:0.0113636, x2:1, y2:1, stop:0 rgba(156, 12, 12, 255), stop:1 rgba(20, 39, 84, 255));\n"
"\n"
"}")
        self.app_amoled.setCheckable(True)
        self.app_amoled.setChecked(False)
        self.app_amoled.setAutoExclusive(True)

        self.horizontalLayout_7.addWidget(self.app_amoled)

        self.app_custom = QPushButton(self.appearanceOptions)
        self.app_custom.setObjectName(u"app_custom")
        self.app_custom.setMinimumSize(QSize(80, 30))
        self.app_custom.setMaximumSize(QSize(80, 30))
        self.app_custom.setStyleSheet(u"QPushButton {\n"
"border:1px solid rgba(240,240,240, 255);\n"
"border-radius:8px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"background-color:rgba(255, 255, 255,50); \n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"background-color:rgba(255, 255, 255,80); \n"
"\n"
"}\n"
"\n"
"QPushButton:checked {\n"
"background-color: qlineargradient(spread:pad, x1:0, y1:0.0113636, x2:1, y2:1, stop:0 rgba(156, 12, 12, 255), stop:1 rgba(20, 39, 84, 255));\n"
"\n"
"}")
        self.app_custom.setCheckable(True)
        self.app_custom.setChecked(False)
        self.app_custom.setAutoExclusive(True)

        self.horizontalLayout_7.addWidget(self.app_custom)

        self.BETAOPTION_blurmode = QFrame(self.appearanceOptions)
        self.BETAOPTION_blurmode.setObjectName(u"BETAOPTION_blurmode")
        self.BETAOPTION_blurmode.setMinimumSize(QSize(90, 35))
        self.BETAOPTION_blurmode.setMaximumSize(QSize(80, 30))
        self.BETAOPTION_blurmode.setStyleSheet(u"border:none;")
        self.BETAOPTION_blurmode.setFrameShape(QFrame.Shape.StyledPanel)
        self.BETAOPTION_blurmode.setFrameShadow(QFrame.Shadow.Raised)
        self.app_blurbeta = QPushButton(self.BETAOPTION_blurmode)
        self.app_blurbeta.setObjectName(u"app_blurbeta")
        self.app_blurbeta.setGeometry(QRect(0, 0, 80, 30))
        self.app_blurbeta.setMinimumSize(QSize(80, 30))
        self.app_blurbeta.setMaximumSize(QSize(80, 30))
        self.app_blurbeta.setStyleSheet(u"QPushButton {\n"
"border:1px solid rgba(240,240,240, 255);\n"
"border-radius:8px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"background-color:rgba(255, 255, 255,50); \n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"background-color:rgba(255, 255, 255,80); \n"
"\n"
"}\n"
"\n"
"QPushButton:checked {\n"
"background-color: qlineargradient(spread:pad, x1:0, y1:0.0113636, x2:1, y2:1, stop:0 rgba(156, 12, 12, 255), stop:1 rgba(20, 39, 84, 255));\n"
"\n"
"}")
        self.app_blurbeta.setCheckable(True)
        self.app_blurbeta.setAutoExclusive(True)
        self.betaLabel = QLabel(self.BETAOPTION_blurmode)
        self.betaLabel.setObjectName(u"betaLabel")
        self.betaLabel.setGeometry(QRect(60, 0, 31, 16))
        font11 = QFont()
        font11.setFamilies([u"Inter"])
        font11.setPointSize(7)
        self.betaLabel.setFont(font11)
        self.betaLabel.setStyleSheet(u"background-color: qlineargradient(spread:pad, x1:0, y1:0.0113636, x2:1, y2:1, stop:0 rgba(156, 12, 12, 255), stop:1 rgba(20, 39, 84, 255));\n"
"border:none;\n"
"padding:2px;\n"
"border-radius:8px;")
        self.betaLabel.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.horizontalLayout_7.addWidget(self.BETAOPTION_blurmode)


        self.verticalLayout_14.addWidget(self.appearanceOptions)

        self.appearanceMoreOptions = QFrame(self.appearanceFrame)
        self.appearanceMoreOptions.setObjectName(u"appearanceMoreOptions")
        self.appearanceMoreOptions.setMinimumSize(QSize(531, 191))
        self.appearanceMoreOptions.setStyleSheet(u"border:none;\n"
" background:rgba(0,0,0,0);")
        self.appearanceMoreOptions.setFrameShape(QFrame.Shape.StyledPanel)
        self.appearanceMoreOptions.setFrameShadow(QFrame.Shadow.Raised)
        self.gridLayout_24 = QGridLayout(self.appearanceMoreOptions)
        self.gridLayout_24.setSpacing(0)
        self.gridLayout_24.setObjectName(u"gridLayout_24")
        self.gridLayout_24.setContentsMargins(0, 0, 0, 0)
        self.apprOptionsViewframe = QStackedWidget(self.appearanceMoreOptions)
        self.apprOptionsViewframe.setObjectName(u"apprOptionsViewframe")
        self.autoMode = QWidget()
        self.autoMode.setObjectName(u"autoMode")
        self.app_auto_2 = QPushButton(self.autoMode)
        self.app_auto_2.setObjectName(u"app_auto_2")
        self.app_auto_2.setGeometry(QRect(20, 20, 80, 30))
        self.app_auto_2.setMinimumSize(QSize(80, 30))
        self.app_auto_2.setMaximumSize(QSize(80, 30))
        self.app_auto_2.setStyleSheet(u"QPushButton {\n"
"border:1px solid rgba(240,240,240, 255);\n"
"border-radius:8px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"background-color:rgba(255, 255, 255,50); \n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"background-color:rgba(255, 255, 255,80); \n"
"\n"
"}\n"
"\n"
"QPushButton:checked {\n"
"background-color: qlineargradient(spread:pad, x1:0, y1:0.0113636, x2:1, y2:1, stop:0 rgba(156, 12, 12, 255), stop:1 rgba(20, 39, 84, 255));\n"
"\n"
"}")
        self.app_auto_2.setCheckable(True)
        self.app_auto_2.setChecked(False)
        self.app_auto_3 = QPushButton(self.autoMode)
        self.app_auto_3.setObjectName(u"app_auto_3")
        self.app_auto_3.setGeometry(QRect(200, 20, 80, 30))
        self.app_auto_3.setMinimumSize(QSize(80, 30))
        self.app_auto_3.setMaximumSize(QSize(80, 30))
        self.app_auto_3.setStyleSheet(u"QPushButton {\n"
"border:1px solid rgba(240,240,240, 255);\n"
"border-radius:8px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"background-color:rgba(255, 255, 255,50); \n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"background-color:rgba(255, 255, 255,80); \n"
"\n"
"}\n"
"\n"
"QPushButton:checked {\n"
"background-color: qlineargradient(spread:pad, x1:0, y1:0.0113636, x2:1, y2:1, stop:0 rgba(156, 12, 12, 255), stop:1 rgba(20, 39, 84, 255));\n"
"\n"
"}")
        self.app_auto_3.setCheckable(True)
        self.app_auto_3.setChecked(False)
        self.app_auto_4 = QPushButton(self.autoMode)
        self.app_auto_4.setObjectName(u"app_auto_4")
        self.app_auto_4.setGeometry(QRect(110, 20, 80, 30))
        self.app_auto_4.setMinimumSize(QSize(80, 30))
        self.app_auto_4.setMaximumSize(QSize(80, 30))
        self.app_auto_4.setStyleSheet(u"QPushButton {\n"
"border:1px solid rgba(240,240,240, 255);\n"
"border-radius:8px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"background-color:rgba(255, 255, 255,50); \n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"background-color:rgba(255, 255, 255,80); \n"
"\n"
"}\n"
"\n"
"QPushButton:checked {\n"
"background-color: qlineargradient(spread:pad, x1:0, y1:0.0113636, x2:1, y2:1, stop:0 rgba(156, 12, 12, 255), stop:1 rgba(20, 39, 84, 255));\n"
"\n"
"}")
        self.app_auto_4.setCheckable(True)
        self.app_auto_4.setChecked(False)
        self.apprOptionsViewframe.addWidget(self.autoMode)
        self.smartMode = QWidget()
        self.smartMode.setObjectName(u"smartMode")
        self.apprOptionsViewframe.addWidget(self.smartMode)
        self.betablurMode = QWidget()
        self.betablurMode.setObjectName(u"betablurMode")
        self.apprOptionsViewframe.addWidget(self.betablurMode)
        self.customMode = QWidget()
        self.customMode.setObjectName(u"customMode")
        self.apprOptionsViewframe.addWidget(self.customMode)

        self.gridLayout_24.addWidget(self.apprOptionsViewframe, 0, 0, 1, 1)


        self.verticalLayout_14.addWidget(self.appearanceMoreOptions)

        self.appearanceFooter = QFrame(self.appearanceFrame)
        self.appearanceFooter.setObjectName(u"appearanceFooter")
        self.appearanceFooter.setMinimumSize(QSize(0, 40))
        self.appearanceFooter.setMaximumSize(QSize(16777215, 60))
        self.appearanceFooter.setStyleSheet(u"border:none;\n"
" background:rgba(0,0,0,0);")
        self.appearanceFooter.setFrameShape(QFrame.Shape.StyledPanel)
        self.appearanceFooter.setFrameShadow(QFrame.Shadow.Raised)
        self.gridLayout_22 = QGridLayout(self.appearanceFooter)
        self.gridLayout_22.setObjectName(u"gridLayout_22")
        self.appearanceInfoIcon = QLabel(self.appearanceFooter)
        self.appearanceInfoIcon.setObjectName(u"appearanceInfoIcon")
        self.appearanceInfoIcon.setMinimumSize(QSize(16, 16))
        self.appearanceInfoIcon.setMaximumSize(QSize(16, 16))
        self.appearanceInfoIcon.setPixmap(QPixmap(u"../../../../Downloads/icons8-info-48 (2).png"))
        self.appearanceInfoIcon.setScaledContents(True)
        self.appearanceInfoIcon.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout_22.addWidget(self.appearanceInfoIcon, 0, 0, 1, 1)

        self.appearanceContext = QLabel(self.appearanceFooter)
        self.appearanceContext.setObjectName(u"appearanceContext")
        self.appearanceContext.setFont(font11)
        self.appearanceContext.setStyleSheet(u"background-color:rgba(0,0,0,0); color:rgba(255,255,255,100);")
        self.appearanceContext.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignTop)
        self.appearanceContext.setWordWrap(True)

        self.gridLayout_22.addWidget(self.appearanceContext, 0, 1, 1, 1)


        self.verticalLayout_14.addWidget(self.appearanceFooter)

        self.settingsScrollArea.setWidget(self.scrollAreaWidgetContents_2)

        self.verticalLayout_12.addWidget(self.settingsScrollArea)


        self.gridLayout_4.addWidget(self.settingsFrame, 1, 0, 1, 1)

        self.viewFrame.addWidget(self.settingsPage)

        self.gridLayout_3.addWidget(self.viewFrame, 0, 0, 1, 1)


        self.gridLayout_2.addWidget(self.BodyFrame, 1, 1, 1, 1)

        self.SideFrame = QFrame(self.MainFrame)
        self.SideFrame.setObjectName(u"SideFrame")
        self.SideFrame.setMaximumSize(QSize(85, 16777215))
        self.SideFrame.setStyleSheet(u"/**background-color: rgba(0,0,0, 100);**/\n"
"background-color: transparent;\n"
"margin:4px 0px 4px 4px;\n"
"border-radius:10px;")
        self.SideFrame.setFrameShape(QFrame.Shape.StyledPanel)
        self.SideFrame.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_8 = QVBoxLayout(self.SideFrame)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.homeBtnFrame = QFrame(self.SideFrame)
        self.homeBtnFrame.setObjectName(u"homeBtnFrame")
        self.homeBtnFrame.setStyleSheet(u"margin:0px; border-radius:10px; background-color:transparent;")
        self.homeBtnFrame.setFrameShape(QFrame.Shape.StyledPanel)
        self.homeBtnFrame.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_4 = QVBoxLayout(self.homeBtnFrame)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(8, 8, 8, 8)
        self.homeBtn = QPushButton(self.homeBtnFrame)
        self.homeBtn.setObjectName(u"homeBtn")
        self.homeBtn.setMinimumSize(QSize(40, 40))
        self.homeBtn.setMaximumSize(QSize(40, 40))
        self.homeBtn.setStyleSheet(u"QPushButton {\n"
"border-radius:20px;\n"
"background-color:rgba(0,0,0,50);\n"
"border:none;\n"
"}\n"
"\n"
"QPushButton::hover {\n"
"border-radius:20px;\n"
"background-color:rgba(255,255,255, 50);\n"
"border:none;\n"
"}\n"
"\n"
"QPushButton::pressed {\n"
"border-radius:20px;\n"
"background-color:rgba(255,255,255, 30);\n"
"border:none;\n"
"}\n"
"")
        icon11 = QIcon()
        icon11.addFile(u"../../../../Downloads/icons8-home-48.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.homeBtn.setIcon(icon11)
        self.homeBtn.setIconSize(QSize(34, 34))

        self.verticalLayout_4.addWidget(self.homeBtn)

        self.home_label = QLabel(self.homeBtnFrame)
        self.home_label.setObjectName(u"home_label")
        font12 = QFont()
        font12.setFamilies([u"Inter 18pt"])
        font12.setPointSize(8)
        self.home_label.setFont(font12)
        self.home_label.setStyleSheet(u"background-color:rgba(0,0,0,0); color:rgba(255,255,255,150);")
        self.home_label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_4.addWidget(self.home_label)


        self.verticalLayout_8.addWidget(self.homeBtnFrame)

        self.exploreBtnFrame = QFrame(self.SideFrame)
        self.exploreBtnFrame.setObjectName(u"exploreBtnFrame")
        self.exploreBtnFrame.setStyleSheet(u"margin:0px; border-radius:10px; background-color:transparent;")
        self.exploreBtnFrame.setFrameShape(QFrame.Shape.StyledPanel)
        self.exploreBtnFrame.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_5 = QVBoxLayout(self.exploreBtnFrame)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_5.setContentsMargins(8, 8, 8, 8)
        self.exploreBtn = QPushButton(self.exploreBtnFrame)
        self.exploreBtn.setObjectName(u"exploreBtn")
        self.exploreBtn.setMinimumSize(QSize(40, 40))
        self.exploreBtn.setMaximumSize(QSize(40, 40))
        self.exploreBtn.setStyleSheet(u"QPushButton {\n"
"border-radius:20px;\n"
"background-color:rgba(0,0,0,50);\n"
"border:none;\n"
"}\n"
"\n"
"QPushButton::hover {\n"
"border-radius:20px;\n"
"background-color:rgba(255,255,255, 50);\n"
"border:none;\n"
"}\n"
"\n"
"QPushButton::pressed {\n"
"border-radius:20px;\n"
"background-color:rgba(255,255,255, 30);\n"
"border:none;\n"
"}\n"
"")
        icon12 = QIcon()
        icon12.addFile(u"../../../../Downloads/icons8-compass-48.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.exploreBtn.setIcon(icon12)
        self.exploreBtn.setIconSize(QSize(34, 34))

        self.verticalLayout_5.addWidget(self.exploreBtn)

        self.explore_label = QLabel(self.exploreBtnFrame)
        self.explore_label.setObjectName(u"explore_label")
        self.explore_label.setFont(font12)
        self.explore_label.setStyleSheet(u"background-color:rgba(0,0,0,0); color:rgba(255,255,255,150);")
        self.explore_label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_5.addWidget(self.explore_label)


        self.verticalLayout_8.addWidget(self.exploreBtnFrame)

        self.libraryBtnFrame = QFrame(self.SideFrame)
        self.libraryBtnFrame.setObjectName(u"libraryBtnFrame")
        self.libraryBtnFrame.setStyleSheet(u"margin:0px; border-radius:10px;\n"
"background-color:transparent;")
        self.libraryBtnFrame.setFrameShape(QFrame.Shape.StyledPanel)
        self.libraryBtnFrame.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_6 = QVBoxLayout(self.libraryBtnFrame)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.verticalLayout_6.setContentsMargins(8, 8, 8, 8)
        self.libraryBtn = QPushButton(self.libraryBtnFrame)
        self.libraryBtn.setObjectName(u"libraryBtn")
        self.libraryBtn.setMinimumSize(QSize(40, 40))
        self.libraryBtn.setMaximumSize(QSize(40, 40))
        self.libraryBtn.setStyleSheet(u"QPushButton {\n"
"border-radius:20px;\n"
"background-color:rgba(0,0,0,50);\n"
"border:none;\n"
"}\n"
"\n"
"QPushButton::hover {\n"
"border-radius:20px;\n"
"background-color:rgba(255,255,255, 50);\n"
"border:none;\n"
"}\n"
"\n"
"QPushButton::pressed {\n"
"border-radius:20px;\n"
"background-color:rgba(255,255,255, 30);\n"
"border:none;\n"
"}\n"
"")
        icon13 = QIcon()
        icon13.addFile(u"../../../../Downloads/icons8-music-library-48.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.libraryBtn.setIcon(icon13)
        self.libraryBtn.setIconSize(QSize(34, 34))

        self.verticalLayout_6.addWidget(self.libraryBtn)

        self.library_label = QLabel(self.libraryBtnFrame)
        self.library_label.setObjectName(u"library_label")
        self.library_label.setFont(font12)
        self.library_label.setStyleSheet(u"background-color:rgba(0,0,0,0); color:rgba(255,255,255,150);")
        self.library_label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_6.addWidget(self.library_label)


        self.verticalLayout_8.addWidget(self.libraryBtnFrame)

        self.settingsBtnFrame = QFrame(self.SideFrame)
        self.settingsBtnFrame.setObjectName(u"settingsBtnFrame")
        self.settingsBtnFrame.setStyleSheet(u"margin:0px; border-radius:10px;\n"
"background-color:transparent;")
        self.settingsBtnFrame.setFrameShape(QFrame.Shape.StyledPanel)
        self.settingsBtnFrame.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_7 = QVBoxLayout(self.settingsBtnFrame)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.verticalLayout_7.setContentsMargins(8, 8, 8, 8)
        self.settingsBtn = QPushButton(self.settingsBtnFrame)
        self.settingsBtn.setObjectName(u"settingsBtn")
        self.settingsBtn.setMinimumSize(QSize(40, 40))
        self.settingsBtn.setMaximumSize(QSize(40, 40))
        self.settingsBtn.setStyleSheet(u"QPushButton {\n"
"border-radius:20px;\n"
"background-color:rgba(0,0,0,50);\n"
"border:none;\n"
"}\n"
"\n"
"QPushButton::hover {\n"
"border-radius:20px;\n"
"background-color:rgba(255,255,255, 50);\n"
"border:none;\n"
"}\n"
"\n"
"QPushButton::pressed {\n"
"border-radius:20px;\n"
"background-color:rgba(255,255,255, 30);\n"
"border:none;\n"
"}\n"
"")
        icon14 = QIcon()
        icon14.addFile(u"../../../../Downloads/icons8-settings-48.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.settingsBtn.setIcon(icon14)
        self.settingsBtn.setIconSize(QSize(34, 34))

        self.verticalLayout_7.addWidget(self.settingsBtn)

        self.settings_label = QLabel(self.settingsBtnFrame)
        self.settings_label.setObjectName(u"settings_label")
        self.settings_label.setFont(font12)
        self.settings_label.setStyleSheet(u"background-color:rgba(0,0,0,0); color:rgba(255,255,255,150);")
        self.settings_label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_7.addWidget(self.settings_label)


        self.verticalLayout_8.addWidget(self.settingsBtnFrame)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_8.addItem(self.verticalSpacer)


        self.gridLayout_2.addWidget(self.SideFrame, 1, 0, 1, 1)


        self.verticalLayout.addWidget(self.MainFrame)

        self.PlayerFrame = QFrame(self.Window)
        self.PlayerFrame.setObjectName(u"PlayerFrame")
        self.PlayerFrame.setMaximumSize(QSize(16777215, 100))
        self.PlayerFrame.setStyleSheet(u"border-radius:0px;\n"
"border-bottom-right-radius:16px;\n"
"border-bottom-left-radius:16px;\n"
"background-color:rgba(0,0,0,50);")
        self.PlayerFrame.setFrameShape(QFrame.Shape.StyledPanel)
        self.PlayerFrame.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.PlayerFrame)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.frame_9 = QFrame(self.PlayerFrame)
        self.frame_9.setObjectName(u"frame_9")
        self.frame_9.setStyleSheet(u"border:none;\n"
"background-color: transparent;")
        self.frame_9.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_9.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_5 = QHBoxLayout(self.frame_9)
        self.horizontalLayout_5.setSpacing(6)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout_5.setContentsMargins(9, 6, 9, 0)
        self.progress = QSlider(self.frame_9)
        self.progress.setObjectName(u"progress")
        self.progress.setMaximumSize(QSize(16777215, 8))
        self.progress.setSizeIncrement(QSize(0, 8))
        self.progress.setStyleSheet(u"QSlider::groove:horizontal {\n"
"    height: 6px;\n"
"	background-color: rgba(0,0,0, 100);\n"
"    border-radius: 3px;\n"
"}\n"
"\n"
"QSlider::handle:horizontal {\n"
"    background: #FFFFFF;\n"
"    width: 10px;\n"
"    height: 4px;\n"
"    border-radius: 2px;\n"
"\n"
"}\n"
"QSlider::handle:horizontal:hover{\n"
"    background: rgb(245,245,245);\n"
"    width: 10px;\n"
"    height: 4px;\n"
"	border-radius:2px;\n"
"}\n"
"\n"
"QSlider::sub-page:horizontal {\n"
"    background: #FFFFFF;\n"
"    border: 1px solid rgba(0,0,0, 10);\n"
"    height: 10px;\n"
"    border-radius: 2px;\n"
"}\n"
"QSlider::add-page:horizontal {\n"
"	background-color: rgba(0,0,0, 25);\n"
"    border: 1px solid rgba(0,0,0, 10);\n"
"    height: 10px;\n"
"    border-radius: 2px;\n"
"}\n"
"")
        self.progress.setPageStep(0)
        self.progress.setOrientation(Qt.Orientation.Horizontal)

        self.horizontalLayout_5.addWidget(self.progress)


        self.verticalLayout_2.addWidget(self.frame_9)

        self.frame_10 = QFrame(self.PlayerFrame)
        self.frame_10.setObjectName(u"frame_10")
        self.frame_10.setStyleSheet(u"border:none;\n"
"background-color: transparent;")
        self.frame_10.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_10.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.frame_10)
        self.horizontalLayout_3.setSpacing(0)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(9, 2, 9, 2)
        self.MediaInfo = QFrame(self.frame_10)
        self.MediaInfo.setObjectName(u"MediaInfo")
        self.MediaInfo.setMinimumSize(QSize(240, 72))
        self.MediaInfo.setMaximumSize(QSize(16777215, 16777215))
        self.MediaInfo.setFrameShape(QFrame.Shape.StyledPanel)
        self.MediaInfo.setFrameShadow(QFrame.Shadow.Raised)
        self.gridLayout_18 = QGridLayout(self.MediaInfo)
        self.gridLayout_18.setObjectName(u"gridLayout_18")
        self.gridLayout_18.setHorizontalSpacing(5)
        self.gridLayout_18.setVerticalSpacing(0)
        self.gridLayout_18.setContentsMargins(5, 0, 9, 0)
        self.likeBtn = QPushButton(self.MediaInfo)
        self.likeBtn.setObjectName(u"likeBtn")
        self.likeBtn.setMinimumSize(QSize(38, 38))
        self.likeBtn.setMaximumSize(QSize(38, 38))
        self.likeBtn.setStyleSheet(u"QPushButton {\n"
"background-color:rgba(0,0,0,0); \n"
"color:white;\n"
"border-radius:19px;\n"
"padding:0px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"background-color:rgba(255, 255, 255,30); \n"
"color:white;\n"
"border-radius:19px;\n"
"padding:0px;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"background-color:rgba(255, 255, 255,50); \n"
"color:white;\n"
"border-radius:19px;\n"
"padding:0px;\n"
"}")
        icon15 = QIcon()
        icon15.addFile(u"../../../../Downloads/icons8-like-48.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.likeBtn.setIcon(icon15)
        self.likeBtn.setIconSize(QSize(26, 26))

        self.gridLayout_18.addWidget(self.likeBtn, 0, 2, 1, 1)

        self.cover_art = QLabel(self.MediaInfo)
        self.cover_art.setObjectName(u"cover_art")
        self.cover_art.setMinimumSize(QSize(50, 50))
        self.cover_art.setMaximumSize(QSize(50, 50))
        self.cover_art.setStyleSheet(u" border-radius:10px;")

        self.gridLayout_18.addWidget(self.cover_art, 0, 0, 1, 1)

        self.MediaInfo_frame = QFrame(self.MediaInfo)
        self.MediaInfo_frame.setObjectName(u"MediaInfo_frame")
        self.MediaInfo_frame.setMinimumSize(QSize(70, 0))
        self.MediaInfo_frame.setFrameShape(QFrame.Shape.StyledPanel)
        self.MediaInfo_frame.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.MediaInfo_frame)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_3.addItem(self.verticalSpacer_2)

        self.title = QLabel(self.MediaInfo_frame)
        self.title.setObjectName(u"title")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.title.sizePolicy().hasHeightForWidth())
        self.title.setSizePolicy(sizePolicy)
        self.title.setMinimumSize(QSize(70, 18))
        self.title.setMaximumSize(QSize(16777215, 18))
        font13 = QFont()
        font13.setFamilies([u"Inter 18pt"])
        font13.setPointSize(10)
        font13.setBold(False)
        self.title.setFont(font13)
        self.title.setStyleSheet(u"")
        self.title.setTextFormat(Qt.TextFormat.RichText)
        self.title.setScaledContents(True)
        self.title.setWordWrap(True)
        self.title.setIndent(0)

        self.verticalLayout_3.addWidget(self.title)

        self.artist = QLabel(self.MediaInfo_frame)
        self.artist.setObjectName(u"artist")
        self.artist.setMinimumSize(QSize(100, 18))
        self.artist.setMaximumSize(QSize(16777215, 26))
        font14 = QFont()
        font14.setFamilies([u"Inter 18pt"])
        font14.setPointSize(9)
        self.artist.setFont(font14)
        self.artist.setStyleSheet(u"color:rgba(255,255,255,200);")

        self.verticalLayout_3.addWidget(self.artist)

        self.verticalSpacer_7 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_3.addItem(self.verticalSpacer_7)


        self.gridLayout_18.addWidget(self.MediaInfo_frame, 0, 1, 1, 1)


        self.horizontalLayout_3.addWidget(self.MediaInfo)

        self.horizontalSpacer = QSpacerItem(170, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer)

        self.frame_7 = QFrame(self.frame_10)
        self.frame_7.setObjectName(u"frame_7")
        self.frame_7.setMaximumSize(QSize(240, 16777215))
        self.frame_7.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_7.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout = QHBoxLayout(self.frame_7)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.shuffleBtn = QPushButton(self.frame_7)
        self.shuffleBtn.setObjectName(u"shuffleBtn")
        self.shuffleBtn.setMinimumSize(QSize(34, 34))
        self.shuffleBtn.setMaximumSize(QSize(34, 34))
        self.shuffleBtn.setStyleSheet(u"QPushButton {\n"
"background-color:rgba(0,0,0,0); \n"
"color:white;\n"
"border-radius:17px;\n"
"padding:0px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"background-color:rgba(255, 255, 255,30); \n"
"color:white;\n"
"border-radius:17px;\n"
"padding:0px;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"background-color:rgba(255, 255, 255,50); \n"
"color:white;\n"
"border-radius:17px;\n"
"padding:0px;\n"
"}")
        icon16 = QIcon()
        icon16.addFile(u"../../../../Downloads/icons8-shuffle-48.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.shuffleBtn.setIcon(icon16)
        self.shuffleBtn.setIconSize(QSize(26, 26))

        self.horizontalLayout.addWidget(self.shuffleBtn)

        self.prevBtn = QPushButton(self.frame_7)
        self.prevBtn.setObjectName(u"prevBtn")
        self.prevBtn.setMinimumSize(QSize(38, 38))
        self.prevBtn.setMaximumSize(QSize(38, 38))
        self.prevBtn.setStyleSheet(u"QPushButton {\n"
"background-color:rgba(0,0,0,0); \n"
"color:white;\n"
"border-radius:19px;\n"
"padding:0px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"background-color:rgba(255, 255, 255,30); \n"
"color:white;\n"
"border-radius:19px;\n"
"padding:0px;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"background-color:rgba(255, 255, 255,50); \n"
"color:white;\n"
"border-radius:19px;\n"
"padding:0px;\n"
"}")
        icon17 = QIcon()
        icon17.addFile(u"../../../../Downloads/icons8-skip-to-start-48.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.prevBtn.setIcon(icon17)
        self.prevBtn.setIconSize(QSize(24, 24))

        self.horizontalLayout.addWidget(self.prevBtn)

        self.playBtn = QPushButton(self.frame_7)
        self.playBtn.setObjectName(u"playBtn")
        self.playBtn.setMinimumSize(QSize(40, 38))
        self.playBtn.setMaximumSize(QSize(40, 38))
        self.playBtn.setStyleSheet(u"QPushButton {\n"
"background-color:rgba(0,0,0,0); \n"
"color:white;\n"
"border-radius:10px;\n"
"padding:0px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"background-color:rgba(255, 255, 255,30); \n"
"color:white;\n"
"border-radius:10px;\n"
"padding:0px;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"background-color:rgba(255, 255, 255,50); \n"
"color:white;\n"
"border-radius:19px;\n"
"padding:0px;\n"
"}")
        icon18 = QIcon()
        icon18.addFile(u"../../../../Downloads/icons8-pause-48.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.playBtn.setIcon(icon18)
        self.playBtn.setIconSize(QSize(42, 42))

        self.horizontalLayout.addWidget(self.playBtn)

        self.nextBtn = QPushButton(self.frame_7)
        self.nextBtn.setObjectName(u"nextBtn")
        self.nextBtn.setMinimumSize(QSize(38, 38))
        self.nextBtn.setMaximumSize(QSize(38, 38))
        self.nextBtn.setStyleSheet(u"QPushButton {\n"
"background-color:rgba(0,0,0,0); \n"
"color:white;\n"
"border-radius:19px;\n"
"padding:0px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"background-color:rgba(255, 255, 255,30); \n"
"color:white;\n"
"border-radius:19px;\n"
"padding:0px;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"background-color:rgba(255, 255, 255,50); \n"
"color:white;\n"
"border-radius:19px;\n"
"padding:0px;\n"
"}")
        icon19 = QIcon()
        icon19.addFile(u"../../../../Downloads/icons8-end-48.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.nextBtn.setIcon(icon19)
        self.nextBtn.setIconSize(QSize(24, 24))

        self.horizontalLayout.addWidget(self.nextBtn)

        self.repeatBtn = QPushButton(self.frame_7)
        self.repeatBtn.setObjectName(u"repeatBtn")
        self.repeatBtn.setMinimumSize(QSize(34, 34))
        self.repeatBtn.setMaximumSize(QSize(34, 34))
        self.repeatBtn.setStyleSheet(u"QPushButton {\n"
"background-color:rgba(0,0,0,0); \n"
"color:white;\n"
"border-radius:17px;\n"
"padding:0px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"background-color:rgba(255, 255, 255,30); \n"
"color:white;\n"
"border-radius:17px;\n"
"padding:0px;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"background-color:rgba(255, 255, 255,50); \n"
"color:white;\n"
"border-radius:17px;\n"
"padding:0px;\n"
"}")
        icon20 = QIcon()
        icon20.addFile(u"../../../../Downloads/icons8-repeat-48.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.repeatBtn.setIcon(icon20)
        self.repeatBtn.setIconSize(QSize(26, 26))

        self.horizontalLayout.addWidget(self.repeatBtn)


        self.horizontalLayout_3.addWidget(self.frame_7)

        self.horizontalSpacer_2 = QSpacerItem(170, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer_2)

        self.frame_8 = QFrame(self.frame_10)
        self.frame_8.setObjectName(u"frame_8")
        self.frame_8.setMinimumSize(QSize(240, 0))
        self.frame_8.setMaximumSize(QSize(240, 16777215))
        self.frame_8.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_8.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.frame_8)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer_3)

        self.volumeBtn = QPushButton(self.frame_8)
        self.volumeBtn.setObjectName(u"volumeBtn")
        self.volumeBtn.setMinimumSize(QSize(38, 38))
        self.volumeBtn.setMaximumSize(QSize(38, 38))
        self.volumeBtn.setStyleSheet(u"QPushButton {\n"
"background-color:rgba(0,0,0,0); \n"
"color:white;\n"
"border-radius:19px;\n"
"padding:0px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"background-color:rgba(255, 255, 255,30); \n"
"color:white;\n"
"border-radius:19px;\n"
"padding:0px;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"background-color:rgba(255, 255, 255,50); \n"
"color:white;\n"
"border-radius:19px;\n"
"padding:0px;\n"
"}")
        icon21 = QIcon()
        icon21.addFile(u"../../../../Downloads/icons8-audio-48.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.volumeBtn.setIcon(icon21)
        self.volumeBtn.setIconSize(QSize(24, 24))

        self.horizontalLayout_2.addWidget(self.volumeBtn)

        self.end_time = QLabel(self.frame_8)
        self.end_time.setObjectName(u"end_time")
        font15 = QFont()
        font15.setFamilies([u"Inter 18pt Light"])
        font15.setPointSize(8)
        self.end_time.setFont(font15)
        self.end_time.setStyleSheet(u"background-color:rgba(0,0,0,0); ")

        self.horizontalLayout_2.addWidget(self.end_time)


        self.horizontalLayout_3.addWidget(self.frame_8)


        self.verticalLayout_2.addWidget(self.frame_10)

        self.resizebtn_frame = QFrame(self.PlayerFrame)
        self.resizebtn_frame.setObjectName(u"resizebtn_frame")
        self.resizebtn_frame.setMinimumSize(QSize(0, 20))
        self.resizebtn_frame.setMaximumSize(QSize(16777215, 20))
        self.resizebtn_frame.setStyleSheet(u"background-color:rgba(0,0,0,0); border:none;")
        self.resizebtn_frame.setFrameShape(QFrame.Shape.StyledPanel)
        self.resizebtn_frame.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_8 = QHBoxLayout(self.resizebtn_frame)
        self.horizontalLayout_8.setSpacing(0)
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.horizontalLayout_8.setContentsMargins(0, 0, 0, 4)
        self.horizontalSpacer_13 = QSpacerItem(731, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_8.addItem(self.horizontalSpacer_13)

        self.resizebtn = QPushButton(self.resizebtn_frame)
        self.resizebtn.setObjectName(u"resizebtn")
        self.resizebtn.setMinimumSize(QSize(20, 20))
        self.resizebtn.setMaximumSize(QSize(20, 20))
        self.resizebtn.setStyleSheet(u"QPushButton {\n"
"border-radius:10px;\n"
"background-color:rgba(0,0,0,10);\n"
"border:none;\n"
"}\n"
"\n"
"QPushButton::hover {\n"
"border-radius:10px;\n"
"background-color:rgba(255,255,255, 50);\n"
"border:none;\n"
"}\n"
"\n"
"QPushButton::pressed {\n"
"border-radius:10px;\n"
"background-color:rgba(255,255,255, 30);\n"
"border:none;\n"
"}\n"
"")
        icon22 = QIcon()
        icon22.addFile(u"../../Downloads/resize-handle-svgrepo-com.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.resizebtn.setIcon(icon22)

        self.horizontalLayout_8.addWidget(self.resizebtn)


        self.verticalLayout_2.addWidget(self.resizebtn_frame)


        self.verticalLayout.addWidget(self.PlayerFrame)


        self.gridLayout.addWidget(self.Window, 0, 0, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget)
#if QT_CONFIG(shortcut)
#endif // QT_CONFIG(shortcut)

        self.retranslateUi(MainWindow)

        self.viewFrame.setCurrentIndex(3)
        self.apprOptionsViewframe.setCurrentIndex(2)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.menuBtn.setText("")
        self.search.setText("")
        self.searchBox.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Search for your favourite music ...", None))
        self.profileBtn.setText("")
        self.minimizeBtn.setText("")
        self.maximiseBtn.setText("")
        self.closeBtn.setText("")
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"Your Favorites", None))
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"It's all empty around here..", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Recently Played", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"It's all empty around here..", None))
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"Your Offline Queue", None))
        self.playBtn_queue.setText("")
        self.newQueue.setText("")
        self.addToQueue.setText("")
        self.removeFromQueue.setText("")
        self.label_9.setText(QCoreApplication.translate("MainWindow", u"It's all empty around here..", None))
        self.loadQueue.setText(QCoreApplication.translate("MainWindow", u"Load a queue?", None))
        self.topResultCoverart.setText("")
        self.topResult_title.setText(QCoreApplication.translate("MainWindow", u"The Hills", None))
        self.topResult_artist.setText(QCoreApplication.translate("MainWindow", u"The weeknd ", None))
        self.playTopResult.setText("")
        self.searchHeading_2.setText(QCoreApplication.translate("MainWindow", u"Top Result", None))
        self.searchHeading_3.setText(QCoreApplication.translate("MainWindow", u"Songs", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Library", None))
        self.settingsHeading.setText(QCoreApplication.translate("MainWindow", u"Settings", None))
        self.appearanceHead.setText(QCoreApplication.translate("MainWindow", u"Appearance", None))
        self.label_12.setText(QCoreApplication.translate("MainWindow", u"In-built Presets", None))
        self.app_auto.setText(QCoreApplication.translate("MainWindow", u"Legacy", None))
        self.app_smart.setText(QCoreApplication.translate("MainWindow", u"Smart", None))
        self.app_amoled.setText(QCoreApplication.translate("MainWindow", u"Amoled", None))
        self.app_custom.setText(QCoreApplication.translate("MainWindow", u"Custom", None))
        self.app_blurbeta.setText(QCoreApplication.translate("MainWindow", u"Blur", None))
        self.betaLabel.setText(QCoreApplication.translate("MainWindow", u"BETA", None))
        self.app_auto_2.setText(QCoreApplication.translate("MainWindow", u"Auto", None))
        self.app_auto_3.setText(QCoreApplication.translate("MainWindow", u"Dark", None))
        self.app_auto_4.setText(QCoreApplication.translate("MainWindow", u"Light", None))
        self.appearanceInfoIcon.setText("")
        self.appearanceContext.setText(QCoreApplication.translate("MainWindow", u"Auto : Automatically sets light/dark theme based on system settings.", None))
        self.homeBtn.setText("")
        self.home_label.setText(QCoreApplication.translate("MainWindow", u"Home", None))
        self.exploreBtn.setText("")
        self.explore_label.setText(QCoreApplication.translate("MainWindow", u"Explore", None))
        self.libraryBtn.setText("")
        self.library_label.setText(QCoreApplication.translate("MainWindow", u"Library", None))
        self.settingsBtn.setText("")
        self.settings_label.setText(QCoreApplication.translate("MainWindow", u"Settings", None))
        self.likeBtn.setText("")
        self.cover_art.setText("")
        self.title.setText(QCoreApplication.translate("MainWindow", u"Nothing playing", None))
        self.artist.setText("")
        self.shuffleBtn.setText("")
        self.prevBtn.setText("")
        self.playBtn.setText("")
        self.nextBtn.setText("")
        self.repeatBtn.setText("")
        self.volumeBtn.setText("")
        self.end_time.setText(QCoreApplication.translate("MainWindow", u"00:00/00:00", None))
        self.resizebtn.setText("")
    # retranslateUi

