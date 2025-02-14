"""
Octave Music [Development] [v1.0.X BETA] : Main Source File
This source code is strictly confidential.
© Aditya Gaur, 2024-2025. All rights reserved.
"""

# Imports.GUI-libs
from PySide6.QtCore import *
from PySide6.QtGui import *
from PySide6.QtWidgets import *
from PySide6.QtWidgets import QDialog
from PySide6.QtCore import Signal
from PySide6 import QtCore, QtGui, QtWidgets

# Imports.System-libs
import os, sys
import multiprocessing
from datetime import datetime
from pathlib import Path

# Imports.OctaveInterfaces-libs
from OctaveInterfaces.InterfaceClasses.ui_musicItem import Ui_musicItem
# from ui_octaveMusicPlayer import Ui_MainWindow
# from OctaveInterfaces.InterfaceClasses.ui_octaveMusic_v2 import Ui_MainWindow
# from OctaveInterfaces.InterfaceClasses.ui_octaveMusicSearchItem import Ui_searchItem

# [Imports] New added
from OctaveInterfaces.InterfaceClasses.ui_octaveMusicV4 import Ui_MainWindow
from OctaveInterfaces.InterfaceClasses.ui_octaveMusicSearchItem_changeone import Ui_searchItem
# from OctaveInterfaces.InterfaceClasses.ui_octaveMusic_v2_changeone import Ui_MainWindow
# from ui_octaveMusic_v2 import Ui_MainWindow

# [Imports] Octave Engine definitions, fetcher, etc
from OctaveEngine import MediaControls
from OctaveEngine.definitions import *
from OctaveEngine.definitions import *
from OctaveEngine.octaveFetch import *
from OctaveEngine.AdvancedMediaControls import *

# [Imports] Others
from CustomQCFx import QCFx_Blur, QCFxInitializer
import asyncio
import threading, time
from enum import Enum, auto
import cProfile


# OBJDEF Setting.ThemePreset (Theme preset class to define themes.)
class ThemePreset:
    def __init__(self):
        self.master_scheme = { 
                        'name':'amoled',
                        'icons': 
                            {'color': 'blue'},
                        'background': 
                            {
                            'primary-background-color':'rgba(0,0,0,245)',
                            'secondary-background-color':'rgba(0,0,0,255)',
                            'primary-foreground-color':'rgba(255,255,255,255)',
                            'secondary-foreground-color':'rgba(0,0,0,180)',
                            'background-path':None
                            },
                        }
        
        self.amoled_preset_values = ('amoled', {'color':'light'}, 
                            {
                            'primary-background-color':'rgba(0,0,0,255)',
                            'secondary-background-color':'rgba(0,0,0,255)',
                            'primary-foreground-color':'rgba(255,255,255,255)',
                            'secondary-foreground-color':'rgba(0,0,0,180)',
                            'background-path':None}
                            )
        
        self.dark_preset_values = ('dark', {'color':'light'}, 
                            {
                            'primary-background-color':'qlineargradient(spread:pad, x1:1, y1:0, x2:1, y2:1, stop:0 rgba(0, 0, 0, 151), stop:1 rgba(0, 0, 0, 0));',
                            'secondary-background-color':'rgba(0,0,0,255)',
                            'primary-foreground-color':'rgba(255,255,255,255)',
                            'secondary-foreground-color':'rgba(0,0,0,100)',
                            'background-path':None}
                            )
        

        self.light_preset_values = ('light', {'color':'dark'}, 
                            {
                            'primary-background-color':'rgba(255,255,255,255)',
                            'secondary-background-color':'rgba(255,255,255,255)',
                            'primary-foreground-color':'rgba(0,0,0,255)',
                            'secondary-foreground-color':'rgba(235, 237, 239,255)',
                            'background-path':None}
                            )
        

    def amoled_preset(self):
        self.update(values=self.amoled_preset_values)
        return self.master_scheme
    
    def dark_preset(self):
        self.update(values=self.dark_preset_values)
        return self.master_scheme
    
    def light_preset(self):
        self.update(values=self.light_preset_values)
        return self.master_scheme

    def custom_preset(self, name, icons_scheme, background_scheme):
        self.update(name, icons_scheme, background_scheme)
        return self.master_scheme
    

    def update(self, name=None, icons_scheme=None, background_scheme=None, values=None):
        temp_scheme = self.master_scheme.copy()

        if not values:
            temp_scheme['name'] = name if name else temp_scheme['name']
            temp_scheme['icons'] = icons_scheme if icons_scheme else temp_scheme['icons']
            temp_scheme['background'] = background_scheme if background_scheme else temp_scheme['background']

        else:
            temp_scheme['name'] = values[0] if values[0] else None
            temp_scheme['icons'] = values[1] if values[1] else None
            temp_scheme['background'] = values[2] if  values[2] else None
        
        if not temp_scheme['name'] or not temp_scheme['icons'] or not temp_scheme['background']:
            return None
        else:
            self.master_scheme = temp_scheme
    

# [Class:Enum] OctaveMusicTheme (Theme enum)
class OctaveMusicTheme(Enum):
    DARK = ThemePreset().dark_preset()
    LIGHT = ThemePreset().light_preset()
    AMOLED = ThemePreset().amoled_preset()
    CUSTOM_BACKGROUND = ThemePreset().custom_preset('custom', {'color':'light'},                             {
                            'primary-background-color':'rgba(0,0,0,0)',
                            'secondary-background-color':'rgba(0,0,0,0)',
                            'primary-foreground-color':'rgba(255,255,255,255)',
                            'secondary-foreground-color':'rgba(0,0,0,180)',
                            'background-path':''})
    
    BLUR_BETA = ThemePreset().custom_preset('blur-beta', {'color':'light'},                             {
                            'primary-background-color':'rgba(0,0,0,0)',
                            'secondary-background-color':'rgba(0,0,0,0)',
                            'primary-foreground-color':'rgba(255,255,255,255)',
                            'secondary-foreground-color':'rgba(0,0,0,180)',
                            'background-path':None})

# [Class:OctaveUserProfile] OctaveUserProfile (User profile class.)
class OctaveUserProfile:
    def __init__(self):
        pass

    def profileLoader_loadfromfile(self, filePath):
        pass

    def profileLoader_loadfromGoogle(self):
        pass

    def getProfileInfo(self):
        return {"name":"Aditya Gaur", "email":"adityagaur.home@gmail.com","avatar":None,"favourites":[], "recently_played":[]}

# [Class:Widget.MusicItem] MusicItemWidget (User profile class.)
class MusicItemWidget(QWidget, Ui_musicItem):
    def __init__(self, parent=None):
        super(MusicItemWidget, self).__init__(parent)
        self.setupUi(self)

# DEF_CLASS Class:Widget.SearchItemWidget] SearchItemWidget (Search Item widget.)
class SearchItemWidget(QWidget, Ui_searchItem):
    def __init__(self, parent=None):
        super(SearchItemWidget, self).__init__(parent)
        self.setupUi(self)

class HoverEventFilter(QObject):
    def eventFilter(self, obj, event):
        if event.type() == QEvent.HoverEnter:
            self.handle_hover(obj, "hovered")
        elif event.type() == QEvent.HoverLeave:
            self.handle_hover(obj, "left hover")
        return super().eventFilter(obj, event)

    def handle_hover(self, obj, hover_state):
        print(f"{hover_state.capitalize()} over: {obj.text()}")
    
class OctaveAnimations:
    def __init__(self): pass
    def animate_fade(self, child, fade_options={'in':[0.0, 1.0], 'out':[1.0, 0.0]}, duration:int = 300, state:str="in", ):
        if type(state) is str and state.lower() in fade_options and type(duration) is int and duration > 0:
            start_val = fade_options[state][0]
            end_val = fade_options[state][1]

            animation = QPropertyAnimation(child, b"opacity")
            animation.setDuration(duration)
            animation.setStartValue(0.0)
            animation.setEndValue(1.0)
            animation.setEasingCurve(QEasingCurve.InOutCubic)
            animation.start()
            # return animation

        else: warn("Octave Music", "OctaveAnimations:animate_fade", f"Invalid state or duration. , '{state}, {duration}'")

    def animate_size(self, child, start_size, end_size, duration:int = 300):
        if type(duration) is int and duration > 0:
            print('animation init')
            self.animation = QPropertyAnimation(child, b"size")
            self.animation.setDuration(duration)
            self.animation.setStartValue(start_size)
            self.animation.setEndValue(end_size)
            self.animation.setEasingCurve(QEasingCurve.InOutCubic)
            self.animation.start()

        else: warn("Octave Music", "OctaveAnimations:animate_fade", f"Invalid duration. , ' {duration}'")

    def cross_fade_icons(self, element, opacity_effect, icon, duration, fade_options={'in':[0.0, 1.0], 'out':[1.0, 0.0]}):
        self.animate_fade(opacity_effect,fade_options=fade_options, duration=duration, state="out")
        # fade_out.finished.connect(lambda: self.__change_icon_fadeIn(element, opacity_effect, fade_options, icon, duration))
        # fade_out.start()
        print('anim sart')

    def __change_icon_fadeIn(self,element, opacity_effect, fade_options, icon, duration):
        print('called')
        element.setIcon(icon)
        fade_in = self.animate_fade(opacity_effect, fade_options=fade_options, duration=duration, state="in")
        fade_in.start()

class FetchWorker(QObject):
    # Define a signal to send the results back to the main thread
    results_ready = Signal(list)
    error_occurred = Signal(str)   # Signal for errors

    def __init__(self, query_results):
        super().__init__()
        self.query_results =  query_results

    def run(self) -> None:
        try : 
            final_results = []
            print('finalizing results ..')
            for i in self.query_results:
                print(f'Processing: {i}')
                final_results.append(StreamMediaObject(i))

            print('Done objetifying data into streamediaobjects ...... ')
    
            pixmaps = []
            try:
                for i,e in enumerate(final_results):
                    print(f'Fetching cover art {i}')
                    if i == 0:
                        pixmaps.append(e.coverArt.return_designed_pixmap(size=140, radius=20, dimension='largest'))
                    else:
                        pixmaps.append(e.coverArt.return_designed_pixmap(size=60, radius=10, dimension='smallest'))

            except Exception as e:
                self.error_occurred.emit(str(e))
            
            results = (final_results, pixmaps)
            self.results_ready.emit(results)

        except Exception as e:
            self.error_occurred.emit(str(e))


class OctaveMusicWindow(QMainWindow):
    def __init__(self, app_options):
        start = time.time()
        super().__init__()

        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.app_options = app_options
        self.DEBUG = self.app_options.get('debug', False)

        self.setWindowTitle("Octave Music")
        self.setWindowIcon(QIcon("resources/octave_icon.ico"))

        # self.theme = OctaveMusicTheme.AMOLED
        # self.updateTheme()

        self.profile = OctaveUserProfile()
        self.profile_info = self.profile.getProfileInfo()

        """
        Media controller parameters.
        """
        self.media = None
        # self.MediaController = OctaveMediaController(parent=self, self.DEBUG=debug, backend=OctaveAudioBackend.VLC)
        self.MediaController = OctaveAdvMediaController(parent=self, debug=self.DEBUG,callback=self.update_slider_position_2,backend=OctaveAudioBackend.VLC)
        # self.MediaController.set_position_callback(self.update_slider_position)

        
        self.octaveFetch = OctaveFetch()


        self.threadt = None

        # self.streamMediaPlayer = StreamMediaControl(ui=self.ui)
        # she elf.isCurrentlyStreaming = False

        self.resized = Signal()  # Emit the custom signal when resized


        self.setWindowFlags(Qt.FramelessWindowHint)
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)


        self.qcfx = None
        self.qcfx_blur = None

        self.search_thread = None  # Thread object
        self.search_worker = None  # Worker object
        self.search_in_progress = False  # Flag to prevent multiple threads

        self.animationManager = OctaveAnimations()
        
        self.RESOURCES_FOLDER = Path("resources")
        self.FONT_FOLDER = self.RESOURCES_FOLDER.joinpath("fonts", "Inter")
        self.BACKGROUNDS_FOLDER = self.RESOURCES_FOLDER.joinpath("backgrounds")

        #TO FIX: 1. thread keeps the app running on offline playback.
        #TO FIX: 2. offline playback broken.
        # 

        self.position_thread = None
        self.slider_updating = False
        
        self.isBlurEnabled = True#BLURENABED
        self.THEME = OctaveMusicTheme.BLUR_BETA 

        self.updateTheme()
        self.updateBackground()


        self.loadFonts()
        self.loadIcons()
        self.initiateTriggers()
        self.initSearchPage()
        # self.loadMediaIntoPlayer(path="C:/Users/Aditya/Projects/OctaveMusic/leanonyou.m4a")
        # self.updateDurations()

        self.ui.volumeBtn.setIcon(self.icon_volume_full)
        self.toggle_volumeicons(self.MediaController.current_volume * 100)

        self.ui.resizebtn.setCursor(Qt.SizeFDiagCursor)

        self.resizing = False
        self.start_pos = QPoint(0, 0)

        # Override the button's mouse events
        self.ui.resizebtn.mousePressEvent = self.start_resize
        self.ui.resizebtn.mouseMoveEvent = self.perform_resize
        self.ui.resizebtn.mouseReleaseEvent = self.stop_resize

        self.start_pos = QPoint(0, 0)


        # self.dragPos = None
        self.ui.TopFrame.mouseMoveEvent = self.moveWindow
        self.original_geo = self.ui.playBtn.size()

        screen = QtWidgets.QApplication.primaryScreen()
        screen_geometry = screen.geometry()

        self.screen_width =  screen_geometry.width()
        self.screen_height = screen_geometry.height()

        self.xcoord = self.screen_width - self.width()
        self.ycoord = self.screen_height - self.height()

        self.originalDimentsions = QRect(self.screen_width//2 - 780//2, self.screen_height//2 - 560//2,780,560)

        self.isWinMaximized = False

        self.ui.maximiseBtn.clicked.connect(self.toggleMinMax)

        self.fetchingResults = False

        self.ui.viewFrame.setCurrentIndex(0)
        
        end = time.time()
        warn("OctaveMusic","Startup", f"It took {end-start:.2f}s to start.")
        self.show()

    # useful quick copy-pastes:
    
        # self.ui.sidePane.hide()
        # self.ui.heading_frame.hide()
        # self.ui.maximiseBtn.hide()
        # self.ui.minimizeBtn.hide()
        # self.ui.PlayerPane.hide()



    def showctxtip_appearance(self, btn_name, event_type):
        print(f"{event_type.capitalize()} over: {btn_name}")


    def appearance_toggle(self, theme_state):
        self.ui.appearanceMoreOptions.hide()

        if theme_state==0:
            self.ui.apprOptionsViewframe.setCurrentIndex(0)
            self.ui.appearanceMoreOptions.show()




    def updateTheme(self):
        self.theme_params = self.THEME.value
        self.theme_name = self.theme_params['name']
        self.theme_icon_theme = self.theme_params['icons']['color']
        self.theme_background_primary = self.theme_params['background']['primary-background-color']
        self.theme_background_secondary =self. theme_params['background']['secondary-background-color']
        self.theme_foreground_primary = self.theme_params['background']['primary-foreground-color']
        print(self.theme_foreground_primary)
        self.theme_foreground_secondary =self. theme_params['background']['secondary-foreground-color']
        self.theme_background_path = self.theme_params['background']['background-path']
        warn("OctaveMusic", "Theme", f"Theme updated to {self.theme_name}")
        print(self.dynamicPropertyNames())

        

        bgs = os.listdir(self.RESOURCES_FOLDER.joinpath("backgrounds"))
        self.InBuildBackgrounds = {}
        for bgname in bgs:
            self.InBuildBackgrounds[Path(bgname).stem] = self.BACKGROUNDS_FOLDER.joinpath(Path(bgname))
        
        self.default_custom_background = 'bg9', self.InBuildBackgrounds['bg9']

        self.ICON_FOLDER = self.RESOURCES_FOLDER.joinpath(f"icons_{self.theme_icon_theme}")
    
        # self.BACKGROUND_NAME = f"bg{bgno}.png"
        # self.BACKGROUND_PATH = f"resources/backgrounds/{self.BACKGROUND_NAME}"

        # DEFAULT STYLESHEETS 
        self.DEFAULT_BG_STYLESHEET_TRANSPARENT = f"""border-radius:16px; background: rgba(0,0,0,0); background-repeat:no-repeat; background-position: center; """

        self.DEFAULT_BG_STYLESHEET_TRANSPARENT_FLAT = f""" border-radius:0px; background: rgba(0,0,0,0); background-repeat:no-repeat; background-position: center;"""

        self.DEFAULT_BG_STYLESHEET_CENTRALW = f""" border-radius:16px;background-color: qlineargradient(spread:pad, x1:1, y1:0, x2:1, y2:1, stop:0 rgba(0, 0, 0, 255), stop:0.994444 rgba(26, 26, 26, 255));;  background-repeat:no-repeat; background-position: center;"""

        self.DEFAULT_BG_STYLESHEET_CENTRALW_FLAT = f""" border-radius:0px;background-color: qlineargradient(spread:pad, x1:1, y1:0, x2:1, y2:1, stop:0 rgba(0, 0, 0, 255), stop:0.994444 rgba(26, 26, 26, 255));;  background-repeat:no-repeat; background-position: center;"""

        self.DEFAULT_BG_FULL_STYLESHEET = f""" border-radius:0px; background-color:rgba(0,0,0,0); background-repeat:no-repeat; background-position: center;"""

        self.WINFRAME_BG_STYLESHEET = f""" border-radius:16px; background-color:rgba(0,0,0,255); background-repeat:no-repeat; background-position: center;"""

        self.WINFRAME_BG_STYLESHEET_TR = f""" border-radius:16px; background-color:rgba(0,0,0,0); background-repeat:no-repeat; background-position: center;"""
        
        if self.theme_name == 'custom':
            self.ui.centralwidget.setStyleSheet(self.DEFAULT_BG_FULL_STYLESHEET)
            self.ui.Window.setStyleSheet(self.WINFRAME_BG_STYLESHEET_TR)


        self.backgroundLayer = QLabel(self)
        self.backgroundLayer.setObjectName(u"backgroundLayer")
        self.backgroundLayer.setGeometry(self.rect())
        self.backgroundLayer.setStyleSheet(self.DEFAULT_BG_STYLESHEET_TRANSPARENT)
        self.windowRadius = 16
        self.backgroundLayer.lower()

        self.BACKGROUND_PIXMAP = None

        if self.theme_name == 'custom' :
            if self.theme_background_path == '':
                self.theme_background_path = self.default_custom_background[1]
            warn("OctaveMusic", "Theme", f"Custom theme background path: {self.theme_background_path}")
            self.BACKGROUND_PIXMAP = QPixmap(self.theme_background_path)

        elif self.theme_name !='blur-beta':

            # self.theme_background_primary # color overall
            # self.theme_background_secondary # color for player pane
            #                      'primary-foreground-color':'rgba(255,255,255,255)',
            #                 'secondary-foreground-color':'rgba(0,0,0,180)',
            
            self.TopFrameStylesheet = f"""background-color:{self.theme_background_primary}; background-repeat:no-repeat; background-position: center; color:{self.theme_foreground_primary};"""

            self.PlayerFrameStylesheet = f"""border-radius:0px; border-bottom-right-radius:16px; border-bottom-left-radius:16px; background-color:{self.theme_background_secondary}; background-repeat:no-repeat; background-position: center; color:{self.theme_foreground_primary}; """
            #121212

            self.SideFrameStylesheet = f"""background-color: transparent; margin:4px 0px 4px 4px; border-radius:10px; color:{self.theme_foreground_primary};"""
            self.BodyFrameStylesheet = f"""background-color: transparent; color:{self.theme_foreground_primary};"""

            self.WinFrameStylesheet = f"""background-color: {self.theme_background_primary};color:{self.theme_foreground_primary};"""
            
            self.ui.centralwidget.setStyleSheet(f'border-radius:16px; background-color: {self.theme_background_primary}; color:{self.theme_foreground_primary};')


            self.ui.TopFrame.setStyleSheet(self.TopFrameStylesheet)
            self.ui.SideFrame.setStyleSheet(self.SideFrameStylesheet)
            self.ui.PlayerFrame.setStyleSheet(self.PlayerFrameStylesheet)
            self.ui.BodyFrame.setStyleSheet(self.BodyFrameStylesheet)
            self.ui.Window.setStyleSheet(self.WinFrameStylesheet)

        elif self.theme_name =='blur-beta' and self.isBlurEnabled:

            self.qcfx = QCFxInitializer()
            self.qcfx_blur = QCFx_Blur(parent=self, overlay_parent=self.ui.centralwidget, overlay=self.backgroundLayer, mode=self.qcfx.MODE_DESKTOPONLY_L)
            self.qcfx_blur.generateParentBackground()
            self.qcfx_blur.updateAsynchronous_(None)
            self.ui.centralwidget.setStyleSheet(self.DEFAULT_BG_STYLESHEET_TRANSPARENT)
            self.BACKGROUND_PIXMAP = QPixmap.fromImage(self.qcfx_blur.cropped_image_qimage)

        warn('BACKGROUND PIXMAP VALUE', self.BACKGROUND_PIXMAP, "")
        if self.BACKGROUND_PIXMAP:
            self.BACKGROUND_PIXMAP: QtGui.QPixmap = self.BACKGROUND_PIXMAP.scaled(self.backgroundLayer.size(), Qt.KeepAspectRatioByExpanding, Qt.SmoothTransformation)



    
    def updateBackground(self):
        self.backgroundLayer.setGeometry(self.rect())

        path = QPainterPath()
        path.addRoundedRect(QRectF(0, 0, self.backgroundLayer.width(), self.backgroundLayer.height()), self.windowRadius, self.windowRadius)
        mask = QRegion(path.toFillPolygon().toPolygon())
        self.backgroundLayer.setMask(mask)

        if self.theme_name == 'blur-beta' and self.isBlurEnabled:
            self.qcfx_blur.generateParentBackground()
            self.qcfx_blur.updateAsynchronous_(None)
            self.BACKGROUND_PIXMAP = QPixmap.fromImage(self.qcfx_blur.cropped_image_qimage)
            
        if self.BACKGROUND_PIXMAP:
            print('HEREEEEEEEEEE')
            scaled_pixmap = self.BACKGROUND_PIXMAP.scaled(self.backgroundLayer.size(), Qt.KeepAspectRatioByExpanding, Qt.SmoothTransformation)

            self.backgroundLayer.setPixmap(scaled_pixmap)



    
    # def style_AMOLED(self):
    #     self.TopFrameStylesheet = """background-color:rgba(0,0,0,255); background-repeat:no-repeat; background-position: center; """
    #     self.PlayerFrameStylesheet = """border-radius:0px; border-bottom-right-radius:16px; border-bottom-left-radius:16px; background-color:rgba(0,0,0,255); background-repeat:no-repeat; background-position: center; """
    #     #121212
    #     self.SideFrameStylesheet = """background-color: transparent; margin:4px 0px 4px 4px; border-radius:10px;"""
    #     self.BodyFrameStylesheet = """background-color: transparent;"""
    #     self.WinFrameStylesheet = """background-color: qlineargradient(spread:pad, x1:1, y1:0, x2:1, y2:1, stop:0 rgba(0, 0, 0, 151), stop:1 rgba(0, 0, 0, 0));"""
        
    #     self.ui.centralwidget.setStyleSheet('border-radius:16px; background-color: qlineargradient(spread:pad, x1:1, y1:0, x2:1, y2:1, stop:0 rgba(0, 0, 0, 255), stop:0.994444 rgba(26, 26, 26, 255));')

    #     self.ui.TopFrame.setStyleSheet(self.TopFrameStylesheet)
    #     self.ui.SideFrame.setStyleSheet(self.SideFrameStylesheet)
    #     self.ui.PlayerFrame.setStyleSheet(self.PlayerFrameStylesheet)
    #     self.ui.BodyFrame.setStyleSheet(self.BodyFrameStylesheet)
    #     self.ui.Window.setStyleSheet(self.WinFrameStylesheet)



    # def style_light(self):
        
    #     #border-radius:0px; border-top-right-radius:16px; border-top-left-radius:16px; 
    #     self.TopFrameStylesheet = """background-color:rgba(255,255,255,255); background-repeat:no-repeat; background-position: center; """
    #     self.PlayerFrameStylesheet = """border-radius:0px; border-bottom-right-radius:16px; border-bottom-left-radius:16px; background-color:rgba(255,255,255,255); background-repeat:no-repeat; background-position: center; """
    #     #121212
    #     self.SideFrameStylesheet = """background-color: transparent; margin:4px 0px 4px 4px; border-radius:10px;"""
    #     self.BodyFrameStylesheet = """background-color: transparent;"""
    #     self.WinFrameStylesheet = """background-color: qlineargradient(spread:pad, x1:1, y1:0, x2:1, y2:1, stop:0 rgba(0, 0, 0, 151), stop:1 rgba(0, 0, 0, 0));"""
        
    #     self.ui.centralwidget.setStyleSheet('border-radius:16px; background-color: qlineargradient(spread:pad, x1:1, y1:0, x2:1, y2:1, stop:0 rgba(0, 0, 0, 255), stop:0.994444 rgba(26, 26, 26, 255));')

    #     self.ui.TopFrame.setStyleSheet(self.TopFrameStylesheet)
    #     self.ui.SideFrame.setStyleSheet(self.SideFrameStylesheet)
    #     self.ui.PlayerFrame.setStyleSheet(self.PlayerFrameStylesheet)
    #     self.ui.BodyFrame.setStyleSheet(self.BodyFrameStylesheet)
    #     self.ui.Window.setStyleSheet(self.WinFrameStylesheet)

    def fetchQueryWithWorker(self, query,  results_limit=6, auto_next=False, force_new=False):
        warn("OctaveMusic","Search", "Searching right now ...")
        
        if self.search_in_progress:
            warn("OctaveMusic", "Search", "A search is already in progress. Please wait.")
            return
        

        try:
            query_results = self.octaveFetch.fetch(query, results_limit, auto_next, force_new)
            self.search_in_progress = True

            self.time_taken_for_results = self.octaveFetch.results_fetch_time[0]
        except Exception as e:
            warn("OctaveMusic", "Error", f"Failed to fetch query results: {e}")
            return

            
        # query_results = self.octaveFetch.fetch(query, results_limit, auto_next, force_new)

        # self.fetchingResults = True
        # self.time_taken_for_results = self.octaveFetch.results_fetch_time[0]

        self.search_thread = QThread()
        self.search_worker = FetchWorker(query_results)

        # Move the worker to the thread
        self.search_worker.moveToThread(self.search_thread)

        # Connect signals and slots
        self.search_thread.started.connect(self.search_worker.run)
        self.search_worker.results_ready.connect(self.onResultsReady)
        self.search_worker.results_ready.connect(self.search_thread.quit)  # Stop the thread when done
        self.search_worker.results_ready.connect(self.search_worker.deleteLater)  # Clean up the worker
        self.search_thread.finished.connect(self.search_thread.deleteLater)  # Clean up the thread

        # Handle errors or cancellations

        self.search_worker.error_occurred.connect(lambda e: warn("OctaveMusic", "Error", f"Worker error: {e}"))
        self.search_thread.finished.connect(lambda: setattr(self, 'search_in_progress', False))

        self.search_thread.start()



    def initSearchPage(self):
        self.searchResults = None
        self.ui.searchResults.hide()
        self.ui.search.clicked.connect(self.searchFromQuery)
        # self.ui.
        self.ui.searchBox.setPlaceholderText("What's the mood?")
        
    def closeEvent(self, event):
        """Ensure threads are stopped properly when the application is closed."""
        if self.search_thread and self.search_thread.isRunning():
            self.search_thread.quit()
            self.search_thread.wait()

        super().closeEvent(event)

    def onResultsReady(self, results):

        self.ui.searchResults.clear()
        self.ui.searchResults.hide()

        self.search_in_progress = False  # Reset the flag


        warn("OctaveMusic","Search", f"Results Successfully fetched, time taken = {self.time_taken_for_results}")
        self.searchResults = results
        print('Before: ')
        print(len(self.searchResults[0]), len(self.searchResults[1]))
        top_result, top_result_coverart = self.searchResults[0].pop(0), self.searchResults[1].pop(0)
        print('After: ')
        print(len(self.searchResults[0]), len(self.searchResults[1]))

        self.ui.topResultCoverart.setPixmap(top_result_coverart)
        self.ui.topResult_title.setText(top_result.title)
        self.ui.topResult_artist.setText(top_result.artist)

        for i,e in enumerate(self.searchResults[0]):

            search_item = SearchItemWidget()
            list_item = QListWidgetItem(self.ui.searchResults)
            search_item.title.setText(e.title)
            search_item.artist.setText(e.artist)
            search_item.coverArt.setPixmap(self.searchResults[1][i])
            search_item.likeBtn.setIcon(self.icon_like)
            search_item.moreOptions.setIcon(self.icon_dotMenu)

            list_item.setSizeHint(QSize(100,80))
            # list_item.setSizeHint(self.ui.searchResults.it)

            self.ui.searchResults.addItem(list_item)
            self.ui.searchResults.setItemWidget(list_item, search_item)
            
        self.ui.searchResults.show()
        self.ui.viewFrame.setCurrentIndex(1)
        

    def enter_searchFromQuery(self):
        if self.ui.searchBox.hasFocus():
            query_text = self.ui.searchBox.text().strip()  
            if query_text:
                self.searchFromQuery()


    def searchFromQuery(self):
        if self.search_in_progress:
            warn("OctaveMusic","Search", "Search already in progress. Please wait.")
            return

        query = self.ui.searchBox.text().strip()
        if not query:
            warn("OctaveMusic","Search", "Search query is empty.")
            return
        
        # self.search_in_progress = True

        # self.ui.search.setDisabled(True)
    
        # if query != '' and not self.fetchingResults and not self.threadt :

        self.fetchQueryWithWorker(query)
            

        self.ui.search.setDisabled(False)
        self.search_shortcut.activated.connect(self.enter_searchFromQuery)


    def on_search_double_clicked(self, item):
        click_index  = self.ui.searchResults.row(item)
        
        media = self.searchResults[0][click_index]
        # self.isCurrentlyStreaming = True
    

        print(click_index, media.title)
        self.loadMediaIntoPlayer(media=media)
        self.MediaController.play()
        # self.togglePlayPause(toggle=False)
        self.setPlayPauseIcon(play=True)



    def toggle_volumeicons(self, volume_value):
        prev_icon = self.ui.volumeBtn.icon()

        if 100>=volume_value >=90 :
            new_icon = self.icon_volume_full
            # self.ui.volumeBtn.setIcon(self.icon_volume_full)

        elif 90> volume_value >=50 :
            # self.ui.volumeBtn.setIcon(self.icon_volume_med)
            new_icon = self.icon_volume_med

        elif 50> volume_value >=1 :
            # self.ui.volumeBtn.setIcon(self.icon_volume_low)
            new_icon = self.icon_volume_low

        elif 1> volume_value >=0 :
            # self.ui.volumeBtn.setIcon(self.icon_volume_zero)
            new_icon = self.icon_volume_zero

        if prev_icon.cacheKey() != new_icon.cacheKey():
            # self.animationManager.cross_fade_icons(self.ui.volumeBtn, self.opacity_effect_volumeBtn, new_icon, duration=100)
            self.ui.volumeBtn.setIcon(new_icon)

    def refreshView(self):
        if self.profile_info['favourites'] != []:pass

    def toggleMinMax(self):
        if self.isWinMaximized:
            self.windowRadius = 16

            self.setGeometry(self.originalDimentsions)

            if self.theme_name == 'blur-beta' and self.isBlurEnabled or self.theme_name == 'custom':
                self.ui.centralwidget.setStyleSheet(self.DEFAULT_BG_STYLESHEET_TRANSPARENT)
            else:
                self.ui.centralwidget.setStyleSheet(self.DEFAULT_BG_STYLESHEET_CENTRALW)
        
            self.ui.resizebtn_frame.show()
            self.ui.maximiseBtn.setIcon(self.icon_maximize)
            self.isWinMaximized = False

        elif not self.isWinMaximized:
            self.windowRadius = 0
            self.setGeometry(QRect(0,0,self.screen_width, self.screen_height))

            self.ui.resizebtn_frame.hide()
            self.isWinMaximized = True
            self.ui.maximiseBtn.setIcon(self.icon_restore)

            if self.theme_name == 'blur-beta' and self.isBlurEnabled or self.theme_name == 'custom':
                self.ui.centralwidget.setStyleSheet(self.DEFAULT_BG_STYLESHEET_TRANSPARENT_FLAT)
            else:
                self.ui.centralwidget.setStyleSheet(self.DEFAULT_BG_STYLESHEET_CENTRALW_FLAT)

    def start_resize(self, event):
        if event.button() == Qt.LeftButton:
            self.resizing = True
            self.start_pos = event.globalPos()

    def perform_resize(self, event):
        if self.resizing:
            # self.toggleBetweenBlur_resize(False)
            diff = event.globalPos() - self.start_pos
            new_width = self.width() + diff.x()
            new_height = self.height() + diff.y()

            new_width = max(self.minimumWidth(), new_width)
            new_height = max(self.minimumHeight(), new_height)
            self.resize(new_width, new_height)
            self.start_pos = event.globalPos()

    def stop_resize(self, event):
        self.resizing = False

    def resizeEvent(self, event):
        self.updateBackground()
        super().resizeEvent(event)

    def toggleBetweenBlurMode(self, forceDark=None):
        if forceDark:
            if self.qcfx_blur:
                self.qcfx_blur.blurLayer.hide()
                self.qcfx_blur.endAll()
            self.ui.centralwidget.setStyleSheet(self.DEFAULT_BG_STYLESHEET_CENTRALW)

        else:
            if self.isBlurEnabled:
                if not self.qcfx_blur:
                    self.qcfx = QCFxInitializer()
                    self.qcfx_blur = QCFx_Blur(parent=self, overlay_parent=self.ui.centralwidget, overlay=self.backgroundLayer, mode=self.qcfx.MODE_DESKTOPONLY_L)

                # self.qcfx_blur.blurLayer.setGeometry(self.rect())
                self.qcfx_blur.generateParentBackground()
                self.qcfx_blur.updateAsynchronous_(None)
                self.ui.centralwidget.setStyleSheet(self.DEFAULT_BG_STYLESHEET_TRANSPARENT)
                self.qcfx_blur.blurLayer.show()


                self.isBlurEnabled = True
            else:
                if self.qcfx_blur:
                    self.qcfx_blur.blurLayer.hide()
                    self.qcfx_blur.endAll()
                    # process = multiprocessing.Process(target=self.qcfx_blur.endAll)
                    # process.start()
                    # process.join()

                self.ui.centralwidget.setStyleSheet(self.DEFAULT_BG_STYLESHEET_CENTRALW)
                self.isBlurEnabled = False

    def initiateTriggers(self): 

        self.ui.playBtn.clicked.connect(self.togglePlayPause)
        self.ui.closeBtn.clicked.connect(self.closeSafely)
        self.ui.minimizeBtn.clicked.connect(self.showMinimized)
        self.ui.addToQueue.clicked.connect(self.addToQueue)
        self.ui.removeFromQueue.clicked.connect(self.removeFromQueue)

        self.ui.nextBtn.clicked.connect(self.playNext)
        self.ui.likeBtn.clicked.connect(self.likeUnlike)
        self.ui.prevBtn.clicked.connect(self.playPrev)

        self.ui.progress.setValue(0)
        self.ui.progress.setRange(0, 100)
        self.ui.progress.setPageStep(0)


        # self.ui.volume.setValue(100)
        # self.ui.volume.setRange(0, 100)
        # self.ui.volume.setPageStep(0)

        self.ui.menuBtn.clicked.connect(self.toggleHamMenu)

        self.ui.homeBtn.clicked.connect(lambda: self.ui.viewFrame.setCurrentIndex(0))
        self.ui.exploreBtn.clicked.connect(lambda: self.ui.viewFrame.setCurrentIndex(1))
        self.ui.libraryBtn.clicked.connect(lambda: self.ui.viewFrame.setCurrentIndex(2))
        self.ui.settingsBtn.clicked.connect(lambda: self.ui.viewFrame.setCurrentIndex(3))

        self.ui.progress.sliderPressed.connect(self.on_slider_pressed)
        self.ui.progress.sliderReleased.connect(self.on_slider_released)
        self.ui.progress.valueChanged.connect(self.updatetime)


        # self.ui.volume.sliderPressed.connect(self.on_volume_slider_pressed)
        # self.ui.volume.sliderReleased.connect(self.on_volume_slider_released)

        self.ui.searchResults.itemDoubleClicked.connect(self.on_search_double_clicked)

        
        self.search_shortcut = QShortcut(QKeySequence("Return"), self)
        self.search_shortcut.activated.connect(self.enter_searchFromQuery)
        
        self.playpause = QShortcut(QKeySequence("Space"), self)
        self.playpause.activated.connect(self.togglePlayPause)

        self.isMenuHidden = False
        
        self.ui.app_auto.clicked.connect(lambda: self.appearance_toggle(0))
        self.ui.app_smart.clicked.connect(lambda: self.appearance_toggle(1))
        self.ui.app_amoled.clicked.connect(lambda: self.appearance_toggle(2))
        self.ui.app_custom.clicked.connect(lambda: self.appearance_toggle(3))
        self.ui.app_blurbeta.clicked.connect(lambda: self.appearance_toggle(4))
        # appearance_ctx_tip_hover_filter
        appr_hoverfilter = HoverEventFilter()

        self.ui.app_auto.installEventFilter(appr_hoverfilter)
        self.ui.app_smart.installEventFilter(appr_hoverfilter)
        self.ui.app_amoled.installEventFilter(appr_hoverfilter)
        self.ui.app_custom.installEventFilter(appr_hoverfilter)
        self.ui.app_blurbeta.installEventFilter(appr_hoverfilter)




        # self.ui.volume.valueChanged.connect(self.toggle_volumeicons)
    def toggleHamMenu(self):
        if self.isMenuHidden:
            self.ui.SideFrame.show()
        else:
            self.ui.SideFrame.hide()

        self.isMenuHidden = not self.isMenuHidden

    def playNext(self):
        next = self.queue.next()
        media = next[1]
        self.media = media

        self.loadMediaIntoPlayer(media=next[1])
        self.togglePlayPause()
        # self.ui.queueWidget.setSelection()

    def likeUnlike(self):
        if self.media.isLiked:
            self.media.isLiked  = False
            self.media.external_metadata_ctx.change_metadata(self.media)
            self.ui.likeBtn.setIcon(self.icon_like)
        else:
            self.media.isLiked  = True
            self.media.external_metadata_ctx.change_metadata(self.media)
            self.ui.likeBtn.setIcon(self.icon_liked)

    def playPrev(self):
        prev = self.queue.previous()
        media = prev[1]
        self.media = media
        warn(media.title, prev[0], self.queue.length)
        self.loadMediaIntoPlayer(media=prev[1])
        self.togglePlayPause()

    def addToQueue(self):
        options = QFileDialog.Options()

        file_dialog = QFileDialog(self, "Open Audio File", "", "Audio Files (*.mp3 *.m4a *.wav *.mp4 *.opus);;All Files (*)", options=options)
        file_dialog.setFileMode(QFileDialog.ExistingFiles)

        # Show the dialog and get the selected file
        if file_dialog.exec_():
            selected_files = file_dialog.selectedFiles()
            for file in selected_files:
                toadd= LocalMediaObject(file)

                self.queue.addToQueue(toadd)

                music_item_widget = MusicItemWidget()
                list_item = QListWidgetItem(self.ui.queueWidget)
                music_item_widget.title.setText(toadd.title)
                music_item_widget.artist.setText(toadd.artist)
                if toadd.coverArt:
                    pixmap = toadd.coverArt.return_designed_pixmap(size=music_item_widget.coverart.width())
                    music_item_widget.coverart.setPixmap(pixmap)

                list_item.setSizeHint(music_item_widget.sizeHint())
                self.ui.queueWidget.addItem(list_item)
                self.ui.queueWidget.setItemWidget(list_item, music_item_widget)

    def removeFromQueue(self):
        selected_item = self.ui.queueWidget.selectedItems()[0] if self.ui.queueWidget.selectedItems()[0] else None
        if selected_item:
            idx = self.ui.queueWidget.row(selected_item)
            self.queue.removeFromQueue(idx)
            self.ui.queueWidget.takeItem(idx)

    def loadFonts(self):
        for font_file in os.listdir(self.FONT_FOLDER):
            if font_file.endswith(".ttf"):
                font_path = self.FONT_FOLDER.joinpath(font_file)
                font_id = QFontDatabase.addApplicationFont(str(font_path))
                if font_id != -1:
                    font_family = QFontDatabase.applicationFontFamilies(font_id)[0]
                    # if self.DEBUG:
                        # warn("Ocatve Music GUI", "Font Loader", f"Loaded font: {font_family} from {font_file}")
                else:
                    warn("Ocatve Music GUI", "Font Loader", f"Failed to load font from {font_file}")
        # warn("Ocatve Music GUI", "Font Loader", f"Fonts loaded.")

    def loadIcons(self):
        self.icon_play = QIcon()
        self.icon_play.addFile(str(self.ICON_FOLDER / "icon_play.png"), QSize(), QIcon.Normal, QIcon.Off)

        self.icon_resizehandle = QIcon()
        self.icon_resizehandle.addFile(str(self.ICON_FOLDER / "icon_resizehandle.png"), QSize(), QIcon.Normal, QIcon.Off)

        self.icon_prev = QIcon()
        self.icon_prev.addFile(str(self.ICON_FOLDER / "icon_prev.png"), QSize(), QIcon.Normal, QIcon.Off)

        self.icon_next = QIcon()
        self.icon_next.addFile(str(self.ICON_FOLDER / "icon_next.png"), QSize(), QIcon.Normal, QIcon.Off)

        self.icon_pause = QIcon()
        self.icon_pause.addFile(str(self.ICON_FOLDER / "icon_pause.png"), QSize(), QIcon.Normal, QIcon.Off)

        self.icon_maximize = QIcon()
        self.icon_maximize.addFile(str(self.ICON_FOLDER / "icon_maximize.png"), QSize(42,42), QIcon.Normal, QIcon.Off)

        self.icon_restore = QIcon()
        self.icon_restore.addFile(str(self.ICON_FOLDER / "icon_restore.png"), QSize(), QIcon.Normal, QIcon.Off)


        self.icon_volume_full = QIcon()
        self.icon_volume_full.addFile(str(self.ICON_FOLDER / "icon_volume_full.png"), QSize(), QIcon.Normal, QIcon.Off)


        self.icon_volume_med = QIcon()
        self.icon_volume_med.addFile(str(self.ICON_FOLDER / "icon_volume_med.png"), QSize(), QIcon.Normal, QIcon.Off)


        self.icon_volume_low = QIcon()
        self.icon_volume_low.addFile(str(self.ICON_FOLDER / "icon_volume_low.png"), QSize(), QIcon.Normal, QIcon.Off)

        self.icon_volume_zero = QIcon()
        self.icon_volume_zero.addFile(str(self.ICON_FOLDER / "icon_volume_zero.png"), QSize(), QIcon.Normal, QIcon.Off)


        self.icon_liked = QIcon()
        self.icon_liked.addFile(str(self.ICON_FOLDER / "icon_liked.png"), QSize(), QIcon.Normal, QIcon.Off)

        self.icon_like = QIcon()
        self.icon_like.addFile(str(self.ICON_FOLDER / "icon_like.png"), QSize(), QIcon.Normal, QIcon.Off)

        self.icon_close = QIcon()
        self.icon_close.addFile(str(self.ICON_FOLDER / "icon_close.png"), QSize(), QIcon.Normal, QIcon.Off)

        self.icon_minimize = QIcon()
        self.icon_minimize.addFile(str(self.ICON_FOLDER / "icon_minimize.png"), QSize(), QIcon.Normal, QIcon.Off)

        self.icon_addToQueue = QIcon()
        self.icon_addToQueue.addFile(str(self.ICON_FOLDER / "icon_addToQueue.png"), QSize(), QIcon.Normal, QIcon.Off)

        self.icon_removeFromQueue = QIcon()
        self.icon_removeFromQueue.addFile(str(self.ICON_FOLDER / "icon_removeFromQueue.png"), QSize(), QIcon.Normal, QIcon.Off)

        self.icon_newQueue = QIcon()
        self.icon_newQueue.addFile(str(self.ICON_FOLDER / "icon_newQueue.png"), QSize(), QIcon.Normal, QIcon.Off)

        self.icon_shuffle = QIcon()
        self.icon_shuffle.addFile(str(self.ICON_FOLDER / "icon_shuffle.png"), QSize(), QIcon.Normal, QIcon.Off)


        self.icon_norepeat = QIcon()
        self.icon_norepeat.addFile(str(self.ICON_FOLDER / "icon_norepeat.png"), QSize(), QIcon.Normal, QIcon.Off)

        self.icon_defaultProfileAvatar = QIcon()
        self.icon_defaultProfileAvatar.addFile(str(self.ICON_FOLDER / "icon_defaultProfileAvatar.png"), QSize(), QIcon.Normal, QIcon.Off)

        self.icon_norepeat = QIcon()
        self.icon_norepeat.addFile(str(self.ICON_FOLDER / "icon_norepeat.png"), QSize(), QIcon.Normal, QIcon.Off)

        self.icon_menu = QIcon()
        self.icon_menu.addFile(str(self.ICON_FOLDER / "icon_menu.png"), QSize(), QIcon.Normal, QIcon.Off)


        self.icon_topResult_pause = QIcon()
        self.icon_topResult_pause.addFile(str(self.ICON_FOLDER / "icon_topResult_pause.png"), QSize(), QIcon.Normal, QIcon.Off)

        self.icon_topResult_play = QIcon()
        self.icon_topResult_play.addFile(str(self.ICON_FOLDER / "icon_topResult_play.png"), QSize(), QIcon.Normal, QIcon.Off)

        self.icon_dotMenu = QIcon()
        self.icon_dotMenu.addFile(str(self.ICON_FOLDER / "icon_dotMenu.png"), QSize(), QIcon.Normal, QIcon.Off)

        self.icon_info = QIcon()
        self.icon_info.addFile(str(self.ICON_FOLDER / "icon_info.png"), QSize(), QIcon.Normal, QIcon.Off)

        self.ui.playTopResult.setIcon(self.icon_topResult_play)
        self.ui.appearanceInfoIcon.setPixmap(self.icon_info.pixmap(QSize(42,42)))

        self.ui.maximiseBtn.setIcon(self.icon_maximize)
        self.ui.closeBtn.setIcon(self.icon_close)
        self.ui.minimizeBtn.setIcon(self.icon_minimize)

        self.ui.playBtn_queue.setIcon(self.icon_play)
        
        self.ui.playBtn.setIcon(self.icon_play)
        self.ui.prevBtn.setIcon(self.icon_prev)
        self.ui.nextBtn.setIcon(self.icon_next)

        self.ui.shuffleBtn.setIcon(self.icon_shuffle)
        self.ui.repeatBtn.setIcon(self.icon_norepeat)

        self.ui.resizebtn.setIcon(self.icon_resizehandle)

        self.ui.profileBtn.setIcon(self.icon_defaultProfileAvatar)
        self.ui.menuBtn.setIcon(self.icon_menu)

        self.icon_home = QIcon()
        self.icon_home.addFile(str(self.ICON_FOLDER / "icon_home.png"), QSize(), QIcon.Normal, QIcon.Off)

        self.icon_explore = QIcon()
        self.icon_explore.addFile(str(self.ICON_FOLDER / "icon_explore.png"), QSize(), QIcon.Normal, QIcon.Off)

        self.icon_library = QIcon()
        self.icon_library.addFile(str(self.ICON_FOLDER / "icon_library.png"), QSize(), QIcon.Normal, QIcon.Off)

        self.icon_settings = QIcon()
        self.icon_settings.addFile(str(self.ICON_FOLDER / "icon_settings.png"), QSize(), QIcon.Normal, QIcon.Off)


        self.icon_search = QIcon()
        self.icon_search.addFile(str(self.ICON_FOLDER / "icon_search.png"), QSize(), QIcon.Normal, QIcon.Off)


        self.ui.homeBtn.setIcon(self.icon_home)
        self.ui.exploreBtn.setIcon(self.icon_explore)
        self.ui.libraryBtn.setIcon(self.icon_library)
        self.ui.settingsBtn.setIcon(self.icon_settings)

        self.ui.likeBtn.setIcon(self.icon_like)
        self.ui.search.setIcon(self.icon_search)

        self.ui.newQueue.setIcon(self.icon_newQueue)
    
        self.ui.addToQueue.setIcon(self.icon_addToQueue)
        self.ui.removeFromQueue.setIcon(self.icon_removeFromQueue)
        

        self.queue  = OctaveQueue()
        self.queue.loadFromFile(self.queue.SAVEDQUEUES_PATH)

        # self.queue.addToQueue(LocalMediaObject("C:/Users/Aditya/Projects/OctaveMusic/sampleAudio/Flores.mp3"))
        if self.queue.current_queue:
            for i in self.queue.current_queue:
                music_item_widget = MusicItemWidget()
                list_item = QListWidgetItem(self.ui.queueWidget)
                music_item_widget.title.setText(i.title)
                music_item_widget.artist.setText(i.artist)
                if i.coverArt:

                    # print(i.coverArt.choices)
                    pixmap = i.coverArt.return_designed_pixmap(size=music_item_widget.coverart.width())
                    music_item_widget.coverart.setPixmap(pixmap)

                list_item.setSizeHint(music_item_widget.sizeHint())
                self.ui.queueWidget.addItem(list_item)
                self.ui.queueWidget.setItemWidget(list_item, music_item_widget)

        self.ui.queueWidget.itemDoubleClicked.connect(self.on_item_double_clicked)

    def on_item_double_clicked(self, item):
        # Slot to handle double-click event
        # QMessageBox.information(self, "Item Double Clicked", f"You double-clicked on: {self.ui.queueWidget.row(item)}")
        click_index  = self.ui.queueWidget.row(item)
        print(click_index)
        self.loadMediaIntoPlayer(path=self.queue.current_queue[click_index].filePath)
        # self.MediaController.playMedia()
        self.togglePlayPause()

    def _update_stream(self, media_object,preference, quality, codec):
        retr =self.octaveFetch.fetch_stream(media_object.watchid, preference=preference, quality=quality,codec= codec)

        response, info = retr[0]['response'], retr[0]['info']
        media_object.stream_url = info['url']

        return response, info

    def loadMediaIntoPlayer(self, path=None, media=None):
        if media==None and path:
            self.media = LocalMediaObject(path)
            self.MediaController.setMedia(self.media)
            pixmap = self.media.coverArt.return_designed_pixmap(size=48,radius=10)
            print(pixmap, self.media.coverArt)
            self.ui.cover_art.setPixmap(pixmap)

            self.ui.playBtn.setIcon(self.icon_play)
            self.ui.playBtn.setIconSize(QSize(42, 42))

            self.updateDurations()

        else:
            self.media = media
            pixmap = self.media.coverArt.return_designed_pixmap(size=48)
            print(pixmap, self.media.coverArt)
            self.ui.cover_art.setPixmap(pixmap)

            self.ui.playBtn.setIcon(self.icon_play)
            self.ui.playBtn.setIconSize(QSize(42, 42))

            if media.isStreamable:
                # TO FIX -> 
                try:
                    with open('audio_settings.json', 'r') as f:
                        data = json.load(f)
                except Exception as e:
                    data = { "audioQualityScheme":
                                                        {
                                                            "preference": "QUALITY_FIRST",
                                                            "quality":"STANDARD",
                                                            "codec":"opus"
                                                        }
                                                    }
                data = data["audioQualityScheme"]
                preference = OctaveStreamFetchPreference[data['preference']]
                quality = OctaveStreamAudioQuality[data['quality']]
                codec = OctaveStreamSupportedCodec[data['codec']]
    
                # preference = OctaveStreamFetchPreference.QUALITY_FIRST
                # quality = OctaveStreamAudioQuality.HIGH
                # codec = OctaveStreamSupportedCodec.opus


                resp, info = self._update_stream(media,preference, quality, codec)

                print(f"[{resp['ultimatum']}] Playing audio at bitrate={round(int(info['bitrate'])/1000, 2)}, quality={resp['quality']}, codec={resp['codec']}")

            self.MediaController.setMedia(self.media)
            self.updateDurations()




            # if self.media.isStreamable:
            #     self.MediaController.setMedia(self.media)
                
            # elif self.media.type=='stream':
            #     self.streamMediaPlayer.setMedia(self.media)

        self.ui.progress.setRange(0, self.media.duration)

        self.ui.title.setText(self.media.title)
        self.ui.artist.setText(self.media.artist)

        if self.media.isLiked:
            self.ui.likeBtn.setIcon(self.icon_liked)
        else:
            self.ui.likeBtn.setIcon(self.icon_like)
            
        # CVRART_bytes = self.media.coverArt.returnCoverArtAsBytes()
        # # pil_art = CVRART_bytes.
        # print(self.ui.cover_art.width(), self.ui.cover_art.height())
        # pixmap = QPixmap()
        # pixmap.loadFromData(CVRART_bytes)



    def update_slider_position_2(self, player, stop_event):
        print('update pos called.')
        duration = self.MediaController.MediaObject.duration   # Convert duration to milliseconds
        # print(f'duration normal {duration}, duration_ms {duration * 1000}')
        
        while not stop_event.is_set():
            if player.is_playing():
                current_time = player.get_time() // 1000  # Get current time in seconds

                # print(f"CURRENT TIME {current_time}")
                self.ui.progress.setValue(current_time)

                # print(f"Current Playback Time: {current_time}s", end='\r', flush=True)
            time.sleep(1)

    def update_slider_position(self, position_ms):
        print("UPDATE SLDIER POSITION IS CALLEDDDDDDDDDDD")

        # duration_ms = self.MediaController.MediaObject.duration * 1000  # Convert duration to milliseconds
        duration_ms = self.MediaController.MediaObject.duration   # Convert duration to milliseconds
        # print(duration_ms)
        # Ensure slider only updates when it's not being dragged
        # if not self.slider_updating:
        if duration_ms > 0:  # Avoid division by zero
            # print(round((position_ms/duration_ms)*100))
            # print(f'should be at {position_ms}')

            self.ui.progress.setValue(position_ms//1000)



    def updateDurations(self):
        time_string = f"00:00/{self.media.duration_formatted}"
        self.ui.end_time.setText(time_string)
        print(self.media.duration_formatted)

    def closeSafely(self):
        self.MediaController.endSession()
        self.close()

    def mousePressEvent(self, event):
        self.dragPos = event.globalPos()

    def moveWindow(self, event):
        if event.buttons() == Qt.LeftButton and self.dragPos and not self.isWinMaximized:
            self.move(self.pos() + event.globalPos() - self.dragPos)
            self.dragPos = event.globalPos()
            event.accept()

    def seek_and_play(self, position_ms):
        # if not self.MediaController.isPlaying:
        #     self.MediaController.seek(position_ms)
        #     self.togglePlayPause()
        # else:
        self.MediaController.seek(position_ms)
        self.togglePlayPause()

        # if not self.MediaController.isPlaying:
        #     self.MediaController.resumeMedia()

    def on_slider_pressed(self):
        self.slider_updating = True
        self.MediaController.pause()

    def on_slider_released(self):
        # slider_value = self.ui.progress.value()
        # duration_ms = self.MediaController.MediaObject.duration * 1000
        slider_value = self.ui.progress.value()  # Get the value from QSlider
        duration_ms = self.MediaController.MediaObject.duration * 1000  # Total duration in ms

        # position_ms = (slider_value / 100) * duration_ms
        position_ms = slider_value * 1000


        print(f"POSITION MS : {position_ms}")

        self.seek_and_play(position_ms//1000)

        self.slider_updating = False

    def updatetime(self, value):
        # if not self.MediaController.isPlaying:
        duration_ms = self.MediaController.MediaObject.duration * 1000
        # else:
            # duration_ms = self.Medi.media.duration * 1000
    
        # self.ui.current_time.setText(self.MediaController.format_time(value * duration_ms / 100))
        time_string = f"{self.MediaController.format_time(value*1000)}/{self.media.duration_formatted}"
        self.ui.end_time.setText(time_string)

    def togglePlayPause(self):
        if self.MediaController.isPlaying :
            self.MediaController.pause()

                # self.opacity_animation_out= QPropertyAnimation(self.opacity_effect_playBtn, b"opacity")
                # self.opacity_animation_out.setDuration(50)
                # self.opacity_animation_out.setEasingCurve(QEasingCurve.InOutCubic)
                # self.opacity_animation_out.setStartValue(1.0)
                # self.opacity_animation_out.setEndValue(0.5)
                # self.opacity_animation_out.finished.connect(lambda: self.change_icon(self.ui.playBtn, self.opacity_effect_playBtn, self.icon_play))
                # self.opacity_animation_out.start()

            self.ui.playBtn.setIcon(self.icon_play)
            self.ui.playBtn.setIconSize(QSize(42, 42))

        elif not self.MediaController.isPlaying:
            self.MediaController.resume()
            self.ui.playBtn.setIcon(self.icon_pause)
            self.ui.playBtn.setIconSize(QSize(42, 42))

    def setPlayPauseIcon(self, play):
        if play:
            self.ui.playBtn.setIcon(self.icon_pause)
            self.ui.playBtn.setIconSize(QSize(42, 42))

        else:
            self.ui.playBtn.setIcon(self.icon_play)
            self.ui.playBtn.setIconSize(QSize(42, 42))

        # elif self.isCurrentlyStreaming:
        #     if self.streamMediaPlayer.isPlaying:
        #         self.streamMediaPlayer.pauseMedia()
        #         self.ui.playBtn.setIcon(self.icon_play)
        #         self.ui.playBtn.setIconSize(QSize(42, 42))
        #         self.isCurrentlyStreaming = False
        #     else:
        #         self.MediaController.resumeMedia()
        #         self.ui.playBtn.setIcon(self.icon_pause)
        #         self.ui.playBtn.setIconSize(QSize(42, 42))
        #         self.isCurrentlyStreaming = True


    def on_volume_slider_released(self):
        # slider_value = self.ui.volume.value()
        
        slider_value = 100.0

        self.MediaController.setVolume(slider_value/100.0)
        self.toggle_volumeicons(slider_value)



    def fade(self, widget, duration=500):
        effect = QGraphicsOpacityEffect()
        widget.setGraphicsEffect(effect)
        animation = QPropertyAnimation(effect, b"opacity")
        animation.setDuration(duration)
        animation.setStartValue(1)
        animation.setEndValue(0)
        animation.start()

    def unfade(self, widget, duration=500):
        effect = QGraphicsOpacityEffect()
        widget.setGraphicsEffect(effect)
        animation = QPropertyAnimation(effect, b"opacity")
        animation.setDuration(duration)
        animation.setStartValue(0)
        animation.setEndValue(1)
        animation.start()


app_options = {'debug':True}

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = OctaveMusicWindow(app_options=app_options)
    sys.exit(app.exec_())
