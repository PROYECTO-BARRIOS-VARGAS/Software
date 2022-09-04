# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'interfaceAsUOxG.ui'
##
## Created by: Qt User Interface Compiler version 5.14.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import (QCoreApplication, QMetaObject, QObject, QPoint,
    QRect, QSize, QUrl, Qt)
from PySide2.QtGui import (QBrush, QColor, QConicalGradient, QCursor, QFont,
    QFontDatabase, QIcon, QLinearGradient, QPalette, QPainter, QPixmap,
    QRadialGradient)
from PySide2.QtWidgets import *

from Custom_Widgets.Widgets import QCustomSlideMenu
from Custom_Widgets.Widgets import QCustomStackedWidget

import resources_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(703, 388)
        font = QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        MainWindow.setFont(font)
        MainWindow.setStyleSheet(u"*{\n"
"	border:none;\n"
"	background-color:transparent;\n"
"	background:transparent;\n"
"	padding: 0;\n"
"	margin: 0;\n"
"}\n"
"#centralwidget{\n"
"	background-color:#2c313c;\n"
"}\n"
"#leftMenuSubContainer{\n"
"	background-color:#d2d8d3;\n"
"}\n"
"#leftMenuSubContainer QPushButton{\n"
"	text-align: left;\n"
"	padding: 5px 10px;\n"
"	border-top-left-radius: 10px;\n"
"	border-bottom-left-radius: 10px;\n"
"}\n"
"#centerMenuSubContainer,#rightMenuSubContainer{\n"
"	background-color:#2c313c;\n"
"}\n"
"#frame_8,#popupNotificationSubContainer, #frame_14{\n"
"	background-color:#d2d8d3;\n"
"	border-radius: 10px;\n"
"}\n"
"#headerContainer,#footerContainer,#plancha1_1,#plancha2_1, #notificaciones{\n"
"	background-color:#d2d8d3;\n"
"}\n"
"#frame_9, #planchasHor2{\n"
"	background-color:#ff5733;\n"
"}\n"
"#frame_10{\n"
"	background-color:#6364a2;\n"
"}\n"
"#planchasHor1{\n"
"	background-color:#6364a2;\n"
"}\n"
"#frame_11, #frame_31{\n"
"	background-color:#4fcd60;\n"
"	border-radius: 10px;\n"
"}\n"
"#frame_9, #frame_10, #n"
                        "otificaciones{\n"
"	border-radius: 10px;\n"
"}\n"
"#headerContainer{\n"
"	height: 150;\n"
"}\n"
"\n"
"")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
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
        self.homeBtn.setStyleSheet(u"background-color: #2c313c;")
        icon1 = QIcon()
        icon1.addFile(u":/icons/icons/home.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.homeBtn.setIcon(icon1)
        self.homeBtn.setIconSize(QSize(24, 24))

        self.verticalLayout_3.addWidget(self.homeBtn)

        self.HOR1Btn_2 = QPushButton(self.frame_2)
        self.HOR1Btn_2.setObjectName(u"HOR1Btn_2")
        icon2 = QIcon()
        icon2.addFile(u":/icons/icons/calendar.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.HOR1Btn_2.setIcon(icon2)
        self.HOR1Btn_2.setIconSize(QSize(24, 24))

        self.verticalLayout_3.addWidget(self.HOR1Btn_2)

        self.HOR2Btn_2 = QPushButton(self.frame_2)
        self.HOR2Btn_2.setObjectName(u"HOR2Btn_2")
        self.HOR2Btn_2.setIcon(icon2)
        self.HOR2Btn_2.setIconSize(QSize(24, 24))

        self.verticalLayout_3.addWidget(self.HOR2Btn_2)


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

        self.settingsBtn = QPushButton(self.frame_3)
        self.settingsBtn.setObjectName(u"settingsBtn")
        icon3 = QIcon()
        icon3.addFile(u":/icons/icons/archive.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.settingsBtn.setIcon(icon3)
        self.settingsBtn.setIconSize(QSize(24, 24))

        self.verticalLayout_4.addWidget(self.settingsBtn)

        self.infoBtn = QPushButton(self.frame_3)
        self.infoBtn.setObjectName(u"infoBtn")
        icon4 = QIcon()
        icon4.addFile(u":/icons/icons/database.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.infoBtn.setIcon(icon4)
        self.infoBtn.setIconSize(QSize(24, 24))

        self.verticalLayout_4.addWidget(self.infoBtn)

        self.helpBtn = QPushButton(self.frame_3)
        self.helpBtn.setObjectName(u"helpBtn")
        icon5 = QIcon()
        icon5.addFile(u":/icons/icons/help-circle.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.helpBtn.setIcon(icon5)
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
        font1 = QFont()
        font1.setBold(True)
        font1.setWeight(75)
        self.label.setFont(font1)
        self.label.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_3.addWidget(self.label)

        self.closeCenterMenuBtn = QPushButton(self.frame_4)
        self.closeCenterMenuBtn.setObjectName(u"closeCenterMenuBtn")
        self.closeCenterMenuBtn.setEnabled(True)
        icon6 = QIcon()
        icon6.addFile(u":/icons/icons/x-circle.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.closeCenterMenuBtn.setIcon(icon6)
        self.closeCenterMenuBtn.setIconSize(QSize(24, 24))

        self.horizontalLayout_3.addWidget(self.closeCenterMenuBtn, 0, Qt.AlignRight)


        self.verticalLayout_6.addWidget(self.frame_4, 0, Qt.AlignTop)

        self.centerMenuPages = QCustomStackedWidget(self.centerMenuSubContainer)
        self.centerMenuPages.setObjectName(u"centerMenuPages")
        self.centerMenuPages.setMinimumSize(QSize(200, 0))
        self.page = QWidget()
        self.page.setObjectName(u"page")
        self.verticalLayout_7 = QVBoxLayout(self.page)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.label_2 = QLabel(self.page)
        self.label_2.setObjectName(u"label_2")
        font2 = QFont()
        font2.setPointSize(13)
        self.label_2.setFont(font2)
        self.label_2.setAlignment(Qt.AlignCenter)

        self.verticalLayout_7.addWidget(self.label_2)

        self.centerMenuPages.addWidget(self.page)
        self.page_3 = QWidget()
        self.page_3.setObjectName(u"page_3")
        self.verticalLayout_9 = QVBoxLayout(self.page_3)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.label_4 = QLabel(self.page_3)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setFont(font2)
        self.label_4.setAlignment(Qt.AlignCenter)

        self.verticalLayout_9.addWidget(self.label_4)

        self.centerMenuPages.addWidget(self.page_3)
        self.page_2 = QWidget()
        self.page_2.setObjectName(u"page_2")
        self.verticalLayout_8 = QVBoxLayout(self.page_2)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.label_3 = QLabel(self.page_2)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setFont(font2)
        self.label_3.setAlignment(Qt.AlignCenter)

        self.verticalLayout_8.addWidget(self.label_3)

        self.centerMenuPages.addWidget(self.page_2)

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
        icon7 = QIcon()
        icon7.addFile(u":/icons/icons/bell.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.notificationBtn.setIcon(icon7)
        self.notificationBtn.setIconSize(QSize(24, 24))

        self.horizontalLayout_6.addWidget(self.notificationBtn)

        self.profileMenuBtn = QPushButton(self.frame_6)
        self.profileMenuBtn.setObjectName(u"profileMenuBtn")
        icon8 = QIcon()
        icon8.addFile(u":/icons/icons/user.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.profileMenuBtn.setIcon(icon8)
        self.profileMenuBtn.setIconSize(QSize(24, 24))

        self.horizontalLayout_6.addWidget(self.profileMenuBtn)

        self.moreMenuBtn = QPushButton(self.frame_6)
        self.moreMenuBtn.setObjectName(u"moreMenuBtn")
        icon9 = QIcon()
        icon9.addFile(u":/icons/icons/more-horizontal.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.moreMenuBtn.setIcon(icon9)
        self.moreMenuBtn.setIconSize(QSize(24, 24))

        self.horizontalLayout_6.addWidget(self.moreMenuBtn)


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
        icon10 = QIcon()
        icon10.addFile(u":/icons/icons/minus.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.minimizeBtn.setIcon(icon10)

        self.horizontalLayout_4.addWidget(self.minimizeBtn)

        self.restoreBtn = QPushButton(self.frame_7)
        self.restoreBtn.setObjectName(u"restoreBtn")
        icon11 = QIcon()
        icon11.addFile(u":/icons/icons/square.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.restoreBtn.setIcon(icon11)

        self.horizontalLayout_4.addWidget(self.restoreBtn)

        self.closeBtn = QPushButton(self.frame_7)
        self.closeBtn.setObjectName(u"closeBtn")
        icon12 = QIcon()
        icon12.addFile(u":/icons/icons/x.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.closeBtn.setIcon(icon12)

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
        self.horizontalLayout_12 = QHBoxLayout(self.frame_10)
        self.horizontalLayout_12.setObjectName(u"horizontalLayout_12")
        self.HOR1Btn = QPushButton(self.frame_10)
        self.HOR1Btn.setObjectName(u"HOR1Btn")
        self.HOR1Btn.setFont(font)
        self.HOR1Btn.setIconSize(QSize(24, 24))

        self.horizontalLayout_12.addWidget(self.HOR1Btn)


        self.horizontalLayout_10.addWidget(self.frame_10)

        self.frame_9 = QFrame(self.frame_15)
        self.frame_9.setObjectName(u"frame_9")
        self.frame_9.setFrameShape(QFrame.StyledPanel)
        self.frame_9.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_11 = QHBoxLayout(self.frame_9)
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.HOR2Btn = QPushButton(self.frame_9)
        self.HOR2Btn.setObjectName(u"HOR2Btn")
        self.HOR2Btn.setFont(font)
        self.HOR2Btn.setIconSize(QSize(24, 24))

        self.horizontalLayout_11.addWidget(self.HOR2Btn)


        self.horizontalLayout_10.addWidget(self.frame_9)


        self.verticalLayout_25.addWidget(self.frame_15)

        self.notificaciones = QFrame(self.menuPrincipal)
        self.notificaciones.setObjectName(u"notificaciones")
        self.notificaciones.setFrameShape(QFrame.StyledPanel)
        self.notificaciones.setFrameShadow(QFrame.Raised)
        self.verticalLayout_24 = QVBoxLayout(self.notificaciones)
        self.verticalLayout_24.setObjectName(u"verticalLayout_24")
        self.label_9 = QLabel(self.notificaciones)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setFont(font)

        self.verticalLayout_24.addWidget(self.label_9, 0, Qt.AlignLeft|Qt.AlignTop)


        self.verticalLayout_25.addWidget(self.notificaciones)

        self.mainPages.addWidget(self.menuPrincipal)
        self.planchasHor2_3 = QWidget()
        self.planchasHor2_3.setObjectName(u"planchasHor2_3")
        self.verticalLayout_17 = QVBoxLayout(self.planchasHor2_3)
        self.verticalLayout_17.setObjectName(u"verticalLayout_17")
        self.frame_17 = QFrame(self.planchasHor2_3)
        self.frame_17.setObjectName(u"frame_17")
        self.frame_17.setFrameShape(QFrame.StyledPanel)
        self.frame_17.setFrameShadow(QFrame.Raised)
        self.pushButton_51 = QPushButton(self.frame_17)
        self.pushButton_51.setObjectName(u"pushButton_51")
        self.pushButton_51.setGeometry(QRect(10, 30, 75, 23))
        self.pushButton_52 = QPushButton(self.frame_17)
        self.pushButton_52.setObjectName(u"pushButton_52")
        self.pushButton_52.setGeometry(QRect(10, 60, 75, 23))
        self.pushButton_53 = QPushButton(self.frame_17)
        self.pushButton_53.setObjectName(u"pushButton_53")
        self.pushButton_53.setGeometry(QRect(10, 10, 75, 23))

        self.verticalLayout_17.addWidget(self.frame_17)

        self.frame_16 = QFrame(self.planchasHor2_3)
        self.frame_16.setObjectName(u"frame_16")
        self.frame_16.setFrameShape(QFrame.StyledPanel)
        self.frame_16.setFrameShadow(QFrame.Raised)

        self.verticalLayout_17.addWidget(self.frame_16)

        self.mainPages.addWidget(self.planchasHor2_3)
        self.page_8 = QWidget()
        self.page_8.setObjectName(u"page_8")
        self.verticalLayout_18 = QVBoxLayout(self.page_8)
        self.verticalLayout_18.setObjectName(u"verticalLayout_18")
        self.reportes = QLabel(self.page_8)
        self.reportes.setObjectName(u"reportes")
        self.reportes.setFont(font2)
        self.reportes.setAlignment(Qt.AlignCenter)

        self.verticalLayout_18.addWidget(self.reportes)

        self.mainPages.addWidget(self.page_8)
        self.planchasHor1 = QWidget()
        self.planchasHor1.setObjectName(u"planchasHor1")
        self.verticalLayout_16 = QVBoxLayout(self.planchasHor1)
        self.verticalLayout_16.setObjectName(u"verticalLayout_16")
        self.frame_12 = QFrame(self.planchasHor1)
        self.frame_12.setObjectName(u"frame_12")
        self.frame_12.setFrameShape(QFrame.StyledPanel)
        self.frame_12.setFrameShadow(QFrame.Raised)
        self.gridLayout_9 = QGridLayout(self.frame_12)
        self.gridLayout_9.setObjectName(u"gridLayout_9")
        self.gridLayout_9.setContentsMargins(-1, -1, -1, 0)
        self.plancha5_1Btn = QPushButton(self.frame_12)
        self.plancha5_1Btn.setObjectName(u"plancha5_1Btn")
        self.plancha5_1Btn.setFont(font)

        self.gridLayout_9.addWidget(self.plancha5_1Btn, 5, 0, 1, 1)

        self.plancha12_1Btn = QPushButton(self.frame_12)
        self.plancha12_1Btn.setObjectName(u"plancha12_1Btn")
        self.plancha12_1Btn.setFont(font)

        self.gridLayout_9.addWidget(self.plancha12_1Btn, 6, 1, 1, 1)

        self.plancha2_1Btn = QPushButton(self.frame_12)
        self.plancha2_1Btn.setObjectName(u"plancha2_1Btn")
        self.plancha2_1Btn.setFont(font)

        self.gridLayout_9.addWidget(self.plancha2_1Btn, 2, 0, 1, 1)

        self.plancha4_1Btn = QPushButton(self.frame_12)
        self.plancha4_1Btn.setObjectName(u"plancha4_1Btn")
        self.plancha4_1Btn.setFont(font)

        self.gridLayout_9.addWidget(self.plancha4_1Btn, 4, 0, 1, 1)

        self.plancha10_1Btn = QPushButton(self.frame_12)
        self.plancha10_1Btn.setObjectName(u"plancha10_1Btn")
        self.plancha10_1Btn.setFont(font)

        self.gridLayout_9.addWidget(self.plancha10_1Btn, 4, 1, 1, 1)

        self.plancha1_1Btn = QPushButton(self.frame_12)
        self.plancha1_1Btn.setObjectName(u"plancha1_1Btn")
        self.plancha1_1Btn.setFont(font)

        self.gridLayout_9.addWidget(self.plancha1_1Btn, 1, 0, 1, 1)

        self.plancha7_1Btn = QPushButton(self.frame_12)
        self.plancha7_1Btn.setObjectName(u"plancha7_1Btn")
        self.plancha7_1Btn.setFont(font)

        self.gridLayout_9.addWidget(self.plancha7_1Btn, 1, 1, 1, 1)

        self.plancha9_1Btn = QPushButton(self.frame_12)
        self.plancha9_1Btn.setObjectName(u"plancha9_1Btn")
        self.plancha9_1Btn.setFont(font)

        self.gridLayout_9.addWidget(self.plancha9_1Btn, 3, 1, 1, 1)

        self.plancha11_1Btn = QPushButton(self.frame_12)
        self.plancha11_1Btn.setObjectName(u"plancha11_1Btn")
        self.plancha11_1Btn.setFont(font)

        self.gridLayout_9.addWidget(self.plancha11_1Btn, 5, 1, 1, 1)

        self.plancha8_1Btn = QPushButton(self.frame_12)
        self.plancha8_1Btn.setObjectName(u"plancha8_1Btn")
        self.plancha8_1Btn.setFont(font)

        self.gridLayout_9.addWidget(self.plancha8_1Btn, 2, 1, 1, 1)

        self.plancha3_1Btn = QPushButton(self.frame_12)
        self.plancha3_1Btn.setObjectName(u"plancha3_1Btn")
        self.plancha3_1Btn.setFont(font)

        self.gridLayout_9.addWidget(self.plancha3_1Btn, 3, 0, 1, 1)

        self.plancha6_1Btn = QPushButton(self.frame_12)
        self.plancha6_1Btn.setObjectName(u"plancha6_1Btn")
        self.plancha6_1Btn.setFont(font)

        self.gridLayout_9.addWidget(self.plancha6_1Btn, 6, 0, 1, 1)

        self.label_22 = QLabel(self.frame_12)
        self.label_22.setObjectName(u"label_22")
        font3 = QFont()
        font3.setPointSize(10)
        font3.setBold(True)
        font3.setUnderline(True)
        font3.setWeight(75)
        self.label_22.setFont(font3)

        self.gridLayout_9.addWidget(self.label_22, 0, 0, 1, 1, Qt.AlignTop)


        self.verticalLayout_16.addWidget(self.frame_12)

        self.frame_11 = QFrame(self.planchasHor1)
        self.frame_11.setObjectName(u"frame_11")
        self.frame_11.setFrameShape(QFrame.StyledPanel)
        self.frame_11.setFrameShadow(QFrame.Raised)
        self.verticalLayout_22 = QVBoxLayout(self.frame_11)
        self.verticalLayout_22.setSpacing(9)
        self.verticalLayout_22.setObjectName(u"verticalLayout_22")
        self.verticalLayout_22.setContentsMargins(0, 0, 0, 0)
        self.iniciarMad_1Btn = QPushButton(self.frame_11)
        self.iniciarMad_1Btn.setObjectName(u"iniciarMad_1Btn")
        self.iniciarMad_1Btn.setMaximumSize(QSize(16777215, 16777215))
        self.iniciarMad_1Btn.setFont(font)
        icon13 = QIcon()
        icon13.addFile(u":/icons/icons/chevron-right.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.iniciarMad_1Btn.setIcon(icon13)
        self.iniciarMad_1Btn.setIconSize(QSize(30, 30))

        self.verticalLayout_22.addWidget(self.iniciarMad_1Btn, 0, Qt.AlignRight|Qt.AlignBottom)


        self.verticalLayout_16.addWidget(self.frame_11, 0, Qt.AlignRight|Qt.AlignBottom)

        self.mainPages.addWidget(self.planchasHor1)
        self.plancha1_1 = QWidget()
        self.plancha1_1.setObjectName(u"plancha1_1")
        self.verticalLayout_23 = QVBoxLayout(self.plancha1_1)
        self.verticalLayout_23.setObjectName(u"verticalLayout_23")
        self.frame_18 = QFrame(self.plancha1_1)
        self.frame_18.setObjectName(u"frame_18")
        self.frame_18.setFrameShape(QFrame.StyledPanel)
        self.frame_18.setFrameShadow(QFrame.Raised)
        self.gridLayout_3 = QGridLayout(self.frame_18)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.label_8 = QLabel(self.frame_18)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setFont(font)

        self.gridLayout_3.addWidget(self.label_8, 1, 0, 1, 1, Qt.AlignLeft|Qt.AlignVCenter)

        self.label_10 = QLabel(self.frame_18)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setFont(font1)

        self.gridLayout_3.addWidget(self.label_10, 1, 2, 1, 1, Qt.AlignLeft)

        self.label_11 = QLabel(self.frame_18)
        self.label_11.setObjectName(u"label_11")
        self.label_11.setFont(font1)

        self.gridLayout_3.addWidget(self.label_11, 2, 2, 1, 1, Qt.AlignLeft)

        self.label_21 = QLabel(self.frame_18)
        self.label_21.setObjectName(u"label_21")
        font4 = QFont()
        font4.setPointSize(12)
        font4.setBold(True)
        font4.setUnderline(True)
        font4.setWeight(75)
        self.label_21.setFont(font4)

        self.gridLayout_3.addWidget(self.label_21, 0, 0, 1, 1)


        self.verticalLayout_23.addWidget(self.frame_18, 0, Qt.AlignTop)

        self.frame_13 = QFrame(self.plancha1_1)
        self.frame_13.setObjectName(u"frame_13")
        self.frame_13.setEnabled(True)
        self.frame_13.setFrameShape(QFrame.StyledPanel)
        self.frame_13.setFrameShadow(QFrame.Raised)
        self.gridLayout = QGridLayout(self.frame_13)
        self.gridLayout.setObjectName(u"gridLayout")
        self.pushButton_9 = QPushButton(self.frame_13)
        self.pushButton_9.setObjectName(u"pushButton_9")
        icon14 = QIcon()
        icon14.addFile(u":/icons/icons/activity.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_9.setIcon(icon14)
        self.pushButton_9.setIconSize(QSize(24, 24))

        self.gridLayout.addWidget(self.pushButton_9, 0, 0, 1, 1, Qt.AlignVCenter)

        self.pushButton_2 = QPushButton(self.frame_13)
        self.pushButton_2.setObjectName(u"pushButton_2")
        self.pushButton_2.setIcon(icon14)
        self.pushButton_2.setIconSize(QSize(24, 24))

        self.gridLayout.addWidget(self.pushButton_2, 3, 1, 1, 1, Qt.AlignVCenter)

        self.pushButton_4 = QPushButton(self.frame_13)
        self.pushButton_4.setObjectName(u"pushButton_4")
        self.pushButton_4.setIcon(icon14)

        self.gridLayout.addWidget(self.pushButton_4, 4, 1, 1, 1, Qt.AlignVCenter)

        self.pushButton = QPushButton(self.frame_13)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setIcon(icon14)
        self.pushButton.setIconSize(QSize(24, 24))

        self.gridLayout.addWidget(self.pushButton, 2, 1, 1, 1, Qt.AlignVCenter)

        self.pushButton_8 = QPushButton(self.frame_13)
        self.pushButton_8.setObjectName(u"pushButton_8")
        self.pushButton_8.setIcon(icon14)
        self.pushButton_8.setIconSize(QSize(24, 24))

        self.gridLayout.addWidget(self.pushButton_8, 1, 0, 1, 1, Qt.AlignVCenter)

        self.pushButton_3 = QPushButton(self.frame_13)
        self.pushButton_3.setObjectName(u"pushButton_3")
        self.pushButton_3.setIcon(icon14)
        self.pushButton_3.setIconSize(QSize(24, 24))

        self.gridLayout.addWidget(self.pushButton_3, 1, 1, 1, 1, Qt.AlignVCenter)

        self.pushButton_5 = QPushButton(self.frame_13)
        self.pushButton_5.setObjectName(u"pushButton_5")
        self.pushButton_5.setIcon(icon14)
        self.pushButton_5.setIconSize(QSize(24, 24))

        self.gridLayout.addWidget(self.pushButton_5, 0, 1, 1, 1, Qt.AlignVCenter)

        self.pushButton_6 = QPushButton(self.frame_13)
        self.pushButton_6.setObjectName(u"pushButton_6")
        self.pushButton_6.setIcon(icon14)
        self.pushButton_6.setIconSize(QSize(24, 24))

        self.gridLayout.addWidget(self.pushButton_6, 4, 0, 1, 1, Qt.AlignVCenter)

        self.pushButton_10 = QPushButton(self.frame_13)
        self.pushButton_10.setObjectName(u"pushButton_10")
        self.pushButton_10.setIcon(icon14)
        self.pushButton_10.setIconSize(QSize(24, 24))

        self.gridLayout.addWidget(self.pushButton_10, 2, 0, 1, 1, Qt.AlignVCenter)

        self.pushButton_7 = QPushButton(self.frame_13)
        self.pushButton_7.setObjectName(u"pushButton_7")
        self.pushButton_7.setIcon(icon14)
        self.pushButton_7.setIconSize(QSize(24, 24))

        self.gridLayout.addWidget(self.pushButton_7, 3, 0, 1, 1, Qt.AlignVCenter)


        self.verticalLayout_23.addWidget(self.frame_13)

        self.mainPages.addWidget(self.plancha1_1)
        self.plancha2_1 = QWidget()
        self.plancha2_1.setObjectName(u"plancha2_1")
        self.verticalLayout_32 = QVBoxLayout(self.plancha2_1)
        self.verticalLayout_32.setObjectName(u"verticalLayout_32")
        self.frame_30 = QFrame(self.plancha2_1)
        self.frame_30.setObjectName(u"frame_30")
        self.frame_30.setFrameShape(QFrame.StyledPanel)
        self.frame_30.setFrameShadow(QFrame.Raised)
        self.gridLayout_8 = QGridLayout(self.frame_30)
        self.gridLayout_8.setObjectName(u"gridLayout_8")
        self.label_18 = QLabel(self.frame_30)
        self.label_18.setObjectName(u"label_18")
        self.label_18.setFont(font1)

        self.gridLayout_8.addWidget(self.label_18, 1, 1, 1, 1)

        self.label_17 = QLabel(self.frame_30)
        self.label_17.setObjectName(u"label_17")
        self.label_17.setFont(font)

        self.gridLayout_8.addWidget(self.label_17, 1, 0, 1, 1)

        self.label_19 = QLabel(self.frame_30)
        self.label_19.setObjectName(u"label_19")
        self.label_19.setFont(font1)

        self.gridLayout_8.addWidget(self.label_19, 2, 1, 1, 1)

        self.label_20 = QLabel(self.frame_30)
        self.label_20.setObjectName(u"label_20")
        self.label_20.setFont(font4)

        self.gridLayout_8.addWidget(self.label_20, 0, 0, 1, 1)


        self.verticalLayout_32.addWidget(self.frame_30)

        self.frame_29 = QFrame(self.plancha2_1)
        self.frame_29.setObjectName(u"frame_29")
        self.frame_29.setEnabled(True)
        self.frame_29.setFrameShape(QFrame.StyledPanel)
        self.frame_29.setFrameShadow(QFrame.Raised)
        self.gridLayout_7 = QGridLayout(self.frame_29)
        self.gridLayout_7.setObjectName(u"gridLayout_7")
        self.pushButton_41 = QPushButton(self.frame_29)
        self.pushButton_41.setObjectName(u"pushButton_41")
        self.pushButton_41.setIcon(icon14)
        self.pushButton_41.setIconSize(QSize(24, 24))

        self.gridLayout_7.addWidget(self.pushButton_41, 0, 0, 1, 1, Qt.AlignVCenter)

        self.pushButton_48 = QPushButton(self.frame_29)
        self.pushButton_48.setObjectName(u"pushButton_48")
        self.pushButton_48.setIcon(icon14)
        self.pushButton_48.setIconSize(QSize(24, 24))

        self.gridLayout_7.addWidget(self.pushButton_48, 4, 0, 1, 1, Qt.AlignVCenter)

        self.pushButton_50 = QPushButton(self.frame_29)
        self.pushButton_50.setObjectName(u"pushButton_50")
        self.pushButton_50.setIcon(icon14)
        self.pushButton_50.setIconSize(QSize(24, 24))

        self.gridLayout_7.addWidget(self.pushButton_50, 3, 0, 1, 1, Qt.AlignVCenter)

        self.pushButton_43 = QPushButton(self.frame_29)
        self.pushButton_43.setObjectName(u"pushButton_43")
        self.pushButton_43.setIcon(icon14)

        self.gridLayout_7.addWidget(self.pushButton_43, 4, 1, 1, 1, Qt.AlignVCenter)

        self.pushButton_46 = QPushButton(self.frame_29)
        self.pushButton_46.setObjectName(u"pushButton_46")
        self.pushButton_46.setIcon(icon14)
        self.pushButton_46.setIconSize(QSize(24, 24))

        self.gridLayout_7.addWidget(self.pushButton_46, 1, 1, 1, 1, Qt.AlignVCenter)

        self.pushButton_44 = QPushButton(self.frame_29)
        self.pushButton_44.setObjectName(u"pushButton_44")
        self.pushButton_44.setIcon(icon14)
        self.pushButton_44.setIconSize(QSize(24, 24))

        self.gridLayout_7.addWidget(self.pushButton_44, 2, 1, 1, 1, Qt.AlignVCenter)

        self.pushButton_49 = QPushButton(self.frame_29)
        self.pushButton_49.setObjectName(u"pushButton_49")
        self.pushButton_49.setIcon(icon14)
        self.pushButton_49.setIconSize(QSize(24, 24))

        self.gridLayout_7.addWidget(self.pushButton_49, 2, 0, 1, 1, Qt.AlignVCenter)

        self.pushButton_42 = QPushButton(self.frame_29)
        self.pushButton_42.setObjectName(u"pushButton_42")
        self.pushButton_42.setIcon(icon14)
        self.pushButton_42.setIconSize(QSize(24, 24))

        self.gridLayout_7.addWidget(self.pushButton_42, 3, 1, 1, 1, Qt.AlignVCenter)

        self.pushButton_45 = QPushButton(self.frame_29)
        self.pushButton_45.setObjectName(u"pushButton_45")
        self.pushButton_45.setIcon(icon14)
        self.pushButton_45.setIconSize(QSize(24, 24))

        self.gridLayout_7.addWidget(self.pushButton_45, 1, 0, 1, 1, Qt.AlignVCenter)

        self.pushButton_47 = QPushButton(self.frame_29)
        self.pushButton_47.setObjectName(u"pushButton_47")
        self.pushButton_47.setIcon(icon14)
        self.pushButton_47.setIconSize(QSize(24, 24))

        self.gridLayout_7.addWidget(self.pushButton_47, 0, 1, 1, 1, Qt.AlignVCenter)


        self.verticalLayout_32.addWidget(self.frame_29)

        self.mainPages.addWidget(self.plancha2_1)
        self.planchasHor2 = QWidget()
        self.planchasHor2.setObjectName(u"planchasHor2")
        self.verticalLayout_33 = QVBoxLayout(self.planchasHor2)
        self.verticalLayout_33.setObjectName(u"verticalLayout_33")
        self.frame_32 = QFrame(self.planchasHor2)
        self.frame_32.setObjectName(u"frame_32")
        self.frame_32.setFrameShape(QFrame.StyledPanel)
        self.frame_32.setFrameShadow(QFrame.Raised)
        self.gridLayout_2 = QGridLayout(self.frame_32)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.pushButton_13 = QPushButton(self.frame_32)
        self.pushButton_13.setObjectName(u"pushButton_13")
        self.pushButton_13.setFont(font)

        self.gridLayout_2.addWidget(self.pushButton_13, 1, 0, 1, 1)

        self.pushButton_11 = QPushButton(self.frame_32)
        self.pushButton_11.setObjectName(u"pushButton_11")
        self.pushButton_11.setFont(font)

        self.gridLayout_2.addWidget(self.pushButton_11, 3, 1, 1, 1)

        self.pushButton_12 = QPushButton(self.frame_32)
        self.pushButton_12.setObjectName(u"pushButton_12")
        self.pushButton_12.setFont(font)

        self.gridLayout_2.addWidget(self.pushButton_12, 5, 1, 1, 1)

        self.pushButton_17 = QPushButton(self.frame_32)
        self.pushButton_17.setObjectName(u"pushButton_17")
        self.pushButton_17.setFont(font)

        self.gridLayout_2.addWidget(self.pushButton_17, 4, 0, 1, 1)

        self.pushButton_18 = QPushButton(self.frame_32)
        self.pushButton_18.setObjectName(u"pushButton_18")
        self.pushButton_18.setFont(font)

        self.gridLayout_2.addWidget(self.pushButton_18, 2, 0, 1, 1)

        self.pushButton_16 = QPushButton(self.frame_32)
        self.pushButton_16.setObjectName(u"pushButton_16")
        self.pushButton_16.setFont(font)

        self.gridLayout_2.addWidget(self.pushButton_16, 2, 1, 1, 1)

        self.pushButton_15 = QPushButton(self.frame_32)
        self.pushButton_15.setObjectName(u"pushButton_15")
        self.pushButton_15.setFont(font)

        self.gridLayout_2.addWidget(self.pushButton_15, 3, 0, 1, 1)

        self.pushButton_19 = QPushButton(self.frame_32)
        self.pushButton_19.setObjectName(u"pushButton_19")
        self.pushButton_19.setFont(font)

        self.gridLayout_2.addWidget(self.pushButton_19, 4, 1, 1, 1)

        self.pushButton_20 = QPushButton(self.frame_32)
        self.pushButton_20.setObjectName(u"pushButton_20")
        self.pushButton_20.setFont(font)

        self.gridLayout_2.addWidget(self.pushButton_20, 5, 0, 1, 1)

        self.label_23 = QLabel(self.frame_32)
        self.label_23.setObjectName(u"label_23")
        self.label_23.setFont(font3)

        self.gridLayout_2.addWidget(self.label_23, 0, 0, 1, 1)

        self.pushButton_14 = QPushButton(self.frame_32)
        self.pushButton_14.setObjectName(u"pushButton_14")
        self.pushButton_14.setFont(font)

        self.gridLayout_2.addWidget(self.pushButton_14, 6, 0, 1, 1)

        self.pushButton_54 = QPushButton(self.frame_32)
        self.pushButton_54.setObjectName(u"pushButton_54")
        self.pushButton_54.setFont(font)

        self.gridLayout_2.addWidget(self.pushButton_54, 1, 1, 1, 1)

        self.pushButton_55 = QPushButton(self.frame_32)
        self.pushButton_55.setObjectName(u"pushButton_55")
        self.pushButton_55.setFont(font)

        self.gridLayout_2.addWidget(self.pushButton_55, 6, 1, 1, 1)


        self.verticalLayout_33.addWidget(self.frame_32)

        self.frame_31 = QFrame(self.planchasHor2)
        self.frame_31.setObjectName(u"frame_31")
        self.frame_31.setFrameShape(QFrame.StyledPanel)
        self.frame_31.setFrameShadow(QFrame.Raised)
        self.verticalLayout_34 = QVBoxLayout(self.frame_31)
        self.verticalLayout_34.setSpacing(0)
        self.verticalLayout_34.setObjectName(u"verticalLayout_34")
        self.verticalLayout_34.setContentsMargins(0, 0, 0, 0)
        self.iniciarMad_2Btn = QPushButton(self.frame_31)
        self.iniciarMad_2Btn.setObjectName(u"iniciarMad_2Btn")
        self.iniciarMad_2Btn.setMaximumSize(QSize(16777215, 16777215))
        self.iniciarMad_2Btn.setFont(font)
        self.iniciarMad_2Btn.setIcon(icon13)
        self.iniciarMad_2Btn.setIconSize(QSize(30, 30))

        self.verticalLayout_34.addWidget(self.iniciarMad_2Btn)


        self.verticalLayout_33.addWidget(self.frame_31, 0, Qt.AlignRight|Qt.AlignBottom)

        self.mainPages.addWidget(self.planchasHor2)

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
        self.frame_5 = QFrame(self.rightMenuSubContainer)
        self.frame_5.setObjectName(u"frame_5")
        self.frame_5.setFrameShape(QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_8 = QHBoxLayout(self.frame_5)
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.label_5 = QLabel(self.frame_5)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_8.addWidget(self.label_5)

        self.closeRightMenuBtn = QPushButton(self.frame_5)
        self.closeRightMenuBtn.setObjectName(u"closeRightMenuBtn")
        self.closeRightMenuBtn.setIcon(icon6)
        self.closeRightMenuBtn.setIconSize(QSize(24, 24))

        self.horizontalLayout_8.addWidget(self.closeRightMenuBtn, 0, Qt.AlignRight)


        self.verticalLayout_12.addWidget(self.frame_5)

        self.rightMenuPages = QCustomStackedWidget(self.rightMenuSubContainer)
        self.rightMenuPages.setObjectName(u"rightMenuPages")
        self.page_4 = QWidget()
        self.page_4.setObjectName(u"page_4")
        self.verticalLayout_13 = QVBoxLayout(self.page_4)
        self.verticalLayout_13.setObjectName(u"verticalLayout_13")
        self.label_6 = QLabel(self.page_4)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setFont(font2)
        self.label_6.setAlignment(Qt.AlignCenter)

        self.verticalLayout_13.addWidget(self.label_6)

        self.rightMenuPages.addWidget(self.page_4)
        self.page_5 = QWidget()
        self.page_5.setObjectName(u"page_5")
        self.verticalLayout_14 = QVBoxLayout(self.page_5)
        self.verticalLayout_14.setObjectName(u"verticalLayout_14")
        self.label_7 = QLabel(self.page_5)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setFont(font2)
        self.label_7.setAlignment(Qt.AlignCenter)

        self.verticalLayout_14.addWidget(self.label_7)

        self.rightMenuPages.addWidget(self.page_5)

        self.verticalLayout_12.addWidget(self.rightMenuPages)


        self.verticalLayout_11.addWidget(self.rightMenuSubContainer)


        self.horizontalLayout_7.addWidget(self.rightMenuContainer, 0, Qt.AlignRight)


        self.verticalLayout_10.addWidget(self.mainBodyContent)

        self.popupNotificationContainer = QCustomSlideMenu(self.mainBodyContainer)
        self.popupNotificationContainer.setObjectName(u"popupNotificationContainer")
        self.verticalLayout_19 = QVBoxLayout(self.popupNotificationContainer)
        self.verticalLayout_19.setObjectName(u"verticalLayout_19")
        self.popupNotificationSubContainer = QWidget(self.popupNotificationContainer)
        self.popupNotificationSubContainer.setObjectName(u"popupNotificationSubContainer")
        self.verticalLayout_20 = QVBoxLayout(self.popupNotificationSubContainer)
        self.verticalLayout_20.setObjectName(u"verticalLayout_20")
        self.label_12 = QLabel(self.popupNotificationSubContainer)
        self.label_12.setObjectName(u"label_12")
        self.label_12.setFont(font)

        self.verticalLayout_20.addWidget(self.label_12, 0, Qt.AlignLeft)

        self.frame_8 = QFrame(self.popupNotificationSubContainer)
        self.frame_8.setObjectName(u"frame_8")
        self.frame_8.setFrameShape(QFrame.StyledPanel)
        self.frame_8.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_9 = QHBoxLayout(self.frame_8)
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.closeNotificationBtn = QPushButton(self.frame_8)
        self.closeNotificationBtn.setObjectName(u"closeNotificationBtn")
        icon15 = QIcon()
        icon15.addFile(u":/icons/icons/x-octagon.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.closeNotificationBtn.setIcon(icon15)
        self.closeNotificationBtn.setIconSize(QSize(24, 24))

        self.horizontalLayout_9.addWidget(self.closeNotificationBtn, 0, Qt.AlignRight|Qt.AlignBottom)


        self.verticalLayout_20.addWidget(self.frame_8)


        self.verticalLayout_19.addWidget(self.popupNotificationSubContainer)


        self.verticalLayout_10.addWidget(self.popupNotificationContainer)


        self.horizontalLayout.addWidget(self.mainBodyContainer)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        self.centerMenuPages.setCurrentIndex(2)
        self.mainPages.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
#if QT_CONFIG(tooltip)
        self.menuBtn.setToolTip(QCoreApplication.translate("MainWindow", u"Menu", None))
#endif // QT_CONFIG(tooltip)
        self.menuBtn.setText("")
#if QT_CONFIG(tooltip)
        self.homeBtn.setToolTip(QCoreApplication.translate("MainWindow", u"Maduraci\u00f3n", None))
#endif // QT_CONFIG(tooltip)
        self.homeBtn.setText(QCoreApplication.translate("MainWindow", u"Men\u00fa", None))
#if QT_CONFIG(tooltip)
        self.HOR1Btn_2.setToolTip(QCoreApplication.translate("MainWindow", u"Datos", None))
#endif // QT_CONFIG(tooltip)
        self.HOR1Btn_2.setText(QCoreApplication.translate("MainWindow", u"HOR1", None))
#if QT_CONFIG(tooltip)
        self.HOR2Btn_2.setToolTip(QCoreApplication.translate("MainWindow", u"Reportes", None))
#endif // QT_CONFIG(tooltip)
        self.HOR2Btn_2.setText(QCoreApplication.translate("MainWindow", u"HOR2", None))
#if QT_CONFIG(tooltip)
        self.settingsBtn.setToolTip(QCoreApplication.translate("MainWindow", u"Ajustes", None))
#endif // QT_CONFIG(tooltip)
        self.settingsBtn.setText(QCoreApplication.translate("MainWindow", u"Logs", None))
#if QT_CONFIG(tooltip)
        self.infoBtn.setToolTip(QCoreApplication.translate("MainWindow", u"Informaci\u00f3n", None))
#endif // QT_CONFIG(tooltip)
        self.infoBtn.setText(QCoreApplication.translate("MainWindow", u"Base de datos", None))
#if QT_CONFIG(tooltip)
        self.helpBtn.setToolTip(QCoreApplication.translate("MainWindow", u"Ayuda", None))
#endif // QT_CONFIG(tooltip)
        self.helpBtn.setText(QCoreApplication.translate("MainWindow", u"Ayuda", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"More Menu", None))
#if QT_CONFIG(tooltip)
        self.closeCenterMenuBtn.setToolTip(QCoreApplication.translate("MainWindow", u"Cerrar", None))
#endif // QT_CONFIG(tooltip)
        self.closeCenterMenuBtn.setText("")
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Ajutes", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"Help", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"Information", None))
#if QT_CONFIG(tooltip)
        self.notificationBtn.setToolTip(QCoreApplication.translate("MainWindow", u"Notificaciones", None))
#endif // QT_CONFIG(tooltip)
        self.notificationBtn.setText("")
#if QT_CONFIG(tooltip)
        self.profileMenuBtn.setToolTip(QCoreApplication.translate("MainWindow", u"Perfil", None))
#endif // QT_CONFIG(tooltip)
        self.profileMenuBtn.setText("")
#if QT_CONFIG(tooltip)
        self.moreMenuBtn.setToolTip(QCoreApplication.translate("MainWindow", u"More", None))
#endif // QT_CONFIG(tooltip)
        self.moreMenuBtn.setText("")
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
        self.pushButton_51.setText(QCoreApplication.translate("MainWindow", u"PushButton", None))
        self.pushButton_52.setText(QCoreApplication.translate("MainWindow", u"PushButton", None))
        self.pushButton_53.setText(QCoreApplication.translate("MainWindow", u"PushButton", None))
        self.reportes.setText(QCoreApplication.translate("MainWindow", u"Reportes", None))
        self.plancha5_1Btn.setText(QCoreApplication.translate("MainWindow", u"Plancha 5", None))
        self.plancha12_1Btn.setText(QCoreApplication.translate("MainWindow", u"Plancha 12", None))
        self.plancha2_1Btn.setText(QCoreApplication.translate("MainWindow", u"Plancha 2", None))
        self.plancha4_1Btn.setText(QCoreApplication.translate("MainWindow", u"Plancha 4", None))
        self.plancha10_1Btn.setText(QCoreApplication.translate("MainWindow", u"Plancha 10", None))
        self.plancha1_1Btn.setText(QCoreApplication.translate("MainWindow", u"Plancha 1", None))
        self.plancha7_1Btn.setText(QCoreApplication.translate("MainWindow", u"Plancha 7", None))
        self.plancha9_1Btn.setText(QCoreApplication.translate("MainWindow", u"Plancha 9", None))
        self.plancha11_1Btn.setText(QCoreApplication.translate("MainWindow", u"Plancha 11", None))
        self.plancha8_1Btn.setText(QCoreApplication.translate("MainWindow", u"Plancha 8", None))
        self.plancha3_1Btn.setText(QCoreApplication.translate("MainWindow", u"Plancha 3", None))
        self.plancha6_1Btn.setText(QCoreApplication.translate("MainWindow", u"Plancha 6", None))
        self.label_22.setText(QCoreApplication.translate("MainWindow", u"HORNO 1", None))
        self.iniciarMad_1Btn.setText(QCoreApplication.translate("MainWindow", u"INICIAR MADURACION", None))
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"Plancha 1", None))
        self.label_10.setText(QCoreApplication.translate("MainWindow", u"Tension: ", None))
        self.label_11.setText(QCoreApplication.translate("MainWindow", u"Temperatura:", None))
        self.label_21.setText(QCoreApplication.translate("MainWindow", u"HORNO 1", None))
        self.pushButton_9.setText(QCoreApplication.translate("MainWindow", u"1", None))
        self.pushButton_2.setText(QCoreApplication.translate("MainWindow", u"8", None))
        self.pushButton_4.setText(QCoreApplication.translate("MainWindow", u"10", None))
        self.pushButton.setText(QCoreApplication.translate("MainWindow", u"6", None))
        self.pushButton_8.setText(QCoreApplication.translate("MainWindow", u"3", None))
        self.pushButton_3.setText(QCoreApplication.translate("MainWindow", u"4", None))
        self.pushButton_5.setText(QCoreApplication.translate("MainWindow", u"2", None))
        self.pushButton_6.setText(QCoreApplication.translate("MainWindow", u"9", None))
        self.pushButton_10.setText(QCoreApplication.translate("MainWindow", u"5", None))
        self.pushButton_7.setText(QCoreApplication.translate("MainWindow", u"7", None))
        self.label_18.setText(QCoreApplication.translate("MainWindow", u"Tension: ", None))
        self.label_17.setText(QCoreApplication.translate("MainWindow", u"Plancha 2", None))
        self.label_19.setText(QCoreApplication.translate("MainWindow", u"Temperatura:", None))
        self.label_20.setText(QCoreApplication.translate("MainWindow", u"HORNO 1", None))
        self.pushButton_41.setText(QCoreApplication.translate("MainWindow", u"1", None))
        self.pushButton_48.setText(QCoreApplication.translate("MainWindow", u"9", None))
        self.pushButton_50.setText(QCoreApplication.translate("MainWindow", u"7", None))
        self.pushButton_43.setText(QCoreApplication.translate("MainWindow", u"10", None))
        self.pushButton_46.setText(QCoreApplication.translate("MainWindow", u"4", None))
        self.pushButton_44.setText(QCoreApplication.translate("MainWindow", u"6", None))
        self.pushButton_49.setText(QCoreApplication.translate("MainWindow", u"5", None))
        self.pushButton_42.setText(QCoreApplication.translate("MainWindow", u"8", None))
        self.pushButton_45.setText(QCoreApplication.translate("MainWindow", u"3", None))
        self.pushButton_47.setText(QCoreApplication.translate("MainWindow", u"2", None))
        self.pushButton_13.setText(QCoreApplication.translate("MainWindow", u"Plancha 1", None))
        self.pushButton_11.setText(QCoreApplication.translate("MainWindow", u"Plancha 9", None))
        self.pushButton_12.setText(QCoreApplication.translate("MainWindow", u"Plancha 11", None))
        self.pushButton_17.setText(QCoreApplication.translate("MainWindow", u"Plancha 4", None))
        self.pushButton_18.setText(QCoreApplication.translate("MainWindow", u"Plancha 2", None))
        self.pushButton_16.setText(QCoreApplication.translate("MainWindow", u"Plancha 8", None))
        self.pushButton_15.setText(QCoreApplication.translate("MainWindow", u"Plancha 3", None))
        self.pushButton_19.setText(QCoreApplication.translate("MainWindow", u"Plancha 10", None))
        self.pushButton_20.setText(QCoreApplication.translate("MainWindow", u"Plancha 5", None))
        self.label_23.setText(QCoreApplication.translate("MainWindow", u"HORNO 2", None))
        self.pushButton_14.setText(QCoreApplication.translate("MainWindow", u"Plancha 6", None))
        self.pushButton_54.setText(QCoreApplication.translate("MainWindow", u"Plancha 7", None))
        self.pushButton_55.setText(QCoreApplication.translate("MainWindow", u"Plancha 12", None))
        self.iniciarMad_2Btn.setText(QCoreApplication.translate("MainWindow", u"INICIAR MADURACION", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"Right Menu", None))
#if QT_CONFIG(tooltip)
        self.closeRightMenuBtn.setToolTip(QCoreApplication.translate("MainWindow", u"Cerrar", None))
#endif // QT_CONFIG(tooltip)
        self.closeRightMenuBtn.setText("")
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"Profile", None))
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"More...", None))
        self.label_12.setText(QCoreApplication.translate("MainWindow", u"Notificaciones", None))
        self.closeNotificationBtn.setText("")
    # retranslateUi

