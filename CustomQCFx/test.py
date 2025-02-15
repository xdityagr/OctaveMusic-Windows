from PySide6.QtCore import *
from PySide6.QtGui import *
from PySide6.QtWidgets import *
import sys
import pyautogui
from PIL import Image, ImageFilter, ImageQt, ImageDraw
from ui_testWindow import Ui_MainWindow
from QCFx import QCFxInitializer, QCFx_Blur
# from test2 import QCFx, QCFx_Blur
import threading
import win32gui
import time



class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        def moveWindow(event):
            if event.buttons() == Qt.LeftButton:
                self.move(self.pos() + event.globalPos() - self.dragPos)
                self.dragPos = event.globalPos()
                event.accept()

        self.qcfx = QCFxInitializer()
        self.blur = QCFx_Blur(self, mode=self.qcfx.MODE_WINDOW_S)
        self.ui.body.setStyleSheet('background-color:rgba(0,0,0,0);')
        self.ui.overlay.setStyleSheet('background-color:rgba(0,0,0,0);')
        # self.qcfx.regenerateSettings()

        self.ui.body.mouseMoveEvent = moveWindow
        self.ui.closeBtn.clicked.connect(self.close)
        self.ui.updateBtn.clicked.connect(self.bleh)

        self.show()

    def bleh(self):
        # self.qcfx.applySetting('recursiveFixedUpdate', True)
        # self.blur.Reload()
        pass
    def mousePressEvent(self, event):
        self.dragPos = event.globalPos()
        

app = QApplication(sys.argv)
window = MainWindow()
sys.exit(app.exec_())
