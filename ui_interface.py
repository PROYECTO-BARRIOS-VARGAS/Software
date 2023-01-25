# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'interfacesBeZSG.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *

from Custom_Widgets.Widgets import QCustomSlideMenu
from Custom_Widgets.Widgets import QCustomStackedWidget

import resources_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1642, 954)
        MainWindow.setMaximumSize(QSize(10000, 10000))
        font = QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        MainWindow.setFont(font)
        MainWindow.setStyleSheet(u"*{\n"
"	border:none;\n"
"	background-color:transparent;\n"
"	background:transparent;\n"
"	padding: 0.031em;\n"
"	margin: 0.031em;\n"
"}\n"
"#MainWindow{\n"
"	height: 700%;\n"
"	width: 900%;\n"
"	max-height: 500%;\n"
"	max-width: 700%;\n"
"}\n"
"#headerContainer,#leftMenuSubContainer{\n"
"	background-color:rgb(65, 67, 95)\n"
"}\n"
"#leftMenuSubContainer QPushButton{\n"
"	text-align: left;\n"
"	padding: 0.313em 0.625em;\n"
"	border-top-left-radius: 10px;\n"
"	border-bottom-left-radius: 10px;\n"
"}\n"
"#centerMenuSubContainer,#rightMenuSubContainer, #mainBodyContent{\n"
"	background-color:#1c2833;\n"
"}\n"
"#footerContainer{\n"
"	background-color:#a49fa5;\n"
"}\n"
"#frame_9, #frame_10{\n"
"	border-radius: 10px;\n"
"}\n"
"#headerContainer{\n"
"	height: 150%;\n"
"}\n"
"#frame_8{\n"
"	background-color: #fdfcf4;\n"
"	border-radius: 10px;\n"
"}\n"
"\n"
"\n"
"\n"
"\n"
"\n"
"")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setStyleSheet(u"")
        self.horizontalLayout = QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.leftMenuContainer = QCustomSlideMenu(self.centralwidget)
        self.leftMenuContainer.setObjectName(u"leftMenuContainer")
        self.leftMenuContainer.setMaximumSize(QSize(45, 16777215))
        self.verticalLayout = QVBoxLayout(self.leftMenuContainer)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.leftMenuSubContainer = QWidget(self.leftMenuContainer)
        self.leftMenuSubContainer.setObjectName(u"leftMenuSubContainer")
        self.leftMenuSubContainer.setStyleSheet(u"QWidget{\n"
"	width: 900%;\n"
"}")
        self.verticalLayout_2 = QVBoxLayout(self.leftMenuSubContainer)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(5, 0, 0, 0)
        self.frame = QFrame(self.leftMenuSubContainer)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.frame)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.menuBtn = QPushButton(self.frame)
        self.menuBtn.setObjectName(u"menuBtn")
        icon = QIcon()
        icon.addFile(u":/icons/icons/align-justify.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.menuBtn.setIcon(icon)
        self.menuBtn.setIconSize(QSize(24, 24))

        self.horizontalLayout_2.addWidget(self.menuBtn)


        self.verticalLayout_2.addWidget(self.frame, 0, Qt.AlignTop)

        self.frame_2 = QFrame(self.leftMenuSubContainer)
        self.frame_2.setObjectName(u"frame_2")
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_2.sizePolicy().hasHeightForWidth())
        self.frame_2.setSizePolicy(sizePolicy)
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.frame_2)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 10, 0, 10)
        self.homeBtn = QPushButton(self.frame_2)
        self.homeBtn.setObjectName(u"homeBtn")
        self.homeBtn.setFont(font)
        self.homeBtn.setStyleSheet(u"background-color: #fdfcf4;\n"
"\n"
"\n"
"")
        icon1 = QIcon()
        icon1.addFile(u":/icons/icons/home.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.homeBtn.setIcon(icon1)
        self.homeBtn.setIconSize(QSize(24, 24))

        self.verticalLayout_3.addWidget(self.homeBtn)

        self.DBBtn = QPushButton(self.frame_2)
        self.DBBtn.setObjectName(u"DBBtn")
        self.DBBtn.setEnabled(True)
        self.DBBtn.setFont(font)
        self.DBBtn.setStyleSheet(u"color: #ffffff;")
        icon2 = QIcon()
        icon2.addFile(u":/icons/icons/database.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.DBBtn.setIcon(icon2)
        self.DBBtn.setIconSize(QSize(24, 24))

        self.verticalLayout_3.addWidget(self.DBBtn)

        self.logsBtn = QPushButton(self.frame_2)
        self.logsBtn.setObjectName(u"logsBtn")
        self.logsBtn.setFont(font)
        self.logsBtn.setStyleSheet(u"color: #ffffff;")
        icon3 = QIcon()
        icon3.addFile(u":/icons/icons/archive.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.logsBtn.setIcon(icon3)
        self.logsBtn.setIconSize(QSize(24, 24))

        self.verticalLayout_3.addWidget(self.logsBtn)


        self.verticalLayout_2.addWidget(self.frame_2, 0, Qt.AlignTop)

        self.frame_3 = QFrame(self.leftMenuSubContainer)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.verticalLayout_4 = QVBoxLayout(self.frame_3)
        self.verticalLayout_4.setSpacing(0)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(0, 10, 0, 10)
        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_4.addItem(self.verticalSpacer)

        self.helpBtn = QPushButton(self.frame_3)
        self.helpBtn.setObjectName(u"helpBtn")
        self.helpBtn.setFont(font)
        self.helpBtn.setStyleSheet(u"color: #ffffff;")
        icon4 = QIcon()
        icon4.addFile(u":/icons/icons/help-circle.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.helpBtn.setIcon(icon4)
        self.helpBtn.setIconSize(QSize(24, 24))

        self.verticalLayout_4.addWidget(self.helpBtn)


        self.verticalLayout_2.addWidget(self.frame_3)


        self.verticalLayout.addWidget(self.leftMenuSubContainer)


        self.horizontalLayout.addWidget(self.leftMenuContainer, 0, Qt.AlignLeft)

        self.centerMenuContainer = QCustomSlideMenu(self.centralwidget)
        self.centerMenuContainer.setObjectName(u"centerMenuContainer")
        self.verticalLayout_5 = QVBoxLayout(self.centerMenuContainer)
        self.verticalLayout_5.setSpacing(0)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.centerMenuSubContainer = QWidget(self.centerMenuContainer)
        self.centerMenuSubContainer.setObjectName(u"centerMenuSubContainer")
        self.centerMenuSubContainer.setMinimumSize(QSize(200, 0))
        self.verticalLayout_6 = QVBoxLayout(self.centerMenuSubContainer)
        self.verticalLayout_6.setSpacing(5)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.verticalLayout_6.setContentsMargins(5, 5, 5, 5)
        self.frame_4 = QFrame(self.centerMenuSubContainer)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setFrameShape(QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.frame_4)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.label = QLabel(self.frame_4)
        self.label.setObjectName(u"label")
        self.label.setFont(font)
        self.label.setStyleSheet(u"color: #ffffff;")
        self.label.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_3.addWidget(self.label)

        self.closeCenterMenuBtn = QPushButton(self.frame_4)
        self.closeCenterMenuBtn.setObjectName(u"closeCenterMenuBtn")
        self.closeCenterMenuBtn.setEnabled(True)
        icon5 = QIcon()
        icon5.addFile(u":/icons/icons/x-circle.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.closeCenterMenuBtn.setIcon(icon5)
        self.closeCenterMenuBtn.setIconSize(QSize(24, 24))

        self.horizontalLayout_3.addWidget(self.closeCenterMenuBtn, 0, Qt.AlignRight)


        self.verticalLayout_6.addWidget(self.frame_4, 0, Qt.AlignTop)

        self.centerMenuPages = QCustomStackedWidget(self.centerMenuSubContainer)
        self.centerMenuPages.setObjectName(u"centerMenuPages")
        self.centerMenuPages.setMinimumSize(QSize(200, 0))
        self.ayuda = QWidget()
        self.ayuda.setObjectName(u"ayuda")
        self.verticalLayout_9 = QVBoxLayout(self.ayuda)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.centerMenuPages.addWidget(self.ayuda)

        self.verticalLayout_6.addWidget(self.centerMenuPages)


        self.verticalLayout_5.addWidget(self.centerMenuSubContainer)


        self.horizontalLayout.addWidget(self.centerMenuContainer)

        self.mainBodyContainer = QWidget(self.centralwidget)
        self.mainBodyContainer.setObjectName(u"mainBodyContainer")
        sizePolicy1 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.mainBodyContainer.sizePolicy().hasHeightForWidth())
        self.mainBodyContainer.setSizePolicy(sizePolicy1)
        self.mainBodyContainer.setStyleSheet(u"")
        self.verticalLayout_10 = QVBoxLayout(self.mainBodyContainer)
        self.verticalLayout_10.setSpacing(0)
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.verticalLayout_10.setContentsMargins(0, 0, 0, 0)
        self.headerContainer = QWidget(self.mainBodyContainer)
        self.headerContainer.setObjectName(u"headerContainer")
        self.headerContainer.setToolTipDuration(-47)
        self.headerContainer.setStyleSheet(u"QWidget{\n"
"	height: 40%\n"
"}")
        self.horizontalLayout_5 = QHBoxLayout(self.headerContainer)
        self.horizontalLayout_5.setSpacing(6)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.frame_6 = QFrame(self.headerContainer)
        self.frame_6.setObjectName(u"frame_6")
        self.frame_6.setFrameShape(QFrame.StyledPanel)
        self.frame_6.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_6 = QHBoxLayout(self.frame_6)
        self.horizontalLayout_6.setSpacing(6)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.horizontalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.notificationBtn = QPushButton(self.frame_6)
        self.notificationBtn.setObjectName(u"notificationBtn")
        icon6 = QIcon()
        icon6.addFile(u":/icons/icons/bell.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.notificationBtn.setIcon(icon6)
        self.notificationBtn.setIconSize(QSize(24, 24))

        self.horizontalLayout_6.addWidget(self.notificationBtn)


        self.horizontalLayout_5.addWidget(self.frame_6)

        self.frame_7 = QFrame(self.headerContainer)
        self.frame_7.setObjectName(u"frame_7")
        self.frame_7.setFrameShape(QFrame.StyledPanel)
        self.frame_7.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_4 = QHBoxLayout(self.frame_7)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.minimizeBtn = QPushButton(self.frame_7)
        self.minimizeBtn.setObjectName(u"minimizeBtn")
        icon7 = QIcon()
        icon7.addFile(u":/icons/icons/minus.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.minimizeBtn.setIcon(icon7)

        self.horizontalLayout_4.addWidget(self.minimizeBtn)

        self.restoreBtn = QPushButton(self.frame_7)
        self.restoreBtn.setObjectName(u"restoreBtn")
        icon8 = QIcon()
        icon8.addFile(u":/icons/icons/square.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.restoreBtn.setIcon(icon8)

        self.horizontalLayout_4.addWidget(self.restoreBtn)

        self.closeBtn = QPushButton(self.frame_7)
        self.closeBtn.setObjectName(u"closeBtn")
        self.closeBtn.setStyleSheet(u"QPushButton:hover {\n"
"	background-color: #ca1310 ;\n"
"	border: 0.313em solid #ca1310;\n"
"	border-radius: 0.313em;\n"
"}")
        icon9 = QIcon()
        icon9.addFile(u":/icons/icons/x.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.closeBtn.setIcon(icon9)

        self.horizontalLayout_4.addWidget(self.closeBtn)


        self.horizontalLayout_5.addWidget(self.frame_7, 0, Qt.AlignRight)


        self.verticalLayout_10.addWidget(self.headerContainer, 0, Qt.AlignTop)

        self.mainBodyContent = QWidget(self.mainBodyContainer)
        self.mainBodyContent.setObjectName(u"mainBodyContent")
        sizePolicy2 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Expanding)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.mainBodyContent.sizePolicy().hasHeightForWidth())
        self.mainBodyContent.setSizePolicy(sizePolicy2)
        self.mainBodyContent.setMinimumSize(QSize(327, 206))
        palette = QPalette()
        brush = QBrush(QColor(28, 40, 51, 255))
        brush.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.Button, brush)
        brush1 = QBrush(QColor(40, 40, 40, 255))
        brush1.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.Base, brush1)
        brush2 = QBrush(QColor(47, 47, 47, 255))
        brush2.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.Window, brush2)
        palette.setBrush(QPalette.Inactive, QPalette.Button, brush)
        palette.setBrush(QPalette.Inactive, QPalette.Base, brush1)
        palette.setBrush(QPalette.Inactive, QPalette.Window, brush2)
        palette.setBrush(QPalette.Disabled, QPalette.Button, brush)
        palette.setBrush(QPalette.Disabled, QPalette.Base, brush2)
        palette.setBrush(QPalette.Disabled, QPalette.Window, brush2)
        self.mainBodyContent.setPalette(palette)
        self.mainBodyContent.setMouseTracking(False)
        self.mainBodyContent.setStyleSheet(u"")
        self.horizontalLayout_7 = QHBoxLayout(self.mainBodyContent)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.mainContentsContainer = QWidget(self.mainBodyContent)
        self.mainContentsContainer.setObjectName(u"mainContentsContainer")
        self.verticalLayout_15 = QVBoxLayout(self.mainContentsContainer)
        self.verticalLayout_15.setObjectName(u"verticalLayout_15")
        self.mainPages = QCustomStackedWidget(self.mainContentsContainer)
        self.mainPages.setObjectName(u"mainPages")
        self.menuPrincipal = QWidget()
        self.menuPrincipal.setObjectName(u"menuPrincipal")
        self.verticalLayout_25 = QVBoxLayout(self.menuPrincipal)
        self.verticalLayout_25.setObjectName(u"verticalLayout_25")
        self.frame_15 = QFrame(self.menuPrincipal)
        self.frame_15.setObjectName(u"frame_15")
        self.frame_15.setFrameShape(QFrame.StyledPanel)
        self.frame_15.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_10 = QHBoxLayout(self.frame_15)
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.frame_10 = QFrame(self.frame_15)
        self.frame_10.setObjectName(u"frame_10")
        self.frame_10.setFrameShape(QFrame.StyledPanel)
        self.frame_10.setFrameShadow(QFrame.Raised)
        self.verticalLayout_22 = QVBoxLayout(self.frame_10)
        self.verticalLayout_22.setObjectName(u"verticalLayout_22")
        self.HOR1Btn = QPushButton(self.frame_10)
        self.HOR1Btn.setObjectName(u"HOR1Btn")
        font1 = QFont()
        font1.setPointSize(10)
        font1.setBold(True)
        font1.setItalic(False)
        font1.setWeight(99)
        self.HOR1Btn.setFont(font1)
        self.HOR1Btn.setStyleSheet(u"QPushButton{\n"
"	color: #ffffff;\n"
"	width: 70%;	\n"
"	background-color: rgb(0, 197, 95 / 85%);\n"
"	height: 100%;\n"
"	font-style: normal;\n"
"	font-weight: 800;\n"
"	height: 200%;\n"
"	width: 250%;\n"
"	border: 1px solid rgb(85, 255, 127 / 20%);\n"
"	border-radius: 5px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	background-color: rgb(0, 197, 95);\n"
"	border: 1px solid rgb(85, 255, 127);\n"
"	border-width: 1px;\n"
"	border-radius: 5px;\n"
"}")
        self.HOR1Btn.setIconSize(QSize(24, 24))

        self.verticalLayout_22.addWidget(self.HOR1Btn)


        self.horizontalLayout_10.addWidget(self.frame_10, 0, Qt.AlignTop)

        self.frame_9 = QFrame(self.frame_15)
        self.frame_9.setObjectName(u"frame_9")
        self.frame_9.setStyleSheet(u"")
        self.frame_9.setFrameShape(QFrame.StyledPanel)
        self.frame_9.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_11 = QHBoxLayout(self.frame_9)
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.HOR2Btn = QPushButton(self.frame_9)
        self.HOR2Btn.setObjectName(u"HOR2Btn")
        self.HOR2Btn.setFont(font1)
        self.HOR2Btn.setStyleSheet(u"QPushButton{\n"
"	color: #ffffff;\n"
"	width: 70%;	\n"
"	height: 100%;\n"
"	background-color: rgb(200, 0, 0 / 85%);\n"
"	font-style: normal;\n"
"	font-weight: 800;\n"
"	height: 200%;\n"
"	width: 250%;\n"
"	border: 1px solid rgb(255, 0, 0 / 20%);\n"
"	border-radius: 5px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	background-color: rgb(220, 0, 0);\n"
"	border: 1px solid rgb(255, 50, 50);\n"
"	border-width: 1px;\n"
"	border-radius: 5px;\n"
"}\n"
"\n"
"")
        self.HOR2Btn.setIconSize(QSize(24, 24))

        self.horizontalLayout_11.addWidget(self.HOR2Btn)


        self.horizontalLayout_10.addWidget(self.frame_9, 0, Qt.AlignTop)


        self.verticalLayout_25.addWidget(self.frame_15)

        self.notificaciones = QFrame(self.menuPrincipal)
        self.notificaciones.setObjectName(u"notificaciones")
        self.notificaciones.setStyleSheet(u"QFrame{\n"
"	background-color: #fdfcf4;\n"
"	border-radius: 10px;\n"
"}\n"
"\n"
"\n"
"")
        self.notificaciones.setFrameShape(QFrame.StyledPanel)
        self.notificaciones.setFrameShadow(QFrame.Raised)
        self.verticalLayout_24 = QVBoxLayout(self.notificaciones)
        self.verticalLayout_24.setObjectName(u"verticalLayout_24")
        self.label_9 = QLabel(self.notificaciones)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setFont(font)

        self.verticalLayout_24.addWidget(self.label_9, 0, Qt.AlignLeft|Qt.AlignTop)

        self.label_37 = QLabel(self.notificaciones)
        self.label_37.setObjectName(u"label_37")
        font2 = QFont()
        font2.setBold(True)
        font2.setWeight(75)
        self.label_37.setFont(font2)

        self.verticalLayout_24.addWidget(self.label_37)

        self.label_36 = QLabel(self.notificaciones)
        self.label_36.setObjectName(u"label_36")
        self.label_36.setFont(font2)

        self.verticalLayout_24.addWidget(self.label_36)


        self.verticalLayout_25.addWidget(self.notificaciones)

        self.mainPages.addWidget(self.menuPrincipal)
        self.plancha2_2 = QWidget()
        self.plancha2_2.setObjectName(u"plancha2_2")
        self.verticalLayout_17 = QVBoxLayout(self.plancha2_2)
        self.verticalLayout_17.setObjectName(u"verticalLayout_17")
        self.frame_22 = QFrame(self.plancha2_2)
        self.frame_22.setObjectName(u"frame_22")
        self.frame_22.setStyleSheet(u"#frame_22{\n"
"	background-color: #fdfcf4;;\n"
"	border-radius: 10px;\n"
"}")
        self.frame_22.setFrameShape(QFrame.StyledPanel)
        self.frame_22.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_17 = QHBoxLayout(self.frame_22)
        self.horizontalLayout_17.setObjectName(u"horizontalLayout_17")
        self.label_30 = QLabel(self.frame_22)
        self.label_30.setObjectName(u"label_30")
        self.label_30.setFont(font)
        self.label_30.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.horizontalLayout_17.addWidget(self.label_30)

        self.backPlancha3Hor1Btn = QPushButton(self.frame_22)
        self.backPlancha3Hor1Btn.setObjectName(u"backPlancha3Hor1Btn")
        self.backPlancha3Hor1Btn.setStyleSheet(u"QPushButton {\n"
"	background-color: #fdfcf4;\n"
"	font-style: normal;\n"
"	font-weight: 800;\n"
"	height: 20%;\n"
"	width: 30%;\n"
"	border-radius: 30%;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	border: 5px solid rgb(0, 0, 0);\n"
"	border-width: 2px;\n"
"	border-radius: 10%;\n"
"}\n"
"")
        icon10 = QIcon()
        icon10.addFile(u":/icons/icons/arrow-left.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.backPlancha3Hor1Btn.setIcon(icon10)

        self.horizontalLayout_17.addWidget(self.backPlancha3Hor1Btn, 0, Qt.AlignRight)


        self.verticalLayout_17.addWidget(self.frame_22)

        self.frame_17 = QFrame(self.plancha2_2)
        self.frame_17.setObjectName(u"frame_17")
        self.frame_17.setFrameShape(QFrame.StyledPanel)
        self.frame_17.setFrameShadow(QFrame.Raised)
        self.gridLayout_5 = QGridLayout(self.frame_17)
        self.gridLayout_5.setObjectName(u"gridLayout_5")
        self.label_27 = QLabel(self.frame_17)
        self.label_27.setObjectName(u"label_27")
        self.label_27.setFont(font2)
        self.label_27.setStyleSheet(u"color: #ffffff;")

        self.gridLayout_5.addWidget(self.label_27, 1, 1, 1, 1)

        self.label_26 = QLabel(self.frame_17)
        self.label_26.setObjectName(u"label_26")
        self.label_26.setFont(font2)
        self.label_26.setStyleSheet(u"color: #ffffff;")

        self.gridLayout_5.addWidget(self.label_26, 0, 1, 1, 1)

        self.label_25 = QLabel(self.frame_17)
        self.label_25.setObjectName(u"label_25")
        self.label_25.setFont(font)
        self.label_25.setStyleSheet(u"color: #ffffff;")

        self.gridLayout_5.addWidget(self.label_25, 0, 0, 1, 1)

        self.label_28 = QLabel(self.frame_17)
        self.label_28.setObjectName(u"label_28")
        self.label_28.setFont(font2)
        self.label_28.setStyleSheet(u"color: #ffffff;")

        self.gridLayout_5.addWidget(self.label_28, 0, 2, 1, 1)

        self.label_29 = QLabel(self.frame_17)
        self.label_29.setObjectName(u"label_29")
        self.label_29.setFont(font2)
        self.label_29.setStyleSheet(u"color: #ffffff;")

        self.gridLayout_5.addWidget(self.label_29, 1, 2, 1, 1)


        self.verticalLayout_17.addWidget(self.frame_17)

        self.frame_16 = QFrame(self.plancha2_2)
        self.frame_16.setObjectName(u"frame_16")
        self.frame_16.setFrameShape(QFrame.StyledPanel)
        self.frame_16.setFrameShadow(QFrame.Raised)
        self.gridLayout_4 = QGridLayout(self.frame_16)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.pushButton_33 = QPushButton(self.frame_16)
        self.pushButton_33.setObjectName(u"pushButton_33")
        self.pushButton_33.setStyleSheet(u"QPushButton{\n"
"	color: #ffffff;\n"
"	width: 70%;	\n"
"	height: 100%;\n"
"	font-style: normal;\n"
"	font-weight: 800;\n"
"	height: 200%;\n"
"	width: 250%;\n"
"	background-color: rgb(60, 60, 60 );\n"
"	border: 1px solid rgb(30, 30, 30 / 50%);\n"
"	border-radius: 5px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	background-color: rgb(60, 60, 60);\n"
"	border: 1px solid rgb(100, 100, 100);\n"
"	border-width: 1px;\n"
"	border-radius: 5px;\n"
"}")
        icon11 = QIcon()
        icon11.addFile(u":/icons/icons/activity.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_33.setIcon(icon11)

        self.gridLayout_4.addWidget(self.pushButton_33, 3, 1, 1, 1)

        self.pushButton_34 = QPushButton(self.frame_16)
        self.pushButton_34.setObjectName(u"pushButton_34")
        self.pushButton_34.setStyleSheet(u"QPushButton{\n"
"	color: #ffffff;\n"
"	width: 70%;	\n"
"	height: 100%;\n"
"	font-style: normal;\n"
"	font-weight: 800;\n"
"	height: 200%;\n"
"	width: 250%;\n"
"	background-color: rgb(60, 60, 60 );\n"
"	border: 1px solid rgb(30, 30, 30 / 50%);\n"
"	border-radius: 5px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	background-color: rgb(60, 60, 60);\n"
"	border: 1px solid rgb(100, 100, 100);\n"
"	border-width: 1px;\n"
"	border-radius: 5px;\n"
"}")
        self.pushButton_34.setIcon(icon11)

        self.gridLayout_4.addWidget(self.pushButton_34, 4, 1, 1, 1)

        self.pushButton_32 = QPushButton(self.frame_16)
        self.pushButton_32.setObjectName(u"pushButton_32")
        self.pushButton_32.setStyleSheet(u"QPushButton{\n"
"	color: #ffffff;\n"
"	width: 70%;	\n"
"	height: 100%;\n"
"	font-style: normal;\n"
"	font-weight: 800;\n"
"	height: 200%;\n"
"	width: 250%;\n"
"	background-color: rgb(60, 60, 60 );\n"
"	border: 1px solid rgb(30, 30, 30 / 50%);\n"
"	border-radius: 5px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	background-color: rgb(60, 60, 60);\n"
"	border: 1px solid rgb(100, 100, 100);\n"
"	border-width: 1px;\n"
"	border-radius: 5px;\n"
"}")
        self.pushButton_32.setIcon(icon11)

        self.gridLayout_4.addWidget(self.pushButton_32, 2, 1, 1, 1)

        self.pushButton_27 = QPushButton(self.frame_16)
        self.pushButton_27.setObjectName(u"pushButton_27")
        self.pushButton_27.setStyleSheet(u"QPushButton{\n"
"	color: #ffffff;\n"
"	width: 70%;	\n"
"	height: 100%;\n"
"	font-style: normal;\n"
"	font-weight: 800;\n"
"	height: 200%;\n"
"	width: 250%;\n"
"	background-color: rgb(60, 60, 60 );\n"
"	border: 1px solid rgb(30, 30, 30 / 50%);\n"
"	border-radius: 5px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	background-color: rgb(60, 60, 60);\n"
"	border: 1px solid rgb(100, 100, 100);\n"
"	border-width: 1px;\n"
"	border-radius: 5px;\n"
"}")
        self.pushButton_27.setIcon(icon11)

        self.gridLayout_4.addWidget(self.pushButton_27, 2, 0, 1, 1)

        self.pushButton_25 = QPushButton(self.frame_16)
        self.pushButton_25.setObjectName(u"pushButton_25")
        self.pushButton_25.setStyleSheet(u"QPushButton{\n"
"	color: #ffffff;\n"
"	width: 70%;	\n"
"	height: 100%;\n"
"	font-style: normal;\n"
"	font-weight: 800;\n"
"	height: 200%;\n"
"	width: 250%;\n"
"	background-color: rgb(60, 60, 60 );\n"
"	border: 1px solid rgb(30, 30, 30 / 50%);\n"
"	border-radius: 5px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	background-color: rgb(60, 60, 60);\n"
"	border: 1px solid rgb(100, 100, 100);\n"
"	border-width: 1px;\n"
"	border-radius: 5px;\n"
"}")
        self.pushButton_25.setIcon(icon11)

        self.gridLayout_4.addWidget(self.pushButton_25, 3, 0, 1, 1)

        self.pushButton_29 = QPushButton(self.frame_16)
        self.pushButton_29.setObjectName(u"pushButton_29")
        self.pushButton_29.setStyleSheet(u"QPushButton{\n"
"	color: #ffffff;\n"
"	width: 70%;	\n"
"	background-color: rgb(0, 197, 95 / 85%);\n"
"	height: 100%;\n"
"	font-style: normal;\n"
"	font-weight: 800;\n"
"	height: 200%;\n"
"	width: 250%;\n"
"	border: 1px solid rgb(85, 255, 127 / 20%);\n"
"	border-radius: 5px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	background-color: rgb(0, 197, 95);\n"
"	border: 1px solid rgb(85, 255, 127);\n"
"	border-width: 1px;\n"
"	border-radius: 5px;\n"
"}")
        self.pushButton_29.setIcon(icon11)

        self.gridLayout_4.addWidget(self.pushButton_29, 0, 0, 1, 1)

        self.pushButton_26 = QPushButton(self.frame_16)
        self.pushButton_26.setObjectName(u"pushButton_26")
        self.pushButton_26.setStyleSheet(u"QPushButton{\n"
"	color: #ffffff;\n"
"	width: 70%;	\n"
"	height: 100%;\n"
"	font-style: normal;\n"
"	font-weight: 800;\n"
"	height: 200%;\n"
"	width: 250%;\n"
"	background-color: rgb(60, 60, 60 );\n"
"	border: 1px solid rgb(30, 30, 30 / 50%);\n"
"	border-radius: 5px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	background-color: rgb(60, 60, 60);\n"
"	border: 1px solid rgb(100, 100, 100);\n"
"	border-width: 1px;\n"
"	border-radius: 5px;\n"
"}")
        self.pushButton_26.setIcon(icon11)

        self.gridLayout_4.addWidget(self.pushButton_26, 4, 0, 1, 1)

        self.pushButton_28 = QPushButton(self.frame_16)
        self.pushButton_28.setObjectName(u"pushButton_28")
        self.pushButton_28.setStyleSheet(u"QPushButton{\n"
"	color: #ffffff;\n"
"	width: 70%;	\n"
"	height: 100%;\n"
"	font-style: normal;\n"
"	font-weight: 800;\n"
"	height: 200%;\n"
"	width: 250%;\n"
"	background-color: rgb(60, 60, 60 );\n"
"	border: 1px solid rgb(30, 30, 30 / 50%);\n"
"	border-radius: 5px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	background-color: rgb(60, 60, 60);\n"
"	border: 1px solid rgb(100, 100, 100);\n"
"	border-width: 1px;\n"
"	border-radius: 5px;\n"
"}")
        self.pushButton_28.setIcon(icon11)

        self.gridLayout_4.addWidget(self.pushButton_28, 1, 0, 1, 1)

        self.pushButton_31 = QPushButton(self.frame_16)
        self.pushButton_31.setObjectName(u"pushButton_31")
        self.pushButton_31.setStyleSheet(u"QPushButton{\n"
"	color: #ffffff;\n"
"	width: 70%;	\n"
"	height: 100%;\n"
"	font-style: normal;\n"
"	font-weight: 800;\n"
"	height: 200%;\n"
"	width: 250%;\n"
"	background-color: rgb(60, 60, 60 );\n"
"	border: 1px solid rgb(30, 30, 30 / 50%);\n"
"	border-radius: 5px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	background-color: rgb(60, 60, 60);\n"
"	border: 1px solid rgb(100, 100, 100);\n"
"	border-width: 1px;\n"
"	border-radius: 5px;\n"
"}")
        self.pushButton_31.setIcon(icon11)

        self.gridLayout_4.addWidget(self.pushButton_31, 1, 1, 1, 1)

        self.pushButton_30 = QPushButton(self.frame_16)
        self.pushButton_30.setObjectName(u"pushButton_30")
        self.pushButton_30.setStyleSheet(u"QPushButton{\n"
"	color: #ffffff;\n"
"	width: 70%;	\n"
"	background-color: rgb(0, 197, 95 / 85%);\n"
"	height: 100%;\n"
"	font-style: normal;\n"
"	font-weight: 800;\n"
"	height: 200%;\n"
"	width: 250%;\n"
"	border: 1px solid rgb(85, 255, 127 / 20%);\n"
"	border-radius: 5px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	background-color: rgb(0, 197, 95);\n"
"	border: 1px solid rgb(85, 255, 127);\n"
"	border-width: 1px;\n"
"	border-radius: 5px;\n"
"}")
        self.pushButton_30.setIcon(icon11)

        self.gridLayout_4.addWidget(self.pushButton_30, 0, 1, 1, 1)


        self.verticalLayout_17.addWidget(self.frame_16)

        self.frame_36 = QFrame(self.plancha2_2)
        self.frame_36.setObjectName(u"frame_36")
        self.frame_36.setFrameShape(QFrame.StyledPanel)
        self.frame_36.setFrameShadow(QFrame.Raised)
        self.verticalLayout_27 = QVBoxLayout(self.frame_36)
        self.verticalLayout_27.setObjectName(u"verticalLayout_27")
        self.initMad_plancha2_horno2Btn = QPushButton(self.frame_36)
        self.initMad_plancha2_horno2Btn.setObjectName(u"initMad_plancha2_horno2Btn")
        self.initMad_plancha2_horno2Btn.setMaximumSize(QSize(16777215, 16777215))
        self.initMad_plancha2_horno2Btn.setFont(font1)
        self.initMad_plancha2_horno2Btn.setStyleSheet(u"QPushButton {\n"
"	background-color: rgb(194, 255, 156);\n"
"	font-style: normal;\n"
"	font-weight: 800;\n"
"	height: 50%;\n"
"	width: 300%;\n"
"	border-radius: 20px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	background-color: rgb(146, 216, 107);\n"
"	border: 5px solid rgb(194, 255, 156);\n"
"	border-width: 1px;\n"
"	border-radius: 20px;\n"
"}\n"
"")
        icon12 = QIcon()
        icon12.addFile(u":/icons/icons/log-in.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.initMad_plancha2_horno2Btn.setIcon(icon12)
        self.initMad_plancha2_horno2Btn.setIconSize(QSize(30, 30))

        self.verticalLayout_27.addWidget(self.initMad_plancha2_horno2Btn)


        self.verticalLayout_17.addWidget(self.frame_36, 0, Qt.AlignRight)

        self.mainPages.addWidget(self.plancha2_2)
        self.plancha1_2 = QWidget()
        self.plancha1_2.setObjectName(u"plancha1_2")
        self.verticalLayout_18 = QVBoxLayout(self.plancha1_2)
        self.verticalLayout_18.setObjectName(u"verticalLayout_18")
        self.frame_24 = QFrame(self.plancha1_2)
        self.frame_24.setObjectName(u"frame_24")
        self.frame_24.setStyleSheet(u"#frame_24{\n"
"	background-color: #fdfcf4;;\n"
"	border-radius: 10px;\n"
"}")
        self.frame_24.setFrameShape(QFrame.StyledPanel)
        self.frame_24.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_18 = QHBoxLayout(self.frame_24)
        self.horizontalLayout_18.setObjectName(u"horizontalLayout_18")
        self.label_24 = QLabel(self.frame_24)
        self.label_24.setObjectName(u"label_24")
        self.label_24.setFont(font)
        self.label_24.setStyleSheet(u"")
        self.label_24.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.horizontalLayout_18.addWidget(self.label_24)

        self.backPlancha1Hor2Btn = QPushButton(self.frame_24)
        self.backPlancha1Hor2Btn.setObjectName(u"backPlancha1Hor2Btn")
        self.backPlancha1Hor2Btn.setStyleSheet(u"QPushButton {\n"
"	background-color: #fdfcf4;\n"
"	font-style: normal;\n"
"	font-weight: 800;\n"
"	height: 20%;\n"
"	width: 30%;\n"
"	border-radius: 30%;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	border: 5px solid rgb(0, 0, 0);\n"
"	border-width: 2px;\n"
"	border-radius: 10%;\n"
"}\n"
"")
        self.backPlancha1Hor2Btn.setIcon(icon10)

        self.horizontalLayout_18.addWidget(self.backPlancha1Hor2Btn, 0, Qt.AlignRight)


        self.verticalLayout_18.addWidget(self.frame_24)

        self.frame_26 = QFrame(self.plancha1_2)
        self.frame_26.setObjectName(u"frame_26")
        self.frame_26.setFrameShape(QFrame.StyledPanel)
        self.frame_26.setFrameShadow(QFrame.Raised)
        self.gridLayout_6 = QGridLayout(self.frame_26)
        self.gridLayout_6.setObjectName(u"gridLayout_6")
        self.label_31 = QLabel(self.frame_26)
        self.label_31.setObjectName(u"label_31")
        self.label_31.setFont(font2)
        self.label_31.setStyleSheet(u"color: #ffffff;")

        self.gridLayout_6.addWidget(self.label_31, 1, 1, 1, 1)

        self.label_32 = QLabel(self.frame_26)
        self.label_32.setObjectName(u"label_32")
        self.label_32.setFont(font2)
        self.label_32.setStyleSheet(u"color: #ffffff;")

        self.gridLayout_6.addWidget(self.label_32, 0, 1, 1, 1)

        self.label_33 = QLabel(self.frame_26)
        self.label_33.setObjectName(u"label_33")
        self.label_33.setFont(font)
        self.label_33.setStyleSheet(u"color: #ffffff;")

        self.gridLayout_6.addWidget(self.label_33, 0, 0, 1, 1)

        self.label_34 = QLabel(self.frame_26)
        self.label_34.setObjectName(u"label_34")
        self.label_34.setFont(font2)
        self.label_34.setStyleSheet(u"color: #ffffff;")

        self.gridLayout_6.addWidget(self.label_34, 0, 2, 1, 1)

        self.label_35 = QLabel(self.frame_26)
        self.label_35.setObjectName(u"label_35")
        self.label_35.setFont(font2)
        self.label_35.setStyleSheet(u"color: #ffffff;")

        self.gridLayout_6.addWidget(self.label_35, 1, 2, 1, 1)


        self.verticalLayout_18.addWidget(self.frame_26)

        self.frame_25 = QFrame(self.plancha1_2)
        self.frame_25.setObjectName(u"frame_25")
        self.frame_25.setFrameShape(QFrame.StyledPanel)
        self.frame_25.setFrameShadow(QFrame.Raised)
        self.gridLayout_10 = QGridLayout(self.frame_25)
        self.gridLayout_10.setObjectName(u"gridLayout_10")
        self.pushButton_46 = QPushButton(self.frame_25)
        self.pushButton_46.setObjectName(u"pushButton_46")
        self.pushButton_46.setStyleSheet(u"QPushButton{\n"
"	color: #ffffff;\n"
"	width: 70%;	\n"
"	height: 100%;\n"
"	font-style: normal;\n"
"	font-weight: 800;\n"
"	height: 200%;\n"
"	width: 250%;\n"
"	background-color: rgb(60, 60, 60 );\n"
"	border: 1px solid rgb(30, 30, 30 / 50%);\n"
"	border-radius: 5px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	background-color: rgb(60, 60, 60);\n"
"	border: 1px solid rgb(100, 100, 100);\n"
"	border-width: 1px;\n"
"	border-radius: 5px;\n"
"}")
        self.pushButton_46.setIcon(icon11)

        self.gridLayout_10.addWidget(self.pushButton_46, 3, 1, 1, 1)

        self.pushButton_47 = QPushButton(self.frame_25)
        self.pushButton_47.setObjectName(u"pushButton_47")
        self.pushButton_47.setStyleSheet(u"QPushButton{\n"
"	color: #ffffff;\n"
"	width: 70%;	\n"
"	height: 100%;\n"
"	font-style: normal;\n"
"	font-weight: 800;\n"
"	height: 200%;\n"
"	width: 250%;\n"
"	background-color: rgb(60, 60, 60 );\n"
"	border: 1px solid rgb(30, 30, 30 / 50%);\n"
"	border-radius: 5px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	background-color: rgb(60, 60, 60);\n"
"	border: 1px solid rgb(100, 100, 100);\n"
"	border-width: 1px;\n"
"	border-radius: 5px;\n"
"}")
        self.pushButton_47.setIcon(icon11)

        self.gridLayout_10.addWidget(self.pushButton_47, 4, 1, 1, 1)

        self.pushButton_48 = QPushButton(self.frame_25)
        self.pushButton_48.setObjectName(u"pushButton_48")
        self.pushButton_48.setStyleSheet(u"QPushButton{\n"
"	color: #ffffff;\n"
"	width: 70%;	\n"
"	height: 100%;\n"
"	font-style: normal;\n"
"	font-weight: 800;\n"
"	height: 200%;\n"
"	width: 250%;\n"
"	background-color: rgb(60, 60, 60 );\n"
"	border: 1px solid rgb(30, 30, 30 / 50%);\n"
"	border-radius: 5px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	background-color: rgb(60, 60, 60);\n"
"	border: 1px solid rgb(100, 100, 100);\n"
"	border-width: 1px;\n"
"	border-radius: 5px;\n"
"}")
        self.pushButton_48.setIcon(icon11)

        self.gridLayout_10.addWidget(self.pushButton_48, 2, 1, 1, 1)

        self.pushButton_49 = QPushButton(self.frame_25)
        self.pushButton_49.setObjectName(u"pushButton_49")
        self.pushButton_49.setStyleSheet(u"QPushButton{\n"
"	color: #ffffff;\n"
"	width: 70%;	\n"
"	height: 100%;\n"
"	font-style: normal;\n"
"	font-weight: 800;\n"
"	height: 200%;\n"
"	width: 250%;\n"
"	background-color: rgb(60, 60, 60 );\n"
"	border: 1px solid rgb(30, 30, 30 / 50%);\n"
"	border-radius: 5px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	background-color: rgb(60, 60, 60);\n"
"	border: 1px solid rgb(100, 100, 100);\n"
"	border-width: 1px;\n"
"	border-radius: 5px;\n"
"}")
        self.pushButton_49.setIcon(icon11)

        self.gridLayout_10.addWidget(self.pushButton_49, 2, 0, 1, 1)

        self.pushButton_50 = QPushButton(self.frame_25)
        self.pushButton_50.setObjectName(u"pushButton_50")
        self.pushButton_50.setStyleSheet(u"QPushButton{\n"
"	color: #ffffff;\n"
"	width: 70%;	\n"
"	height: 100%;\n"
"	font-style: normal;\n"
"	font-weight: 800;\n"
"	height: 200%;\n"
"	width: 250%;\n"
"	background-color: rgb(60, 60, 60 );\n"
"	border: 1px solid rgb(30, 30, 30 / 50%);\n"
"	border-radius: 5px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	background-color: rgb(60, 60, 60);\n"
"	border: 1px solid rgb(100, 100, 100);\n"
"	border-width: 1px;\n"
"	border-radius: 5px;\n"
"}")
        self.pushButton_50.setIcon(icon11)

        self.gridLayout_10.addWidget(self.pushButton_50, 3, 0, 1, 1)

        self.pushButton_51 = QPushButton(self.frame_25)
        self.pushButton_51.setObjectName(u"pushButton_51")
        self.pushButton_51.setStyleSheet(u"QPushButton{\n"
"	color: #ffffff;\n"
"	width: 70%;	\n"
"	background-color: rgb(0, 197, 95 / 85%);\n"
"	height: 100%;\n"
"	font-style: normal;\n"
"	font-weight: 800;\n"
"	height: 200%;\n"
"	width: 250%;\n"
"	border: 1px solid rgb(85, 255, 127 / 20%);\n"
"	border-radius: 5px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	background-color: rgb(0, 197, 95);\n"
"	border: 1px solid rgb(85, 255, 127);\n"
"	border-width: 1px;\n"
"	border-radius: 5px;\n"
"}")
        self.pushButton_51.setIcon(icon11)

        self.gridLayout_10.addWidget(self.pushButton_51, 0, 0, 1, 1)

        self.pushButton_52 = QPushButton(self.frame_25)
        self.pushButton_52.setObjectName(u"pushButton_52")
        self.pushButton_52.setStyleSheet(u"QPushButton{\n"
"	color: #ffffff;\n"
"	width: 70%;	\n"
"	height: 100%;\n"
"	font-style: normal;\n"
"	font-weight: 800;\n"
"	height: 200%;\n"
"	width: 250%;\n"
"	background-color: rgb(60, 60, 60 );\n"
"	border: 1px solid rgb(30, 30, 30 / 50%);\n"
"	border-radius: 5px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	background-color: rgb(60, 60, 60);\n"
"	border: 1px solid rgb(100, 100, 100);\n"
"	border-width: 1px;\n"
"	border-radius: 5px;\n"
"}")
        self.pushButton_52.setIcon(icon11)

        self.gridLayout_10.addWidget(self.pushButton_52, 4, 0, 1, 1)

        self.pushButton_53 = QPushButton(self.frame_25)
        self.pushButton_53.setObjectName(u"pushButton_53")
        self.pushButton_53.setStyleSheet(u"QPushButton{\n"
"	color: #ffffff;\n"
"	width: 70%;	\n"
"	height: 100%;\n"
"	font-style: normal;\n"
"	font-weight: 800;\n"
"	height: 200%;\n"
"	width: 250%;\n"
"	background-color: rgb(60, 60, 60 );\n"
"	border: 1px solid rgb(30, 30, 30 / 50%);\n"
"	border-radius: 5px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	background-color: rgb(60, 60, 60);\n"
"	border: 1px solid rgb(100, 100, 100);\n"
"	border-width: 1px;\n"
"	border-radius: 5px;\n"
"}")
        self.pushButton_53.setIcon(icon11)

        self.gridLayout_10.addWidget(self.pushButton_53, 1, 0, 1, 1)

        self.pushButton_56 = QPushButton(self.frame_25)
        self.pushButton_56.setObjectName(u"pushButton_56")
        self.pushButton_56.setStyleSheet(u"QPushButton{\n"
"	color: #ffffff;\n"
"	width: 70%;	\n"
"	height: 100%;\n"
"	font-style: normal;\n"
"	font-weight: 800;\n"
"	height: 200%;\n"
"	width: 250%;\n"
"	background-color: rgb(60, 60, 60 );\n"
"	border: 1px solid rgb(30, 30, 30 / 50%);\n"
"	border-radius: 5px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	background-color: rgb(60, 60, 60);\n"
"	border: 1px solid rgb(100, 100, 100);\n"
"	border-width: 1px;\n"
"	border-radius: 5px;\n"
"}")
        self.pushButton_56.setIcon(icon11)

        self.gridLayout_10.addWidget(self.pushButton_56, 1, 1, 1, 1)

        self.pushButton_57 = QPushButton(self.frame_25)
        self.pushButton_57.setObjectName(u"pushButton_57")
        self.pushButton_57.setStyleSheet(u"QPushButton{\n"
"	color: #ffffff;\n"
"	width: 70%;	\n"
"	background-color: rgb(0, 197, 95 / 85%);\n"
"	height: 100%;\n"
"	font-style: normal;\n"
"	font-weight: 800;\n"
"	height: 200%;\n"
"	width: 250%;\n"
"	border: 1px solid rgb(85, 255, 127 / 20%);\n"
"	border-radius: 5px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	background-color: rgb(0, 197, 95);\n"
"	border: 1px solid rgb(85, 255, 127);\n"
"	border-width: 1px;\n"
"	border-radius: 5px;\n"
"}")
        self.pushButton_57.setIcon(icon11)

        self.gridLayout_10.addWidget(self.pushButton_57, 0, 1, 1, 1)


        self.verticalLayout_18.addWidget(self.frame_25)

        self.frame_35 = QFrame(self.plancha1_2)
        self.frame_35.setObjectName(u"frame_35")
        self.frame_35.setFrameShape(QFrame.StyledPanel)
        self.frame_35.setFrameShadow(QFrame.Raised)
        self.verticalLayout_26 = QVBoxLayout(self.frame_35)
        self.verticalLayout_26.setObjectName(u"verticalLayout_26")
        self.iniciarMad_1Btn_4 = QPushButton(self.frame_35)
        self.iniciarMad_1Btn_4.setObjectName(u"iniciarMad_1Btn_4")
        self.iniciarMad_1Btn_4.setMaximumSize(QSize(16777215, 16777215))
        self.iniciarMad_1Btn_4.setFont(font1)
        self.iniciarMad_1Btn_4.setStyleSheet(u"QPushButton {\n"
"	background-color: rgb(194, 255, 156);\n"
"	font-style: normal;\n"
"	font-weight: 800;\n"
"	height: 50%;\n"
"	width: 300%;\n"
"	border-radius: 20px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	background-color: rgb(146, 216, 107);\n"
"	border: 5px solid rgb(194, 255, 156);\n"
"	border-width: 1px;\n"
"	border-radius: 20px;\n"
"}\n"
"\n"
"\n"
"\n"
"")
        self.iniciarMad_1Btn_4.setIcon(icon12)
        self.iniciarMad_1Btn_4.setIconSize(QSize(30, 30))

        self.verticalLayout_26.addWidget(self.iniciarMad_1Btn_4)


        self.verticalLayout_18.addWidget(self.frame_35, 0, Qt.AlignRight)

        self.mainPages.addWidget(self.plancha1_2)
        self.planchasHor1 = QWidget()
        self.planchasHor1.setObjectName(u"planchasHor1")
        self.verticalLayout_16 = QVBoxLayout(self.planchasHor1)
        self.verticalLayout_16.setObjectName(u"verticalLayout_16")
        self.frame_14 = QFrame(self.planchasHor1)
        self.frame_14.setObjectName(u"frame_14")
        self.frame_14.setStyleSheet(u"#frame_14{\n"
"	background-color: #fdfcf4;;\n"
"	border-radius: 10px;\n"
"}")
        self.frame_14.setFrameShape(QFrame.StyledPanel)
        self.frame_14.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_13 = QHBoxLayout(self.frame_14)
        self.horizontalLayout_13.setObjectName(u"horizontalLayout_13")
        self.label_13 = QLabel(self.frame_14)
        self.label_13.setObjectName(u"label_13")
        self.label_13.setFont(font)
        self.label_13.setLayoutDirection(Qt.LeftToRight)
        self.label_13.setStyleSheet(u"")
        self.label_13.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.horizontalLayout_13.addWidget(self.label_13)

        self.backHor1Btn = QPushButton(self.frame_14)
        self.backHor1Btn.setObjectName(u"backHor1Btn")
        self.backHor1Btn.setStyleSheet(u"QPushButton {\n"
"	background-color: #fdfcf4;\n"
"	font-style: normal;\n"
"	font-weight: 800;\n"
"	height: 20%;\n"
"	width: 30%;\n"
"	border-radius: 30%;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	border: 5px solid rgb(0, 0, 0);\n"
"	border-width: 2px;\n"
"	border-radius: 10%;\n"
"}\n"
"\n"
"	\n"
"")
        self.backHor1Btn.setIcon(icon10)

        self.horizontalLayout_13.addWidget(self.backHor1Btn, 0, Qt.AlignRight|Qt.AlignVCenter)


        self.verticalLayout_16.addWidget(self.frame_14)

        self.frame_12 = QFrame(self.planchasHor1)
        self.frame_12.setObjectName(u"frame_12")
        self.frame_12.setStyleSheet(u"QFrame {\n"
"	width: 270%;\n"
"	height: 30%;\n"
"}")
        self.frame_12.setFrameShape(QFrame.StyledPanel)
        self.frame_12.setFrameShadow(QFrame.Raised)
        self.verticalLayout_28 = QVBoxLayout(self.frame_12)
        self.verticalLayout_28.setObjectName(u"verticalLayout_28")
        self.verticalLayout_28.setContentsMargins(-1, -1, -1, 0)
        self.plancha1_horno1Btn = QPushButton(self.frame_12)
        self.plancha1_horno1Btn.setObjectName(u"plancha1_horno1Btn")
        self.plancha1_horno1Btn.setFont(font1)
        self.plancha1_horno1Btn.setStyleSheet(u"QPushButton{\n"
"	color: #ffffff;\n"
"	width: 70%;	\n"
"	background-color: rgb(0, 197, 95 / 85%);\n"
"	height: 100%;\n"
"	font-style: normal;\n"
"	font-weight: 800;\n"
"	height: 200%;\n"
"	width: 250%;\n"
"	border: 1px solid rgb(85, 255, 127 / 20%);\n"
"	border-radius: 5px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	background-color: rgb(0, 197, 95);\n"
"	border: 1px solid rgb(85, 255, 127);\n"
"	border-width: 1px;\n"
"	border-radius: 5px;\n"
"}")

        self.verticalLayout_28.addWidget(self.plancha1_horno1Btn)

        self.plancha2_horno1Btn = QPushButton(self.frame_12)
        self.plancha2_horno1Btn.setObjectName(u"plancha2_horno1Btn")
        self.plancha2_horno1Btn.setFont(font1)
        self.plancha2_horno1Btn.setStyleSheet(u"QPushButton{\n"
"	color: #ffffff;\n"
"	width: 70%;	\n"
"	height: 100%;\n"
"	background-color: rgb(200, 0, 0 / 85%);\n"
"	font-style: normal;\n"
"	font-weight: 800;\n"
"	height: 200%;\n"
"	width: 250%;\n"
"	border: 1px solid rgb(255, 0, 0 / 20%);\n"
"	border-radius: 5px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	background-color: rgb(220, 0, 0);\n"
"	border: 1px solid rgb(255, 50, 50);\n"
"	border-width: 1px;\n"
"	border-radius: 5px;\n"
"}\n"
"\n"
"")

        self.verticalLayout_28.addWidget(self.plancha2_horno1Btn)

        self.plancha3_1Btn = QPushButton(self.frame_12)
        self.plancha3_1Btn.setObjectName(u"plancha3_1Btn")
        self.plancha3_1Btn.setFont(font1)
        self.plancha3_1Btn.setStyleSheet(u"QPushButton{\n"
"	color: #ffffff;\n"
"	width: 70%;	\n"
"	height: 100%;\n"
"	font-style: normal;\n"
"	font-weight: 800;\n"
"	height: 200%;\n"
"	width: 250%;\n"
"	background-color: rgb(60, 60, 60 );\n"
"	border: 1px solid rgb(30, 30, 30 / 50%);\n"
"	border-radius: 5px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	background-color: rgb(60, 60, 60);\n"
"	border: 1px solid rgb(100, 100, 100);\n"
"	border-width: 1px;\n"
"	border-radius: 5px;\n"
"}")

        self.verticalLayout_28.addWidget(self.plancha3_1Btn)

        self.plancha4_1Btn = QPushButton(self.frame_12)
        self.plancha4_1Btn.setObjectName(u"plancha4_1Btn")
        self.plancha4_1Btn.setFont(font1)
        self.plancha4_1Btn.setStyleSheet(u"QPushButton{\n"
"	color: #ffffff;\n"
"	width: 70%;	\n"
"	height: 100%;\n"
"	font-style: normal;\n"
"	font-weight: 800;\n"
"	height: 200%;\n"
"	width: 250%;\n"
"	background-color: rgb(60, 60, 60 );\n"
"	border: 1px solid rgb(30, 30, 30 / 50%);\n"
"	border-radius: 5px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	background-color: rgb(60, 60, 60);\n"
"	border: 1px solid rgb(100, 100, 100);\n"
"	border-width: 1px;\n"
"	border-radius: 5px;\n"
"}")

        self.verticalLayout_28.addWidget(self.plancha4_1Btn)

        self.plancha5_1Btn = QPushButton(self.frame_12)
        self.plancha5_1Btn.setObjectName(u"plancha5_1Btn")
        self.plancha5_1Btn.setFont(font1)
        self.plancha5_1Btn.setStyleSheet(u"QPushButton{\n"
"	color: #ffffff;\n"
"	width: 70%;	\n"
"	height: 100%;\n"
"	font-style: normal;\n"
"	font-weight: 800;\n"
"	height: 200%;\n"
"	width: 250%;\n"
"	background-color: rgb(60, 60, 60 );\n"
"	border: 1px solid rgb(30, 30, 30 / 50%);\n"
"	border-radius: 5px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	background-color: rgb(60, 60, 60);\n"
"	border: 1px solid rgb(100, 100, 100);\n"
"	border-width: 1px;\n"
"	border-radius: 5px;\n"
"}")

        self.verticalLayout_28.addWidget(self.plancha5_1Btn)

        self.plancha6_1Btn = QPushButton(self.frame_12)
        self.plancha6_1Btn.setObjectName(u"plancha6_1Btn")
        self.plancha6_1Btn.setFont(font1)
        self.plancha6_1Btn.setStyleSheet(u"QPushButton{\n"
"	color: #ffffff;\n"
"	width: 70%;	\n"
"	height: 100%;\n"
"	font-style: normal;\n"
"	font-weight: 800;\n"
"	height: 200%;\n"
"	width: 250%;\n"
"	background-color: rgb(60, 60, 60 );\n"
"	border: 1px solid rgb(30, 30, 30 / 50%);\n"
"	border-radius: 5px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	background-color: rgb(60, 60, 60);\n"
"	border: 1px solid rgb(100, 100, 100);\n"
"	border-width: 1px;\n"
"	border-radius: 5px;\n"
"}")

        self.verticalLayout_28.addWidget(self.plancha6_1Btn)

        self.plancha7_1Btn = QPushButton(self.frame_12)
        self.plancha7_1Btn.setObjectName(u"plancha7_1Btn")
        self.plancha7_1Btn.setFont(font1)
        self.plancha7_1Btn.setStyleSheet(u"QPushButton{\n"
"	color: #ffffff;\n"
"	width: 70%;	\n"
"	height: 100%;\n"
"	font-style: normal;\n"
"	font-weight: 800;\n"
"	height: 200%;\n"
"	width: 250%;\n"
"	background-color: rgb(60, 60, 60 );\n"
"	border: 1px solid rgb(30, 30, 30 / 50%);\n"
"	border-radius: 5px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	background-color: rgb(60, 60, 60);\n"
"	border: 1px solid rgb(100, 100, 100);\n"
"	border-width: 1px;\n"
"	border-radius: 5px;\n"
"}")

        self.verticalLayout_28.addWidget(self.plancha7_1Btn)

        self.plancha8_1Btn = QPushButton(self.frame_12)
        self.plancha8_1Btn.setObjectName(u"plancha8_1Btn")
        self.plancha8_1Btn.setFont(font1)
        self.plancha8_1Btn.setStyleSheet(u"QPushButton{\n"
"	color: #ffffff;\n"
"	width: 70%;	\n"
"	height: 100%;\n"
"	font-style: normal;\n"
"	font-weight: 800;\n"
"	height: 200%;\n"
"	width: 250%;\n"
"	background-color: rgb(60, 60, 60 );\n"
"	border: 1px solid rgb(30, 30, 30 / 50%);\n"
"	border-radius: 5px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	background-color: rgb(60, 60, 60);\n"
"	border: 1px solid rgb(100, 100, 100);\n"
"	border-width: 1px;\n"
"	border-radius: 5px;\n"
"}")

        self.verticalLayout_28.addWidget(self.plancha8_1Btn)

        self.plancha9_1Btn = QPushButton(self.frame_12)
        self.plancha9_1Btn.setObjectName(u"plancha9_1Btn")
        self.plancha9_1Btn.setFont(font1)
        self.plancha9_1Btn.setStyleSheet(u"QPushButton{\n"
"	color: #ffffff;\n"
"	width: 70%;	\n"
"	height: 100%;\n"
"	font-style: normal;\n"
"	font-weight: 800;\n"
"	height: 200%;\n"
"	width: 250%;\n"
"	background-color: rgb(60, 60, 60 );\n"
"	border: 1px solid rgb(30, 30, 30 / 50%);\n"
"	border-radius: 5px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	background-color: rgb(60, 60, 60);\n"
"	border: 1px solid rgb(100, 100, 100);\n"
"	border-width: 1px;\n"
"	border-radius: 5px;\n"
"}")

        self.verticalLayout_28.addWidget(self.plancha9_1Btn)

        self.plancha10_1Btn = QPushButton(self.frame_12)
        self.plancha10_1Btn.setObjectName(u"plancha10_1Btn")
        self.plancha10_1Btn.setFont(font1)
        self.plancha10_1Btn.setStyleSheet(u"QPushButton{\n"
"	color: #ffffff;\n"
"	width: 70%;	\n"
"	height: 100%;\n"
"	font-style: normal;\n"
"	font-weight: 800;\n"
"	height: 200%;\n"
"	width: 250%;\n"
"	background-color: rgb(60, 60, 60 );\n"
"	border: 1px solid rgb(30, 30, 30 / 50%);\n"
"	border-radius: 5px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	background-color: rgb(60, 60, 60);\n"
"	border: 1px solid rgb(100, 100, 100);\n"
"	border-width: 1px;\n"
"	border-radius: 5px;\n"
"}")

        self.verticalLayout_28.addWidget(self.plancha10_1Btn)

        self.plancha11_1Btn = QPushButton(self.frame_12)
        self.plancha11_1Btn.setObjectName(u"plancha11_1Btn")
        self.plancha11_1Btn.setFont(font1)
        self.plancha11_1Btn.setStyleSheet(u"QPushButton{\n"
"	color: #ffffff;\n"
"	width: 70%;	\n"
"	height: 100%;\n"
"	font-style: normal;\n"
"	font-weight: 800;\n"
"	height: 200%;\n"
"	width: 250%;\n"
"	background-color: rgb(60, 60, 60 );\n"
"	border: 1px solid rgb(30, 30, 30 / 50%);\n"
"	border-radius: 5px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	background-color: rgb(60, 60, 60);\n"
"	border: 1px solid rgb(100, 100, 100);\n"
"	border-width: 1px;\n"
"	border-radius: 5px;\n"
"}")

        self.verticalLayout_28.addWidget(self.plancha11_1Btn)

        self.plancha12_1Btn = QPushButton(self.frame_12)
        self.plancha12_1Btn.setObjectName(u"plancha12_1Btn")
        self.plancha12_1Btn.setFont(font1)
        self.plancha12_1Btn.setStyleSheet(u"QPushButton{\n"
"	color: #ffffff;\n"
"	width: 70%;	\n"
"	height: 100%;\n"
"	font-style: normal;\n"
"	font-weight: 800;\n"
"	height: 200%;\n"
"	width: 250%;\n"
"	background-color: rgb(60, 60, 60 );\n"
"	border: 1px solid rgb(30, 30, 30 / 50%);\n"
"	border-radius: 5px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	background-color: rgb(60, 60, 60);\n"
"	border: 1px solid rgb(100, 100, 100);\n"
"	border-width: 1px;\n"
"	border-radius: 5px;\n"
"}")

        self.verticalLayout_28.addWidget(self.plancha12_1Btn)


        self.verticalLayout_16.addWidget(self.frame_12, 0, Qt.AlignTop)

        self.mainPages.addWidget(self.planchasHor1)
        self.plancha1_1 = QWidget()
        self.plancha1_1.setObjectName(u"plancha1_1")
        self.verticalLayout_23 = QVBoxLayout(self.plancha1_1)
        self.verticalLayout_23.setObjectName(u"verticalLayout_23")
        self.frame_19 = QFrame(self.plancha1_1)
        self.frame_19.setObjectName(u"frame_19")
        self.frame_19.setStyleSheet(u"#frame_19{\n"
"	background-color: #fdfcf4;;\n"
"	border-radius: 10px;\n"
"}")
        self.frame_19.setFrameShape(QFrame.StyledPanel)
        self.frame_19.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_14 = QHBoxLayout(self.frame_19)
        self.horizontalLayout_14.setObjectName(u"horizontalLayout_14")
        self.label_14 = QLabel(self.frame_19)
        self.label_14.setObjectName(u"label_14")
        self.label_14.setFont(font)
        self.label_14.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.horizontalLayout_14.addWidget(self.label_14)

        self.backPlancha1Hor1Btn = QPushButton(self.frame_19)
        self.backPlancha1Hor1Btn.setObjectName(u"backPlancha1Hor1Btn")
        self.backPlancha1Hor1Btn.setStyleSheet(u"QPushButton {\n"
"	background-color: #fdfcf4;\n"
"	font-style: normal;\n"
"	font-weight: 800;\n"
"	height: 20%;\n"
"	width: 30%;\n"
"	border-radius: 30%;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	border: 5px solid rgb(0, 0, 0);\n"
"	border-width: 2px;\n"
"	border-radius: 10%;\n"
"}\n"
"\n"
"")
        self.backPlancha1Hor1Btn.setIcon(icon10)

        self.horizontalLayout_14.addWidget(self.backPlancha1Hor1Btn, 0, Qt.AlignRight|Qt.AlignVCenter)


        self.verticalLayout_23.addWidget(self.frame_19)

        self.frame_18 = QFrame(self.plancha1_1)
        self.frame_18.setObjectName(u"frame_18")
        self.frame_18.setFrameShape(QFrame.StyledPanel)
        self.frame_18.setFrameShadow(QFrame.Raised)
        self.gridLayout_3 = QGridLayout(self.frame_18)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.label_16 = QLabel(self.frame_18)
        self.label_16.setObjectName(u"label_16")
        self.label_16.setFont(font2)
        self.label_16.setStyleSheet(u"color: #ffffff;")

        self.gridLayout_3.addWidget(self.label_16, 1, 3, 1, 1, Qt.AlignRight)

        self.label_11 = QLabel(self.frame_18)
        self.label_11.setObjectName(u"label_11")
        self.label_11.setFont(font2)
        self.label_11.setStyleSheet(u"color: #ffffff;")

        self.gridLayout_3.addWidget(self.label_11, 1, 2, 1, 1, Qt.AlignLeft)

        self.label_15 = QLabel(self.frame_18)
        self.label_15.setObjectName(u"label_15")
        self.label_15.setFont(font2)
        self.label_15.setStyleSheet(u"color: #ffffff;")

        self.gridLayout_3.addWidget(self.label_15, 0, 3, 1, 1, Qt.AlignRight)

        self.label_10 = QLabel(self.frame_18)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setFont(font2)
        self.label_10.setStyleSheet(u"color: #ffffff;")

        self.gridLayout_3.addWidget(self.label_10, 0, 2, 1, 1, Qt.AlignLeft)

        self.label_8 = QLabel(self.frame_18)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setFont(font)
        self.label_8.setStyleSheet(u"color: #ffffff;")

        self.gridLayout_3.addWidget(self.label_8, 0, 0, 1, 1)


        self.verticalLayout_23.addWidget(self.frame_18, 0, Qt.AlignTop)

        self.frame_13 = QFrame(self.plancha1_1)
        self.frame_13.setObjectName(u"frame_13")
        self.frame_13.setEnabled(True)
        self.frame_13.setFrameShape(QFrame.StyledPanel)
        self.frame_13.setFrameShadow(QFrame.Raised)
        self.gridLayout = QGridLayout(self.frame_13)
        self.gridLayout.setObjectName(u"gridLayout")
        self.pushButton_10 = QPushButton(self.frame_13)
        self.pushButton_10.setObjectName(u"pushButton_10")
        self.pushButton_10.setStyleSheet(u"QPushButton{\n"
"	color: #ffffff;\n"
"	width: 70%;	\n"
"	height: 100%;\n"
"	font-style: normal;\n"
"	font-weight: 800;\n"
"	height: 200%;\n"
"	width: 250%;\n"
"	background-color: rgb(60, 60, 60 );\n"
"	border: 1px solid rgb(30, 30, 30 / 50%);\n"
"	border-radius: 5px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	background-color: rgb(60, 60, 60);\n"
"	border: 1px solid rgb(100, 100, 100);\n"
"	border-width: 1px;\n"
"	border-radius: 5px;\n"
"}")
        self.pushButton_10.setIcon(icon11)

        self.gridLayout.addWidget(self.pushButton_10, 4, 1, 1, 1)

        self.pushButton_9 = QPushButton(self.frame_13)
        self.pushButton_9.setObjectName(u"pushButton_9")
        self.pushButton_9.setStyleSheet(u"QPushButton{\n"
"	color: #ffffff;\n"
"	width: 70%;	\n"
"	height: 100%;\n"
"	background-color: rgb(200, 0, 0 / 85%);\n"
"	font-style: normal;\n"
"	font-weight: 800;\n"
"	height: 200%;\n"
"	width: 250%;\n"
"	border: 1px solid rgb(255, 0, 0 / 20%);\n"
"	border-radius: 5px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	background-color: rgb(220, 0, 0);\n"
"	border: 1px solid rgb(255, 50, 50);\n"
"	border-width: 1px;\n"
"	border-radius: 5px;\n"
"}\n"
"\n"
"")
        self.pushButton_9.setIcon(icon11)

        self.gridLayout.addWidget(self.pushButton_9, 0, 0, 1, 1)

        self.pushButton_8 = QPushButton(self.frame_13)
        self.pushButton_8.setObjectName(u"pushButton_8")
        self.pushButton_8.setStyleSheet(u"QPushButton{\n"
"	color: #ffffff;\n"
"	width: 70%;	\n"
"	height: 100%;\n"
"	font-style: normal;\n"
"	font-weight: 800;\n"
"	height: 200%;\n"
"	width: 250%;\n"
"	background-color: rgb(60, 60, 60 );\n"
"	border: 1px solid rgb(30, 30, 30 / 50%);\n"
"	border-radius: 5px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	background-color: rgb(60, 60, 60);\n"
"	border: 1px solid rgb(100, 100, 100);\n"
"	border-width: 1px;\n"
"	border-radius: 5px;\n"
"}")
        self.pushButton_8.setIcon(icon11)

        self.gridLayout.addWidget(self.pushButton_8, 2, 1, 1, 1)

        self.pushButton_4 = QPushButton(self.frame_13)
        self.pushButton_4.setObjectName(u"pushButton_4")
        self.pushButton_4.setStyleSheet(u"QPushButton{\n"
"	color: #ffffff;\n"
"	width: 70%;	\n"
"	height: 100%;\n"
"	font-style: normal;\n"
"	font-weight: 800;\n"
"	height: 200%;\n"
"	width: 250%;\n"
"	background-color: rgb(60, 60, 60 );\n"
"	border: 1px solid rgb(30, 30, 30 / 50%);\n"
"	border-radius: 5px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	background-color: rgb(60, 60, 60);\n"
"	border: 1px solid rgb(100, 100, 100);\n"
"	border-width: 1px;\n"
"	border-radius: 5px;\n"
"}")
        self.pushButton_4.setIcon(icon11)

        self.gridLayout.addWidget(self.pushButton_4, 3, 1, 1, 1)

        self.pushButton_3 = QPushButton(self.frame_13)
        self.pushButton_3.setObjectName(u"pushButton_3")
        self.pushButton_3.setStyleSheet(u"QPushButton{\n"
"	color: #ffffff;\n"
"	width: 70%;	\n"
"	height: 100%;\n"
"	font-style: normal;\n"
"	font-weight: 800;\n"
"	height: 200%;\n"
"	width: 250%;\n"
"	background-color: rgb(60, 60, 60 );\n"
"	border: 1px solid rgb(30, 30, 30 / 50%);\n"
"	border-radius: 5px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	background-color: rgb(60, 60, 60);\n"
"	border: 1px solid rgb(100, 100, 100);\n"
"	border-width: 1px;\n"
"	border-radius: 5px;\n"
"}")
        self.pushButton_3.setIcon(icon11)

        self.gridLayout.addWidget(self.pushButton_3, 4, 0, 1, 1)

        self.pushButton_6 = QPushButton(self.frame_13)
        self.pushButton_6.setObjectName(u"pushButton_6")
        self.pushButton_6.setStyleSheet(u"QPushButton{\n"
"	color: #ffffff;\n"
"	width: 70%;	\n"
"	height: 100%;\n"
"	font-style: normal;\n"
"	font-weight: 800;\n"
"	height: 200%;\n"
"	width: 250%;\n"
"	background-color: rgb(60, 60, 60 );\n"
"	border: 1px solid rgb(30, 30, 30 / 50%);\n"
"	border-radius: 5px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	background-color: rgb(60, 60, 60);\n"
"	border: 1px solid rgb(100, 100, 100);\n"
"	border-width: 1px;\n"
"	border-radius: 5px;\n"
"}")
        self.pushButton_6.setIcon(icon11)

        self.gridLayout.addWidget(self.pushButton_6, 1, 0, 1, 1)

        self.pushButton_7 = QPushButton(self.frame_13)
        self.pushButton_7.setObjectName(u"pushButton_7")
        self.pushButton_7.setStyleSheet(u"QPushButton{\n"
"	color: #ffffff;\n"
"	width: 70%;	\n"
"	height: 100%;\n"
"	font-style: normal;\n"
"	font-weight: 800;\n"
"	height: 200%;\n"
"	width: 250%;\n"
"	background-color: rgb(60, 60, 60 );\n"
"	border: 1px solid rgb(30, 30, 30 / 50%);\n"
"	border-radius: 5px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	background-color: rgb(60, 60, 60);\n"
"	border: 1px solid rgb(100, 100, 100);\n"
"	border-width: 1px;\n"
"	border-radius: 5px;\n"
"}")
        self.pushButton_7.setIcon(icon11)

        self.gridLayout.addWidget(self.pushButton_7, 2, 0, 1, 1)

        self.pushButton_2 = QPushButton(self.frame_13)
        self.pushButton_2.setObjectName(u"pushButton_2")
        self.pushButton_2.setStyleSheet(u"QPushButton{\n"
"	color: #ffffff;\n"
"	width: 70%;	\n"
"	height: 100%;\n"
"	font-style: normal;\n"
"	font-weight: 800;\n"
"	height: 200%;\n"
"	width: 250%;\n"
"	background-color: rgb(60, 60, 60 );\n"
"	border: 1px solid rgb(30, 30, 30 / 50%);\n"
"	border-radius: 5px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	background-color: rgb(60, 60, 60);\n"
"	border: 1px solid rgb(100, 100, 100);\n"
"	border-width: 1px;\n"
"	border-radius: 5px;\n"
"}")
        self.pushButton_2.setIcon(icon11)

        self.gridLayout.addWidget(self.pushButton_2, 1, 1, 1, 1)

        self.pushButton_5 = QPushButton(self.frame_13)
        self.pushButton_5.setObjectName(u"pushButton_5")
        self.pushButton_5.setStyleSheet(u"QPushButton{\n"
"	color: #ffffff;\n"
"	width: 70%;	\n"
"	background-color: rgb(0, 197, 95 / 85%);\n"
"	height: 100%;\n"
"	font-style: normal;\n"
"	font-weight: 800;\n"
"	height: 200%;\n"
"	width: 250%;\n"
"	border: 1px solid rgb(85, 255, 127 / 20%);\n"
"	border-radius: 5px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	background-color: rgb(0, 197, 95);\n"
"	border: 1px solid rgb(85, 255, 127);\n"
"	border-width: 1px;\n"
"	border-radius: 5px;\n"
"}")
        self.pushButton_5.setIcon(icon11)

        self.gridLayout.addWidget(self.pushButton_5, 0, 1, 1, 1)

        self.pushButton = QPushButton(self.frame_13)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setStyleSheet(u"QPushButton{\n"
"	color: #ffffff;\n"
"	width: 70%;	\n"
"	height: 100%;\n"
"	font-style: normal;\n"
"	font-weight: 800;\n"
"	height: 200%;\n"
"	width: 250%;\n"
"	background-color: rgb(60, 60, 60 );\n"
"	border: 1px solid rgb(30, 30, 30 / 50%);\n"
"	border-radius: 5px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	background-color: rgb(60, 60, 60);\n"
"	border: 1px solid rgb(100, 100, 100);\n"
"	border-width: 1px;\n"
"	border-radius: 5px;\n"
"}")
        self.pushButton.setIcon(icon11)

        self.gridLayout.addWidget(self.pushButton, 3, 0, 1, 1)


        self.verticalLayout_23.addWidget(self.frame_13)

        self.frame_28 = QFrame(self.plancha1_1)
        self.frame_28.setObjectName(u"frame_28")
        self.frame_28.setFrameShape(QFrame.StyledPanel)
        self.frame_28.setFrameShadow(QFrame.Raised)
        self.verticalLayout_13 = QVBoxLayout(self.frame_28)
        self.verticalLayout_13.setObjectName(u"verticalLayout_13")
        self.initMad_plancha1_horno1Btn = QPushButton(self.frame_28)
        self.initMad_plancha1_horno1Btn.setObjectName(u"initMad_plancha1_horno1Btn")
        self.initMad_plancha1_horno1Btn.setMaximumSize(QSize(16777215, 16777215))
        self.initMad_plancha1_horno1Btn.setFont(font1)
        self.initMad_plancha1_horno1Btn.setStyleSheet(u"QPushButton {\n"
"	background-color: rgb(194, 255, 156);\n"
"	font-style: normal;\n"
"	font-weight: 800;\n"
"	height: 50%;\n"
"	width: 300%;\n"
"	border-radius: 20px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	background-color: rgb(146, 216, 107);\n"
"	border: 5px solid rgb(194, 255, 156);\n"
"	border-width: 1px;\n"
"	border-radius: 20px;\n"
"}\n"
"\n"
"\n"
"\n"
"")
        self.initMad_plancha1_horno1Btn.setIcon(icon12)
        self.initMad_plancha1_horno1Btn.setIconSize(QSize(30, 30))

        self.verticalLayout_13.addWidget(self.initMad_plancha1_horno1Btn, 0, Qt.AlignRight|Qt.AlignBottom)


        self.verticalLayout_23.addWidget(self.frame_28)

        self.mainPages.addWidget(self.plancha1_1)
        self.plancha2_1 = QWidget()
        self.plancha2_1.setObjectName(u"plancha2_1")
        self.verticalLayout_32 = QVBoxLayout(self.plancha2_1)
        self.verticalLayout_32.setObjectName(u"verticalLayout_32")
        self.frame_21 = QFrame(self.plancha2_1)
        self.frame_21.setObjectName(u"frame_21")
        self.frame_21.setStyleSheet(u"#frame_21{\n"
"	background-color: #fdfcf4;;\n"
"	border-radius: 10px;\n"
"}")
        self.frame_21.setFrameShape(QFrame.StyledPanel)
        self.frame_21.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_16 = QHBoxLayout(self.frame_21)
        self.horizontalLayout_16.setObjectName(u"horizontalLayout_16")
        self.label_20 = QLabel(self.frame_21)
        self.label_20.setObjectName(u"label_20")
        self.label_20.setFont(font)
        self.label_20.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.horizontalLayout_16.addWidget(self.label_20)

        self.backPlancha2Hor1Btn = QPushButton(self.frame_21)
        self.backPlancha2Hor1Btn.setObjectName(u"backPlancha2Hor1Btn")
        self.backPlancha2Hor1Btn.setStyleSheet(u"QPushButton {\n"
"	background-color: #fdfcf4;\n"
"	font-style: normal;\n"
"	font-weight: 800;\n"
"	height: 20%;\n"
"	width: 30%;\n"
"	border-radius: 30%;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	border: 5px solid rgb(0, 0, 0);\n"
"	border-width: 2px;\n"
"	border-radius: 10%;\n"
"}\n"
"\n"
"	\n"
"")
        self.backPlancha2Hor1Btn.setIcon(icon10)

        self.horizontalLayout_16.addWidget(self.backPlancha2Hor1Btn, 0, Qt.AlignRight|Qt.AlignVCenter)


        self.verticalLayout_32.addWidget(self.frame_21)

        self.frame_30 = QFrame(self.plancha2_1)
        self.frame_30.setObjectName(u"frame_30")
        self.frame_30.setFrameShape(QFrame.StyledPanel)
        self.frame_30.setFrameShadow(QFrame.Raised)
        self.gridLayout_8 = QGridLayout(self.frame_30)
        self.gridLayout_8.setObjectName(u"gridLayout_8")
        self.label_19 = QLabel(self.frame_30)
        self.label_19.setObjectName(u"label_19")
        self.label_19.setFont(font2)
        self.label_19.setStyleSheet(u"color: #ffffff;")

        self.gridLayout_8.addWidget(self.label_19, 1, 1, 1, 1, Qt.AlignLeft)

        self.label_18 = QLabel(self.frame_30)
        self.label_18.setObjectName(u"label_18")
        self.label_18.setFont(font2)
        self.label_18.setStyleSheet(u"color: #ffffff;")

        self.gridLayout_8.addWidget(self.label_18, 0, 1, 1, 1, Qt.AlignLeft)

        self.label_17 = QLabel(self.frame_30)
        self.label_17.setObjectName(u"label_17")
        self.label_17.setFont(font)
        self.label_17.setStyleSheet(u"color: #ffffff;")

        self.gridLayout_8.addWidget(self.label_17, 0, 0, 1, 1, Qt.AlignLeft)

        self.label_22 = QLabel(self.frame_30)
        self.label_22.setObjectName(u"label_22")
        self.label_22.setFont(font2)
        self.label_22.setStyleSheet(u"color: #ffffff;")

        self.gridLayout_8.addWidget(self.label_22, 0, 2, 1, 1, Qt.AlignRight)

        self.label_23 = QLabel(self.frame_30)
        self.label_23.setObjectName(u"label_23")
        font3 = QFont()
        font3.setPointSize(8)
        font3.setBold(True)
        font3.setWeight(75)
        self.label_23.setFont(font3)
        self.label_23.setStyleSheet(u"color: #ffffff;")

        self.gridLayout_8.addWidget(self.label_23, 1, 2, 1, 1, Qt.AlignRight)


        self.verticalLayout_32.addWidget(self.frame_30)

        self.frame_29 = QFrame(self.plancha2_1)
        self.frame_29.setObjectName(u"frame_29")
        self.frame_29.setEnabled(True)
        self.frame_29.setFrameShape(QFrame.StyledPanel)
        self.frame_29.setFrameShadow(QFrame.Raised)
        self.gridLayout_7 = QGridLayout(self.frame_29)
        self.gridLayout_7.setObjectName(u"gridLayout_7")
        self.pushButton_35 = QPushButton(self.frame_29)
        self.pushButton_35.setObjectName(u"pushButton_35")
        self.pushButton_35.setStyleSheet(u"QPushButton{\n"
"	color: #ffffff;\n"
"	width: 70%;	\n"
"	height: 100%;\n"
"	font-style: normal;\n"
"	font-weight: 800;\n"
"	height: 200%;\n"
"	width: 250%;\n"
"	background-color: rgb(60, 60, 60 );\n"
"	border: 1px solid rgb(30, 30, 30 / 50%);\n"
"	border-radius: 5px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	background-color: rgb(60, 60, 60);\n"
"	border: 1px solid rgb(100, 100, 100);\n"
"	border-width: 1px;\n"
"	border-radius: 5px;\n"
"}")
        self.pushButton_35.setIcon(icon11)

        self.gridLayout_7.addWidget(self.pushButton_35, 1, 1, 1, 1)

        self.pushButton_42 = QPushButton(self.frame_29)
        self.pushButton_42.setObjectName(u"pushButton_42")
        self.pushButton_42.setStyleSheet(u"QPushButton{\n"
"	color: #ffffff;\n"
"	width: 70%;	\n"
"	height: 100%;\n"
"	font-style: normal;\n"
"	font-weight: 800;\n"
"	height: 200%;\n"
"	width: 250%;\n"
"	background-color: rgb(60, 60, 60 );\n"
"	border: 1px solid rgb(30, 30, 30 / 50%);\n"
"	border-radius: 5px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	background-color: rgb(60, 60, 60);\n"
"	border: 1px solid rgb(100, 100, 100);\n"
"	border-width: 1px;\n"
"	border-radius: 5px;\n"
"}")
        self.pushButton_42.setIcon(icon11)

        self.gridLayout_7.addWidget(self.pushButton_42, 3, 1, 1, 1)

        self.pushButton_37 = QPushButton(self.frame_29)
        self.pushButton_37.setObjectName(u"pushButton_37")
        self.pushButton_37.setStyleSheet(u"QPushButton{\n"
"	color: #ffffff;\n"
"	width: 70%;	\n"
"	background-color: rgb(0, 197, 95 / 85%);\n"
"	height: 100%;\n"
"	font-style: normal;\n"
"	font-weight: 800;\n"
"	height: 200%;\n"
"	width: 250%;\n"
"	border: 1px solid rgb(85, 255, 127 / 20%);\n"
"	border-radius: 5px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	background-color: rgb(0, 197, 95);\n"
"	border: 1px solid rgb(85, 255, 127);\n"
"	border-width: 1px;\n"
"	border-radius: 5px;\n"
"}")
        self.pushButton_37.setIcon(icon11)

        self.gridLayout_7.addWidget(self.pushButton_37, 0, 0, 1, 1)

        self.pushButton_39 = QPushButton(self.frame_29)
        self.pushButton_39.setObjectName(u"pushButton_39")
        self.pushButton_39.setStyleSheet(u"QPushButton{\n"
"	color: #ffffff;\n"
"	width: 70%;	\n"
"	height: 100%;\n"
"	font-style: normal;\n"
"	font-weight: 800;\n"
"	height: 200%;\n"
"	width: 250%;\n"
"	background-color: rgb(60, 60, 60 );\n"
"	border: 1px solid rgb(30, 30, 30 / 50%);\n"
"	border-radius: 5px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	background-color: rgb(60, 60, 60);\n"
"	border: 1px solid rgb(100, 100, 100);\n"
"	border-width: 1px;\n"
"	border-radius: 5px;\n"
"}")
        self.pushButton_39.setIcon(icon11)

        self.gridLayout_7.addWidget(self.pushButton_39, 2, 0, 1, 1)

        self.pushButton_41 = QPushButton(self.frame_29)
        self.pushButton_41.setObjectName(u"pushButton_41")
        self.pushButton_41.setStyleSheet(u"QPushButton{\n"
"	color: #ffffff;\n"
"	width: 70%;	\n"
"	height: 100%;\n"
"	font-style: normal;\n"
"	font-weight: 800;\n"
"	height: 200%;\n"
"	width: 250%;\n"
"	background-color: rgb(60, 60, 60 );\n"
"	border: 1px solid rgb(30, 30, 30 / 50%);\n"
"	border-radius: 5px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	background-color: rgb(60, 60, 60);\n"
"	border: 1px solid rgb(100, 100, 100);\n"
"	border-width: 1px;\n"
"	border-radius: 5px;\n"
"}")
        self.pushButton_41.setIcon(icon11)

        self.gridLayout_7.addWidget(self.pushButton_41, 3, 0, 1, 1)

        self.pushButton_36 = QPushButton(self.frame_29)
        self.pushButton_36.setObjectName(u"pushButton_36")
        self.pushButton_36.setStyleSheet(u"QPushButton{\n"
"	color: #ffffff;\n"
"	width: 70%;	\n"
"	height: 100%;\n"
"	font-style: normal;\n"
"	font-weight: 800;\n"
"	height: 200%;\n"
"	width: 250%;\n"
"	background-color: rgb(60, 60, 60 );\n"
"	border: 1px solid rgb(30, 30, 30 / 50%);\n"
"	border-radius: 5px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	background-color: rgb(60, 60, 60);\n"
"	border: 1px solid rgb(100, 100, 100);\n"
"	border-width: 1px;\n"
"	border-radius: 5px;\n"
"}")
        self.pushButton_36.setIcon(icon11)

        self.gridLayout_7.addWidget(self.pushButton_36, 1, 0, 1, 1)

        self.pushButton_44 = QPushButton(self.frame_29)
        self.pushButton_44.setObjectName(u"pushButton_44")
        self.pushButton_44.setStyleSheet(u"QPushButton{\n"
"	color: #ffffff;\n"
"	width: 70%;	\n"
"	height: 100%;\n"
"	font-style: normal;\n"
"	font-weight: 800;\n"
"	height: 200%;\n"
"	width: 250%;\n"
"	background-color: rgb(60, 60, 60 );\n"
"	border: 1px solid rgb(30, 30, 30 / 50%);\n"
"	border-radius: 5px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	background-color: rgb(60, 60, 60);\n"
"	border: 1px solid rgb(100, 100, 100);\n"
"	border-width: 1px;\n"
"	border-radius: 5px;\n"
"}")
        self.pushButton_44.setIcon(icon11)

        self.gridLayout_7.addWidget(self.pushButton_44, 4, 1, 1, 1)

        self.pushButton_43 = QPushButton(self.frame_29)
        self.pushButton_43.setObjectName(u"pushButton_43")
        self.pushButton_43.setStyleSheet(u"QPushButton{\n"
"	color: #ffffff;\n"
"	width: 70%;	\n"
"	height: 100%;\n"
"	font-style: normal;\n"
"	font-weight: 800;\n"
"	height: 200%;\n"
"	width: 250%;\n"
"	background-color: rgb(60, 60, 60 );\n"
"	border: 1px solid rgb(30, 30, 30 / 50%);\n"
"	border-radius: 5px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	background-color: rgb(60, 60, 60);\n"
"	border: 1px solid rgb(100, 100, 100);\n"
"	border-width: 1px;\n"
"	border-radius: 5px;\n"
"}")
        self.pushButton_43.setIcon(icon11)

        self.gridLayout_7.addWidget(self.pushButton_43, 4, 0, 1, 1)

        self.pushButton_38 = QPushButton(self.frame_29)
        self.pushButton_38.setObjectName(u"pushButton_38")
        self.pushButton_38.setStyleSheet(u"QPushButton{\n"
"	color: #ffffff;\n"
"	width: 70%;	\n"
"	background-color: rgb(0, 197, 95 / 85%);\n"
"	height: 100%;\n"
"	font-style: normal;\n"
"	font-weight: 800;\n"
"	height: 200%;\n"
"	width: 250%;\n"
"	border: 1px solid rgb(85, 255, 127 / 20%);\n"
"	border-radius: 5px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	background-color: rgb(0, 197, 95);\n"
"	border: 1px solid rgb(85, 255, 127);\n"
"	border-width: 1px;\n"
"	border-radius: 5px;\n"
"}")
        self.pushButton_38.setIcon(icon11)

        self.gridLayout_7.addWidget(self.pushButton_38, 0, 1, 1, 1)

        self.pushButton_40 = QPushButton(self.frame_29)
        self.pushButton_40.setObjectName(u"pushButton_40")
        self.pushButton_40.setStyleSheet(u"QPushButton{\n"
"	color: #ffffff;\n"
"	width: 70%;	\n"
"	height: 100%;\n"
"	font-style: normal;\n"
"	font-weight: 800;\n"
"	height: 200%;\n"
"	width: 250%;\n"
"	background-color: rgb(60, 60, 60 );\n"
"	border: 1px solid rgb(30, 30, 30 / 50%);\n"
"	border-radius: 5px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	background-color: rgb(60, 60, 60);\n"
"	border: 1px solid rgb(100, 100, 100);\n"
"	border-width: 1px;\n"
"	border-radius: 5px;\n"
"}")
        self.pushButton_40.setIcon(icon11)

        self.gridLayout_7.addWidget(self.pushButton_40, 2, 1, 1, 1)


        self.verticalLayout_32.addWidget(self.frame_29)

        self.frame_34 = QFrame(self.plancha2_1)
        self.frame_34.setObjectName(u"frame_34")
        self.frame_34.setFrameShape(QFrame.StyledPanel)
        self.frame_34.setFrameShadow(QFrame.Raised)
        self.verticalLayout_21 = QVBoxLayout(self.frame_34)
        self.verticalLayout_21.setObjectName(u"verticalLayout_21")
        self.initMad_plancha2_horno1Btn = QPushButton(self.frame_34)
        self.initMad_plancha2_horno1Btn.setObjectName(u"initMad_plancha2_horno1Btn")
        self.initMad_plancha2_horno1Btn.setMaximumSize(QSize(16777215, 16777215))
        self.initMad_plancha2_horno1Btn.setFont(font1)
        self.initMad_plancha2_horno1Btn.setStyleSheet(u"QPushButton {\n"
"	background-color: rgb(194, 255, 156);\n"
"	font-style: normal;\n"
"	font-weight: 800;\n"
"	height: 50%;\n"
"	width: 300%;\n"
"	border-radius: 20px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	background-color: rgb(146, 216, 107);\n"
"	border: 5px solid rgb(194, 255, 156);\n"
"	border-width: 1px;\n"
"	border-radius: 20px;\n"
"}\n"
"\n"
"\n"
"\n"
"")
        self.initMad_plancha2_horno1Btn.setIcon(icon12)
        self.initMad_plancha2_horno1Btn.setIconSize(QSize(30, 30))

        self.verticalLayout_21.addWidget(self.initMad_plancha2_horno1Btn)


        self.verticalLayout_32.addWidget(self.frame_34, 0, Qt.AlignRight)

        self.mainPages.addWidget(self.plancha2_1)
        self.planchasHor2 = QWidget()
        self.planchasHor2.setObjectName(u"planchasHor2")
        self.verticalLayout_33 = QVBoxLayout(self.planchasHor2)
        self.verticalLayout_33.setObjectName(u"verticalLayout_33")
        self.frame_20 = QFrame(self.planchasHor2)
        self.frame_20.setObjectName(u"frame_20")
        self.frame_20.setStyleSheet(u"#frame_20{\n"
"	background-color: #fdfcf4;\n"
"	border-radius: 10px;\n"
"}")
        self.frame_20.setFrameShape(QFrame.StyledPanel)
        self.frame_20.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_15 = QHBoxLayout(self.frame_20)
        self.horizontalLayout_15.setObjectName(u"horizontalLayout_15")
        self.label_21 = QLabel(self.frame_20)
        self.label_21.setObjectName(u"label_21")
        self.label_21.setFont(font)
        self.label_21.setStyleSheet(u"")
        self.label_21.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.horizontalLayout_15.addWidget(self.label_21)

        self.backHor2Btn = QPushButton(self.frame_20)
        self.backHor2Btn.setObjectName(u"backHor2Btn")
        self.backHor2Btn.setStyleSheet(u"QPushButton {\n"
"	background-color: #fdfcf4;\n"
"	font-style: normal;\n"
"	font-weight: 800;\n"
"	height: 20%;\n"
"	width: 30%;\n"
"	border-radius: 30%;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	border: 5px solid rgb(0, 0, 0);\n"
"	border-width: 2px;\n"
"	border-radius: 10%;\n"
"}\n"
"\n"
"\n"
"	\n"
"\n"
"")
        self.backHor2Btn.setIcon(icon10)

        self.horizontalLayout_15.addWidget(self.backHor2Btn)


        self.verticalLayout_33.addWidget(self.frame_20)

        self.frame_32 = QFrame(self.planchasHor2)
        self.frame_32.setObjectName(u"frame_32")
        self.frame_32.setFrameShape(QFrame.StyledPanel)
        self.frame_32.setFrameShadow(QFrame.Raised)
        self.verticalLayout_29 = QVBoxLayout(self.frame_32)
        self.verticalLayout_29.setObjectName(u"verticalLayout_29")
        self.plancha1_horno2Btn = QPushButton(self.frame_32)
        self.plancha1_horno2Btn.setObjectName(u"plancha1_horno2Btn")
        self.plancha1_horno2Btn.setFont(font1)
        self.plancha1_horno2Btn.setStyleSheet(u"QPushButton{\n"
"	color: #ffffff;\n"
"	width: 70%;	\n"
"	background-color: rgb(0, 197, 95 / 85%);\n"
"	height: 100%;\n"
"	font-style: normal;\n"
"	font-weight: 800;\n"
"	height: 200%;\n"
"	width: 250%;\n"
"	border: 1px solid rgb(85, 255, 127 / 20%);\n"
"	border-radius: 5px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	background-color: rgb(0, 197, 95);\n"
"	border: 1px solid rgb(85, 255, 127);\n"
"	border-width: 1px;\n"
"	border-radius: 5px;\n"
"}")

        self.verticalLayout_29.addWidget(self.plancha1_horno2Btn)

        self.plancha2_horno2Btn = QPushButton(self.frame_32)
        self.plancha2_horno2Btn.setObjectName(u"plancha2_horno2Btn")
        self.plancha2_horno2Btn.setFont(font1)
        self.plancha2_horno2Btn.setStyleSheet(u"QPushButton{\n"
"	color: #ffffff;\n"
"	width: 70%;	\n"
"	background-color: rgb(0, 197, 95 / 85%);\n"
"	height: 100%;\n"
"	font-style: normal;\n"
"	font-weight: 800;\n"
"	height: 200%;\n"
"	width: 250%;\n"
"	border: 1px solid rgb(85, 255, 127 / 20%);\n"
"	border-radius: 5px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	background-color: rgb(0, 197, 95);\n"
"	border: 1px solid rgb(85, 255, 127);\n"
"	border-width: 1px;\n"
"	border-radius: 5px;\n"
"}")

        self.verticalLayout_29.addWidget(self.plancha2_horno2Btn)

        self.pushButton_16 = QPushButton(self.frame_32)
        self.pushButton_16.setObjectName(u"pushButton_16")
        self.pushButton_16.setFont(font1)
        self.pushButton_16.setStyleSheet(u"QPushButton{\n"
"	color: #ffffff;\n"
"	width: 70%;	\n"
"	height: 100%;\n"
"	font-style: normal;\n"
"	font-weight: 800;\n"
"	height: 200%;\n"
"	width: 250%;\n"
"	background-color: rgb(60, 60, 60 );\n"
"	border: 1px solid rgb(30, 30, 30 / 50%);\n"
"	border-radius: 5px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	background-color: rgb(60, 60, 60);\n"
"	border: 1px solid rgb(100, 100, 100);\n"
"	border-width: 1px;\n"
"	border-radius: 5px;\n"
"}")

        self.verticalLayout_29.addWidget(self.pushButton_16)

        self.pushButton_18 = QPushButton(self.frame_32)
        self.pushButton_18.setObjectName(u"pushButton_18")
        self.pushButton_18.setFont(font1)
        self.pushButton_18.setStyleSheet(u"QPushButton{\n"
"	color: #ffffff;\n"
"	width: 70%;	\n"
"	height: 100%;\n"
"	font-style: normal;\n"
"	font-weight: 800;\n"
"	height: 200%;\n"
"	width: 250%;\n"
"	background-color: rgb(60, 60, 60 );\n"
"	border: 1px solid rgb(30, 30, 30 / 50%);\n"
"	border-radius: 5px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	background-color: rgb(60, 60, 60);\n"
"	border: 1px solid rgb(100, 100, 100);\n"
"	border-width: 1px;\n"
"	border-radius: 5px;\n"
"}")

        self.verticalLayout_29.addWidget(self.pushButton_18)

        self.pushButton_15 = QPushButton(self.frame_32)
        self.pushButton_15.setObjectName(u"pushButton_15")
        self.pushButton_15.setFont(font1)
        self.pushButton_15.setStyleSheet(u"QPushButton{\n"
"	color: #ffffff;\n"
"	width: 70%;	\n"
"	height: 100%;\n"
"	font-style: normal;\n"
"	font-weight: 800;\n"
"	height: 200%;\n"
"	width: 250%;\n"
"	background-color: rgb(60, 60, 60 );\n"
"	border: 1px solid rgb(30, 30, 30 / 50%);\n"
"	border-radius: 5px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	background-color: rgb(60, 60, 60);\n"
"	border: 1px solid rgb(100, 100, 100);\n"
"	border-width: 1px;\n"
"	border-radius: 5px;\n"
"}")

        self.verticalLayout_29.addWidget(self.pushButton_15)

        self.pushButton_11 = QPushButton(self.frame_32)
        self.pushButton_11.setObjectName(u"pushButton_11")
        self.pushButton_11.setFont(font1)
        self.pushButton_11.setStyleSheet(u"QPushButton{\n"
"	color: #ffffff;\n"
"	width: 70%;	\n"
"	height: 100%;\n"
"	font-style: normal;\n"
"	font-weight: 800;\n"
"	height: 200%;\n"
"	width: 250%;\n"
"	background-color: rgb(60, 60, 60 );\n"
"	border: 1px solid rgb(30, 30, 30 / 50%);\n"
"	border-radius: 5px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	background-color: rgb(60, 60, 60);\n"
"	border: 1px solid rgb(100, 100, 100);\n"
"	border-width: 1px;\n"
"	border-radius: 5px;\n"
"}")

        self.verticalLayout_29.addWidget(self.pushButton_11)

        self.pushButton_19 = QPushButton(self.frame_32)
        self.pushButton_19.setObjectName(u"pushButton_19")
        self.pushButton_19.setFont(font1)
        self.pushButton_19.setStyleSheet(u"QPushButton{\n"
"	color: #ffffff;\n"
"	width: 70%;	\n"
"	height: 100%;\n"
"	font-style: normal;\n"
"	font-weight: 800;\n"
"	height: 200%;\n"
"	width: 250%;\n"
"	background-color: rgb(60, 60, 60 );\n"
"	border: 1px solid rgb(30, 30, 30 / 50%);\n"
"	border-radius: 5px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	background-color: rgb(60, 60, 60);\n"
"	border: 1px solid rgb(100, 100, 100);\n"
"	border-width: 1px;\n"
"	border-radius: 5px;\n"
"}")

        self.verticalLayout_29.addWidget(self.pushButton_19)

        self.pushButton_17 = QPushButton(self.frame_32)
        self.pushButton_17.setObjectName(u"pushButton_17")
        self.pushButton_17.setFont(font1)
        self.pushButton_17.setStyleSheet(u"QPushButton{\n"
"	color: #ffffff;\n"
"	width: 70%;	\n"
"	height: 100%;\n"
"	font-style: normal;\n"
"	font-weight: 800;\n"
"	height: 200%;\n"
"	width: 250%;\n"
"	background-color: rgb(60, 60, 60 );\n"
"	border: 1px solid rgb(30, 30, 30 / 50%);\n"
"	border-radius: 5px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	background-color: rgb(60, 60, 60);\n"
"	border: 1px solid rgb(100, 100, 100);\n"
"	border-width: 1px;\n"
"	border-radius: 5px;\n"
"}")

        self.verticalLayout_29.addWidget(self.pushButton_17)

        self.pushButton_12 = QPushButton(self.frame_32)
        self.pushButton_12.setObjectName(u"pushButton_12")
        self.pushButton_12.setFont(font1)
        self.pushButton_12.setStyleSheet(u"QPushButton{\n"
"	color: #ffffff;\n"
"	width: 70%;	\n"
"	height: 100%;\n"
"	font-style: normal;\n"
"	font-weight: 800;\n"
"	height: 200%;\n"
"	width: 250%;\n"
"	background-color: rgb(60, 60, 60 );\n"
"	border: 1px solid rgb(30, 30, 30 / 50%);\n"
"	border-radius: 5px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	background-color: rgb(60, 60, 60);\n"
"	border: 1px solid rgb(100, 100, 100);\n"
"	border-width: 1px;\n"
"	border-radius: 5px;\n"
"}")

        self.verticalLayout_29.addWidget(self.pushButton_12)

        self.pushButton_20 = QPushButton(self.frame_32)
        self.pushButton_20.setObjectName(u"pushButton_20")
        self.pushButton_20.setFont(font1)
        self.pushButton_20.setStyleSheet(u"QPushButton{\n"
"	color: #ffffff;\n"
"	width: 70%;	\n"
"	height: 100%;\n"
"	font-style: normal;\n"
"	font-weight: 800;\n"
"	height: 200%;\n"
"	width: 250%;\n"
"	background-color: rgb(60, 60, 60 );\n"
"	border: 1px solid rgb(30, 30, 30 / 50%);\n"
"	border-radius: 5px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	background-color: rgb(60, 60, 60);\n"
"	border: 1px solid rgb(100, 100, 100);\n"
"	border-width: 1px;\n"
"	border-radius: 5px;\n"
"}")

        self.verticalLayout_29.addWidget(self.pushButton_20)

        self.pushButton_14 = QPushButton(self.frame_32)
        self.pushButton_14.setObjectName(u"pushButton_14")
        self.pushButton_14.setFont(font1)
        self.pushButton_14.setStyleSheet(u"QPushButton{\n"
"	color: #ffffff;\n"
"	width: 70%;	\n"
"	height: 100%;\n"
"	font-style: normal;\n"
"	font-weight: 800;\n"
"	height: 200%;\n"
"	width: 250%;\n"
"	background-color: rgb(60, 60, 60 );\n"
"	border: 1px solid rgb(30, 30, 30 / 50%);\n"
"	border-radius: 5px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	background-color: rgb(60, 60, 60);\n"
"	border: 1px solid rgb(100, 100, 100);\n"
"	border-width: 1px;\n"
"	border-radius: 5px;\n"
"}")

        self.verticalLayout_29.addWidget(self.pushButton_14)

        self.pushButton_55 = QPushButton(self.frame_32)
        self.pushButton_55.setObjectName(u"pushButton_55")
        self.pushButton_55.setFont(font1)
        self.pushButton_55.setStyleSheet(u"QPushButton{\n"
"	color: #ffffff;\n"
"	width: 70%;	\n"
"	height: 100%;\n"
"	font-style: normal;\n"
"	font-weight: 800;\n"
"	height: 200%;\n"
"	width: 250%;\n"
"	background-color: rgb(60, 60, 60 );\n"
"	border: 1px solid rgb(30, 30, 30 / 50%);\n"
"	border-radius: 5px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	background-color: rgb(60, 60, 60);\n"
"	border: 1px solid rgb(100, 100, 100);\n"
"	border-width: 1px;\n"
"	border-radius: 5px;\n"
"}")

        self.verticalLayout_29.addWidget(self.pushButton_55)


        self.verticalLayout_33.addWidget(self.frame_32)

        self.mainPages.addWidget(self.planchasHor2)
        self.baseDeDatos = QWidget()
        self.baseDeDatos.setObjectName(u"baseDeDatos")
        self.gridLayout_11 = QGridLayout(self.baseDeDatos)
        self.gridLayout_11.setObjectName(u"gridLayout_11")
        self.frame_23 = QFrame(self.baseDeDatos)
        self.frame_23.setObjectName(u"frame_23")
        self.frame_23.setStyleSheet(u"#frame_23{\n"
"	background-color: #fdfcf4;\n"
"	border-radius: 10px;\n"
"}")
        self.frame_23.setFrameShape(QFrame.StyledPanel)
        self.frame_23.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_19 = QHBoxLayout(self.frame_23)
        self.horizontalLayout_19.setObjectName(u"horizontalLayout_19")
        self.label_3 = QLabel(self.frame_23)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setFont(font)
        self.label_3.setStyleSheet(u"")
        self.label_3.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.horizontalLayout_19.addWidget(self.label_3)

        self.backDBBtn = QPushButton(self.frame_23)
        self.backDBBtn.setObjectName(u"backDBBtn")
        self.backDBBtn.setStyleSheet(u"QPushButton {\n"
"	background-color: #fdfcf4;\n"
"	font-style: normal;\n"
"	font-weight: 800;\n"
"	height: 20%;\n"
"	width: 30%;\n"
"	border-radius: 30%;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	border: 5px solid rgb(0, 0, 0);\n"
"	border-width: 2px;\n"
"	border-radius: 10%;\n"
"}")
        self.backDBBtn.setIcon(icon10)

        self.horizontalLayout_19.addWidget(self.backDBBtn, 0, Qt.AlignRight)


        self.gridLayout_11.addWidget(self.frame_23, 0, 0, 1, 1, Qt.AlignTop)

        self.frame_27 = QFrame(self.baseDeDatos)
        self.frame_27.setObjectName(u"frame_27")
        self.frame_27.setStyleSheet(u"")
        self.frame_27.setFrameShape(QFrame.StyledPanel)
        self.frame_27.setFrameShadow(QFrame.Raised)
        self.gridLayout_12 = QGridLayout(self.frame_27)
        self.gridLayout_12.setObjectName(u"gridLayout_12")
        self.label_4 = QLabel(self.frame_27)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setFont(font)
        self.label_4.setStyleSheet(u"color: #ffffff;")
        self.label_4.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_12.addWidget(self.label_4, 0, 0, 1, 1)


        self.gridLayout_11.addWidget(self.frame_27, 1, 0, 1, 1, Qt.AlignHCenter|Qt.AlignVCenter)

        self.mainPages.addWidget(self.baseDeDatos)

        self.verticalLayout_15.addWidget(self.mainPages)


        self.horizontalLayout_7.addWidget(self.mainContentsContainer)

        self.rightMenuContainer = QCustomSlideMenu(self.mainBodyContent)
        self.rightMenuContainer.setObjectName(u"rightMenuContainer")
        self.rightMenuContainer.setMinimumSize(QSize(200, 0))
        self.rightMenuContainer.setMaximumSize(QSize(200, 188))
        self.verticalLayout_11 = QVBoxLayout(self.rightMenuContainer)
        self.verticalLayout_11.setSpacing(0)
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.verticalLayout_11.setContentsMargins(0, 0, 0, 0)
        self.rightMenuSubContainer = QWidget(self.rightMenuContainer)
        self.rightMenuSubContainer.setObjectName(u"rightMenuSubContainer")
        self.rightMenuSubContainer.setMinimumSize(QSize(200, 0))
        self.verticalLayout_12 = QVBoxLayout(self.rightMenuSubContainer)
        self.verticalLayout_12.setSpacing(5)
        self.verticalLayout_12.setObjectName(u"verticalLayout_12")
        self.verticalLayout_12.setContentsMargins(5, 5, 5, 5)
        self.rightMenuPages = QCustomStackedWidget(self.rightMenuSubContainer)
        self.rightMenuPages.setObjectName(u"rightMenuPages")
        self.logsPage = QWidget()
        self.logsPage.setObjectName(u"logsPage")
        self.verticalLayout_14 = QVBoxLayout(self.logsPage)
        self.verticalLayout_14.setObjectName(u"verticalLayout_14")
        self.logs = QFrame(self.logsPage)
        self.logs.setObjectName(u"logs")
        self.logs.setStyleSheet(u"QFrame{\n"
"	background-color: #fdfcf4;\n"
"	border-radius: 10px;\n"
"}\n"
"\n"
"\n"
"")
        self.logs.setFrameShape(QFrame.StyledPanel)
        self.logs.setFrameShadow(QFrame.Raised)
        self.verticalLayout_7 = QVBoxLayout(self.logs)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.frame_5 = QFrame(self.logs)
        self.frame_5.setObjectName(u"frame_5")
        self.frame_5.setFrameShape(QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_8 = QHBoxLayout(self.frame_5)
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.label_2 = QLabel(self.frame_5)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setFont(font)
        self.label_2.setStyleSheet(u"")

        self.horizontalLayout_8.addWidget(self.label_2)

        self.closeRightMenuBtn = QPushButton(self.frame_5)
        self.closeRightMenuBtn.setObjectName(u"closeRightMenuBtn")
        self.closeRightMenuBtn.setIcon(icon5)
        self.closeRightMenuBtn.setIconSize(QSize(24, 24))

        self.horizontalLayout_8.addWidget(self.closeRightMenuBtn, 0, Qt.AlignRight)


        self.verticalLayout_7.addWidget(self.frame_5)


        self.verticalLayout_14.addWidget(self.logs, 0, Qt.AlignTop)

        self.frame_33 = QFrame(self.logsPage)
        self.frame_33.setObjectName(u"frame_33")
        self.frame_33.setFrameShape(QFrame.StyledPanel)
        self.frame_33.setFrameShadow(QFrame.Raised)
        self.verticalLayout_8 = QVBoxLayout(self.frame_33)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.label_40 = QLabel(self.frame_33)
        self.label_40.setObjectName(u"label_40")
        self.label_40.setFont(font2)
        self.label_40.setStyleSheet(u"color: #ffffff;")

        self.verticalLayout_8.addWidget(self.label_40)

        self.label_39 = QLabel(self.frame_33)
        self.label_39.setObjectName(u"label_39")
        self.label_39.setFont(font2)
        self.label_39.setStyleSheet(u"color: #ffffff;")

        self.verticalLayout_8.addWidget(self.label_39)


        self.verticalLayout_14.addWidget(self.frame_33)

        self.iniciarMad_2Btn_2 = QPushButton(self.logsPage)
        self.iniciarMad_2Btn_2.setObjectName(u"iniciarMad_2Btn_2")
        self.iniciarMad_2Btn_2.setMaximumSize(QSize(16777215, 16777215))
        self.iniciarMad_2Btn_2.setFont(font1)
        self.iniciarMad_2Btn_2.setStyleSheet(u"QPushButton{\n"
"	width: 70%;	\n"
"	height: 100%;\n"
"	font-style: normal;\n"
"	font-weight: 800;\n"
"	height: 50%;\n"
"	width: 150%;\n"
"   background-color: #fdfcf4;\n"
"	border-radius: 5px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	background-color: rgb(161, 156, 137);\n"
"	border: 1px solid rgb(255, 254, 216);\n"
"	border-width: 1px;\n"
"	border-radius: 5px;\n"
"}\n"
"")
        self.iniciarMad_2Btn_2.setIconSize(QSize(30, 30))

        self.verticalLayout_14.addWidget(self.iniciarMad_2Btn_2, 0, Qt.AlignRight|Qt.AlignBottom)

        self.rightMenuPages.addWidget(self.logsPage)

        self.verticalLayout_12.addWidget(self.rightMenuPages)


        self.verticalLayout_11.addWidget(self.rightMenuSubContainer)


        self.horizontalLayout_7.addWidget(self.rightMenuContainer, 0, Qt.AlignRight)


        self.verticalLayout_10.addWidget(self.mainBodyContent)

        self.popupNotificationContainer = QCustomSlideMenu(self.mainBodyContainer)
        self.popupNotificationContainer.setObjectName(u"popupNotificationContainer")
        self.popupNotificationContainer.setStyleSheet(u"background-color: #fdfcf4;\n"
"border-radius: 30px;")
        self.verticalLayout_19 = QVBoxLayout(self.popupNotificationContainer)
        self.verticalLayout_19.setObjectName(u"verticalLayout_19")
        self.popupNotificationSubContainer = QWidget(self.popupNotificationContainer)
        self.popupNotificationSubContainer.setObjectName(u"popupNotificationSubContainer")
        self.verticalLayout_20 = QVBoxLayout(self.popupNotificationSubContainer)
        self.verticalLayout_20.setObjectName(u"verticalLayout_20")
        self.frame_8 = QFrame(self.popupNotificationSubContainer)
        self.frame_8.setObjectName(u"frame_8")
        self.frame_8.setStyleSheet(u"background-color: #fdfcf4;")
        self.frame_8.setFrameShape(QFrame.StyledPanel)
        self.frame_8.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_9 = QHBoxLayout(self.frame_8)
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.label_12 = QLabel(self.frame_8)
        self.label_12.setObjectName(u"label_12")
        self.label_12.setFont(font)

        self.horizontalLayout_9.addWidget(self.label_12, 0, Qt.AlignLeft|Qt.AlignTop)

        self.closeNotificationBtn = QPushButton(self.frame_8)
        self.closeNotificationBtn.setObjectName(u"closeNotificationBtn")
        self.closeNotificationBtn.setIcon(icon5)
        self.closeNotificationBtn.setIconSize(QSize(24, 24))

        self.horizontalLayout_9.addWidget(self.closeNotificationBtn, 0, Qt.AlignRight|Qt.AlignTop)


        self.verticalLayout_20.addWidget(self.frame_8)


        self.verticalLayout_19.addWidget(self.popupNotificationSubContainer)


        self.verticalLayout_10.addWidget(self.popupNotificationContainer)


        self.horizontalLayout.addWidget(self.mainBodyContainer)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        self.centerMenuPages.setCurrentIndex(0)
        self.mainPages.setCurrentIndex(0)
        self.rightMenuPages.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
#if QT_CONFIG(tooltip)
        self.menuBtn.setToolTip(QCoreApplication.translate("MainWindow", u"Menu", None))
#endif // QT_CONFIG(tooltip)
        self.menuBtn.setText("")
#if QT_CONFIG(tooltip)
        self.homeBtn.setToolTip(QCoreApplication.translate("MainWindow", u"Hornos", None))
#endif // QT_CONFIG(tooltip)
        self.homeBtn.setText(QCoreApplication.translate("MainWindow", u"Hornos", None))
#if QT_CONFIG(tooltip)
        self.DBBtn.setToolTip(QCoreApplication.translate("MainWindow", u"Base de datos", None))
#endif // QT_CONFIG(tooltip)
        self.DBBtn.setText(QCoreApplication.translate("MainWindow", u"Base de datos", None))
#if QT_CONFIG(tooltip)
        self.logsBtn.setToolTip(QCoreApplication.translate("MainWindow", u"Logs", None))
#endif // QT_CONFIG(tooltip)
        self.logsBtn.setText(QCoreApplication.translate("MainWindow", u"Logs", None))
#if QT_CONFIG(tooltip)
        self.helpBtn.setToolTip(QCoreApplication.translate("MainWindow", u"Ayuda", None))
#endif // QT_CONFIG(tooltip)
        self.helpBtn.setText(QCoreApplication.translate("MainWindow", u"Ayuda", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"AYUDA", None))
#if QT_CONFIG(tooltip)
        self.closeCenterMenuBtn.setToolTip(QCoreApplication.translate("MainWindow", u"Cerrar", None))
#endif // QT_CONFIG(tooltip)
        self.closeCenterMenuBtn.setText("")
#if QT_CONFIG(tooltip)
        self.notificationBtn.setToolTip(QCoreApplication.translate("MainWindow", u"Notificaciones", None))
#endif // QT_CONFIG(tooltip)
        self.notificationBtn.setText("")
#if QT_CONFIG(tooltip)
        self.minimizeBtn.setToolTip(QCoreApplication.translate("MainWindow", u"Minimizar", None))
#endif // QT_CONFIG(tooltip)
        self.minimizeBtn.setText("")
#if QT_CONFIG(tooltip)
        self.restoreBtn.setToolTip(QCoreApplication.translate("MainWindow", u"Expandir", None))
#endif // QT_CONFIG(tooltip)
        self.restoreBtn.setText("")
#if QT_CONFIG(tooltip)
        self.closeBtn.setToolTip(QCoreApplication.translate("MainWindow", u"Cerrar", None))
#endif // QT_CONFIG(tooltip)
        self.closeBtn.setText("")
        self.HOR1Btn.setText(QCoreApplication.translate("MainWindow", u"HOR1", None))
        self.HOR2Btn.setText(QCoreApplication.translate("MainWindow", u"HOR2", None))
        self.label_9.setText(QCoreApplication.translate("MainWindow", u"Notificaciones", None))
        self.label_37.setText(QCoreApplication.translate("MainWindow", u"Error detectado de tensi\u00f3n en HORNO 1, Plancha 2", None))
        self.label_36.setText(QCoreApplication.translate("MainWindow", u"Error detectado en HORNO1, Plancha 1, Posicion (1,3)", None))
        self.label_30.setText(QCoreApplication.translate("MainWindow", u"HORNO 2", None))
        self.backPlancha3Hor1Btn.setText("")
        self.label_27.setText(QCoreApplication.translate("MainWindow", u"Temperatura:", None))
        self.label_26.setText(QCoreApplication.translate("MainWindow", u"Tension:", None))
        self.label_25.setText(QCoreApplication.translate("MainWindow", u"Plancha 2", None))
        self.label_28.setText(QCoreApplication.translate("MainWindow", u"3,9 V", None))
        self.label_29.setText(QCoreApplication.translate("MainWindow", u"98 \u00ba C", None))
        self.pushButton_33.setText(QCoreApplication.translate("MainWindow", u"8", None))
        self.pushButton_34.setText(QCoreApplication.translate("MainWindow", u"10", None))
        self.pushButton_32.setText(QCoreApplication.translate("MainWindow", u"6", None))
        self.pushButton_27.setText(QCoreApplication.translate("MainWindow", u"5", None))
        self.pushButton_25.setText(QCoreApplication.translate("MainWindow", u"7", None))
        self.pushButton_29.setText(QCoreApplication.translate("MainWindow", u"1", None))
        self.pushButton_26.setText(QCoreApplication.translate("MainWindow", u"9", None))
        self.pushButton_28.setText(QCoreApplication.translate("MainWindow", u"3", None))
        self.pushButton_31.setText(QCoreApplication.translate("MainWindow", u"4", None))
        self.pushButton_30.setText(QCoreApplication.translate("MainWindow", u"2", None))
        self.initMad_plancha2_horno2Btn.setText(QCoreApplication.translate("MainWindow", u"INICIAR MADURACION", None))
        self.label_24.setText(QCoreApplication.translate("MainWindow", u"HORNO 2", None))
        self.backPlancha1Hor2Btn.setText("")
        self.label_31.setText(QCoreApplication.translate("MainWindow", u"Temperatura:", None))
        self.label_32.setText(QCoreApplication.translate("MainWindow", u"Tension:", None))
        self.label_33.setText(QCoreApplication.translate("MainWindow", u"Plancha 1", None))
        self.label_34.setText(QCoreApplication.translate("MainWindow", u"3,9 V", None))
        self.label_35.setText(QCoreApplication.translate("MainWindow", u"98 \u00ba C", None))
        self.pushButton_46.setText(QCoreApplication.translate("MainWindow", u"8", None))
        self.pushButton_47.setText(QCoreApplication.translate("MainWindow", u"10", None))
        self.pushButton_48.setText(QCoreApplication.translate("MainWindow", u"6", None))
        self.pushButton_49.setText(QCoreApplication.translate("MainWindow", u"5", None))
        self.pushButton_50.setText(QCoreApplication.translate("MainWindow", u"7", None))
        self.pushButton_51.setText(QCoreApplication.translate("MainWindow", u"1", None))
        self.pushButton_52.setText(QCoreApplication.translate("MainWindow", u"9", None))
        self.pushButton_53.setText(QCoreApplication.translate("MainWindow", u"3", None))
        self.pushButton_56.setText(QCoreApplication.translate("MainWindow", u"4", None))
        self.pushButton_57.setText(QCoreApplication.translate("MainWindow", u"2", None))
        self.iniciarMad_1Btn_4.setText(QCoreApplication.translate("MainWindow", u"INICIAR MADURACION", None))
        self.label_13.setText(QCoreApplication.translate("MainWindow", u"HORNO 1", None))
#if QT_CONFIG(tooltip)
        self.backHor1Btn.setToolTip(QCoreApplication.translate("MainWindow", u"Atr\u00e1s", None))
#endif // QT_CONFIG(tooltip)
        self.backHor1Btn.setText("")
        self.plancha1_horno1Btn.setText(QCoreApplication.translate("MainWindow", u"Plancha 1", None))
        self.plancha2_horno1Btn.setText(QCoreApplication.translate("MainWindow", u"Plancha 2", None))
        self.plancha3_1Btn.setText(QCoreApplication.translate("MainWindow", u"Plancha 3", None))
        self.plancha4_1Btn.setText(QCoreApplication.translate("MainWindow", u"Plancha 4", None))
        self.plancha5_1Btn.setText(QCoreApplication.translate("MainWindow", u"Plancha 5", None))
        self.plancha6_1Btn.setText(QCoreApplication.translate("MainWindow", u"Plancha 6", None))
        self.plancha7_1Btn.setText(QCoreApplication.translate("MainWindow", u"Plancha 7", None))
        self.plancha8_1Btn.setText(QCoreApplication.translate("MainWindow", u"Plancha 8", None))
        self.plancha9_1Btn.setText(QCoreApplication.translate("MainWindow", u"Plancha 9", None))
        self.plancha10_1Btn.setText(QCoreApplication.translate("MainWindow", u"Plancha 10", None))
        self.plancha11_1Btn.setText(QCoreApplication.translate("MainWindow", u"Plancha 11", None))
        self.plancha12_1Btn.setText(QCoreApplication.translate("MainWindow", u"Plancha 12", None))
        self.label_14.setText(QCoreApplication.translate("MainWindow", u"HORNO 1", None))
#if QT_CONFIG(tooltip)
        self.backPlancha1Hor1Btn.setToolTip(QCoreApplication.translate("MainWindow", u"Atr\u00e1s", None))
#endif // QT_CONFIG(tooltip)
        self.backPlancha1Hor1Btn.setText("")
        self.label_16.setText(QCoreApplication.translate("MainWindow", u"100 \u00b0C", None))
        self.label_11.setText(QCoreApplication.translate("MainWindow", u"Temperatura:", None))
        self.label_15.setText(QCoreApplication.translate("MainWindow", u"2,9 V", None))
        self.label_10.setText(QCoreApplication.translate("MainWindow", u"Tension: ", None))
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"Plancha 1", None))
        self.pushButton_10.setText(QCoreApplication.translate("MainWindow", u"10", None))
        self.pushButton_9.setText(QCoreApplication.translate("MainWindow", u"1", None))
        self.pushButton_8.setText(QCoreApplication.translate("MainWindow", u"6", None))
        self.pushButton_4.setText(QCoreApplication.translate("MainWindow", u"8", None))
        self.pushButton_3.setText(QCoreApplication.translate("MainWindow", u"9", None))
        self.pushButton_6.setText(QCoreApplication.translate("MainWindow", u"3", None))
        self.pushButton_7.setText(QCoreApplication.translate("MainWindow", u"5", None))
        self.pushButton_2.setText(QCoreApplication.translate("MainWindow", u"4", None))
        self.pushButton_5.setText(QCoreApplication.translate("MainWindow", u"2", None))
        self.pushButton.setText(QCoreApplication.translate("MainWindow", u"7", None))
        self.initMad_plancha1_horno1Btn.setText(QCoreApplication.translate("MainWindow", u"INICIAR MADURACION", None))
        self.label_20.setText(QCoreApplication.translate("MainWindow", u"HORNO 1", None))
        self.backPlancha2Hor1Btn.setText("")
        self.label_19.setText(QCoreApplication.translate("MainWindow", u"Temperatura:", None))
        self.label_18.setText(QCoreApplication.translate("MainWindow", u"Tension: ", None))
        self.label_17.setText(QCoreApplication.translate("MainWindow", u"Plancha 2", None))
        self.label_22.setText(QCoreApplication.translate("MainWindow", u"2,9 V", None))
        self.label_23.setText(QCoreApplication.translate("MainWindow", u"100 \u00b0C", None))
        self.pushButton_35.setText(QCoreApplication.translate("MainWindow", u"4", None))
        self.pushButton_42.setText(QCoreApplication.translate("MainWindow", u"8", None))
        self.pushButton_37.setText(QCoreApplication.translate("MainWindow", u"1", None))
        self.pushButton_39.setText(QCoreApplication.translate("MainWindow", u"5", None))
        self.pushButton_41.setText(QCoreApplication.translate("MainWindow", u"7", None))
        self.pushButton_36.setText(QCoreApplication.translate("MainWindow", u"3", None))
        self.pushButton_44.setText(QCoreApplication.translate("MainWindow", u"10", None))
        self.pushButton_43.setText(QCoreApplication.translate("MainWindow", u"9", None))
        self.pushButton_38.setText(QCoreApplication.translate("MainWindow", u"2", None))
        self.pushButton_40.setText(QCoreApplication.translate("MainWindow", u"6", None))
        self.initMad_plancha2_horno1Btn.setText(QCoreApplication.translate("MainWindow", u"INICIAR MADURACION", None))
        self.label_21.setText(QCoreApplication.translate("MainWindow", u"HORNO 2", None))
        self.backHor2Btn.setText("")
        self.plancha1_horno2Btn.setText(QCoreApplication.translate("MainWindow", u"Plancha 1", None))
        self.plancha2_horno2Btn.setText(QCoreApplication.translate("MainWindow", u"Plancha 2", None))
        self.pushButton_16.setText(QCoreApplication.translate("MainWindow", u"Plancha 4", None))
        self.pushButton_18.setText(QCoreApplication.translate("MainWindow", u"Plancha 3", None))
        self.pushButton_15.setText(QCoreApplication.translate("MainWindow", u"Plancha 5", None))
        self.pushButton_11.setText(QCoreApplication.translate("MainWindow", u"Plancha 6", None))
        self.pushButton_19.setText(QCoreApplication.translate("MainWindow", u"Plancha 8", None))
        self.pushButton_17.setText(QCoreApplication.translate("MainWindow", u"Plancha 7", None))
        self.pushButton_12.setText(QCoreApplication.translate("MainWindow", u"Plancha 10", None))
        self.pushButton_20.setText(QCoreApplication.translate("MainWindow", u"Plancha 9", None))
        self.pushButton_14.setText(QCoreApplication.translate("MainWindow", u"Plancha 11", None))
        self.pushButton_55.setText(QCoreApplication.translate("MainWindow", u"Plancha 12", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"BASE DE DATOS", None))
        self.backDBBtn.setText("")
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"INFO A DETERMINAR", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"LOGS", None))
#if QT_CONFIG(tooltip)
        self.closeRightMenuBtn.setToolTip(QCoreApplication.translate("MainWindow", u"Cerrar", None))
#endif // QT_CONFIG(tooltip)
        self.closeRightMenuBtn.setText("")
        self.label_40.setText(QCoreApplication.translate("MainWindow", u"Error detectado en HORNO1, Plancha 1, Posicion (1,3)", None))
        self.label_39.setText(QCoreApplication.translate("MainWindow", u"Error detectado de tensi\u00f3n en HORNO 1, Plancha 2", None))
        self.iniciarMad_2Btn_2.setText(QCoreApplication.translate("MainWindow", u"Descargar", None))
        self.label_12.setText(QCoreApplication.translate("MainWindow", u"Notificaciones", None))
        self.closeNotificationBtn.setText("")
    # retranslateUi

