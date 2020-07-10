from PyQt5 import QtCore, QtGui, QtWidgets, QtMultimediaWidgets,QtMultimedia
from PyQt5.QtGui import QIcon, QFont,QPalette,QColor, QMoveEvent, QKeySequence,QPainter,QImage
from PyQt5.QtCore import QDir, Qt, QUrl, QSize, Qt,QPoint, QRect, pyqtSignal
from PyQt5.QtMultimedia import QMediaContent, QMediaPlayer, QVideoFrame,QAbstractVideoBuffer,QVideoSurfaceFormat,QAbstractVideoSurface
from PyQt5.QtMultimediaWidgets import QVideoWidget
from PyQt5.QtWidgets import (QApplication, QFileDialog, QHBoxLayout, QLabel, 
        QPushButton, QSizePolicy, QSlider, QStyle, QVBoxLayout, QWidget, QStatusBar, QShortcut, QDialog)
import os
import requests, json, pickle
from translate import translateLang


# statusList = ['Video Settings', 'Select Video Quality', 'OK', 'Close', ' Enter URL', ' Status: Open File',
#                 'Select Media File', ' Status: Getting Video Online', 'Status: Fetching Video Details',
#                 'Status: Invalid URL', ' Status: URL Box Empty', 'Status: NO Online Video Playing','Status: Playing '
#                 ,'Status: Time in Wrong Format Be In (HH:MM:SS)',"Status : "]

class SettingDialog(QDialog):
    
    def __init__(self):
        super(SettingDialog, self).__init__()

        self.setObjectName("self")
        self.resize(477, 248)
        self.setStyleSheet("background-color:black;")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.close = QtWidgets.QPushButton(self)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.close.sizePolicy().hasHeightForWidth())
        self.close.setSizePolicy(sizePolicy)
        self.close.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.close.setText("")
        self.close.setIcon(QIcon('cross.png'))
        self.close.setIconSize(QtCore.QSize(16, 16))
        self.close.setDefault(False)
        self.close.setFlat(True)
        self.close.setObjectName("close")
        self.close.clicked.connect(self.exit)
        self.verticalLayout_2.addWidget(self.close)
        self.groupBox = QtWidgets.QGroupBox(self)
        self.groupBox.setStyleSheet(" QGroupBox\n"
"        {\n"
"            color: white;\n"
"            border: 5px solid #2f3338;\n"
"            font-weight: bold;\n"
"            font-size: 8pt;\n"
"        }")
        self.groupBox.setObjectName("groupBox")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.groupBox)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.scrollArea = QtWidgets.QScrollArea(self.groupBox)
        self.scrollArea.setStyleSheet("            color:rgb(255, 255, 255)    ;\n"
"            border: 0px solid #2f3338;\n"
"            font-weight: bold;\n"
"            font-size: 8pt;")
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 402, 337))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.scrollAreaWidgetContents)
        self.verticalLayout.setObjectName("verticalLayout")
        self.arabic_radio = QtWidgets.QRadioButton(self.scrollAreaWidgetContents)
        self.arabic_radio.setObjectName("arabic_radio")
        self.verticalLayout.addWidget(self.arabic_radio)
        self.bulgarian_radio = QtWidgets.QRadioButton(self.scrollAreaWidgetContents)
        self.bulgarian_radio.setObjectName("bulgarian_radio")
        self.verticalLayout.addWidget(self.bulgarian_radio)
        self.danish_radio = QtWidgets.QRadioButton(self.scrollAreaWidgetContents)
        self.danish_radio.setObjectName("danish_radio")
        self.verticalLayout.addWidget(self.danish_radio)
        self.english_radio = QtWidgets.QRadioButton(self.scrollAreaWidgetContents)
        self.english_radio.setObjectName("english_radio")
        self.verticalLayout.addWidget(self.english_radio)
        self.german_radio = QtWidgets.QRadioButton(self.scrollAreaWidgetContents)
        self.german_radio.setObjectName("german_radio")
        self.verticalLayout.addWidget(self.german_radio)
        self.greek_radio = QtWidgets.QRadioButton(self.scrollAreaWidgetContents)
        self.greek_radio.setObjectName("greek_radio")
        self.verticalLayout.addWidget(self.greek_radio)
        self.hindi_radio = QtWidgets.QRadioButton(self.scrollAreaWidgetContents)
        self.hindi_radio.setObjectName("hindi_radio")
        self.verticalLayout.addWidget(self.hindi_radio)
        self.italian_radio = QtWidgets.QRadioButton(self.scrollAreaWidgetContents)
        self.italian_radio.setObjectName("italian_radio")
        self.verticalLayout.addWidget(self.italian_radio)
        self.japanese_radio = QtWidgets.QRadioButton(self.scrollAreaWidgetContents)
        self.japanese_radio.setObjectName("japanese_radio")
        self.verticalLayout.addWidget(self.japanese_radio)
        self.korean_radio = QtWidgets.QRadioButton(self.scrollAreaWidgetContents)
        self.korean_radio.setObjectName("korean_radio")
        self.verticalLayout.addWidget(self.korean_radio)
        self.persian_radio = QtWidgets.QRadioButton(self.scrollAreaWidgetContents)
        self.persian_radio.setObjectName("persian")
        self.verticalLayout.addWidget(self.persian_radio)
        self.polish_radio = QtWidgets.QRadioButton(self.scrollAreaWidgetContents)
        self.polish_radio.setObjectName("polish_radio")
        self.verticalLayout.addWidget(self.polish_radio)
        self.spanish_radio = QtWidgets.QRadioButton(self.scrollAreaWidgetContents)
        self.spanish_radio.setObjectName("spanish_radio")
        self.verticalLayout.addWidget(self.spanish_radio)
        self.urdu_radio = QtWidgets.QRadioButton(self.scrollAreaWidgetContents)
        self.urdu_radio.setObjectName("urdu_radio")
        self.verticalLayout.addWidget(self.urdu_radio)
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.verticalLayout_3.addWidget(self.scrollArea)
        self.verticalLayout_2.addWidget(self.groupBox)


        self.language = [
                "English",
                "Spanish",
                "French",
                "Arabic",
                "Bulgarian",
                "Danish",
                "German",
                "Greek",
                "Persian",
                "Hindi",
                "Italian",
                "Japanese",
                "Korean",
                "Polish",
                "Urdu",
            ]
        
        QtCore.QMetaObject.connectSlotsByName(self)
        self.setTabOrder(self.scrollArea, self.arabic_radio)
        self.setTabOrder(self.arabic_radio, self.bulgarian_radio)
        self.setTabOrder(self.bulgarian_radio, self.danish_radio)
        self.setTabOrder(self.danish_radio, self.english_radio)
        self.setTabOrder(self.english_radio, self.german_radio)
        self.setTabOrder(self.german_radio, self.greek_radio)
        self.setTabOrder(self.greek_radio, self.hindi_radio)
        self.setTabOrder(self.hindi_radio, self.italian_radio)
        self.setTabOrder(self.italian_radio, self.japanese_radio)
        self.setTabOrder(self.japanese_radio, self.korean_radio)
        self.setTabOrder(self.korean_radio, self.persian_radio)
        self.setTabOrder(self.persian_radio, self.polish_radio)
        self.setTabOrder(self.polish_radio, self.spanish_radio)
        self.setTabOrder(self.spanish_radio, self.urdu_radio)

        self.btnList = [self.arabic_radio,
                        self.bulgarian_radio,
                        self.danish_radio,
                        self.english_radio,
                        self.german_radio,
                        self.greek_radio,
                        self.hindi_radio,
                        self.italian_radio,
                        self.japanese_radio,
                        self.korean_radio,
                        self.persian_radio,
                        self.polish_radio,
                        self.spanish_radio,
                        self.urdu_radio
                        ]

        self.arabic_radio.toggled.connect(self.checkRadio)
        self.bulgarian_radio.toggled.connect(self.checkRadio)
        self.danish_radio.toggled.connect(self.checkRadio)
        self.english_radio.toggled.connect(self.checkRadio)
        self.german_radio.toggled.connect(self.checkRadio)
        self.greek_radio.toggled.connect(self.checkRadio)
        self.hindi_radio.toggled.connect(self.checkRadio)
        self.italian_radio.toggled.connect(self.checkRadio)
        self.japanese_radio.toggled.connect(self.checkRadio)
        self.korean_radio.toggled.connect(self.checkRadio)
        self.persian_radio.toggled.connect(self.checkRadio)
        self.polish_radio.toggled.connect(self.checkRadio)
        self.spanish_radio.toggled.connect(self.checkRadio)
        self.urdu_radio.toggled.connect(self.checkRadio)
        
        
        _translate = QtCore.QCoreApplication.translate
        self.setWindowTitle(_translate("self", "self"))
        self.groupBox.setTitle(_translate("self", "Language"))
        self.arabic_radio.setText(_translate("self", "Arabic"))
        self.bulgarian_radio.setText(_translate("self", "Bulgarian"))
        self.danish_radio.setText(_translate("self", "Danish"))
        self.english_radio.setText(_translate("self", "English"))
        self.german_radio.setText(_translate("self", "German"))
        self.greek_radio.setText(_translate("self", "Greek"))
        self.hindi_radio.setText(_translate("self", "Hindi"))
        self.italian_radio.setText(_translate("self", "Italian"))
        self.japanese_radio.setText(_translate("self", "Japanese"))
        self.korean_radio.setText(_translate("self", "Korean"))
        self.persian_radio.setText(_translate("self", "Persian"))
        self.polish_radio.setText(_translate("self", "Polish"))
        self.spanish_radio.setText(_translate("self", "Spanish"))
        self.urdu_radio.setText(_translate("self", "Urdu"))
        
    def exit(self):
        self.hide()

    def checkRadio(self):
        for btn in self.btnList:
            if btn.isChecked():
                self.changeLanguage(btn.text())
                break
    
    def changeLanguage(self,lang):
        langdict = translateLang(lang)
        statusList = langdict['present']
        msg = QtWidgets.QMessageBox(self)
        msg.setWindowIcon(QIcon('play-button.ico'))
        msg.setIcon(QtWidgets.QMessageBox.Information)
        msg.setStyleSheet("color:White;")
        msg.setText("Restart Required to Apply Change")
        msg.setWindowTitle("! IMPORTANT")
        # msg.windowFlags(Qt.FramelessWindowHint)
        msg.setDetailedText("The details are as follows: Restart Required to change language")
        msg.show()
        # self.hide()

    def mouseMoveEvent (self, event):
        if event.buttons() == Qt.LeftButton:
            self.move(event.globalPos() \
                        - QPoint(int(self.geometry().width() / 2), int(self.geometry().height() / 2)))
            event.accept()  
    
class CustomDialog(QDialog):

    def __init__(self):
        super(CustomDialog, self).__init__()
        
        self.setObjectName("Dialog")
        self.resize(295, 127)
        self.verticalLayout = QtWidgets.QVBoxLayout(self)
        self.verticalLayout.setObjectName("verticalLayout")
        self.frame = QtWidgets.QFrame(self)
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.frame)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label = QtWidgets.QLabel(self.frame)
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        self.comboBox = QtWidgets.QComboBox(self.frame)
        self.comboBox.setObjectName("comboBox")
        self.horizontalLayout.addWidget(self.comboBox)
        self.verticalLayout.addWidget(self.frame)
        self.frame_2 = QtWidgets.QFrame(self)
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.frame_2)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.pushButton = QtWidgets.QPushButton(self.frame_2)
        self.pushButton.setObjectName("pushButton")
        self.horizontalLayout_2.addWidget(self.pushButton)
        self.pushButton_2 = QtWidgets.QPushButton(self.frame_2)
        self.pushButton_2.setObjectName("pushButton_2")
        self.horizontalLayout_2.addWidget(self.pushButton_2)
        self.verticalLayout.addWidget(self.frame_2)

        self.quality = 'best'
        self.setStyleSheet("background-color: black")
        self.frame.setStyleSheet(self.stylesheet())
        self.frame_2.setStyleSheet(self.stylesheet())

        self.pushButton.clicked.connect(self.ok)
        self.pushButton_2.clicked.connect(self.close)

        # Shortcut Assign
        shortcut = QtWidgets.QShortcut(QtGui.QKeySequence('Return'),self)
        shortcut.activated.connect(self.ok)
        shortcut = QtWidgets.QShortcut(QtGui.QKeySequence('q'),self)
        shortcut.activated.connect(self.close)

        QtCore.QMetaObject.connectSlotsByName(self)

        _translate = QtCore.QCoreApplication.translate
        self.setWindowTitle(_translate("Dialog", statusList[0]))
        self.label.setText(_translate("Dialog", statusList[1]))
        self.pushButton.setText(_translate("Dialog", statusList[2]))
        self.pushButton_2.setText(_translate("Dialog", statusList[3]))

    def ok(self):
        self.quality = self.comboBox.currentText()
        self.hide()

    def getQuality(self):
        return self.quality

    def additems(self, Iterable):
        for k in Iterable:
            self.comboBox.addItem(k)

    def close(self):
        self.hide()

    def stylesheet(self):
        return """
        QPushButton
        {
        background: #515757;
        color: black;
        border: 0px solid black;
        font-size: 8pt;
        font-weight: bold;
        background-color: grey;
        }
        QLabel
        {
        background: black;
        color: #585858;
        border: 0px solid #076100;
        font-size: 8pt;
        font-weight: bold;
        }
        QComboBox
        {
        background: #515757;
        color: black;
        cursor:pointer;
        border: 0px solid black;
        font-size: 8pt;
        font-weight: bold;
        background-color: grey;
        }
        QComboBox QAbstractItemView 
        {
        background: #515757;
        border: 2px solid darkgray;
        selection-background-color: #5f7cd9;
        }
        """


class window(QWidget):
    def leaveEvent(self, event):
        if ui.isMini :
            ui.frame_2.hide()
            ui.pos_frame.hide()
            ui.frame.hide()

    def enterEvent(self, event):
        if ui.isMini:
            ui.frame_2.show()
            ui.pos_frame.show()
            ui.frame.show()

class Videowidget(QVideoWidget):
    def __init__(self,master):
        super().__init__(parent = master)

    def mouseMoveEvent (self, event):
        if event.buttons() == Qt.LeftButton:
            Form.move(event.globalPos() \
                        - QPoint(int(Form.geometry().width() / 2), int(Form.geometry().height() / 2)))
            event.accept()  

    def mouseDoubleClickEvent (self, event):
        if event.buttons() == Qt.LeftButton:
            ui.fullscreen_video()

    
        

class PosSlider(QSlider):
    def __init__(self,master):
        super().__init__(parent = master)
          
    def mousePressEvent (self, event):
        if event.buttons() == Qt.LeftButton:
            ui.mediaPlayer.setPosition(QStyle.sliderValueFromPosition(self.minimum(), self.maximum(), event.x(), self.width()))
            

    def mouseMoveEvent (self, event):
        if event.buttons() == Qt.LeftButton:
            ui.mediaPlayer.setPosition(QStyle.sliderValueFromPosition(self.minimum(), self.maximum(), event.x(), self.width()))


class VolSlider(QSlider):
    def __init__(self,master):
        super().__init__(parent = master)
          
    def mousePressEvent (self, event):
        if event.buttons() == Qt.LeftButton:
            self.setValue(QStyle.sliderValueFromPosition(self.minimum(), self.maximum(), event.x(), self.width()))
            

    def mouseMoveEvent (self, event):
        if event.buttons() == Qt.LeftButton:
            self.setValue(QStyle.sliderValueFromPosition(self.minimum(), self.maximum(), event.x(), self.width()))


    
class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(767, 496)
        self.isOnline = False
        self.isMini = False
        self.isOnTop = True
        self.mediaPlayer = QMediaPlayer(None,QMediaPlayer.VideoSurface)
    
    
        self.verticalLayout = QtWidgets.QVBoxLayout(Form)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName("verticalLayout")

        self.video_playback = Videowidget(Form)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(200)
        sizePolicy.setHeightForWidth(self.video_playback.sizePolicy().hasHeightForWidth())
        self.video_playback.setSizePolicy(sizePolicy)
        

        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Light, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Midlight, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Dark, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Mid, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.BrightText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Shadow, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.AlternateBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 220))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.ToolTipBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.ToolTipText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Light, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Midlight, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Dark, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Mid, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.BrightText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Shadow, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.AlternateBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 220))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.ToolTipBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.ToolTipText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Light, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Midlight, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Dark, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Mid, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.BrightText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Shadow, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.AlternateBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 220))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.ToolTipBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.ToolTipText, brush)

        self.video_playback.setPalette(palette)
        self.video_playback.setMouseTracking(False)
        self.video_playback.setTabletTracking(False)
        self.video_playback.setAcceptDrops(False)
        self.video_playback.setAutoFillBackground(True)
        # self.video_playback.setFrameShape(QtWidgets.QFrame.StyledPanel)
        # self.video_playback.setFrameShadow(QtWidgets.QFrame.Raised)
        self.video_playback.setObjectName("video_playback")
        self.verticalLayout.addWidget(self.video_playback)
        
        self.pos_frame = QtWidgets.QFrame(Form)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(10)
        sizePolicy.setHeightForWidth(self.pos_frame.sizePolicy().hasHeightForWidth())
        self.pos_frame.setSizePolicy(sizePolicy)
        self.pos_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.pos_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.pos_frame.setObjectName("pos_frame")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.pos_frame)
        self.horizontalLayout.setObjectName("horizontalLayout")

        self.duration_status = QtWidgets.QLabel(self.pos_frame)
        font = QtGui.QFont()
        font.setFamily("Lucida Console")
        font.setPointSize(7)
        self.duration_status.setFont(font)
        self.duration_status.setObjectName("duration_status")
        self.horizontalLayout.addWidget(self.duration_status)

        self.position_slider = PosSlider(self.pos_frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(100)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.position_slider.sizePolicy().hasHeightForWidth())
        self.position_slider.setSizePolicy(sizePolicy)
        self.position_slider.setAutoFillBackground(True)
        self.position_slider.setOrientation(QtCore.Qt.Horizontal)
        self.position_slider.setObjectName("position_slider")
        self.horizontalLayout.addWidget(self.position_slider)
        
        self.time_status = QtWidgets.QLabel(self.pos_frame)
        font = QtGui.QFont()
        font.setFamily("Lucida Console")
        font.setPointSize(7)
        self.time_status.setFont(font)
        self.time_status.setObjectName("time_status")
        self.horizontalLayout.addWidget(self.time_status)
        self.verticalLayout.addWidget(self.pos_frame)
       
        self.frame_2 = QtWidgets.QFrame(Form)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(20)
        sizePolicy.setHeightForWidth(self.frame_2.sizePolicy().hasHeightForWidth())
        self.frame_2.setSizePolicy(sizePolicy)
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.frame_2)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        
        self.play_button = QtWidgets.QPushButton(self.frame_2)
        self.play_button.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.play_button.setText("")
        self.play_button.setIcon(QIcon("play.png"))
        self.play_button.setEnabled(False)
        self.play_button.setObjectName("play_button")
        
        self.horizontalLayout_4.addWidget(self.play_button)
        
        self.playback_button = QtWidgets.QPushButton(self.frame_2)
        self.playback_button.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.playback_button.setText("")
        self.playback_button.setIcon(QIcon(QtGui.QPixmap('stopplayback.png')))
        self.playback_button.setObjectName("playback_button")
        self.horizontalLayout_4.addWidget(self.playback_button)
        
        self.stop_button = QtWidgets.QPushButton(self.frame_2)
        self.stop_button.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.stop_button.setText("")
        self.stop_button.setIcon(QIcon("stop.png"))
        self.stop_button.setObjectName("stop_button")
        self.horizontalLayout_4.addWidget(self.stop_button)
        self.stop_button.clicked.connect(self.stop)

        
        self.open_file_button = QtWidgets.QPushButton(self.frame_2)
        self.open_file_button.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.open_file_button.setText("")
        self.open_file_button.setIcon(QIcon('newfile.png'))
        self.open_file_button.setObjectName("open_file_button")
        self.horizontalLayout_4.addWidget(self.open_file_button)

        self.miniplayer_button = QtWidgets.QPushButton(self.frame_2)
        self.miniplayer_button.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.miniplayer_button.setText("")
        self.miniplayer_button.setIcon(QIcon(QtGui.QPixmap('m.png')))
        self.miniplayer_button.setObjectName("miniplayer_button")
        self.horizontalLayout_4.addWidget(self.miniplayer_button)
        
        self.always_on_top_button = QtWidgets.QPushButton(self.frame_2)
        self.always_on_top_button.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.always_on_top_button.setText("")
        self.always_on_top_button.setIcon(QIcon(QtGui.QPixmap('top_on.png')))
        self.always_on_top_button.setObjectName("always_on_top_button_button")
        self.horizontalLayout_4.addWidget(self.always_on_top_button)
        self.always_on_top_button.clicked.connect(self.checkOnTop)
        
        
        self.set_time = QtWidgets.QLineEdit(self.frame_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.set_time.sizePolicy().hasHeightForWidth())
        self.set_time.setSizePolicy(sizePolicy)
        self.set_time.setInputMethodHints(QtCore.Qt.ImhTime)
        self.set_time.setReadOnly(False)
        self.set_time.setClearButtonEnabled(False)
        self.set_time.setObjectName("set_time")
        self.horizontalLayout_4.addWidget(self.set_time)
        
        self.set_position_button = QtWidgets.QPushButton(self.frame_2)
        self.set_position_button.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.set_position_button.setText("")
        self.set_position_button.setIcon(QIcon('tick.png'))
        self.set_position_button.setObjectName("set_position_button")
        self.horizontalLayout_4.addWidget(self.set_position_button)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem)
        
        self.screenshot_button = QtWidgets.QPushButton(self.frame_2)
        self.screenshot_button.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.screenshot_button.setText("")
        self.screenshot_button.setIcon(QIcon(QtGui.QPixmap('screenshot.png')))
        self.screenshot_button.setObjectName("screenshot_button")
        self.horizontalLayout_4.addWidget(self.screenshot_button)
        
        self.video_setting_button = QtWidgets.QPushButton(self.frame_2)
        self.video_setting_button.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.video_setting_button.setText("")
        self.video_setting_button.setIcon(QIcon(QtGui.QPixmap('video_settings.png')))
        self.video_setting_button.setIconSize(QtCore.QSize(20, 20))
        
        self.horizontalLayout_4.addWidget(self.video_setting_button)
        
        self.fullscreen_button = QtWidgets.QPushButton(self.frame_2)
        self.fullscreen_button.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.fullscreen_button.setIcon(QIcon("fullscreen.png"))
        self.fullscreen_button.setIconSize(QtCore.QSize(16, 16))
        self.fullscreen_button.setObjectName("fullscreen_button")
        self.horizontalLayout_4.addWidget(self.fullscreen_button)
        self.fullscreen_button.clicked.connect(self.fullscreen_video)
        
        self.setting_button = QtWidgets.QPushButton(self.frame_2)
        self.setting_button.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.setting_button.setText("")
        self.setting_button.setIcon(QIcon('settings.png'))
        self.setting_button.setIconSize(QtCore.QSize(20, 20))
        self.setting_button.setObjectName("setting_button")
        self.horizontalLayout_4.addWidget(self.setting_button)
        
        self.volume_button = QtWidgets.QPushButton(self.frame_2)
        self.volume_button.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.volume_button.setText("")
        self.volume_button.setIconSize(QtCore.QSize(15, 15))
        self.volume_button.setCheckable(True)
        self.volume_button.setFlat(True)
        self.volume_button.setIcon(QIcon("full_volume.png"))
        self.volume_button.setObjectName("volume_button")
        self.horizontalLayout_4.addWidget(self.volume_button)
        
        self.volumeslider = VolSlider(self.frame_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.volumeslider.sizePolicy().hasHeightForWidth())
        self.volumeslider.setSizePolicy(sizePolicy)
        self.volumeslider.setAutoFillBackground(True)
        self.volumeslider.setOrientation(QtCore.Qt.Horizontal)
        self.volumeslider.setObjectName("volume_slider")
        self.horizontalLayout_4.addWidget(self.volumeslider)
        self.verticalLayout.addWidget(self.frame_2)
        
        self.frame = QtWidgets.QFrame(Form)
        font = QtGui.QFont()
        font.setFamily("Lucida Console")
        self.frame.setFont(font)
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout(self.frame)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.enter_url_label = QtWidgets.QLabel(self.frame)
        font = QtGui.QFont()
        font.setFamily("Lucida Console")
        font.setPointSize(10)
        self.enter_url_label.setFont(font)
        self.enter_url_label.setObjectName("enter_url_label")
        self.horizontalLayout_5.addWidget(self.enter_url_label)
        self.url_box = QtWidgets.QComboBox(self.frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(200)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.url_box.sizePolicy().hasHeightForWidth())
        self.url_box.setSizePolicy(sizePolicy)
        self.url_box.setInputMethodHints(QtCore.Qt.ImhUrlCharactersOnly)
        self.url_box.setEditable(True)
        self.url_box.setCurrentText("")
        self.url_box.setMaxVisibleItems(100)
        self.url_box.setInsertPolicy(QtWidgets.QComboBox.InsertAtTop)
        self.url_box.setSizeAdjustPolicy(QtWidgets.QComboBox.AdjustToContentsOnFirstShow)
        self.url_box.setMinimumContentsLength(2)
        self.url_box.setDuplicatesEnabled(False)
        self.url_box.setFrame(True)
        self.url_box.setObjectName("url_box")
        self.horizontalLayout_5.addWidget(self.url_box)

        self.url_search_button = QtWidgets.QPushButton(self.frame_2)
        self.url_search_button.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.url_search_button.setText("")
        self.url_search_button.setIcon(QIcon('urlSearch.png'))
        self.url_search_button.setObjectName("open_file_button")
        self.horizontalLayout_5.addWidget(self.url_search_button)
        self.verticalLayout.addWidget(self.frame)
        
        
        self.frame_3 = QtWidgets.QFrame(Form)
        self.frame_3.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_3.setObjectName("frame_3")
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout(self.frame_3)
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        
        font = QtGui.QFont()
        font.setFamily("Lucida Console")
        font.setPointSize(10)
        self.status_label = QtWidgets.QLabel(self.frame_3)
        self.status_label.setFont(font)
        self.status_label.setObjectName("status_label")
        self.horizontalLayout_6.addWidget(self.status_label)
        self.verticalLayout.addWidget(self.frame_3)

        # Setting Icons to button
        
        # self.video_setting_button.setIcon(QIcon("video_settings.png"))
        # self.setting_button.setIcon(QIcon("settings.png"))
        # self.volume_button.setIcon(QIcon("full_volume.png"))
        # self.screenshot_button.setIcon(QIcon("screenshot.png"))
        
        
        # self.miniplayer_button.setIcon(QIcon('miniplayer.png'))
        self.volumeslider.setRange(0,100)
        self.volumeslider.setValue(75)
        self.mediaPlayer.setVolume(75)
        self.position_slider.setRange(0,100)

        self.url_box.setDuplicatesEnabled(False)
        
        self.miniplayer_button.clicked.connect(self.setupMiniPlayer)
        self.position_slider.sliderMoved.connect(self.setPosition)
        self.position_slider.sliderMoved.connect(self.handleLabel)
        self.volume_button.clicked.connect(self.mute)
        self.volumeslider.valueChanged.connect(self.setVolume)
        self.screenshot_button.clicked.connect(self.screenshot)
        self.playback_button.clicked.connect(self.stopplayback)
        self.open_file_button.clicked.connect(self.open_file)
        self.play_button.clicked.connect(self.play)
        self.video_setting_button.clicked.connect(self.handleQuality)
        self.url_search_button.clicked.connect(self.playOnline)
        self.setting_button.clicked.connect(self.handleSetting)
        # self.close_button.clicked.connect(self.exit)
        self.set_position_button.clicked.connect(self.setGivenPos)
        
        shortcut = QShortcut(QKeySequence('Esc'),self.video_playback)
        shortcut.activated.connect(self.EscFun)
        shortcut = QShortcut(QKeySequence('Space'),self.video_playback)
        shortcut.activated.connect(self.play)
        shortcut = QShortcut(QKeySequence('f'),self.video_playback)
        shortcut.activated.connect(self.fullscreen_video)
        shortcut = QShortcut(QKeySequence('o'),self.video_playback)
        shortcut.activated.connect(self.open_file)
        shortcut = QShortcut(QKeySequence('v'),self.video_playback)
        shortcut.activated.connect(self.handleQuality)
        shortcut = QShortcut(QKeySequence("Return"),self.video_playback)
        shortcut.activated.connect(self.playOnline)
        shortcut = QShortcut(QKeySequence('m'),self.video_playback)
        shortcut.activated.connect(self.mute)
        shortcut = QShortcut(QKeySequence(Qt.Key_Right), self.video_playback)
        shortcut.activated.connect(self.forwardSlider)
        shortcut = QShortcut(QKeySequence(Qt.Key_Left), self.video_playback)
        shortcut.activated.connect(self.backSlider)
        shortcut = QShortcut(QKeySequence(Qt.Key_Up), self.video_playback)
        shortcut.activated.connect(self.volumeUp)
        shortcut = QShortcut(QKeySequence(Qt.Key_Down), self.video_playback)
        shortcut.activated.connect(self.volumeDown)    
        shortcut = QShortcut(QKeySequence(Qt.ControlModifier +  Qt.Key_Right) , self.video_playback)
        shortcut.activated.connect(self.forwardSlider10)
        shortcut = QShortcut(QKeySequence(Qt.ControlModifier +  Qt.Key_Left) , self.video_playback)
        shortcut.activated.connect(self.backSlider10)
        shortcut = QShortcut(QKeySequence(Qt.AltModifier +  Qt.Key_Left) , self.video_playback)
        shortcut.activated.connect(self.backSlider5)    
        shortcut = QShortcut(QKeySequence(Qt.AltModifier +  Qt.Key_Right) , self.video_playback)
        shortcut.activated.connect(self.forwardSlider5) 
        
        items = self.load()
        self.url_box.addItems(items)
        self.mediaPlayer.setVideoOutput(self.video_playback)
        self.mediaPlayer.stateChanged.connect(self.mediaStateChanged)
        self.mediaPlayer.positionChanged.connect(self.positionChanged)
        self.mediaPlayer.positionChanged.connect(self.handleLabel)
        self.mediaPlayer.durationChanged.connect(self.durationChanged)
    
        # self.video_playback.mouseMoveEvent(self.mouseMoveEvent)
        

        self.frame.setStyleSheet(self.stylesheet())
        self.frame_2.setStyleSheet(self.stylesheet())
        self.frame_3.setStyleSheet(self.stylesheet())
        # self.position_slider.setStyleSheet(self.stylesheet())
        self.volumeslider.setStyleSheet(self.stylesheet())
        self.position_slider.setAttribute(Qt.WA_TranslucentBackground, True)
        self.pos_frame.setStyleSheet(self.stylesheet())
        
        Form.setStyleSheet("background-color: black;border-color:white;")
        
        self.retranslateUi(Form)
        self.url_box.setCurrentIndex(-1)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Q-Stream Player"))
        self.time_status.setText(_translate("Form", "00:00:00"))
        self.duration_status.setText(_translate("Form", "00:00:00"))
        self.set_time.setText(_translate("Form", "00:00:00"))
        self.enter_url_label.setText(_translate("Form", statusList[4]))
        self.status_label.setText(_translate("Form",  statusList[14]))
        
    
    def handleLabel(self):
        self.time_status.clear()
        mtime = QtCore.QTime(0,0,0,0)
        self.time = mtime.addMSecs(self.mediaPlayer.position())
        self.time_status.setText(self.time.toString())

    def hide_all(self):
        self.frame_3.close()
        self.frame.close()
        self.playback_button.close()
        self.stop_button.close()
        self.open_file_button.close()
        self.set_time.close()
        self.set_position_button.close()
        self.screenshot_button.close()
        self.video_setting_button.close()
        self.setting_button.close()
        self.fullscreen_button.close()
    
    def show_all(self):
        self.frame_3.show()
        self.frame.show()
        self.playback_button.show()
        self.stop_button.show()
        self.open_file_button.show()
        self.set_time.show()
        self.set_position_button.show()
        self.screenshot_button.show()
        self.video_setting_button.show()
        self.setting_button.show()
        self.fullscreen_button.show()


    def checkOnTop(self):
        self.isOnTop = not self.isOnTop
        if self.isOnTop:
            self.always_on_top_button.setIcon(QIcon('top_on.png'))
            Form.setWindowFlags(Form.windowFlags() | QtCore.Qt.WindowStaysOnTopHint)
        else:
            self.always_on_top_button.setIcon(QIcon('top_off.png'))
            Form.setWindowFlags(Form.windowFlags() & ~QtCore.Qt.WindowStaysOnTopHint)
        
        Form.show()
        
    def setupMiniPlayer(self):
        self.isMini = not self.isMini
        if  self.isMini:
            self.miniplayer_button.setIcon(QIcon('s.png'))
            self.hide_all()
            Form.resize(600,400)
        else:
            Form.resize(767, 496)
            self.miniplayer_button.setIcon(QIcon('m.png'))
            self.show_all()

        
    def load(self):
        scorefile = "db.bat"
        if os.path.exists(scorefile):
            with open(scorefile, 'rb') as sf:
                scores = pickle.load(sf)
        else:
            scores = []

        with open(scorefile, "wb") as sf:
            pickle.dump(scores, sf)
        return scores

    def changestats(self):
        self.status_label.setText("Restart required to apply change")
    def scor_func(self, url):
        scorefile = "db.bat"
        if os.path.exists(scorefile):
            with open(scorefile, 'rb') as sf:
                scores = pickle.load(sf)
        else:
            scores = []
        scores.append(url)

        with open(scorefile, "wb") as sf:
            if len(scores) > 100:
                print("here", scores)
                scores = scores[1:]
            pickle.dump(scores, sf)
        return scores

    def mute(self):
        if self.mediaPlayer.isMuted():
            print('[ ! Full Volume]')
            self.mediaPlayer.setMuted(False)
            self.volume_button.setIcon(QIcon('full_volume.png'))
            # self.volumeslider.setEnabled(True)
        else:
            print('[ ! Mute Volume]')
            self.mediaPlayer.setMuted(True)
            self.volume_button.setIcon(QIcon('mute.png'))
            # self.volumeslider.setEnabled(False)

    def play(self):
        if self.mediaPlayer.isVideoAvailable():
            if self.mediaPlayer.state() == QMediaPlayer.PlayingState:
                print("[ ! PAUSE PRESSED ]")
                self.mediaPlayer.pause()
                
            else:
                print("[ ! PLAY PRESSED ]")
                self.mediaPlayer.play()
                
        else:
            self.open_file()
    
    def open_file(self):
        print('[ ! OPEN FILE ]')
        self.status_label.setText(statusList[5])
        fileName, _ = QFileDialog.getOpenFileName(self.video_playback, statusList[6],
                QDir.homePath() + "/Videos", "Video Files (*.mp4 *.flv *.ts *.mts *.avi )")
        if fileName != '':
            self.mediaPlayer.setMedia(QMediaContent(QUrl.fromLocalFile(fileName)))
            isOnline = False
            self.play_video()

    def playOnline(self):
        

        self.preQuality = 'best'
        if self.url_box.currentText() != '':
            self.status_label.setText(statusList[7])
            print('[ ! GETTING VIDEO ONLINE ]')
            fileName = self.url_box.currentText()
            res = requests.get('https://mediaplayerserver.herokuapp.com/', params={"key": fileName})
            try:
                self.status_label.setText(statusList[8])
                self.streams = json.loads(res.text)
                
                try:
                    self.mediaPlayer.setMedia(QMediaContent(QUrl(self.streams[self.preQuality])))
                    self.play_video()
                    self.isOnline = True
                    self.status_label.setText(statusList[12]+ " " + fileName)
                    if self.url_box.findText(fileName,Qt.MatchExactly) < 0:
                        self.url_box.addItem(fileName)
                        self.scor_func(fileName)
                except KeyError:
                    self.status_label.setText(statusList[15])
                    print("[ ! Error Video Not Supported By platform]")
                
            except json.JSONDecodeError:
                print("[ ! Error NoPluginError]")
                self.status_label.setText(statusList[9])
            finally:
                self.url_box.setCurrentText("")
            
        else:
            self.status_label.setText(statusList[10])
            
    def play_video(self):   
        print('[ ! PLAYING VIDEO ]')
        self.play_button.setEnabled(True)
        self.play_button.setIcon(QIcon('play.png'))
        if self.mediaPlayer.state() == QMediaPlayer.PlayingState:
            self.mediaPlayer.pause()
        else:
            self.mediaPlayer.play()

    def mediaStateChanged(self, state):
        print('[ ! CHANGING MEDIA STATE ]')
        if self.mediaPlayer.state() == QMediaPlayer.PlayingState:
            self.play_button.setIconSize(QSize(25,25))
            self.play_button.setIcon(QIcon("pause.png"))
        else:
            self.play_button.setIcon(QIcon("play.png"))

    def stop(self):
        print('[ ! STOP VIDEO ]')
        self.mediaPlayer.stop()
        if self.mediaPlayer.state() != QMediaPlayer.PlayingState:
            self.play_button.setIcon(QIcon("play.png"))
            

    def stopplayback(self):
        print('[ ! STOP PLAYBACK VIDEO ]')
        self.stop()
        self.play_video()

    def positionChanged(self, position):
        print('[ ! POSITION CHANGED ]')
        self.position_slider.setValue(position)

    def durationChanged(self, duration):
        print('[ ! DURATION CHANGED ]')
        self.position_slider.setRange(0, duration)
        self.duration_status.clear()
        mtime = QtCore.QTime(0,0,0,0)
        time = mtime.addMSecs(self.mediaPlayer.duration())
        self.duration_status.setText(time.toString())

    def setPosition(self, position):
        print('[ ! POSITION SET ]')
        self.mediaPlayer.setPosition(position)
    

    def setVolumePos(self,remain):
        print('[ ! REMANING VOLUME ]')
        print(remain)
        self.volumeslider.setRange(remain,100)
        
    def setVolume(self,vol):
        print('[ ! SET VOLUME ]')
        print("set volume  = " + str(vol))
        self.volumeslider.setValue(vol)
        self.mediaPlayer.setVolume(vol)
    
    def screenshot(self):
        import pyautogui, uuid, getpass

        print('[ ! SCREENSHOT ]')
        wincen = Form.geometry() 
        print(wincen)
        topX = wincen.topLeft().x()
        topY = wincen.topLeft().y()
        username = getpass.getuser()
        geo = self.video_playback.geometry()
        image = pyautogui.screenshot(region=(topX, topY, geo.width(), geo.height()))
        filename = "screenshot" + str(uuid.uuid4()) + ".png"
        path = 'C:/Users/'+username+'/Pictures/'+filename
        image.save(path)
        
        
    def EscFun(self):
        if self.video_playback.isFullScreen():
            Form.show()
            self.video_playback.setFullScreen(False)
            

    def fullscreen_video(self):
        if self.mediaPlayer.isVideoAvailable():
            if self.video_playback.isFullScreen():
                Form.show()
                self.video_playback.setFullScreen(False)
                print('[ ! Full Screen ]')
            else:
                Form.hide()
                print('[ ! Normal Screen ]')
                self.video_playback.setFullScreen(True)
    
    def getFormat(self):
        li = [k for k in self.streams.keys()]
        for q in li:
            if q.startswith('audio'):
                li.remove(q)
                try:
                    li.remove('audio_opus')
                except ValueError:
                    pass
        return li

    def setGivenPos(self):
        import time
        import datetime
        try:
            x = time.strptime(self.set_time.text().split(',')[0],'%H:%M:%S')
            mtime = datetime.timedelta(hours=x.tm_hour,minutes=x.tm_min,seconds=x.tm_sec).total_seconds()
            self.setPosition(mtime * 1000)
        except ValueError:
            self.status_label.setText(statusList[13])

    def changeQuality(self,quality):
        if quality != self.preQuality:
             self.preQuality = quality
             pos = self.mediaPlayer.position()
             self.mediaPlayer.setMedia(QMediaContent(QUrl(self.streams[self.preQuality])))
             self.setPosition(pos)
             self.mediaPlayer.play()
             
    def handleSetting(self):
        dlg = SettingDialog()
        dlg.setWindowFlags(Qt.FramelessWindowHint | Qt.WindowStaysOnTopHint )
        dlg.exec_()
         
    def handleQuality(self):
        if self.isOnline:        
            dlg = CustomDialog()
            dlg.setWindowFlags(Qt.FramelessWindowHint | Qt.WindowStaysOnTopHint)
            dlg.additems(self.getFormat())
            dlg.exec_()
            self.changeQuality(dlg.getQuality())
        else:
            self.status_label.setText(statusList[11])
    
    def forwardSlider(self):
        self.mediaPlayer.setPosition(self.mediaPlayer.position() + 1000)

    def forwardSlider10(self):
            self.mediaPlayer.setPosition(self.mediaPlayer.position() + 10000)
    
    def forwardSlider5(self):
            self.mediaPlayer.setPosition(self.mediaPlayer.position() + 5000)

    def backSlider(self):
        self.mediaPlayer.setPosition(self.mediaPlayer.position() - 1000)

    def backSlider10(self):
        self.mediaPlayer.setPosition(self.mediaPlayer.position() - 10000)

    def backSlider5(self):
        self.mediaPlayer.setPosition(self.mediaPlayer.position() - 5000)    

    def volumeUp(self):
        self.setVolume(self.mediaPlayer.volume() + 10)
        print("Volume: " + str(self.mediaPlayer.volume()))
    
    def volumeDown(self):
        self.setVolume(self.mediaPlayer.volume() - 10)
        print("Volume: " + str(self.mediaPlayer.volume()))
    

    def exit(self):
        self.mediaPlayer.stop()
        print("Goodbye ...")
        app.quit()


    def stylesheet(self):
        return """
    QSlider::handle:horizontal 
    {
    background: transparent;
    width: 8px;
    }
    QSlider::groove:horizontal {
    border: 1px solid #444444;
    height: 8px;
    background: qlineargradient(y1: 0, y2: 1,stop: 0 #2e3436, stop: 1.0 #000000);
    }
    QSlider::sub-page:horizontal {
    background: qlineargradient( y1: 0, y2: 1,
        stop: 0 #729fcf, stop: 1 #2a82da);
    border: 1px solid #777;
    height: 8px;
    }
    QSlider::handle:horizontal:hover {
    background: #2a82da;
    height: 8px;
    width: 8px;
    border: 1px solid #2e3436;
    }
    QSlider::sub-page:horizontal:disabled {
    background: #bbbbbb;
    border-color: #999999;
    }
    QSlider::add-page:horizontal:disabled {
    background: #2a82da;
    border-color: #999999;
    }
    QSlider::handle:horizontal:disabled {
    background: #2a82da;
    }
    QLineEdit
    {
    background: black;
    color: #515757;
    border: 0px solid white;
    font-size: 8pt;
    font-weight: bold;
    }
    QLabel
    {
    background: black;
    color: #bfbeba;
    border: 0px solid #076100;
    font-size: 8pt;
    font-weight: bold;
    }
    QComboBox
    {
    background: #515757;
    color: black;
    border: 0px solid black;
    font-size: 8pt;
    font-weight: bold;
    background-color: grey;
    }
    QComboBox QAbstractItemView 
    {
    background: #515757;
    border: 2px solid darkgray;
    selection-background-color: #5f7cd9;
    }
    """

# def setup():
#     app = QtWidgets.QApplication(sys.argv)
#     newForm = QtWidgets.QWidget()
#     ui = Ui_Form()
#     ui.setupUi(newForm)
#     newForm.show()
#     sys.exit(app.exec_())


    
    
if __name__ == "__main__":
    import sys
    with open("lang.bat", 'rb') as sf:
        langs = pickle.load(sf)
        statusList =  langs['present']
    

    app = QtWidgets.QApplication(sys.argv)
    app.setWindowIcon(QIcon('play-button.ico'))
    Form = window()
    Form.setWindowFlags(Qt.WindowStaysOnTopHint)
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
    
   
