# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'mainwindow.ui'
##
## Created by: Qt User Interface Compiler version 6.8.0
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
from PySide6.QtWidgets import (QApplication, QCheckBox, QComboBox, QFrame,
    QHBoxLayout, QLabel, QLineEdit, QMainWindow,
    QProgressBar, QScrollArea, QSizePolicy, QSpacerItem,
    QStackedWidget, QToolButton, QVBoxLayout, QWidget)
import resources_rc

class Ui_Nugget(object):
    def setupUi(self, Nugget):
        if not Nugget.objectName():
            Nugget.setObjectName(u"Nugget")
        Nugget.resize(1000, 600)
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Nugget.sizePolicy().hasHeightForWidth())
        Nugget.setSizePolicy(sizePolicy)
        Nugget.setMinimumSize(QSize(1000, 600))
        Nugget.setMaximumSize(QSize(1000, 600))
        Nugget.setWindowOpacity(1.000000000000000)
        Nugget.setStyleSheet(u"QWidget {\n"
"    color: #FFFFFF;\n"
"    background-color: transparent;\n"
"	spacing: 0px;\n"
"}\n"
"\n"
"QWidget:focus {\n"
"    outline: none;\n"
"}\n"
"\n"
"QWidget [cls=central] {\n"
"    background-color: #1e1e1e;\n"
"	border-radius: 0px;\n"
"	border: 1px solid #4B4B4B;\n"
"}\n"
"\n"
"QLabel {\n"
"    font-size: 14px;\n"
"}\n"
"\n"
"QToolButton {\n"
"    background-color: #3b3b3b;\n"
"    border: none;\n"
"    color: #e8e8e8;\n"
"    font-size: 14px;\n"
"	min-height: 35px;\n"
"	icon-size: 16px;\n"
"	padding-left: 10px;\n"
"	padding-right: 10px;\n"
"	border-radius: 8px;\n"
"}\n"
"\n"
"QToolButton[cls=sidebarBtn] {\n"
"    background-color: transparent;\n"
"	icon-size: 24px;\n"
"}\n"
"\n"
"QToolButton:pressed {\n"
"    background-color: #535353;\n"
"    color: #FFFFFF;\n"
"}\n"
"\n"
"QToolButton:checked {\n"
"    background-color: #2860ca;\n"
"    color: #FFFFFF;\n"
"}\n"
"\n"
"QCheckBox {\n"
"	spacing: 8px;\n"
"	font-size: 14px;\n"
"}\n"
"\n"
"QRadioButton {\n"
"	spacing: 8px;\n"
"	font-size: 14px;\n"
"}\n"
""
                        "\n"
"QLineEdit {\n"
"	border: none;\n"
"	background-color: transparent;\n"
"	color: #FFFFFF;\n"
"	font-size: 14px;\n"
"}\n"
"\n"
"QScrollBar:vertical {\n"
"    background: transparent;\n"
"    width: 8px;\n"
"}\n"
"\n"
"QScrollBar:horizontal {\n"
"    background: transparent;\n"
"    height: 8px;\n"
"}\n"
"\n"
"QScrollBar::handle {\n"
"    background: #3b3b3b;\n"
"    border-radius: 4px;\n"
"}\n"
"\n"
"QScrollBar::handle:pressed {\n"
"    background: #535353;\n"
"}\n"
"\n"
"QScrollBar::add-line,\n"
"QScrollBar::sub-line {\n"
"    background: none;\n"
"}\n"
"\n"
"QScrollBar::add-page,\n"
"QScrollBar::sub-page {\n"
"    background: none;\n"
"}\n"
"\n"
"QSlider::groove:horizontal {\n"
"    background-color: #3b3b3b;\n"
"    height: 4px;\n"
"	border-radius: 2px;\n"
"}\n"
"\n"
"QSlider::handle:horizontal {\n"
"    background-color: #535353;\n"
"    width: 8px;\n"
"    margin: -8px 0;\n"
"    border-radius: 4px;\n"
"}\n"
"\n"
"QSlider::handle:horizontal:pressed {\n"
"    background-color: #3b82f7;\n"
"}\n"
"\n"
"QSl"
                        "ider::tick:horizontal {\n"
"    background-color: #535353;\n"
"    width: 1px;\n"
"}\n"
"")
        self.centralwidget = QWidget(Nugget)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setEnabled(True)
        self.centralwidget.setContextMenuPolicy(Qt.NoContextMenu)
        self.centralwidget.setLocale(QLocale(QLocale.English, QLocale.UnitedStates))
        self.verticalLayout_11 = QVBoxLayout(self.centralwidget)
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.deviceBar = QWidget(self.centralwidget)
        self.deviceBar.setObjectName(u"deviceBar")
        self.horizontalLayout_4 = QHBoxLayout(self.deviceBar)
        self.horizontalLayout_4.setSpacing(1)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.horizontalWidget_2 = QWidget(self.deviceBar)
        self.horizontalWidget_2.setObjectName(u"horizontalWidget_2")
        self.horizontalWidget_2.setMinimumSize(QSize(300, 0))
        self.horizontalLayout_19 = QHBoxLayout(self.horizontalWidget_2)
        self.horizontalLayout_19.setSpacing(1)
        self.horizontalLayout_19.setObjectName(u"horizontalLayout_19")
        self.horizontalLayout_19.setContentsMargins(0, 0, 0, 0)
        self.horizontalWidget_3 = QWidget(self.horizontalWidget_2)
        self.horizontalWidget_3.setObjectName(u"horizontalWidget_3")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.horizontalWidget_3.sizePolicy().hasHeightForWidth())
        self.horizontalWidget_3.setSizePolicy(sizePolicy1)
        self.horizontalLayout_15 = QHBoxLayout(self.horizontalWidget_3)
        self.horizontalLayout_15.setSpacing(0)
        self.horizontalLayout_15.setObjectName(u"horizontalLayout_15")
        self.horizontalLayout_15.setContentsMargins(0, 0, 0, 0)
        self.toolButton_6 = QToolButton(self.horizontalWidget_3)
        self.toolButton_6.setObjectName(u"toolButton_6")
        self.toolButton_6.setEnabled(False)
        self.toolButton_6.setStyleSheet(u"QToolButton {\n"
"	border-top-right-radius: 0px;\n"
"	border-bottom-right-radius: 0px;\n"
"}")
        icon = QIcon()
        icon.addFile(u":/icon/phone.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.toolButton_6.setIcon(icon)

        self.horizontalLayout_15.addWidget(self.toolButton_6)

        self.devicePicker = QComboBox(self.horizontalWidget_3)
        self.devicePicker.setObjectName(u"devicePicker")
        self.devicePicker.setStyleSheet(u"#devicePicker {\n"
"	background-color: #3b3b3b;\n"
"    border: none;\n"
"    color: #e8e8e8;\n"
"    font-size: 14px;\n"
"    min-height: 38px;\n"
"	min-width: 35px;\n"
"	padding-left: 8px;\n"
"}\n"
"\n"
"#devicePicker::drop-down {\n"
"    image: url(:/icon/caret-down-fill.svg);\n"
"	icon-size: 16px;\n"
"    subcontrol-position: right center;\n"
"	margin-right: 8px;\n"
"}\n"
"\n"
"#devicePicker QAbstractItemView {\n"
"	background-color: #3b3b3b;\n"
"    outline: none;\n"
"	margin-top: 1px;\n"
"}\n"
"\n"
"#devicePicker QAbstractItemView::item {\n"
"	background-color: #3b3b3b;\n"
"	color: #e8e8e8;\n"
"	min-height: 38px;\n"
"    padding-left: 8px;\n"
"}\n"
"\n"
"#devicePicker QAbstractItemView::item:hover {\n"
"    background-color: #535353;\n"
"    color: #ffffff;\n"
"}")
        self.devicePicker.setDuplicatesEnabled(True)

        self.horizontalLayout_15.addWidget(self.devicePicker)


        self.horizontalLayout_19.addWidget(self.horizontalWidget_3)

        self.refreshBtn = QToolButton(self.horizontalWidget_2)
        self.refreshBtn.setObjectName(u"refreshBtn")
        self.refreshBtn.setStyleSheet(u"QToolButton {\n"
"	border-radius: 0px;\n"
"}")
        icon1 = QIcon()
        icon1.addFile(u":/icon/arrow-clockwise.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.refreshBtn.setIcon(icon1)
        self.refreshBtn.setCheckable(False)
        self.refreshBtn.setToolButtonStyle(Qt.ToolButtonIconOnly)

        self.horizontalLayout_19.addWidget(self.refreshBtn)


        self.horizontalLayout_4.addWidget(self.horizontalWidget_2)

        self.titleBar = QToolButton(self.deviceBar)
        self.titleBar.setObjectName(u"titleBar")
        self.titleBar.setEnabled(False)
        sizePolicy2 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Fixed)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.titleBar.sizePolicy().hasHeightForWidth())
        self.titleBar.setSizePolicy(sizePolicy2)
        self.titleBar.setStyleSheet(u"QToolButton {\n"
"	border-top-left-radius: 0px;\n"
"	border-bottom-left-radius: 0px;\n"
"}")

        self.horizontalLayout_4.addWidget(self.titleBar)


        self.verticalLayout_11.addWidget(self.deviceBar)

        self.body = QWidget(self.centralwidget)
        self.body.setObjectName(u"body")
        self.body.setMinimumSize(QSize(0, 20))
        self.horizontalLayout_18 = QHBoxLayout(self.body)
        self.horizontalLayout_18.setObjectName(u"horizontalLayout_18")
        self.horizontalLayout_18.setContentsMargins(0, 0, 0, 0)
        self.sidebar = QWidget(self.body)
        self.sidebar.setObjectName(u"sidebar")
        sizePolicy3 = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Preferred)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.sidebar.sizePolicy().hasHeightForWidth())
        self.sidebar.setSizePolicy(sizePolicy3)
        self.sidebar.setMinimumSize(QSize(300, 0))
        self.sidebar.setStyleSheet(u"QFrame {\n"
"	color: #414141;\n"
"}")
        self.verticalLayout = QVBoxLayout(self.sidebar)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 9, 9, 0)
        self.homePageBtn = QToolButton(self.sidebar)
        self.homePageBtn.setObjectName(u"homePageBtn")
        sizePolicy2.setHeightForWidth(self.homePageBtn.sizePolicy().hasHeightForWidth())
        self.homePageBtn.setSizePolicy(sizePolicy2)
        icon2 = QIcon()
        icon2.addFile(u":/icon/house.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.homePageBtn.setIcon(icon2)
        self.homePageBtn.setCheckable(True)
        self.homePageBtn.setChecked(True)
        self.homePageBtn.setAutoExclusive(True)
        self.homePageBtn.setToolButtonStyle(Qt.ToolButtonIconOnly)

        self.verticalLayout.addWidget(self.homePageBtn)

        self.explorePageBtn = QToolButton(self.sidebar)
        self.explorePageBtn.setObjectName(u"explorePageBtn")
        self.explorePageBtn.setEnabled(True)
        sizePolicy2.setHeightForWidth(self.explorePageBtn.sizePolicy().hasHeightForWidth())
        self.explorePageBtn.setSizePolicy(sizePolicy2)
        icon3 = QIcon()
        icon3.addFile(u":/icon/compass.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.explorePageBtn.setIcon(icon3)
        self.explorePageBtn.setCheckable(True)
        self.explorePageBtn.setAutoExclusive(True)
        self.explorePageBtn.setToolButtonStyle(Qt.ToolButtonIconOnly)

        self.verticalLayout.addWidget(self.explorePageBtn)

        self.sidebarDiv1 = QFrame(self.sidebar)
        self.sidebarDiv1.setObjectName(u"sidebarDiv1")
        self.sidebarDiv1.setStyleSheet(u"QFrame {\n"
"	color: #414141;\n"
"}")
        self.sidebarDiv1.setFrameShape(QFrame.Shape.VLine)
        self.sidebarDiv1.setFrameShadow(QFrame.Shadow.Sunken)

        self.verticalLayout.addWidget(self.sidebarDiv1)

        self.gestaltPageBtn = QToolButton(self.sidebar)
        self.gestaltPageBtn.setObjectName(u"gestaltPageBtn")
        sizePolicy2.setHeightForWidth(self.gestaltPageBtn.sizePolicy().hasHeightForWidth())
        self.gestaltPageBtn.setSizePolicy(sizePolicy2)
        icon4 = QIcon()
        icon4.addFile(u":/icon/iphone-island.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.gestaltPageBtn.setIcon(icon4)
        self.gestaltPageBtn.setIconSize(QSize(24, 28))
        self.gestaltPageBtn.setCheckable(True)
        self.gestaltPageBtn.setAutoExclusive(True)
        self.gestaltPageBtn.setToolButtonStyle(Qt.ToolButtonIconOnly)
        self.gestaltPageBtn.setArrowType(Qt.NoArrow)

        self.verticalLayout.addWidget(self.gestaltPageBtn)

        self.featureFlagsPageBtn = QToolButton(self.sidebar)
        self.featureFlagsPageBtn.setObjectName(u"featureFlagsPageBtn")
        sizePolicy2.setHeightForWidth(self.featureFlagsPageBtn.sizePolicy().hasHeightForWidth())
        self.featureFlagsPageBtn.setSizePolicy(sizePolicy2)
        font = QFont()
        font.setFamilies([u".AppleSystemUIFont"])
        self.featureFlagsPageBtn.setFont(font)
        icon5 = QIcon()
        icon5.addFile(u":/icon/flag.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.featureFlagsPageBtn.setIcon(icon5)
        self.featureFlagsPageBtn.setCheckable(True)
        self.featureFlagsPageBtn.setAutoExclusive(True)
        self.featureFlagsPageBtn.setToolButtonStyle(Qt.ToolButtonIconOnly)

        self.verticalLayout.addWidget(self.featureFlagsPageBtn)

        self.euEnablerPageBtn = QToolButton(self.sidebar)
        self.euEnablerPageBtn.setObjectName(u"euEnablerPageBtn")
        sizePolicy2.setHeightForWidth(self.euEnablerPageBtn.sizePolicy().hasHeightForWidth())
        self.euEnablerPageBtn.setSizePolicy(sizePolicy2)
        icon6 = QIcon()
        icon6.addFile(u":/icon/geo-alt.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.euEnablerPageBtn.setIcon(icon6)
        self.euEnablerPageBtn.setCheckable(True)
        self.euEnablerPageBtn.setAutoExclusive(True)
        self.euEnablerPageBtn.setToolButtonStyle(Qt.ToolButtonIconOnly)

        self.verticalLayout.addWidget(self.euEnablerPageBtn)

        self.springboardOptionsPageBtn = QToolButton(self.sidebar)
        self.springboardOptionsPageBtn.setObjectName(u"springboardOptionsPageBtn")
        sizePolicy2.setHeightForWidth(self.springboardOptionsPageBtn.sizePolicy().hasHeightForWidth())
        self.springboardOptionsPageBtn.setSizePolicy(sizePolicy2)
        icon7 = QIcon()
        icon7.addFile(u":/icon/app-indicator.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.springboardOptionsPageBtn.setIcon(icon7)
        self.springboardOptionsPageBtn.setCheckable(True)
        self.springboardOptionsPageBtn.setAutoExclusive(True)
        self.springboardOptionsPageBtn.setToolButtonStyle(Qt.ToolButtonIconOnly)

        self.verticalLayout.addWidget(self.springboardOptionsPageBtn)

        self.internalOptionsPageBtn = QToolButton(self.sidebar)
        self.internalOptionsPageBtn.setObjectName(u"internalOptionsPageBtn")
        sizePolicy2.setHeightForWidth(self.internalOptionsPageBtn.sizePolicy().hasHeightForWidth())
        self.internalOptionsPageBtn.setSizePolicy(sizePolicy2)
        icon8 = QIcon()
        icon8.addFile(u":/icon/hdd.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.internalOptionsPageBtn.setIcon(icon8)
        self.internalOptionsPageBtn.setCheckable(True)
        self.internalOptionsPageBtn.setAutoExclusive(True)
        self.internalOptionsPageBtn.setToolButtonStyle(Qt.ToolButtonIconOnly)

        self.verticalLayout.addWidget(self.internalOptionsPageBtn)

        self.advancedPageBtn = QToolButton(self.sidebar)
        self.advancedPageBtn.setObjectName(u"advancedPageBtn")
        sizePolicy2.setHeightForWidth(self.advancedPageBtn.sizePolicy().hasHeightForWidth())
        self.advancedPageBtn.setSizePolicy(sizePolicy2)
        icon9 = QIcon()
        icon9.addFile(u":/icon/star.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.advancedPageBtn.setIcon(icon9)
        self.advancedPageBtn.setCheckable(True)
        self.advancedPageBtn.setAutoExclusive(True)
        self.advancedPageBtn.setToolButtonStyle(Qt.ToolButtonIconOnly)

        self.verticalLayout.addWidget(self.advancedPageBtn)

        self.sidebarDiv2 = QFrame(self.sidebar)
        self.sidebarDiv2.setObjectName(u"sidebarDiv2")
        self.sidebarDiv2.setStyleSheet(u"QFrame {\n"
"	color: #414141;\n"
"}")
        self.sidebarDiv2.setFrameShape(QFrame.Shape.VLine)
        self.sidebarDiv2.setFrameShadow(QFrame.Shadow.Sunken)

        self.verticalLayout.addWidget(self.sidebarDiv2)

        self.applyPageBtn = QToolButton(self.sidebar)
        self.applyPageBtn.setObjectName(u"applyPageBtn")
        sizePolicy2.setHeightForWidth(self.applyPageBtn.sizePolicy().hasHeightForWidth())
        self.applyPageBtn.setSizePolicy(sizePolicy2)
        icon10 = QIcon()
        icon10.addFile(u":/icon/check-circle.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.applyPageBtn.setIcon(icon10)
        self.applyPageBtn.setCheckable(True)
        self.applyPageBtn.setAutoExclusive(True)
        self.applyPageBtn.setToolButtonStyle(Qt.ToolButtonIconOnly)

        self.verticalLayout.addWidget(self.applyPageBtn)

        self.settingsPageBtn = QToolButton(self.sidebar)
        self.settingsPageBtn.setObjectName(u"settingsPageBtn")
        sizePolicy2.setHeightForWidth(self.settingsPageBtn.sizePolicy().hasHeightForWidth())
        self.settingsPageBtn.setSizePolicy(sizePolicy2)
        icon11 = QIcon()
        icon11.addFile(u":/icon/gear.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.settingsPageBtn.setIcon(icon11)
        self.settingsPageBtn.setCheckable(True)
        self.settingsPageBtn.setAutoExclusive(True)
        self.settingsPageBtn.setToolButtonStyle(Qt.ToolButtonIconOnly)

        self.verticalLayout.addWidget(self.settingsPageBtn)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.verticalLayout.addItem(self.verticalSpacer)


        self.horizontalLayout_18.addWidget(self.sidebar)

        self.main = QWidget(self.body)
        self.main.setObjectName(u"main")
        sizePolicy4 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Preferred)
        sizePolicy4.setHorizontalStretch(0)
        sizePolicy4.setVerticalStretch(0)
        sizePolicy4.setHeightForWidth(self.main.sizePolicy().hasHeightForWidth())
        self.main.setSizePolicy(sizePolicy4)
        self._3 = QVBoxLayout(self.main)
        self._3.setSpacing(0)
        self._3.setObjectName(u"_3")
        self._3.setContentsMargins(9, 0, 0, 0)
        self.pages = QStackedWidget(self.main)
        self.pages.setObjectName(u"pages")
        self.homePage = QWidget()
        self.homePage.setObjectName(u"homePage")
        self.homePage.setFont(font)
        self.verticalLayout_2 = QVBoxLayout(self.homePage)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalWidget = QWidget(self.homePage)
        self.horizontalWidget.setObjectName(u"horizontalWidget")
        self.horizontalLayout = QHBoxLayout(self.horizontalWidget)
        self.horizontalLayout.setSpacing(10)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 9, 0, 9)
        self.toolButton_9 = QToolButton(self.horizontalWidget)
        self.toolButton_9.setObjectName(u"toolButton_9")
        self.toolButton_9.setEnabled(False)
        self.toolButton_9.setStyleSheet(u"QToolButton {\n"
"	icon-size: 24px;\n"
"	background-color: transparent;\n"
"	padding-left: 0px;\n"
"	padding-right: 5px;\n"
"	border-radius: 0px;\n"
"}")
        self.toolButton_9.setIcon(icon)

        self.horizontalLayout.addWidget(self.toolButton_9)

        self.verticalWidget = QWidget(self.horizontalWidget)
        self.verticalWidget.setObjectName(u"verticalWidget")
        self.verticalLayout_3 = QVBoxLayout(self.verticalWidget)
        self.verticalLayout_3.setSpacing(6)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.phoneNameLbl = QLabel(self.verticalWidget)
        self.phoneNameLbl.setObjectName(u"phoneNameLbl")
        font1 = QFont()
        font1.setBold(False)
        self.phoneNameLbl.setFont(font1)

        self.verticalLayout_3.addWidget(self.phoneNameLbl)

        self.phoneVersionLbl = QLabel(self.verticalWidget)
        self.phoneVersionLbl.setObjectName(u"phoneVersionLbl")
        self.phoneVersionLbl.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.phoneVersionLbl.setTextFormat(Qt.PlainText)
        self.phoneVersionLbl.setOpenExternalLinks(False)

        self.verticalLayout_3.addWidget(self.phoneVersionLbl)


        self.horizontalLayout.addWidget(self.verticalWidget)

        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer_3)


        self.verticalLayout_2.addWidget(self.horizontalWidget)

        self.line_4 = QFrame(self.homePage)
        self.line_4.setObjectName(u"line_4")
        self.line_4.setStyleSheet(u"QFrame {\n"
"	color: #414141;\n"
"}")
        self.line_4.setFrameShape(QFrame.Shape.VLine)
        self.line_4.setFrameShadow(QFrame.Shadow.Sunken)

        self.verticalLayout_2.addWidget(self.line_4)

        self.horizontalWidget1 = QWidget(self.homePage)
        self.horizontalWidget1.setObjectName(u"horizontalWidget1")
        self.horizontalLayout_27 = QHBoxLayout(self.horizontalWidget1)
        self.horizontalLayout_27.setSpacing(50)
        self.horizontalLayout_27.setObjectName(u"horizontalLayout_27")
        self.horizontalLayout_27.setContentsMargins(0, 0, 0, 0)
        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_27.addItem(self.horizontalSpacer_2)

        self.bigNuggetBtn = QToolButton(self.horizontalWidget1)
        self.bigNuggetBtn.setObjectName(u"bigNuggetBtn")
        self.bigNuggetBtn.setStyleSheet(u"QToolButton {\n"
"	background-color: transparent;\n"
"	padding: 0px;\n"
"}")
        icon12 = QIcon()
        icon12.addFile(u":/credits/big_nugget.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.bigNuggetBtn.setIcon(icon12)
        self.bigNuggetBtn.setIconSize(QSize(150, 200))

        self.horizontalLayout_27.addWidget(self.bigNuggetBtn)

        self.verticalWidget1 = QWidget(self.horizontalWidget1)
        self.verticalWidget1.setObjectName(u"verticalWidget1")
        self.verticalLayout_26 = QVBoxLayout(self.verticalWidget1)
        self.verticalLayout_26.setObjectName(u"verticalLayout_26")
        self.verticalLayout_26.setContentsMargins(0, 0, 0, 0)
        self.verticalSpacer_11 = QSpacerItem(20, 40, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.verticalLayout_26.addItem(self.verticalSpacer_11)

        self.label_2 = QLabel(self.verticalWidget1)
        self.label_2.setObjectName(u"label_2")
        font2 = QFont()
        font2.setBold(True)
        self.label_2.setFont(font2)
        self.label_2.setStyleSheet(u"QLabel {\n"
"	font-size: 35px;\n"
"}")

        self.verticalLayout_26.addWidget(self.label_2)

        self.verticalSpacer_12 = QSpacerItem(20, 40, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.verticalLayout_26.addItem(self.verticalSpacer_12)

        self.horizontalLayout_8 = QHBoxLayout()
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.horizontalLayout_8.setContentsMargins(-1, -1, 0, 0)
        self.discordBtn = QToolButton(self.verticalWidget1)
        self.discordBtn.setObjectName(u"discordBtn")
        icon13 = QIcon()
        icon13.addFile(u":/icon/discord.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.discordBtn.setIcon(icon13)
        self.discordBtn.setToolButtonStyle(Qt.ToolButtonIconOnly)

        self.horizontalLayout_8.addWidget(self.discordBtn)

        self.starOnGithubBtn = QToolButton(self.verticalWidget1)
        self.starOnGithubBtn.setObjectName(u"starOnGithubBtn")
        self.starOnGithubBtn.setIcon(icon9)
        self.starOnGithubBtn.setToolButtonStyle(Qt.ToolButtonIconOnly)

        self.horizontalLayout_8.addWidget(self.starOnGithubBtn)


        self.verticalLayout_26.addLayout(self.horizontalLayout_8)

        self.verticalSpacer_4 = QSpacerItem(20, 40, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.verticalLayout_26.addItem(self.verticalSpacer_4)


        self.horizontalLayout_27.addWidget(self.verticalWidget1)

        self.horizontalSpacer_12 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_27.addItem(self.horizontalSpacer_12)


        self.verticalLayout_2.addWidget(self.horizontalWidget1)

        self.verticalWidget_2 = QWidget(self.homePage)
        self.verticalWidget_2.setObjectName(u"verticalWidget_2")
        self.verticalLayout_25 = QVBoxLayout(self.verticalWidget_2)
        self.verticalLayout_25.setSpacing(15)
        self.verticalLayout_25.setObjectName(u"verticalLayout_25")
        self.verticalLayout_25.setContentsMargins(0, 30, 0, 30)
        self.horizontalWidget2 = QWidget(self.verticalWidget_2)
        self.horizontalWidget2.setObjectName(u"horizontalWidget2")
        self.horizontalWidget2.setEnabled(True)
        self.horizontalLayout_6 = QHBoxLayout(self.horizontalWidget2)
        self.horizontalLayout_6.setSpacing(0)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.horizontalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.leminBtn = QToolButton(self.horizontalWidget2)
        self.leminBtn.setObjectName(u"leminBtn")
        self.leminBtn.setEnabled(True)
        self.leminBtn.setMinimumSize(QSize(150, 35))
        self.leminBtn.setStyleSheet(u"QToolButton {\n"
"	background: none;\n"
"}")
        icon14 = QIcon()
        icon14.addFile(u":/credits/LeminLimez.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.leminBtn.setIcon(icon14)
        self.leminBtn.setToolButtonStyle(Qt.ToolButtonIconOnly)

        self.horizontalLayout_6.addWidget(self.leminBtn)

        self.leminTwitterBtn = QToolButton(self.horizontalWidget2)
        self.leminTwitterBtn.setObjectName(u"leminTwitterBtn")
        self.leminTwitterBtn.setStyleSheet(u"QToolButton {\n"
"	border-top-right-radius: 0px;\n"
"	border-bottom-right-radius: 0px;\n"
"	background: none;\n"
"	border: 1px solid #3b3b3b;\n"
"}\n"
"\n"
"QToolButton:pressed {\n"
"    background-color: #535353;\n"
"    color: #FFFFFF;\n"
"}")
        icon15 = QIcon()
        icon15.addFile(u":/icon/twitter.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.leminTwitterBtn.setIcon(icon15)

        self.horizontalLayout_6.addWidget(self.leminTwitterBtn)

        self.leminGithubBtn = QToolButton(self.horizontalWidget2)
        self.leminGithubBtn.setObjectName(u"leminGithubBtn")
        self.leminGithubBtn.setStyleSheet(u"QToolButton {\n"
"	border-radius: 0px;\n"
"	background: none;\n"
"	border: 1px solid #3b3b3b;\n"
"	border-left: none;\n"
"}\n"
"\n"
"QToolButton:pressed {\n"
"    background-color: #535353;\n"
"    color: #FFFFFF;\n"
"}")
        icon16 = QIcon()
        icon16.addFile(u":/icon/github.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.leminGithubBtn.setIcon(icon16)

        self.horizontalLayout_6.addWidget(self.leminGithubBtn)

        self.leminKoFiBtn = QToolButton(self.horizontalWidget2)
        self.leminKoFiBtn.setObjectName(u"leminKoFiBtn")
        self.leminKoFiBtn.setStyleSheet(u"QToolButton {\n"
"	border-top-left-radius: 0px;\n"
"	border-bottom-left-radius: 0px;\n"
"	background: none;\n"
"	border: 1px solid #3b3b3b;\n"
"	border-left: none;\n"
"}\n"
"\n"
"QToolButton:pressed {\n"
"    background-color: #535353;\n"
"    color: #FFFFFF;\n"
"}")
        icon17 = QIcon()
        icon17.addFile(u":/icon/currency-dollar.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.leminKoFiBtn.setIcon(icon17)

        self.horizontalLayout_6.addWidget(self.leminKoFiBtn)

        self.horizontalSpacer = QSpacerItem(10, 20, QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_6.addItem(self.horizontalSpacer)

        self.toolButton_14 = QToolButton(self.horizontalWidget2)
        self.toolButton_14.setObjectName(u"toolButton_14")
        self.toolButton_14.setEnabled(False)
        sizePolicy2.setHeightForWidth(self.toolButton_14.sizePolicy().hasHeightForWidth())
        self.toolButton_14.setSizePolicy(sizePolicy2)
        self.toolButton_14.setStyleSheet(u"QToolButton {\n"
"	background: none;\n"
"}")

        self.horizontalLayout_6.addWidget(self.toolButton_14)

        self.horizontalSpacer_5 = QSpacerItem(40, 20, QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_6.addItem(self.horizontalSpacer_5)


        self.verticalLayout_25.addWidget(self.horizontalWidget2)

        self.verticalSpacer_16 = QSpacerItem(20, 10, QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Minimum)

        self.verticalLayout_25.addItem(self.verticalSpacer_16)

        self.horizontalWidget_21 = QWidget(self.verticalWidget_2)
        self.horizontalWidget_21.setObjectName(u"horizontalWidget_21")
        self.horizontalLayout_2 = QHBoxLayout(self.horizontalWidget_21)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.helpFromBtn = QToolButton(self.horizontalWidget_21)
        self.helpFromBtn.setObjectName(u"helpFromBtn")
        self.helpFromBtn.setEnabled(True)
        self.helpFromBtn.setMinimumSize(QSize(150, 35))
        self.helpFromBtn.setStyleSheet(u"QToolButton {\n"
"	background: none;\n"
"}")
        self.helpFromBtn.setToolButtonStyle(Qt.ToolButtonIconOnly)

        self.horizontalLayout_2.addWidget(self.helpFromBtn)

        self.jjtechBtn = QToolButton(self.horizontalWidget_21)
        self.jjtechBtn.setObjectName(u"jjtechBtn")
        sizePolicy2.setHeightForWidth(self.jjtechBtn.sizePolicy().hasHeightForWidth())
        self.jjtechBtn.setSizePolicy(sizePolicy2)
        self.jjtechBtn.setMinimumSize(QSize(0, 37))
        self.jjtechBtn.setStyleSheet(u"QToolButton {\n"
"	border-top-right-radius: 0px;\n"
"	border-bottom-right-radius: 0px;\n"
"	background: none;\n"
"	border: 1px solid #3b3b3b;\n"
"}\n"
"\n"
"QToolButton:pressed {\n"
"    background-color: #535353;\n"
"    color: #FFFFFF;\n"
"}")

        self.horizontalLayout_2.addWidget(self.jjtechBtn)

        self.disfordottieBtn = QToolButton(self.horizontalWidget_21)
        self.disfordottieBtn.setObjectName(u"disfordottieBtn")
        sizePolicy2.setHeightForWidth(self.disfordottieBtn.sizePolicy().hasHeightForWidth())
        self.disfordottieBtn.setSizePolicy(sizePolicy2)
        self.disfordottieBtn.setMinimumSize(QSize(0, 37))
        self.disfordottieBtn.setStyleSheet(u"QToolButton {\n"
"	border-radius: 0px;\n"
"	background: none;\n"
"	border: 1px solid #3b3b3b;\n"
"	border-left: none;\n"
"}\n"
"\n"
"QToolButton:pressed {\n"
"    background-color: #535353;\n"
"    color: #FFFFFF;\n"
"}")

        self.horizontalLayout_2.addWidget(self.disfordottieBtn)

        self.lrdsnowBtn = QToolButton(self.horizontalWidget_21)
        self.lrdsnowBtn.setObjectName(u"lrdsnowBtn")
        sizePolicy2.setHeightForWidth(self.lrdsnowBtn.sizePolicy().hasHeightForWidth())
        self.lrdsnowBtn.setSizePolicy(sizePolicy2)
        self.lrdsnowBtn.setMinimumSize(QSize(0, 37))
        self.lrdsnowBtn.setStyleSheet(u"QToolButton {\n"
"	border-top-left-radius: 0px;\n"
"	border-bottom-left-radius: 0px;\n"
"	background: none;\n"
"	border: 1px solid #3b3b3b;\n"
"	border-left: none;\n"
"}\n"
"\n"
"QToolButton:pressed {\n"
"    background-color: #535353;\n"
"    color: #FFFFFF;\n"
"}")

        self.horizontalLayout_2.addWidget(self.lrdsnowBtn)


        self.verticalLayout_25.addWidget(self.horizontalWidget_21)

        self.horizontalWidget3 = QWidget(self.verticalWidget_2)
        self.horizontalWidget3.setObjectName(u"horizontalWidget3")
        self.horizontalLayout_24 = QHBoxLayout(self.horizontalWidget3)
        self.horizontalLayout_24.setSpacing(0)
        self.horizontalLayout_24.setObjectName(u"horizontalLayout_24")
        self.horizontalLayout_24.setContentsMargins(0, 0, 0, 0)
        self.toolButton_15 = QToolButton(self.horizontalWidget3)
        self.toolButton_15.setObjectName(u"toolButton_15")
        self.toolButton_15.setEnabled(False)
        self.toolButton_15.setMinimumSize(QSize(150, 35))
        self.toolButton_15.setStyleSheet(u"QToolButton {\n"
"	background: none;\n"
"}")

        self.horizontalLayout_24.addWidget(self.toolButton_15)

        self.libiBtn = QToolButton(self.horizontalWidget3)
        self.libiBtn.setObjectName(u"libiBtn")
        sizePolicy2.setHeightForWidth(self.libiBtn.sizePolicy().hasHeightForWidth())
        self.libiBtn.setSizePolicy(sizePolicy2)
        self.libiBtn.setStyleSheet(u"QToolButton {\n"
"	border-top-right-radius: 0px;\n"
"	border-bottom-right-radius: 0px;\n"
"	background: none;\n"
"	border: 1px solid #3b3b3b;\n"
"}\n"
"\n"
"QToolButton:pressed {\n"
"    background-color: #535353;\n"
"    color: #FFFFFF;\n"
"}")

        self.horizontalLayout_24.addWidget(self.libiBtn)

        self.qtBtn = QToolButton(self.horizontalWidget3)
        self.qtBtn.setObjectName(u"qtBtn")
        sizePolicy2.setHeightForWidth(self.qtBtn.sizePolicy().hasHeightForWidth())
        self.qtBtn.setSizePolicy(sizePolicy2)
        self.qtBtn.setStyleSheet(u"QToolButton {\n"
"	border-top-left-radius: 0px;\n"
"	border-bottom-left-radius: 0px;\n"
"	background: none;\n"
"	border: 1px solid #3b3b3b;\n"
"	border-left: none;\n"
"}\n"
"\n"
"QToolButton:pressed {\n"
"    background-color: #535353;\n"
"    color: #FFFFFF;\n"
"}")

        self.horizontalLayout_24.addWidget(self.qtBtn)


        self.verticalLayout_25.addWidget(self.horizontalWidget3)


        self.verticalLayout_2.addWidget(self.verticalWidget_2)

        self.label = QLabel(self.homePage)
        self.label.setObjectName(u"label")

        self.verticalLayout_2.addWidget(self.label)

        self.pages.addWidget(self.homePage)
        self.gestaltPage = QWidget()
        self.gestaltPage.setObjectName(u"gestaltPage")
        self.verticalLayout_4 = QVBoxLayout(self.gestaltPage)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.statusBarPageHeader = QWidget(self.gestaltPage)
        self.statusBarPageHeader.setObjectName(u"statusBarPageHeader")
        self.horizontalLayout_5 = QHBoxLayout(self.statusBarPageHeader)
        self.horizontalLayout_5.setSpacing(10)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout_5.setContentsMargins(0, -1, 0, -1)
        self.toolButton_8 = QToolButton(self.statusBarPageHeader)
        self.toolButton_8.setObjectName(u"toolButton_8")
        self.toolButton_8.setEnabled(False)
        self.toolButton_8.setStyleSheet(u"QToolButton {\n"
"	icon-size: 24px;\n"
"	background-color: transparent;\n"
"	padding-left: 0px;\n"
"	padding-right: 5px;\n"
"	border-radius: 0px;\n"
"}")
        self.toolButton_8.setIcon(icon4)
        self.toolButton_8.setIconSize(QSize(30, 30))

        self.horizontalLayout_5.addWidget(self.toolButton_8)

        self.verticalWidget_21 = QWidget(self.statusBarPageHeader)
        self.verticalWidget_21.setObjectName(u"verticalWidget_21")
        self.verticalLayout_5 = QVBoxLayout(self.verticalWidget_21)
        self.verticalLayout_5.setSpacing(6)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.statusBarLbl = QLabel(self.verticalWidget_21)
        self.statusBarLbl.setObjectName(u"statusBarLbl")
        self.statusBarLbl.setFont(font1)

        self.verticalLayout_5.addWidget(self.statusBarLbl)

        self.verticalSpacer_8 = QSpacerItem(20, 16, QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Minimum)

        self.verticalLayout_5.addItem(self.verticalSpacer_8)


        self.horizontalLayout_5.addWidget(self.verticalWidget_21)

        self.horizontalSpacer_4 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_5.addItem(self.horizontalSpacer_4)


        self.verticalLayout_4.addWidget(self.statusBarPageHeader)

        self.line_8 = QFrame(self.gestaltPage)
        self.line_8.setObjectName(u"line_8")
        self.line_8.setStyleSheet(u"QFrame {\n"
"	color: #414141;\n"
"}")
        self.line_8.setFrameShape(QFrame.Shape.VLine)
        self.line_8.setFrameShadow(QFrame.Shadow.Sunken)

        self.verticalLayout_4.addWidget(self.line_8)

        self.mgaWarningLbl = QLabel(self.gestaltPage)
        self.mgaWarningLbl.setObjectName(u"mgaWarningLbl")
        self.mgaWarningLbl.setFont(font2)

        self.verticalLayout_4.addWidget(self.mgaWarningLbl)

        self.scrollArea = QScrollArea(self.gestaltPage)
        self.scrollArea.setObjectName(u"scrollArea")
        self.scrollArea.setFrameShape(QFrame.NoFrame)
        self.scrollArea.setLineWidth(0)
        self.scrollArea.setHorizontalScrollBarPolicy(Qt.ScrollBarAsNeeded)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 650, 1200))
        self.scrollAreaWidgetContents.setMinimumSize(QSize(650, 1200))
        self.scrollAreaWidgetContents.setMaximumSize(QSize(650, 1200))
        self.verticalLayout_9 = QVBoxLayout(self.scrollAreaWidgetContents)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.verticalLayout_9.setContentsMargins(0, 0, 0, 0)
        self.gestaltPageContent = QWidget(self.scrollAreaWidgetContents)
        self.gestaltPageContent.setObjectName(u"gestaltPageContent")
        self.gestaltPageContent.setEnabled(True)
        self.verticalLayout_8 = QVBoxLayout(self.gestaltPageContent)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.verticalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.label_9 = QLabel(self.gestaltPageContent)
        self.label_9.setObjectName(u"label_9")

        self.verticalLayout_8.addWidget(self.label_9)

        self.dynamicIslandDrp = QComboBox(self.gestaltPageContent)
        self.dynamicIslandDrp.addItem("")
        self.dynamicIslandDrp.addItem("")
        self.dynamicIslandDrp.addItem("")
        self.dynamicIslandDrp.addItem("")
        self.dynamicIslandDrp.addItem("")
        self.dynamicIslandDrp.addItem("")
        self.dynamicIslandDrp.addItem("")
        self.dynamicIslandDrp.setObjectName(u"dynamicIslandDrp")
        self.dynamicIslandDrp.setMinimumSize(QSize(0, 0))
        self.dynamicIslandDrp.setMaximumSize(QSize(325, 16777215))
        self.dynamicIslandDrp.setStyleSheet(u"QComboBox {\n"
"	background-color: #3b3b3b;\n"
"    border: none;\n"
"    color: #e8e8e8;\n"
"    font-size: 14px;\n"
"	padding-left: 8px;\n"
"	border-radius: 8px;\n"
"}\n"
"\n"
"QComboBox::drop-down {\n"
"    image: url(:/icon/caret-down-fill.svg);\n"
"	icon-size: 16px;\n"
"    subcontrol-position: right center;\n"
"	margin-right: 8px;\n"
"}\n"
"\n"
"QComboBox QAbstractItemView {\n"
"	background-color: #3b3b3b;\n"
"    outline: none;\n"
"	margin-top: 1px;\n"
"}\n"
"\n"
"QComboBox QAbstractItemView::item {\n"
"	background-color: #3b3b3b;\n"
"	color: #e8e8e8;\n"
"    padding-left: 8px;\n"
"}\n"
"\n"
"QComboBox QAbstractItemView::item:hover {\n"
"    background-color: #535353;\n"
"    color: #ffffff;\n"
"}")
        self.dynamicIslandDrp.setMaxVisibleItems(15)

        self.verticalLayout_8.addWidget(self.dynamicIslandDrp)

        self.rdarFixChk = QCheckBox(self.gestaltPageContent)
        self.rdarFixChk.setObjectName(u"rdarFixChk")

        self.verticalLayout_8.addWidget(self.rdarFixChk)

        self.modelNameChk = QCheckBox(self.gestaltPageContent)
        self.modelNameChk.setObjectName(u"modelNameChk")

        self.verticalLayout_8.addWidget(self.modelNameChk)

        self.modelNameTxt = QLineEdit(self.gestaltPageContent)
        self.modelNameTxt.setObjectName(u"modelNameTxt")

        self.verticalLayout_8.addWidget(self.modelNameTxt)

        self.bootChimeChk = QCheckBox(self.gestaltPageContent)
        self.bootChimeChk.setObjectName(u"bootChimeChk")

        self.verticalLayout_8.addWidget(self.bootChimeChk)

        self.chargeLimitChk = QCheckBox(self.gestaltPageContent)
        self.chargeLimitChk.setObjectName(u"chargeLimitChk")

        self.verticalLayout_8.addWidget(self.chargeLimitChk)

        self.tapToWakeChk = QCheckBox(self.gestaltPageContent)
        self.tapToWakeChk.setObjectName(u"tapToWakeChk")

        self.verticalLayout_8.addWidget(self.tapToWakeChk)

        self.iphone16SettingsChk = QCheckBox(self.gestaltPageContent)
        self.iphone16SettingsChk.setObjectName(u"iphone16SettingsChk")

        self.verticalLayout_8.addWidget(self.iphone16SettingsChk)

        self.parallaxChk = QCheckBox(self.gestaltPageContent)
        self.parallaxChk.setObjectName(u"parallaxChk")

        self.verticalLayout_8.addWidget(self.parallaxChk)

        self.line_7 = QFrame(self.gestaltPageContent)
        self.line_7.setObjectName(u"line_7")
        self.line_7.setStyleSheet(u"QFrame {\n"
"	color: #414141;\n"
"}")
        self.line_7.setFrameShape(QFrame.Shape.VLine)
        self.line_7.setFrameShadow(QFrame.Shadow.Sunken)

        self.verticalLayout_8.addWidget(self.line_7)

        self.stageManagerChk = QCheckBox(self.gestaltPageContent)
        self.stageManagerChk.setObjectName(u"stageManagerChk")

        self.verticalLayout_8.addWidget(self.stageManagerChk)

        self.enableMedusaChk = QCheckBox(self.gestaltPageContent)
        self.enableMedusaChk.setObjectName(u"enableMedusaChk")

        self.verticalLayout_8.addWidget(self.enableMedusaChk)

        self.ipadAppsChk = QCheckBox(self.gestaltPageContent)
        self.ipadAppsChk.setObjectName(u"ipadAppsChk")

        self.verticalLayout_8.addWidget(self.ipadAppsChk)

        self.shutterChk = QCheckBox(self.gestaltPageContent)
        self.shutterChk.setObjectName(u"shutterChk")

        self.verticalLayout_8.addWidget(self.shutterChk)

        self.findMyFriendsChk = QCheckBox(self.gestaltPageContent)
        self.findMyFriendsChk.setObjectName(u"findMyFriendsChk")

        self.verticalLayout_8.addWidget(self.findMyFriendsChk)

        self.pencilChk = QCheckBox(self.gestaltPageContent)
        self.pencilChk.setObjectName(u"pencilChk")

        self.verticalLayout_8.addWidget(self.pencilChk)

        self.actionButtonChk = QCheckBox(self.gestaltPageContent)
        self.actionButtonChk.setObjectName(u"actionButtonChk")

        self.verticalLayout_8.addWidget(self.actionButtonChk)

        self.line_9 = QFrame(self.gestaltPageContent)
        self.line_9.setObjectName(u"line_9")
        self.line_9.setStyleSheet(u"QFrame {\n"
"	color: #414141;\n"
"}")
        self.line_9.setFrameShape(QFrame.Shape.VLine)
        self.line_9.setFrameShadow(QFrame.Shadow.Sunken)

        self.verticalLayout_8.addWidget(self.line_9)

        self.internalInstallChk = QCheckBox(self.gestaltPageContent)
        self.internalInstallChk.setObjectName(u"internalInstallChk")

        self.verticalLayout_8.addWidget(self.internalInstallChk)

        self.internalStorageChk = QCheckBox(self.gestaltPageContent)
        self.internalStorageChk.setObjectName(u"internalStorageChk")

        self.verticalLayout_8.addWidget(self.internalStorageChk)

        self.line_10 = QFrame(self.gestaltPageContent)
        self.line_10.setObjectName(u"line_10")
        self.line_10.setStyleSheet(u"QFrame {\n"
"	color: #414141;\n"
"}")
        self.line_10.setFrameShape(QFrame.Shape.VLine)
        self.line_10.setFrameShadow(QFrame.Shadow.Sunken)

        self.verticalLayout_8.addWidget(self.line_10)

        self.collisionSOSChk = QCheckBox(self.gestaltPageContent)
        self.collisionSOSChk.setObjectName(u"collisionSOSChk")

        self.verticalLayout_8.addWidget(self.collisionSOSChk)

        self.aodChk = QCheckBox(self.gestaltPageContent)
        self.aodChk.setObjectName(u"aodChk")

        self.verticalLayout_8.addWidget(self.aodChk)

        self.line_22 = QFrame(self.gestaltPageContent)
        self.line_22.setObjectName(u"line_22")
        self.line_22.setStyleSheet(u"QFrame {\n"
"	color: #414141;\n"
"}")
        self.line_22.setFrameShape(QFrame.Shape.VLine)
        self.line_22.setFrameShadow(QFrame.Shadow.Sunken)

        self.verticalLayout_8.addWidget(self.line_22)

        self.horizontalLayout_11 = QHBoxLayout()
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.horizontalLayout_11.setContentsMargins(-1, -1, -1, 0)
        self.label_10 = QLabel(self.gestaltPageContent)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setEnabled(True)

        self.horizontalLayout_11.addWidget(self.label_10)

        self.addGestaltKeyBtn = QToolButton(self.gestaltPageContent)
        self.addGestaltKeyBtn.setObjectName(u"addGestaltKeyBtn")
        self.addGestaltKeyBtn.setEnabled(True)
        icon18 = QIcon()
        icon18.addFile(u":/icon/plus.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.addGestaltKeyBtn.setIcon(icon18)
        self.addGestaltKeyBtn.setCheckable(False)
        self.addGestaltKeyBtn.setToolButtonStyle(Qt.ToolButtonIconOnly)

        self.horizontalLayout_11.addWidget(self.addGestaltKeyBtn)


        self.verticalLayout_8.addLayout(self.horizontalLayout_11)

        self.label_12 = QLabel(self.gestaltPageContent)
        self.label_12.setObjectName(u"label_12")

        self.verticalLayout_8.addWidget(self.label_12)

        self.line_23 = QFrame(self.gestaltPageContent)
        self.line_23.setObjectName(u"line_23")
        self.line_23.setStyleSheet(u"QFrame {\n"
"	color: #414141;\n"
"}")
        self.line_23.setFrameShape(QFrame.Shape.VLine)
        self.line_23.setFrameShadow(QFrame.Shadow.Sunken)

        self.verticalLayout_8.addWidget(self.line_23)

        self.customKeysCnt = QWidget(self.gestaltPageContent)
        self.customKeysCnt.setObjectName(u"customKeysCnt")
        self.customKeysCnt.setEnabled(True)
        self.verticalLayout_32 = QVBoxLayout(self.customKeysCnt)
        self.verticalLayout_32.setObjectName(u"verticalLayout_32")
        self.customKeysLayout = QVBoxLayout()
        self.customKeysLayout.setObjectName(u"customKeysLayout")

        self.verticalLayout_32.addLayout(self.customKeysLayout)


        self.verticalLayout_8.addWidget(self.customKeysCnt)

        self.verticalSpacer_3 = QSpacerItem(20, 40, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.verticalLayout_8.addItem(self.verticalSpacer_3)


        self.verticalLayout_9.addWidget(self.gestaltPageContent)

        self.scrollArea.setWidget(self.scrollAreaWidgetContents)

        self.verticalLayout_4.addWidget(self.scrollArea)

        self.pages.addWidget(self.gestaltPage)
        self.featureFlagsPage = QWidget()
        self.featureFlagsPage.setObjectName(u"featureFlagsPage")
        self.verticalLayout_14 = QVBoxLayout(self.featureFlagsPage)
        self.verticalLayout_14.setObjectName(u"verticalLayout_14")
        self.verticalLayout_14.setContentsMargins(0, 0, 0, 0)
        self.horizontalWidget_5 = QWidget(self.featureFlagsPage)
        self.horizontalWidget_5.setObjectName(u"horizontalWidget_5")
        self.horizontalLayout_20 = QHBoxLayout(self.horizontalWidget_5)
        self.horizontalLayout_20.setSpacing(10)
        self.horizontalLayout_20.setObjectName(u"horizontalLayout_20")
        self.horizontalLayout_20.setContentsMargins(0, 9, 0, 9)
        self.toolButton_10 = QToolButton(self.horizontalWidget_5)
        self.toolButton_10.setObjectName(u"toolButton_10")
        self.toolButton_10.setEnabled(False)
        self.toolButton_10.setStyleSheet(u"QToolButton {\n"
"	icon-size: 24px;\n"
"	background-color: transparent;\n"
"	padding-left: 0px;\n"
"	padding-right: 5px;\n"
"	border-radius: 0px;\n"
"}")
        self.toolButton_10.setIcon(icon5)

        self.horizontalLayout_20.addWidget(self.toolButton_10)

        self.verticalWidget_4 = QWidget(self.horizontalWidget_5)
        self.verticalWidget_4.setObjectName(u"verticalWidget_4")
        self.verticalLayout_12 = QVBoxLayout(self.verticalWidget_4)
        self.verticalLayout_12.setSpacing(6)
        self.verticalLayout_12.setObjectName(u"verticalLayout_12")
        self.verticalLayout_12.setContentsMargins(0, 0, 0, 0)
        self.internalOptionsLbl = QLabel(self.verticalWidget_4)
        self.internalOptionsLbl.setObjectName(u"internalOptionsLbl")
        self.internalOptionsLbl.setFont(font1)

        self.verticalLayout_12.addWidget(self.internalOptionsLbl)

        self.verticalSpacer_15 = QSpacerItem(20, 16, QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Minimum)

        self.verticalLayout_12.addItem(self.verticalSpacer_15)


        self.horizontalLayout_20.addWidget(self.verticalWidget_4)

        self.horizontalSpacer_7 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_20.addItem(self.horizontalSpacer_7)


        self.verticalLayout_14.addWidget(self.horizontalWidget_5)

        self.line_12 = QFrame(self.featureFlagsPage)
        self.line_12.setObjectName(u"line_12")
        self.line_12.setStyleSheet(u"QFrame {\n"
"	color: #414141;\n"
"}")
        self.line_12.setFrameShape(QFrame.Shape.VLine)
        self.line_12.setFrameShadow(QFrame.Shadow.Sunken)

        self.verticalLayout_14.addWidget(self.line_12)

        self.featureFlagsPageContent = QWidget(self.featureFlagsPage)
        self.featureFlagsPageContent.setObjectName(u"featureFlagsPageContent")
        self.featureFlagsPageContent.setEnabled(True)
        self.verticalLayout_13 = QVBoxLayout(self.featureFlagsPageContent)
        self.verticalLayout_13.setObjectName(u"verticalLayout_13")
        self.verticalLayout_13.setContentsMargins(0, 0, 0, 0)
        self.clockAnimChk = QCheckBox(self.featureFlagsPageContent)
        self.clockAnimChk.setObjectName(u"clockAnimChk")

        self.verticalLayout_13.addWidget(self.clockAnimChk)

        self.lockscreenChk = QCheckBox(self.featureFlagsPageContent)
        self.lockscreenChk.setObjectName(u"lockscreenChk")

        self.verticalLayout_13.addWidget(self.lockscreenChk)

        self.div = QFrame(self.featureFlagsPageContent)
        self.div.setObjectName(u"div")
        self.div.setEnabled(False)
        self.div.setStyleSheet(u"QFrame {\n"
"	color: #414141;\n"
"}")
        self.div.setFrameShape(QFrame.Shape.VLine)
        self.div.setFrameShadow(QFrame.Shadow.Sunken)

        self.verticalLayout_13.addWidget(self.div)

        self.photosChk = QCheckBox(self.featureFlagsPageContent)
        self.photosChk.setObjectName(u"photosChk")

        self.verticalLayout_13.addWidget(self.photosChk)

        self.aiChk = QCheckBox(self.featureFlagsPageContent)
        self.aiChk.setObjectName(u"aiChk")

        self.verticalLayout_13.addWidget(self.aiChk)

        self.verticalSpacer_6 = QSpacerItem(20, 40, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.verticalLayout_13.addItem(self.verticalSpacer_6)


        self.verticalLayout_14.addWidget(self.featureFlagsPageContent)

        self.pages.addWidget(self.featureFlagsPage)
        self.euEnablerPage = QWidget()
        self.euEnablerPage.setObjectName(u"euEnablerPage")
        self.verticalLayout_17 = QVBoxLayout(self.euEnablerPage)
        self.verticalLayout_17.setObjectName(u"verticalLayout_17")
        self.verticalLayout_17.setContentsMargins(0, 0, 0, 0)
        self.horizontalWidget_6 = QWidget(self.euEnablerPage)
        self.horizontalWidget_6.setObjectName(u"horizontalWidget_6")
        self.horizontalLayout_21 = QHBoxLayout(self.horizontalWidget_6)
        self.horizontalLayout_21.setSpacing(10)
        self.horizontalLayout_21.setObjectName(u"horizontalLayout_21")
        self.horizontalLayout_21.setContentsMargins(0, 9, 0, 9)
        self.toolButton_11 = QToolButton(self.horizontalWidget_6)
        self.toolButton_11.setObjectName(u"toolButton_11")
        self.toolButton_11.setEnabled(False)
        self.toolButton_11.setStyleSheet(u"QToolButton {\n"
"	icon-size: 24px;\n"
"	background-color: transparent;\n"
"	padding-left: 0px;\n"
"	padding-right: 5px;\n"
"	border-radius: 0px;\n"
"}")
        self.toolButton_11.setIcon(icon6)

        self.horizontalLayout_21.addWidget(self.toolButton_11)

        self.verticalWidget_5 = QWidget(self.horizontalWidget_6)
        self.verticalWidget_5.setObjectName(u"verticalWidget_5")
        self.verticalLayout_15 = QVBoxLayout(self.verticalWidget_5)
        self.verticalLayout_15.setSpacing(6)
        self.verticalLayout_15.setObjectName(u"verticalLayout_15")
        self.verticalLayout_15.setContentsMargins(0, 0, 0, 0)
        self.eligibilityLbl = QLabel(self.verticalWidget_5)
        self.eligibilityLbl.setObjectName(u"eligibilityLbl")
        self.eligibilityLbl.setFont(font1)

        self.verticalLayout_15.addWidget(self.eligibilityLbl)

        self.verticalSpacer_20 = QSpacerItem(20, 16, QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Minimum)

        self.verticalLayout_15.addItem(self.verticalSpacer_20)


        self.horizontalLayout_21.addWidget(self.verticalWidget_5)

        self.horizontalSpacer_8 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_21.addItem(self.horizontalSpacer_8)


        self.verticalLayout_17.addWidget(self.horizontalWidget_6)

        self.line_13 = QFrame(self.euEnablerPage)
        self.line_13.setObjectName(u"line_13")
        self.line_13.setStyleSheet(u"QFrame {\n"
"	color: #414141;\n"
"}")
        self.line_13.setFrameShape(QFrame.Shape.VLine)
        self.line_13.setFrameShadow(QFrame.Shadow.Sunken)

        self.verticalLayout_17.addWidget(self.line_13)

        self.euEnablerPageContent = QWidget(self.euEnablerPage)
        self.euEnablerPageContent.setObjectName(u"euEnablerPageContent")
        self.euEnablerPageContent.setEnabled(False)
        self.verticalLayout_16 = QVBoxLayout(self.euEnablerPageContent)
        self.verticalLayout_16.setObjectName(u"verticalLayout_16")
        self.verticalLayout_16.setContentsMargins(0, 0, 0, 0)
        self.euEnablerContent = QWidget(self.euEnablerPageContent)
        self.euEnablerContent.setObjectName(u"euEnablerContent")
        self.verticalLayout_36 = QVBoxLayout(self.euEnablerContent)
        self.verticalLayout_36.setObjectName(u"verticalLayout_36")
        self.verticalLayout_36.setContentsMargins(0, 0, 0, 0)
        self.euEnablerEnabledChk = QCheckBox(self.euEnablerContent)
        self.euEnablerEnabledChk.setObjectName(u"euEnablerEnabledChk")

        self.verticalLayout_36.addWidget(self.euEnablerEnabledChk)

        self.label_5 = QLabel(self.euEnablerContent)
        self.label_5.setObjectName(u"label_5")

        self.verticalLayout_36.addWidget(self.label_5)

        self.methodChoiceDrp = QComboBox(self.euEnablerContent)
        self.methodChoiceDrp.addItem("")
        self.methodChoiceDrp.addItem("")
        self.methodChoiceDrp.setObjectName(u"methodChoiceDrp")
        self.methodChoiceDrp.setMaximumSize(QSize(150, 16777215))
        self.methodChoiceDrp.setStyleSheet(u"QComboBox {\n"
"	background-color: #3b3b3b;\n"
"    border: none;\n"
"    color: #e8e8e8;\n"
"    font-size: 14px;\n"
"	padding-left: 8px;\n"
"	border-radius: 8px;\n"
"}\n"
"\n"
"QComboBox::drop-down {\n"
"    image: url(:/icon/caret-down-fill.svg);\n"
"	icon-size: 16px;\n"
"    subcontrol-position: right center;\n"
"	margin-right: 8px;\n"
"}\n"
"\n"
"QComboBox QAbstractItemView {\n"
"	background-color: #3b3b3b;\n"
"    outline: none;\n"
"	margin-top: 1px;\n"
"}\n"
"\n"
"QComboBox QAbstractItemView::item {\n"
"	background-color: #3b3b3b;\n"
"	color: #e8e8e8;\n"
"    padding-left: 8px;\n"
"}\n"
"\n"
"QComboBox QAbstractItemView::item:hover {\n"
"    background-color: #535353;\n"
"    color: #ffffff;\n"
"}")

        self.verticalLayout_36.addWidget(self.methodChoiceDrp)

        self.label_6 = QLabel(self.euEnablerContent)
        self.label_6.setObjectName(u"label_6")

        self.verticalLayout_36.addWidget(self.label_6)

        self.regionCodeTxt = QLineEdit(self.euEnablerContent)
        self.regionCodeTxt.setObjectName(u"regionCodeTxt")

        self.verticalLayout_36.addWidget(self.regionCodeTxt)

        self.line_16 = QFrame(self.euEnablerContent)
        self.line_16.setObjectName(u"line_16")
        self.line_16.setEnabled(False)
        self.line_16.setStyleSheet(u"QFrame {\n"
"	color: #414141;\n"
"}")
        self.line_16.setFrameShape(QFrame.Shape.VLine)
        self.line_16.setFrameShadow(QFrame.Shadow.Sunken)

        self.verticalLayout_36.addWidget(self.line_16)


        self.verticalLayout_16.addWidget(self.euEnablerContent)

        self.mgaWarningLbl2 = QLabel(self.euEnablerPageContent)
        self.mgaWarningLbl2.setObjectName(u"mgaWarningLbl2")
        self.mgaWarningLbl2.setFont(font2)

        self.verticalLayout_16.addWidget(self.mgaWarningLbl2)

        self.enableAIChk = QCheckBox(self.euEnablerPageContent)
        self.enableAIChk.setObjectName(u"enableAIChk")

        self.verticalLayout_16.addWidget(self.enableAIChk)

        self.aiEnablerContent = QWidget(self.euEnablerPageContent)
        self.aiEnablerContent.setObjectName(u"aiEnablerContent")
        self.verticalLayout_34 = QVBoxLayout(self.aiEnablerContent)
        self.verticalLayout_34.setObjectName(u"verticalLayout_34")
        self.verticalLayout_34.setContentsMargins(0, 5, 0, 5)
        self.eligFileChk = QCheckBox(self.aiEnablerContent)
        self.eligFileChk.setObjectName(u"eligFileChk")

        self.verticalLayout_34.addWidget(self.eligFileChk)

        self.languageLbl = QLabel(self.aiEnablerContent)
        self.languageLbl.setObjectName(u"languageLbl")

        self.verticalLayout_34.addWidget(self.languageLbl)

        self.languageTxt = QLineEdit(self.aiEnablerContent)
        self.languageTxt.setObjectName(u"languageTxt")

        self.verticalLayout_34.addWidget(self.languageTxt)

        self.line_21 = QFrame(self.aiEnablerContent)
        self.line_21.setObjectName(u"line_21")
        self.line_21.setStyleSheet(u"QFrame {\n"
"	color: #414141;\n"
"}")
        self.line_21.setFrameShape(QFrame.Shape.VLine)
        self.line_21.setFrameShadow(QFrame.Shadow.Sunken)

        self.verticalLayout_34.addWidget(self.line_21)

        self.aiInfoLabel = QLabel(self.aiEnablerContent)
        self.aiInfoLabel.setObjectName(u"aiInfoLabel")
        sizePolicy1.setHeightForWidth(self.aiInfoLabel.sizePolicy().hasHeightForWidth())
        self.aiInfoLabel.setSizePolicy(sizePolicy1)
        self.aiInfoLabel.setMaximumSize(QSize(16777215, 16777215))
        self.aiInfoLabel.setTextFormat(Qt.PlainText)
        self.aiInfoLabel.setScaledContents(False)

        self.verticalLayout_34.addWidget(self.aiInfoLabel)

        self.label_8 = QLabel(self.aiEnablerContent)
        self.label_8.setObjectName(u"label_8")

        self.verticalLayout_34.addWidget(self.label_8)

        self.spoofedModelDrp = QComboBox(self.aiEnablerContent)
        self.spoofedModelDrp.addItem("")
        self.spoofedModelDrp.addItem("")
        self.spoofedModelDrp.addItem("")
        self.spoofedModelDrp.addItem("")
        self.spoofedModelDrp.addItem("")
        self.spoofedModelDrp.addItem("")
        self.spoofedModelDrp.addItem("")
        self.spoofedModelDrp.addItem("")
        self.spoofedModelDrp.addItem("")
        self.spoofedModelDrp.addItem("")
        self.spoofedModelDrp.addItem("")
        self.spoofedModelDrp.addItem("")
        self.spoofedModelDrp.addItem("")
        self.spoofedModelDrp.addItem("")
        self.spoofedModelDrp.addItem("")
        self.spoofedModelDrp.addItem("")
        self.spoofedModelDrp.addItem("")
        self.spoofedModelDrp.addItem("")
        self.spoofedModelDrp.addItem("")
        self.spoofedModelDrp.addItem("")
        self.spoofedModelDrp.addItem("")
        self.spoofedModelDrp.addItem("")
        self.spoofedModelDrp.addItem("")
        self.spoofedModelDrp.addItem("")
        self.spoofedModelDrp.addItem("")
        self.spoofedModelDrp.addItem("")
        self.spoofedModelDrp.addItem("")
        self.spoofedModelDrp.setObjectName(u"spoofedModelDrp")
        self.spoofedModelDrp.setMaximumSize(QSize(325, 16777215))
        self.spoofedModelDrp.setStyleSheet(u"QComboBox {\n"
"	background-color: #3b3b3b;\n"
"    border: none;\n"
"    color: #e8e8e8;\n"
"    font-size: 14px;\n"
"	padding-left: 8px;\n"
"	border-radius: 8px;\n"
"}\n"
"\n"
"QComboBox::drop-down {\n"
"    image: url(:/icon/caret-down-fill.svg);\n"
"	icon-size: 16px;\n"
"    subcontrol-position: right center;\n"
"	margin-right: 8px;\n"
"}\n"
"\n"
"QComboBox QAbstractItemView {\n"
"	background-color: #3b3b3b;\n"
"    outline: none;\n"
"	margin-top: 1px;\n"
"}\n"
"\n"
"QComboBox QAbstractItemView::item {\n"
"	background-color: #3b3b3b;\n"
"	color: #e8e8e8;\n"
"    padding-left: 8px;\n"
"}\n"
"\n"
"QComboBox QAbstractItemView::item:hover {\n"
"    background-color: #535353;\n"
"    color: #ffffff;\n"
"}")

        self.verticalLayout_34.addWidget(self.spoofedModelDrp)


        self.verticalLayout_16.addWidget(self.aiEnablerContent)

        self.verticalSpacer_7 = QSpacerItem(20, 40, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.verticalLayout_16.addItem(self.verticalSpacer_7)


        self.verticalLayout_17.addWidget(self.euEnablerPageContent)

        self.pages.addWidget(self.euEnablerPage)
        self.springboardOptionsPage = QWidget()
        self.springboardOptionsPage.setObjectName(u"springboardOptionsPage")
        self.verticalLayout_10 = QVBoxLayout(self.springboardOptionsPage)
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.verticalLayout_10.setContentsMargins(0, 0, 0, 0)
        self.horizontalWidget_4 = QWidget(self.springboardOptionsPage)
        self.horizontalWidget_4.setObjectName(u"horizontalWidget_4")
        self.horizontalLayout_13 = QHBoxLayout(self.horizontalWidget_4)
        self.horizontalLayout_13.setSpacing(10)
        self.horizontalLayout_13.setObjectName(u"horizontalLayout_13")
        self.horizontalLayout_13.setContentsMargins(0, 9, 0, 9)
        self.toolButton_7 = QToolButton(self.horizontalWidget_4)
        self.toolButton_7.setObjectName(u"toolButton_7")
        self.toolButton_7.setEnabled(False)
        self.toolButton_7.setStyleSheet(u"QToolButton {\n"
"	icon-size: 24px;\n"
"	background-color: transparent;\n"
"	padding-left: 0px;\n"
"	padding-right: 5px;\n"
"	border-radius: 0px;\n"
"}")
        self.toolButton_7.setIcon(icon7)

        self.horizontalLayout_13.addWidget(self.toolButton_7)

        self.verticalWidget_3 = QWidget(self.horizontalWidget_4)
        self.verticalWidget_3.setObjectName(u"verticalWidget_3")
        self.verticalLayout_7 = QVBoxLayout(self.verticalWidget_3)
        self.verticalLayout_7.setSpacing(6)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.verticalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.springboardOptionsLbl = QLabel(self.verticalWidget_3)
        self.springboardOptionsLbl.setObjectName(u"springboardOptionsLbl")
        self.springboardOptionsLbl.setFont(font1)

        self.verticalLayout_7.addWidget(self.springboardOptionsLbl)

        self.verticalSpacer_19 = QSpacerItem(20, 16, QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Minimum)

        self.verticalLayout_7.addItem(self.verticalSpacer_19)


        self.horizontalLayout_13.addWidget(self.verticalWidget_3)

        self.horizontalSpacer_6 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_13.addItem(self.horizontalSpacer_6)


        self.verticalLayout_10.addWidget(self.horizontalWidget_4)

        self.line_11 = QFrame(self.springboardOptionsPage)
        self.line_11.setObjectName(u"line_11")
        self.line_11.setStyleSheet(u"QFrame {\n"
"	color: #414141;\n"
"}")
        self.line_11.setFrameShape(QFrame.Shape.VLine)
        self.line_11.setFrameShadow(QFrame.Shadow.Sunken)

        self.verticalLayout_10.addWidget(self.line_11)

        self.springboardOptionsPageContent = QWidget(self.springboardOptionsPage)
        self.springboardOptionsPageContent.setObjectName(u"springboardOptionsPageContent")
        self.springboardOptionsPageContent.setEnabled(False)
        self.springboardOptionsPageContent.setMaximumSize(QSize(650, 16777215))
        self._2 = QVBoxLayout(self.springboardOptionsPageContent)
        self._2.setObjectName(u"_2")
        self._2.setContentsMargins(0, 0, 0, 0)
        self.label_13 = QLabel(self.springboardOptionsPageContent)
        self.label_13.setObjectName(u"label_13")

        self._2.addWidget(self.label_13)

        self.footnoteTxt = QLineEdit(self.springboardOptionsPageContent)
        self.footnoteTxt.setObjectName(u"footnoteTxt")

        self._2.addWidget(self.footnoteTxt)

        self.line_6 = QFrame(self.springboardOptionsPageContent)
        self.line_6.setObjectName(u"line_6")
        self.line_6.setStyleSheet(u"QFrame {\n"
"	color: #414141;\n"
"}")
        self.line_6.setFrameShape(QFrame.Shape.VLine)
        self.line_6.setFrameShadow(QFrame.Shadow.Sunken)

        self._2.addWidget(self.line_6)

        self.disableLockRespringChk = QCheckBox(self.springboardOptionsPageContent)
        self.disableLockRespringChk.setObjectName(u"disableLockRespringChk")

        self._2.addWidget(self.disableLockRespringChk)

        self.disableDimmingChk = QCheckBox(self.springboardOptionsPageContent)
        self.disableDimmingChk.setObjectName(u"disableDimmingChk")

        self._2.addWidget(self.disableDimmingChk)

        self.disableBatteryAlertsChk = QCheckBox(self.springboardOptionsPageContent)
        self.disableBatteryAlertsChk.setObjectName(u"disableBatteryAlertsChk")

        self._2.addWidget(self.disableBatteryAlertsChk)

        self.disableCrumbChk = QCheckBox(self.springboardOptionsPageContent)
        self.disableCrumbChk.setObjectName(u"disableCrumbChk")

        self._2.addWidget(self.disableCrumbChk)

        self.enableSupervisionTextChk = QCheckBox(self.springboardOptionsPageContent)
        self.enableSupervisionTextChk.setObjectName(u"enableSupervisionTextChk")

        self._2.addWidget(self.enableSupervisionTextChk)

        self.enableAirPlayChk = QCheckBox(self.springboardOptionsPageContent)
        self.enableAirPlayChk.setObjectName(u"enableAirPlayChk")

        self._2.addWidget(self.enableAirPlayChk)

        self.verticalSpacer_5 = QSpacerItem(20, 40, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self._2.addItem(self.verticalSpacer_5)


        self.verticalLayout_10.addWidget(self.springboardOptionsPageContent)

        self.pages.addWidget(self.springboardOptionsPage)
        self.internalOptionsPage = QWidget()
        self.internalOptionsPage.setObjectName(u"internalOptionsPage")
        self.verticalLayout_141 = QVBoxLayout(self.internalOptionsPage)
        self.verticalLayout_141.setObjectName(u"verticalLayout_141")
        self.verticalLayout_141.setContentsMargins(0, 0, 0, 0)
        self.horizontalWidget_51 = QWidget(self.internalOptionsPage)
        self.horizontalWidget_51.setObjectName(u"horizontalWidget_51")
        self.horizontalLayout_201 = QHBoxLayout(self.horizontalWidget_51)
        self.horizontalLayout_201.setSpacing(10)
        self.horizontalLayout_201.setObjectName(u"horizontalLayout_201")
        self.horizontalLayout_201.setContentsMargins(0, 9, 0, 9)
        self.toolButton_101 = QToolButton(self.horizontalWidget_51)
        self.toolButton_101.setObjectName(u"toolButton_101")
        self.toolButton_101.setEnabled(False)
        self.toolButton_101.setStyleSheet(u"QToolButton {\n"
"	icon-size: 24px;\n"
"	background-color: transparent;\n"
"	padding-left: 0px;\n"
"	padding-right: 5px;\n"
"	border-radius: 0px;\n"
"}")
        self.toolButton_101.setIcon(icon8)

        self.horizontalLayout_201.addWidget(self.toolButton_101)

        self.verticalWidget_41 = QWidget(self.horizontalWidget_51)
        self.verticalWidget_41.setObjectName(u"verticalWidget_41")
        self.verticalLayout_121 = QVBoxLayout(self.verticalWidget_41)
        self.verticalLayout_121.setSpacing(6)
        self.verticalLayout_121.setObjectName(u"verticalLayout_121")
        self.verticalLayout_121.setContentsMargins(0, 0, 0, 0)
        self.internalOptionsLbl1 = QLabel(self.verticalWidget_41)
        self.internalOptionsLbl1.setObjectName(u"internalOptionsLbl1")
        self.internalOptionsLbl1.setFont(font1)

        self.verticalLayout_121.addWidget(self.internalOptionsLbl1)

        self.verticalSpacer_18 = QSpacerItem(20, 16, QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Minimum)

        self.verticalLayout_121.addItem(self.verticalSpacer_18)


        self.horizontalLayout_201.addWidget(self.verticalWidget_41)

        self.horizontalSpacer_71 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_201.addItem(self.horizontalSpacer_71)


        self.verticalLayout_141.addWidget(self.horizontalWidget_51)

        self.line_121 = QFrame(self.internalOptionsPage)
        self.line_121.setObjectName(u"line_121")
        self.line_121.setStyleSheet(u"QFrame {\n"
"	color: #414141;\n"
"}")
        self.line_121.setFrameShape(QFrame.Shape.VLine)
        self.line_121.setFrameShadow(QFrame.Shadow.Sunken)

        self.verticalLayout_141.addWidget(self.line_121)

        self.internalOptionsPageContent = QWidget(self.internalOptionsPage)
        self.internalOptionsPageContent.setObjectName(u"internalOptionsPageContent")
        self.internalOptionsPageContent.setEnabled(False)
        self.verticalLayout_131 = QVBoxLayout(self.internalOptionsPageContent)
        self.verticalLayout_131.setObjectName(u"verticalLayout_131")
        self.verticalLayout_131.setContentsMargins(0, 0, 0, 0)
        self.buildVersionChk = QCheckBox(self.internalOptionsPageContent)
        self.buildVersionChk.setObjectName(u"buildVersionChk")

        self.verticalLayout_131.addWidget(self.buildVersionChk)

        self.RTLChk = QCheckBox(self.internalOptionsPageContent)
        self.RTLChk.setObjectName(u"RTLChk")

        self.verticalLayout_131.addWidget(self.RTLChk)

        self.div1 = QFrame(self.internalOptionsPageContent)
        self.div1.setObjectName(u"div1")
        self.div1.setEnabled(False)
        self.div1.setStyleSheet(u"QFrame {\n"
"	color: #414141;\n"
"}")
        self.div1.setFrameShape(QFrame.Shape.VLine)
        self.div1.setFrameShadow(QFrame.Shadow.Sunken)

        self.verticalLayout_131.addWidget(self.div1)

        self.metalHUDChk = QCheckBox(self.internalOptionsPageContent)
        self.metalHUDChk.setObjectName(u"metalHUDChk")

        self.verticalLayout_131.addWidget(self.metalHUDChk)

        self.iMessageChk = QCheckBox(self.internalOptionsPageContent)
        self.iMessageChk.setObjectName(u"iMessageChk")

        self.verticalLayout_131.addWidget(self.iMessageChk)

        self.IDSChk = QCheckBox(self.internalOptionsPageContent)
        self.IDSChk.setObjectName(u"IDSChk")

        self.verticalLayout_131.addWidget(self.IDSChk)

        self.VCChk = QCheckBox(self.internalOptionsPageContent)
        self.VCChk.setObjectName(u"VCChk")

        self.verticalLayout_131.addWidget(self.VCChk)

        self.line_17 = QFrame(self.internalOptionsPageContent)
        self.line_17.setObjectName(u"line_17")
        self.line_17.setStyleSheet(u"QFrame {\n"
"	color: #414141;\n"
"}")
        self.line_17.setFrameShape(QFrame.Shape.VLine)
        self.line_17.setFrameShadow(QFrame.Shadow.Sunken)

        self.verticalLayout_131.addWidget(self.line_17)

        self.appStoreChk = QCheckBox(self.internalOptionsPageContent)
        self.appStoreChk.setObjectName(u"appStoreChk")

        self.verticalLayout_131.addWidget(self.appStoreChk)

        self.notesChk = QCheckBox(self.internalOptionsPageContent)
        self.notesChk.setObjectName(u"notesChk")

        self.verticalLayout_131.addWidget(self.notesChk)

        self.line_18 = QFrame(self.internalOptionsPageContent)
        self.line_18.setObjectName(u"line_18")
        self.line_18.setStyleSheet(u"QFrame {\n"
"	color: #414141;\n"
"}")
        self.line_18.setFrameShape(QFrame.Shape.VLine)
        self.line_18.setFrameShadow(QFrame.Shadow.Sunken)

        self.verticalLayout_131.addWidget(self.line_18)

        self.showTouchesChk = QCheckBox(self.internalOptionsPageContent)
        self.showTouchesChk.setObjectName(u"showTouchesChk")

        self.verticalLayout_131.addWidget(self.showTouchesChk)

        self.hideRespringChk = QCheckBox(self.internalOptionsPageContent)
        self.hideRespringChk.setObjectName(u"hideRespringChk")

        self.verticalLayout_131.addWidget(self.hideRespringChk)

        self.enableWakeVibrateChk = QCheckBox(self.internalOptionsPageContent)
        self.enableWakeVibrateChk.setObjectName(u"enableWakeVibrateChk")

        self.verticalLayout_131.addWidget(self.enableWakeVibrateChk)

        self.line_19 = QFrame(self.internalOptionsPageContent)
        self.line_19.setObjectName(u"line_19")
        self.line_19.setStyleSheet(u"QFrame {\n"
"	color: #414141;\n"
"}")
        self.line_19.setFrameShape(QFrame.Shape.VLine)
        self.line_19.setFrameShadow(QFrame.Shadow.Sunken)

        self.verticalLayout_131.addWidget(self.line_19)

        self.pasteSoundChk = QCheckBox(self.internalOptionsPageContent)
        self.pasteSoundChk.setObjectName(u"pasteSoundChk")

        self.verticalLayout_131.addWidget(self.pasteSoundChk)

        self.notifyPastesChk = QCheckBox(self.internalOptionsPageContent)
        self.notifyPastesChk.setObjectName(u"notifyPastesChk")

        self.verticalLayout_131.addWidget(self.notifyPastesChk)

        self.verticalSpacer_61 = QSpacerItem(20, 40, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.verticalLayout_131.addItem(self.verticalSpacer_61)


        self.verticalLayout_141.addWidget(self.internalOptionsPageContent)

        self.pages.addWidget(self.internalOptionsPage)
        self.advancedOptionsPage = QWidget()
        self.advancedOptionsPage.setObjectName(u"advancedOptionsPage")
        self.verticalLayout_142 = QVBoxLayout(self.advancedOptionsPage)
        self.verticalLayout_142.setObjectName(u"verticalLayout_142")
        self.verticalLayout_142.setContentsMargins(0, 0, 0, 0)
        self.horizontalWidget_52 = QWidget(self.advancedOptionsPage)
        self.horizontalWidget_52.setObjectName(u"horizontalWidget_52")
        self.horizontalLayout_202 = QHBoxLayout(self.horizontalWidget_52)
        self.horizontalLayout_202.setSpacing(10)
        self.horizontalLayout_202.setObjectName(u"horizontalLayout_202")
        self.horizontalLayout_202.setContentsMargins(0, 9, 0, 9)
        self.toolButton_102 = QToolButton(self.horizontalWidget_52)
        self.toolButton_102.setObjectName(u"toolButton_102")
        self.toolButton_102.setEnabled(False)
        self.toolButton_102.setStyleSheet(u"QToolButton {\n"
"	icon-size: 24px;\n"
"	background-color: transparent;\n"
"	padding-left: 0px;\n"
"	padding-right: 5px;\n"
"	border-radius: 0px;\n"
"}")
        self.toolButton_102.setIcon(icon9)

        self.horizontalLayout_202.addWidget(self.toolButton_102)

        self.verticalWidget_42 = QWidget(self.horizontalWidget_52)
        self.verticalWidget_42.setObjectName(u"verticalWidget_42")
        self.verticalLayout_122 = QVBoxLayout(self.verticalWidget_42)
        self.verticalLayout_122.setSpacing(6)
        self.verticalLayout_122.setObjectName(u"verticalLayout_122")
        self.verticalLayout_122.setContentsMargins(0, 0, 0, 0)
        self.advancedOptionsLbl = QLabel(self.verticalWidget_42)
        self.advancedOptionsLbl.setObjectName(u"advancedOptionsLbl")
        self.advancedOptionsLbl.setFont(font1)

        self.verticalLayout_122.addWidget(self.advancedOptionsLbl)

        self.verticalSpacer_181 = QSpacerItem(20, 16, QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Minimum)

        self.verticalLayout_122.addItem(self.verticalSpacer_181)


        self.horizontalLayout_202.addWidget(self.verticalWidget_42)

        self.horizontalSpacer_72 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_202.addItem(self.horizontalSpacer_72)


        self.verticalLayout_142.addWidget(self.horizontalWidget_52)

        self.line_122 = QFrame(self.advancedOptionsPage)
        self.line_122.setObjectName(u"line_122")
        self.line_122.setStyleSheet(u"QFrame {\n"
"	color: #414141;\n"
"}")
        self.line_122.setFrameShape(QFrame.Shape.VLine)
        self.line_122.setFrameShadow(QFrame.Shadow.Sunken)

        self.verticalLayout_142.addWidget(self.line_122)

        self.advancedOptionsPageContent = QWidget(self.advancedOptionsPage)
        self.advancedOptionsPageContent.setObjectName(u"advancedOptionsPageContent")
        self.advancedOptionsPageContent.setEnabled(True)
        self.verticalLayout_132 = QVBoxLayout(self.advancedOptionsPageContent)
        self.verticalLayout_132.setObjectName(u"verticalLayout_132")
        self.verticalLayout_132.setContentsMargins(0, 0, 0, 0)
        self.label_17 = QLabel(self.advancedOptionsPageContent)
        self.label_17.setObjectName(u"label_17")
        font3 = QFont()
        font3.setFamilies([u"\u5b8b\u4f53"])
        self.label_17.setFont(font3)

        self.verticalLayout_132.addWidget(self.label_17)

        self.line_191 = QFrame(self.advancedOptionsPageContent)
        self.line_191.setObjectName(u"line_191")
        self.line_191.setStyleSheet(u"QFrame {\n"
"	color: #414141;\n"
"}")
        self.line_191.setFrameShape(QFrame.Shape.VLine)
        self.line_191.setFrameShadow(QFrame.Shadow.Sunken)

        self.verticalLayout_132.addWidget(self.line_191)

        self.disableOTAChk = QCheckBox(self.advancedOptionsPageContent)
        self.disableOTAChk.setObjectName(u"disableOTAChk")

        self.verticalLayout_132.addWidget(self.disableOTAChk)

        self.line_181 = QFrame(self.advancedOptionsPageContent)
        self.line_181.setObjectName(u"line_181")
        self.line_181.setStyleSheet(u"QFrame {\n"
"	color: #414141;\n"
"}")
        self.line_181.setFrameShape(QFrame.Shape.VLine)
        self.line_181.setFrameShadow(QFrame.Shadow.Sunken)

        self.verticalLayout_132.addWidget(self.line_181)

        self.enableResolutionChk = QCheckBox(self.advancedOptionsPageContent)
        self.enableResolutionChk.setObjectName(u"enableResolutionChk")

        self.verticalLayout_132.addWidget(self.enableResolutionChk)

        self.resChangerContent = QWidget(self.advancedOptionsPageContent)
        self.resChangerContent.setObjectName(u"resChangerContent")
        self.resChangerContent.setEnabled(True)
        self.verticalLayout_35 = QVBoxLayout(self.resChangerContent)
        self.verticalLayout_35.setObjectName(u"verticalLayout_35")
        self.verticalLayout_35.setContentsMargins(0, 0, 0, 0)
        self.resHeightLbl = QLabel(self.resChangerContent)
        self.resHeightLbl.setObjectName(u"resHeightLbl")
        self.resHeightLbl.setEnabled(False)

        self.verticalLayout_35.addWidget(self.resHeightLbl)

        self.horizontalLayout_9 = QHBoxLayout()
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.horizontalLayout_9.setContentsMargins(-1, -1, -1, 5)
        self.resHeightTxt = QLineEdit(self.resChangerContent)
        self.resHeightTxt.setObjectName(u"resHeightTxt")
        self.resHeightTxt.setEnabled(True)

        self.horizontalLayout_9.addWidget(self.resHeightTxt)

        self.resHeightWarningLbl = QLabel(self.resChangerContent)
        self.resHeightWarningLbl.setObjectName(u"resHeightWarningLbl")
        self.resHeightWarningLbl.setMinimumSize(QSize(22, 0))
        self.resHeightWarningLbl.setStyleSheet(u"QLabel {\n"
"		border: 2px solid red;\n"
"		border-radius: 25px;\n"
"		color: red;\n"
"}")
        self.resHeightWarningLbl.setFrameShape(QFrame.NoFrame)
        self.resHeightWarningLbl.setScaledContents(False)

        self.horizontalLayout_9.addWidget(self.resHeightWarningLbl)


        self.verticalLayout_35.addLayout(self.horizontalLayout_9)

        self.resWidthLbl = QLabel(self.resChangerContent)
        self.resWidthLbl.setObjectName(u"resWidthLbl")

        self.verticalLayout_35.addWidget(self.resWidthLbl)

        self.resolutionContent = QVBoxLayout()
        self.resolutionContent.setObjectName(u"resolutionContent")
        self.resolutionContent.setContentsMargins(-1, -1, -1, 0)
        self.horizontalLayout_10 = QHBoxLayout()
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.horizontalLayout_10.setContentsMargins(-1, -1, -1, 5)
        self.resWidthTxt = QLineEdit(self.resChangerContent)
        self.resWidthTxt.setObjectName(u"resWidthTxt")

        self.horizontalLayout_10.addWidget(self.resWidthTxt)

        self.resWidthWarningLbl = QLabel(self.resChangerContent)
        self.resWidthWarningLbl.setObjectName(u"resWidthWarningLbl")
        self.resWidthWarningLbl.setMinimumSize(QSize(22, 0))
        self.resWidthWarningLbl.setStyleSheet(u"QLabel {\n"
"		border: 2px solid red;\n"
"		border-radius: 25px;\n"
"		color: red;\n"
"}")

        self.horizontalLayout_10.addWidget(self.resWidthWarningLbl)


        self.resolutionContent.addLayout(self.horizontalLayout_10)


        self.verticalLayout_35.addLayout(self.resolutionContent)


        self.verticalLayout_132.addWidget(self.resChangerContent)

        self.verticalSpacer_62 = QSpacerItem(20, 40, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.verticalLayout_132.addItem(self.verticalSpacer_62)


        self.verticalLayout_142.addWidget(self.advancedOptionsPageContent)

        self.pages.addWidget(self.advancedOptionsPage)
        self.applyPage = QWidget()
        self.applyPage.setObjectName(u"applyPage")
        self.verticalLayout_6 = QVBoxLayout(self.applyPage)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.verticalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.verticalWidget2 = QWidget(self.applyPage)
        self.verticalWidget2.setObjectName(u"verticalWidget2")
        self.verticalLayout_24 = QVBoxLayout(self.verticalWidget2)
        self.verticalLayout_24.setObjectName(u"verticalLayout_24")
        self.verticalLayout_24.setContentsMargins(0, 0, 0, 0)
        self.locSimPageHeader_2 = QWidget(self.verticalWidget2)
        self.locSimPageHeader_2.setObjectName(u"locSimPageHeader_2")
        self.horizontalLayout_33 = QHBoxLayout(self.locSimPageHeader_2)
        self.horizontalLayout_33.setSpacing(10)
        self.horizontalLayout_33.setObjectName(u"horizontalLayout_33")
        self.horizontalLayout_33.setContentsMargins(0, -1, 0, -1)
        self.toolButton_18 = QToolButton(self.locSimPageHeader_2)
        self.toolButton_18.setObjectName(u"toolButton_18")
        self.toolButton_18.setEnabled(False)
        self.toolButton_18.setStyleSheet(u"QToolButton {\n"
"	icon-size: 24px;\n"
"	background-color: transparent;\n"
"	padding-left: 0px;\n"
"	padding-right: 5px;\n"
"	border-radius: 0px;\n"
"}")
        self.toolButton_18.setIcon(icon10)

        self.horizontalLayout_33.addWidget(self.toolButton_18)

        self.verticalWidget_11 = QWidget(self.locSimPageHeader_2)
        self.verticalWidget_11.setObjectName(u"verticalWidget_11")
        self.verticalLayout_33 = QVBoxLayout(self.verticalWidget_11)
        self.verticalLayout_33.setSpacing(6)
        self.verticalLayout_33.setObjectName(u"verticalLayout_33")
        self.verticalLayout_33.setContentsMargins(0, 0, 0, 0)
        self.statusBarLbl_5 = QLabel(self.verticalWidget_11)
        self.statusBarLbl_5.setObjectName(u"statusBarLbl_5")
        self.statusBarLbl_5.setFont(font1)

        self.verticalLayout_33.addWidget(self.statusBarLbl_5)

        self.label_16 = QLabel(self.verticalWidget_11)
        self.label_16.setObjectName(u"label_16")

        self.verticalLayout_33.addWidget(self.label_16)


        self.horizontalLayout_33.addWidget(self.verticalWidget_11)

        self.horizontalSpacer_15 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_33.addItem(self.horizontalSpacer_15)


        self.verticalLayout_24.addWidget(self.locSimPageHeader_2)

        self.line_5 = QFrame(self.verticalWidget2)
        self.line_5.setObjectName(u"line_5")
        self.line_5.setStyleSheet(u"QFrame {\n"
"	color: #414141;\n"
"}")
        self.line_5.setFrameShape(QFrame.Shape.VLine)
        self.line_5.setFrameShadow(QFrame.Shadow.Sunken)

        self.verticalLayout_24.addWidget(self.line_5)

        self.verticalSpacer_10 = QSpacerItem(20, 40, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.verticalLayout_24.addItem(self.verticalSpacer_10)

        self.modifiedTweaksLbl = QLabel(self.verticalWidget2)
        self.modifiedTweaksLbl.setObjectName(u"modifiedTweaksLbl")

        self.verticalLayout_24.addWidget(self.modifiedTweaksLbl)

        self.gestaltLocationLbl = QLabel(self.verticalWidget2)
        self.gestaltLocationLbl.setObjectName(u"gestaltLocationLbl")

        self.verticalLayout_24.addWidget(self.gestaltLocationLbl)

        self.horizontalLayout_7 = QHBoxLayout()
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.horizontalLayout_7.setContentsMargins(-1, 10, -1, 0)
        self.chooseGestaltBtn = QToolButton(self.verticalWidget2)
        self.chooseGestaltBtn.setObjectName(u"chooseGestaltBtn")
        icon19 = QIcon()
        icon19.addFile(u":/icon/folder.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.chooseGestaltBtn.setIcon(icon19)
        self.chooseGestaltBtn.setToolButtonStyle(Qt.ToolButtonIconOnly)

        self.horizontalLayout_7.addWidget(self.chooseGestaltBtn)


        self.verticalLayout_24.addLayout(self.horizontalLayout_7)

        self.horizontalWidget4 = QWidget(self.verticalWidget2)
        self.horizontalWidget4.setObjectName(u"horizontalWidget4")
        self.horizontalLayout_17 = QHBoxLayout(self.horizontalWidget4)
        self.horizontalLayout_17.setObjectName(u"horizontalLayout_17")
        self.horizontalLayout_17.setContentsMargins(0, 0, 0, 0)
        self.applyTweaksBtn = QToolButton(self.horizontalWidget4)
        self.applyTweaksBtn.setObjectName(u"applyTweaksBtn")
        self.applyTweaksBtn.setIcon(icon10)
        self.applyTweaksBtn.setToolButtonStyle(Qt.ToolButtonIconOnly)

        self.horizontalLayout_17.addWidget(self.applyTweaksBtn)


        self.verticalLayout_24.addWidget(self.horizontalWidget4)

        self.statusLbl = QLabel(self.verticalWidget2)
        self.statusLbl.setObjectName(u"statusLbl")

        self.verticalLayout_24.addWidget(self.statusLbl)

        self.restoreProgressBar = QProgressBar(self.verticalWidget2)
        self.restoreProgressBar.setObjectName(u"restoreProgressBar")
        sizePolicy.setHeightForWidth(self.restoreProgressBar.sizePolicy().hasHeightForWidth())
        self.restoreProgressBar.setSizePolicy(sizePolicy)
        self.restoreProgressBar.setMinimumSize(QSize(150, 0))
        self.restoreProgressBar.setValue(0)

        self.verticalLayout_24.addWidget(self.restoreProgressBar)

        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.verticalLayout_24.addItem(self.verticalSpacer_2)

        self.horizontalWidget5 = QWidget(self.verticalWidget2)
        self.horizontalWidget5.setObjectName(u"horizontalWidget5")
        self.horizontalLayout_25 = QHBoxLayout(self.horizontalWidget5)
        self.horizontalLayout_25.setObjectName(u"horizontalLayout_25")
        self.horizontalLayout_25.setContentsMargins(0, 0, 0, 0)
        self.horizontalSpacer_14 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_25.addItem(self.horizontalSpacer_14)

        self.removeTweaksBtn = QToolButton(self.horizontalWidget5)
        self.removeTweaksBtn.setObjectName(u"removeTweaksBtn")

        self.horizontalLayout_25.addWidget(self.removeTweaksBtn)

        self.resetGestaltBtn = QToolButton(self.horizontalWidget5)
        self.resetGestaltBtn.setObjectName(u"resetGestaltBtn")

        self.horizontalLayout_25.addWidget(self.resetGestaltBtn)

        self.horizontalSpacer_16 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_25.addItem(self.horizontalSpacer_16)


        self.verticalLayout_24.addWidget(self.horizontalWidget5)


        self.verticalLayout_6.addWidget(self.verticalWidget2)

        self.pages.addWidget(self.applyPage)
        self.settingsPage = QWidget()
        self.settingsPage.setObjectName(u"settingsPage")
        self.verticalLayout_101 = QVBoxLayout(self.settingsPage)
        self.verticalLayout_101.setObjectName(u"verticalLayout_101")
        self.verticalLayout_101.setContentsMargins(0, 0, 0, 0)
        self.horizontalWidget_41 = QWidget(self.settingsPage)
        self.horizontalWidget_41.setObjectName(u"horizontalWidget_41")
        self.horizontalLayout_131 = QHBoxLayout(self.horizontalWidget_41)
        self.horizontalLayout_131.setSpacing(10)
        self.horizontalLayout_131.setObjectName(u"horizontalLayout_131")
        self.horizontalLayout_131.setContentsMargins(0, 9, 0, 9)
        self.toolButton_71 = QToolButton(self.horizontalWidget_41)
        self.toolButton_71.setObjectName(u"toolButton_71")
        self.toolButton_71.setEnabled(False)
        self.toolButton_71.setStyleSheet(u"QToolButton {\n"
"	icon-size: 24px;\n"
"	background-color: transparent;\n"
"	padding-left: 0px;\n"
"	padding-right: 5px;\n"
"	border-radius: 0px;\n"
"}")
        self.toolButton_71.setIcon(icon11)

        self.horizontalLayout_131.addWidget(self.toolButton_71)

        self.verticalWidget_31 = QWidget(self.horizontalWidget_41)
        self.verticalWidget_31.setObjectName(u"verticalWidget_31")
        self.verticalLayout_71 = QVBoxLayout(self.verticalWidget_31)
        self.verticalLayout_71.setSpacing(6)
        self.verticalLayout_71.setObjectName(u"verticalLayout_71")
        self.verticalLayout_71.setContentsMargins(0, 0, 0, 0)
        self.springboardOptionsLbl1 = QLabel(self.verticalWidget_31)
        self.springboardOptionsLbl1.setObjectName(u"springboardOptionsLbl1")
        self.springboardOptionsLbl1.setFont(font1)

        self.verticalLayout_71.addWidget(self.springboardOptionsLbl1)

        self.verticalSpacer_17 = QSpacerItem(20, 16, QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Minimum)

        self.verticalLayout_71.addItem(self.verticalSpacer_17)


        self.horizontalLayout_131.addWidget(self.verticalWidget_31)

        self.horizontalSpacer_61 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_131.addItem(self.horizontalSpacer_61)


        self.verticalLayout_101.addWidget(self.horizontalWidget_41)

        self.line_111 = QFrame(self.settingsPage)
        self.line_111.setObjectName(u"line_111")
        self.line_111.setStyleSheet(u"QFrame {\n"
"	color: #414141;\n"
"}")
        self.line_111.setFrameShape(QFrame.Shape.VLine)
        self.line_111.setFrameShadow(QFrame.Shadow.Sunken)

        self.verticalLayout_101.addWidget(self.line_111)

        self.settingsPageContent = QWidget(self.settingsPage)
        self.settingsPageContent.setObjectName(u"settingsPageContent")
        self.settingsPageContent.setEnabled(True)
        self.settingsPageContent.setMaximumSize(QSize(650, 16777215))
        self._21 = QVBoxLayout(self.settingsPageContent)
        self._21.setObjectName(u"_21")
        self._21.setContentsMargins(0, 0, 0, 0)
        self.allowWifiApplyingChk = QCheckBox(self.settingsPageContent)
        self.allowWifiApplyingChk.setObjectName(u"allowWifiApplyingChk")
        self.allowWifiApplyingChk.setChecked(True)

        self._21.addWidget(self.allowWifiApplyingChk)

        self.autoRebootChk = QCheckBox(self.settingsPageContent)
        self.autoRebootChk.setObjectName(u"autoRebootChk")
        self.autoRebootChk.setChecked(True)

        self._21.addWidget(self.autoRebootChk)

        self.showRiskyChk = QCheckBox(self.settingsPageContent)
        self.showRiskyChk.setObjectName(u"showRiskyChk")

        self._21.addWidget(self.showRiskyChk)

        self.line_24 = QFrame(self.settingsPageContent)
        self.line_24.setObjectName(u"line_24")
        self.line_24.setStyleSheet(u"QFrame {\n"
"	color: #414141;\n"
"}")
        self.line_24.setFrameShape(QFrame.Shape.VLine)
        self.line_24.setFrameShadow(QFrame.Shadow.Sunken)

        self._21.addWidget(self.line_24)

        self.skipSetupChk = QCheckBox(self.settingsPageContent)
        self.skipSetupChk.setObjectName(u"skipSetupChk")
        self.skipSetupChk.setChecked(True)

        self._21.addWidget(self.skipSetupChk)

        self.supervisionChk = QCheckBox(self.settingsPageContent)
        self.supervisionChk.setObjectName(u"supervisionChk")
        self.supervisionChk.setEnabled(True)
        self.supervisionChk.setChecked(False)

        self._21.addWidget(self.supervisionChk)

        self.supervisionOrganization = QLineEdit(self.settingsPageContent)
        self.supervisionOrganization.setObjectName(u"supervisionOrganization")

        self._21.addWidget(self.supervisionOrganization)

        self.verticalSpacer_21 = QSpacerItem(20, 10, QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Minimum)

        self._21.addItem(self.verticalSpacer_21)

        self.label_15 = QLabel(self.settingsPageContent)
        self.label_15.setObjectName(u"label_15")

        self._21.addWidget(self.label_15)

        self.line_20 = QFrame(self.settingsPageContent)
        self.line_20.setObjectName(u"line_20")
        self.line_20.setStyleSheet(u"QFrame {\n"
"	color: #414141;\n"
"}")
        self.line_20.setFrameShape(QFrame.Shape.VLine)
        self.line_20.setFrameShadow(QFrame.Shadow.Sunken)

        self._21.addWidget(self.line_20)

        self.deviceSettingsBtns = QHBoxLayout()
        self.deviceSettingsBtns.setObjectName(u"deviceSettingsBtns")
        self.deviceSettingsBtns.setContentsMargins(-1, -1, -1, 0)
        self.resetPairBtn = QToolButton(self.settingsPageContent)
        self.resetPairBtn.setObjectName(u"resetPairBtn")

        self.deviceSettingsBtns.addWidget(self.resetPairBtn)


        self._21.addLayout(self.deviceSettingsBtns)

        self.verticalSpacer_51 = QSpacerItem(20, 40, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self._21.addItem(self.verticalSpacer_51)


        self.verticalLayout_101.addWidget(self.settingsPageContent)

        self.pages.addWidget(self.settingsPage)
        self.locSimPage = QWidget()
        self.locSimPage.setObjectName(u"locSimPage")
        self.verticalLayout_28 = QVBoxLayout(self.locSimPage)
        self.verticalLayout_28.setObjectName(u"verticalLayout_28")
        self.verticalLayout_28.setContentsMargins(0, 0, 0, 0)
        self.locSimPageHeader = QWidget(self.locSimPage)
        self.locSimPageHeader.setObjectName(u"locSimPageHeader")
        self.horizontalLayout_28 = QHBoxLayout(self.locSimPageHeader)
        self.horizontalLayout_28.setSpacing(10)
        self.horizontalLayout_28.setObjectName(u"horizontalLayout_28")
        self.horizontalLayout_28.setContentsMargins(0, -1, 0, -1)
        self.toolButton_13 = QToolButton(self.locSimPageHeader)
        self.toolButton_13.setObjectName(u"toolButton_13")
        self.toolButton_13.setEnabled(False)
        self.toolButton_13.setStyleSheet(u"QToolButton {\n"
"	icon-size: 24px;\n"
"	background-color: transparent;\n"
"	padding-left: 0px;\n"
"	padding-right: 5px;\n"
"	border-radius: 0px;\n"
"}")
        self.toolButton_13.setIcon(icon6)

        self.horizontalLayout_28.addWidget(self.toolButton_13)

        self.verticalWidget_8 = QWidget(self.locSimPageHeader)
        self.verticalWidget_8.setObjectName(u"verticalWidget_8")
        self.verticalLayout_27 = QVBoxLayout(self.verticalWidget_8)
        self.verticalLayout_27.setSpacing(6)
        self.verticalLayout_27.setObjectName(u"verticalLayout_27")
        self.verticalLayout_27.setContentsMargins(0, 0, 0, 0)
        self.statusBarLbl_2 = QLabel(self.verticalWidget_8)
        self.statusBarLbl_2.setObjectName(u"statusBarLbl_2")
        self.statusBarLbl_2.setFont(font1)

        self.verticalLayout_27.addWidget(self.statusBarLbl_2)

        self.label_4 = QLabel(self.verticalWidget_8)
        self.label_4.setObjectName(u"label_4")

        self.verticalLayout_27.addWidget(self.label_4)


        self.horizontalLayout_28.addWidget(self.verticalWidget_8)

        self.horizontalSpacer_11 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_28.addItem(self.horizontalSpacer_11)

        self.loadLocSimBtn = QToolButton(self.locSimPageHeader)
        self.loadLocSimBtn.setObjectName(u"loadLocSimBtn")

        self.horizontalLayout_28.addWidget(self.loadLocSimBtn)


        self.verticalLayout_28.addWidget(self.locSimPageHeader)

        self.line_2 = QFrame(self.locSimPage)
        self.line_2.setObjectName(u"line_2")
        self.line_2.setStyleSheet(u"QFrame {\n"
"	color: #414141;\n"
"}")
        self.line_2.setFrameShape(QFrame.Shape.VLine)
        self.line_2.setFrameShadow(QFrame.Shadow.Sunken)

        self.verticalLayout_28.addWidget(self.line_2)

        self.verticalSpacer_14 = QSpacerItem(20, 40, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.verticalLayout_28.addItem(self.verticalSpacer_14)

        self.locSimCnt = QWidget(self.locSimPage)
        self.locSimCnt.setObjectName(u"locSimCnt")
        self.locSimPageContent = QVBoxLayout(self.locSimCnt)
        self.locSimPageContent.setObjectName(u"locSimPageContent")
        self.locSimPageContent.setContentsMargins(0, 0, 0, 0)
        self.verticalWidget3 = QWidget(self.locSimCnt)
        self.verticalWidget3.setObjectName(u"verticalWidget3")
        self.verticalLayout_29 = QVBoxLayout(self.verticalWidget3)
        self.verticalLayout_29.setObjectName(u"verticalLayout_29")
        self.verticalLayout_29.setContentsMargins(0, 0, 0, 0)
        self.label_7 = QLabel(self.verticalWidget3)
        self.label_7.setObjectName(u"label_7")

        self.verticalLayout_29.addWidget(self.label_7)

        self.latitudeTxt = QLineEdit(self.verticalWidget3)
        self.latitudeTxt.setObjectName(u"latitudeTxt")

        self.verticalLayout_29.addWidget(self.latitudeTxt)

        self.label_11 = QLabel(self.verticalWidget3)
        self.label_11.setObjectName(u"label_11")

        self.verticalLayout_29.addWidget(self.label_11)

        self.longitudeTxt = QLineEdit(self.verticalWidget3)
        self.longitudeTxt.setObjectName(u"longitudeTxt")

        self.verticalLayout_29.addWidget(self.longitudeTxt)

        self.horizontalWidget6 = QWidget(self.verticalWidget3)
        self.horizontalWidget6.setObjectName(u"horizontalWidget6")
        self.horizontalLayout_3 = QHBoxLayout(self.horizontalWidget6)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.setLocationBtn = QToolButton(self.horizontalWidget6)
        self.setLocationBtn.setObjectName(u"setLocationBtn")

        self.horizontalLayout_3.addWidget(self.setLocationBtn)


        self.verticalLayout_29.addWidget(self.horizontalWidget6)

        self.horizontalWidget_22 = QWidget(self.verticalWidget3)
        self.horizontalWidget_22.setObjectName(u"horizontalWidget_22")
        self.horizontalLayout_29 = QHBoxLayout(self.horizontalWidget_22)
        self.horizontalLayout_29.setObjectName(u"horizontalLayout_29")
        self.horizontalLayout_29.setContentsMargins(0, 0, 0, 0)
        self.resetLocationBtn = QToolButton(self.horizontalWidget_22)
        self.resetLocationBtn.setObjectName(u"resetLocationBtn")

        self.horizontalLayout_29.addWidget(self.resetLocationBtn)


        self.verticalLayout_29.addWidget(self.horizontalWidget_22)


        self.locSimPageContent.addWidget(self.verticalWidget3)


        self.verticalLayout_28.addWidget(self.locSimCnt)

        self.verticalSpacer_13 = QSpacerItem(20, 40, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.verticalLayout_28.addItem(self.verticalSpacer_13)

        self.pages.addWidget(self.locSimPage)
        self.customOperationsPage = QWidget()
        self.customOperationsPage.setObjectName(u"customOperationsPage")
        self.verticalLayout_20 = QVBoxLayout(self.customOperationsPage)
        self.verticalLayout_20.setObjectName(u"verticalLayout_20")
        self.verticalLayout_20.setContentsMargins(0, 0, 0, 0)
        self.horizontalWidget_7 = QWidget(self.customOperationsPage)
        self.horizontalWidget_7.setObjectName(u"horizontalWidget_7")
        self.horizontalLayout_22 = QHBoxLayout(self.horizontalWidget_7)
        self.horizontalLayout_22.setSpacing(10)
        self.horizontalLayout_22.setObjectName(u"horizontalLayout_22")
        self.horizontalLayout_22.setContentsMargins(0, 9, 0, 9)
        self.toolButton_12 = QToolButton(self.horizontalWidget_7)
        self.toolButton_12.setObjectName(u"toolButton_12")
        self.toolButton_12.setEnabled(False)
        self.toolButton_12.setStyleSheet(u"QToolButton {\n"
"	icon-size: 24px;\n"
"	background-color: transparent;\n"
"	padding-left: 0px;\n"
"	padding-right: 5px;\n"
"	border-radius: 0px;\n"
"}")
        icon20 = QIcon()
        icon20.addFile(u":/icon/pencil.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.toolButton_12.setIcon(icon20)
        self.toolButton_12.setIconSize(QSize(25, 25))

        self.horizontalLayout_22.addWidget(self.toolButton_12)

        self.verticalWidget_6 = QWidget(self.horizontalWidget_7)
        self.verticalWidget_6.setObjectName(u"verticalWidget_6")
        self.verticalLayout_18 = QVBoxLayout(self.verticalWidget_6)
        self.verticalLayout_18.setSpacing(6)
        self.verticalLayout_18.setObjectName(u"verticalLayout_18")
        self.verticalLayout_18.setContentsMargins(0, 0, 0, 0)
        self.customOperationsLbl = QLabel(self.verticalWidget_6)
        self.customOperationsLbl.setObjectName(u"customOperationsLbl")
        self.customOperationsLbl.setFont(font1)

        self.verticalLayout_18.addWidget(self.customOperationsLbl)

        self.label_14 = QLabel(self.verticalWidget_6)
        self.label_14.setObjectName(u"label_14")

        self.verticalLayout_18.addWidget(self.label_14)


        self.horizontalLayout_22.addWidget(self.verticalWidget_6)

        self.horizontalSpacer_9 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_22.addItem(self.horizontalSpacer_9)


        self.verticalLayout_20.addWidget(self.horizontalWidget_7)

        self.line_14 = QFrame(self.customOperationsPage)
        self.line_14.setObjectName(u"line_14")
        self.line_14.setStyleSheet(u"QFrame {\n"
"	color: #414141;\n"
"}")
        self.line_14.setFrameShape(QFrame.Shape.VLine)
        self.line_14.setFrameShadow(QFrame.Shadow.Sunken)

        self.verticalLayout_20.addWidget(self.line_14)

        self.customOperationsPageContent = QWidget(self.customOperationsPage)
        self.customOperationsPageContent.setObjectName(u"customOperationsPageContent")
        self.customOperationsPageContent.setEnabled(True)
        self.verticalLayout_19 = QVBoxLayout(self.customOperationsPageContent)
        self.verticalLayout_19.setObjectName(u"verticalLayout_19")
        self.verticalLayout_19.setContentsMargins(0, 0, 0, 0)
        self.customOpsTopBtns = QHBoxLayout()
        self.customOpsTopBtns.setSpacing(6)
        self.customOpsTopBtns.setObjectName(u"customOpsTopBtns")
        self.customOpsTopBtns.setContentsMargins(-1, -1, -1, 0)
        self.horizontalSpacer_17 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.customOpsTopBtns.addItem(self.horizontalSpacer_17)

        self.importOperationBtn = QToolButton(self.customOperationsPageContent)
        self.importOperationBtn.setObjectName(u"importOperationBtn")
        self.importOperationBtn.setEnabled(True)
        icon21 = QIcon()
        icon21.addFile(u":/icon/import.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.importOperationBtn.setIcon(icon21)
        self.importOperationBtn.setIconSize(QSize(20, 20))
        self.importOperationBtn.setToolButtonStyle(Qt.ToolButtonIconOnly)

        self.customOpsTopBtns.addWidget(self.importOperationBtn)

        self.newOperationBtn = QToolButton(self.customOperationsPageContent)
        self.newOperationBtn.setObjectName(u"newOperationBtn")
        self.newOperationBtn.setEnabled(True)
        sizePolicy2.setHeightForWidth(self.newOperationBtn.sizePolicy().hasHeightForWidth())
        self.newOperationBtn.setSizePolicy(sizePolicy2)
        self.newOperationBtn.setMinimumSize(QSize(0, 35))
        self.newOperationBtn.setIcon(icon18)
        self.newOperationBtn.setIconSize(QSize(16, 16))
        self.newOperationBtn.setCheckable(False)
        self.newOperationBtn.setAutoExclusive(True)
        self.newOperationBtn.setToolButtonStyle(Qt.ToolButtonIconOnly)

        self.customOpsTopBtns.addWidget(self.newOperationBtn)


        self.verticalLayout_19.addLayout(self.customOpsTopBtns)

        self.operationsCnt = QWidget(self.customOperationsPageContent)
        self.operationsCnt.setObjectName(u"operationsCnt")
        self.operationsCnt.setEnabled(True)
        sizePolicy5 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        sizePolicy5.setHorizontalStretch(0)
        sizePolicy5.setVerticalStretch(0)
        sizePolicy5.setHeightForWidth(self.operationsCnt.sizePolicy().hasHeightForWidth())
        self.operationsCnt.setSizePolicy(sizePolicy5)

        self.verticalLayout_19.addWidget(self.operationsCnt)


        self.verticalLayout_20.addWidget(self.customOperationsPageContent)

        self.pages.addWidget(self.customOperationsPage)
        self.explorePage = QWidget()
        self.explorePage.setObjectName(u"explorePage")
        self.verticalLayout_31 = QVBoxLayout(self.explorePage)
        self.verticalLayout_31.setObjectName(u"verticalLayout_31")
        self.verticalLayout_31.setContentsMargins(0, 0, 0, 0)
        self.explorePageHeader = QWidget(self.explorePage)
        self.explorePageHeader.setObjectName(u"explorePageHeader")
        self.horizontalLayout_31 = QHBoxLayout(self.explorePageHeader)
        self.horizontalLayout_31.setSpacing(10)
        self.horizontalLayout_31.setObjectName(u"horizontalLayout_31")
        self.horizontalLayout_31.setContentsMargins(0, -1, 0, -1)
        self.toolButton_16 = QToolButton(self.explorePageHeader)
        self.toolButton_16.setObjectName(u"toolButton_16")
        self.toolButton_16.setEnabled(False)
        self.toolButton_16.setStyleSheet(u"QToolButton {\n"
"	icon-size: 24px;\n"
"	background-color: transparent;\n"
"	padding-left: 0px;\n"
"	padding-right: 5px;\n"
"	border-radius: 0px;\n"
"}")
        self.toolButton_16.setIcon(icon3)

        self.horizontalLayout_31.addWidget(self.toolButton_16)

        self.verticalWidget_9 = QWidget(self.explorePageHeader)
        self.verticalWidget_9.setObjectName(u"verticalWidget_9")
        self.verticalLayout_30 = QVBoxLayout(self.verticalWidget_9)
        self.verticalLayout_30.setSpacing(6)
        self.verticalLayout_30.setObjectName(u"verticalLayout_30")
        self.verticalLayout_30.setContentsMargins(0, 0, 0, 0)
        self.exploreLbl = QLabel(self.verticalWidget_9)
        self.exploreLbl.setObjectName(u"exploreLbl")
        self.exploreLbl.setFont(font1)

        self.verticalLayout_30.addWidget(self.exploreLbl)

        self.exploreSubLbl = QLabel(self.verticalWidget_9)
        self.exploreSubLbl.setObjectName(u"exploreSubLbl")

        self.verticalLayout_30.addWidget(self.exploreSubLbl)


        self.horizontalLayout_31.addWidget(self.verticalWidget_9)

        self.horizontalSpacer_13 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_31.addItem(self.horizontalSpacer_13)


        self.verticalLayout_31.addWidget(self.explorePageHeader)

        self.line_3 = QFrame(self.explorePage)
        self.line_3.setObjectName(u"line_3")
        self.line_3.setStyleSheet(u"QFrame {\n"
"	color: #414141;\n"
"}")
        self.line_3.setFrameShape(QFrame.Shape.VLine)
        self.line_3.setFrameShadow(QFrame.Shadow.Sunken)

        self.verticalLayout_31.addWidget(self.line_3)

        self.exploreThemesCnt = QWidget(self.explorePage)
        self.exploreThemesCnt.setObjectName(u"exploreThemesCnt")
        sizePolicy5.setHeightForWidth(self.exploreThemesCnt.sizePolicy().hasHeightForWidth())
        self.exploreThemesCnt.setSizePolicy(sizePolicy5)

        self.verticalLayout_31.addWidget(self.exploreThemesCnt)

        self.pages.addWidget(self.explorePage)
        self.themingPage = QWidget()
        self.themingPage.setObjectName(u"themingPage")
        self.verticalLayout_23 = QVBoxLayout(self.themingPage)
        self.verticalLayout_23.setObjectName(u"verticalLayout_23")
        self.verticalLayout_23.setContentsMargins(0, 0, 0, 0)
        self.horizontalWidget_8 = QWidget(self.themingPage)
        self.horizontalWidget_8.setObjectName(u"horizontalWidget_8")
        self.horizontalLayout_23 = QHBoxLayout(self.horizontalWidget_8)
        self.horizontalLayout_23.setSpacing(10)
        self.horizontalLayout_23.setObjectName(u"horizontalLayout_23")
        self.horizontalLayout_23.setContentsMargins(0, 9, 0, 9)
        self.themesBtn = QToolButton(self.horizontalWidget_8)
        self.themesBtn.setObjectName(u"themesBtn")
        self.themesBtn.setEnabled(True)
        self.themesBtn.setStyleSheet(u"QToolButton {\n"
"	icon-size: 24px;\n"
"	background-color: transparent;\n"
"	padding-left: 0px;\n"
"	padding-right: 5px;\n"
"	border-radius: 0px;\n"
"}")
        self.themesBtn.setIcon(icon4)
        self.themesBtn.setIconSize(QSize(30, 30))

        self.horizontalLayout_23.addWidget(self.themesBtn)

        self.verticalWidget_7 = QWidget(self.horizontalWidget_8)
        self.verticalWidget_7.setObjectName(u"verticalWidget_7")
        self.verticalLayout_21 = QVBoxLayout(self.verticalWidget_7)
        self.verticalLayout_21.setSpacing(6)
        self.verticalLayout_21.setObjectName(u"verticalLayout_21")
        self.verticalLayout_21.setContentsMargins(0, 0, 0, 0)
        self.themesLbl = QLabel(self.verticalWidget_7)
        self.themesLbl.setObjectName(u"themesLbl")
        self.themesLbl.setFont(font1)

        self.verticalLayout_21.addWidget(self.themesLbl)


        self.horizontalLayout_23.addWidget(self.verticalWidget_7)

        self.horizontalSpacer_10 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_23.addItem(self.horizontalSpacer_10)

        self.horizontalWidget7 = QWidget(self.horizontalWidget_8)
        self.horizontalWidget7.setObjectName(u"horizontalWidget7")
        self.horizontalLayout_26 = QHBoxLayout(self.horizontalWidget7)
        self.horizontalLayout_26.setObjectName(u"horizontalLayout_26")
        self.horizontalLayout_26.setContentsMargins(0, 0, 0, 0)
        self.importThemeBtn = QToolButton(self.horizontalWidget7)
        self.importThemeBtn.setObjectName(u"importThemeBtn")
        self.importThemeBtn.setEnabled(False)
        self.importThemeBtn.setStyleSheet(u"QToolButton {\n"
"	background: none;\n"
"}")

        self.horizontalLayout_26.addWidget(self.importThemeBtn)

        self.importThemeFolderBtn = QToolButton(self.horizontalWidget7)
        self.importThemeFolderBtn.setObjectName(u"importThemeFolderBtn")
        self.importThemeFolderBtn.setIcon(icon19)

        self.horizontalLayout_26.addWidget(self.importThemeFolderBtn)

        self.importThemeZipBtn = QToolButton(self.horizontalWidget7)
        self.importThemeZipBtn.setObjectName(u"importThemeZipBtn")
        icon22 = QIcon()
        icon22.addFile(u":/icon/file-earmark-zip.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.importThemeZipBtn.setIcon(icon22)

        self.horizontalLayout_26.addWidget(self.importThemeZipBtn)


        self.horizontalLayout_23.addWidget(self.horizontalWidget7)


        self.verticalLayout_23.addWidget(self.horizontalWidget_8)

        self.line_15 = QFrame(self.themingPage)
        self.line_15.setObjectName(u"line_15")
        self.line_15.setStyleSheet(u"QFrame {\n"
"	color: #414141;\n"
"}")
        self.line_15.setFrameShape(QFrame.Shape.VLine)
        self.line_15.setFrameShadow(QFrame.Shadow.Sunken)

        self.verticalLayout_23.addWidget(self.line_15)

        self.themesPageContent = QWidget(self.themingPage)
        self.themesPageContent.setObjectName(u"themesPageContent")
        self.themesPageContent.setEnabled(False)
        self.verticalLayout_22 = QVBoxLayout(self.themesPageContent)
        self.verticalLayout_22.setObjectName(u"verticalLayout_22")
        self.verticalLayout_22.setContentsMargins(0, 0, 0, 0)
        self.themesCnt = QWidget(self.themesPageContent)
        self.themesCnt.setObjectName(u"themesCnt")

        self.verticalLayout_22.addWidget(self.themesCnt)

        self.line = QFrame(self.themesPageContent)
        self.line.setObjectName(u"line")
        self.line.setStyleSheet(u"QFrame {\n"
"	color: #414141;\n"
"}")
        self.line.setFrameShape(QFrame.Shape.VLine)
        self.line.setFrameShadow(QFrame.Shadow.Sunken)

        self.verticalLayout_22.addWidget(self.line)

        self.label_3 = QLabel(self.themesPageContent)
        self.label_3.setObjectName(u"label_3")

        self.verticalLayout_22.addWidget(self.label_3)

        self.iconsCnt = QWidget(self.themesPageContent)
        self.iconsCnt.setObjectName(u"iconsCnt")

        self.verticalLayout_22.addWidget(self.iconsCnt)

        self.verticalSpacer_9 = QSpacerItem(20, 40, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.verticalLayout_22.addItem(self.verticalSpacer_9)

        self.horizontalWidget8 = QWidget(self.themesPageContent)
        self.horizontalWidget8.setObjectName(u"horizontalWidget8")
        self.horizontalLayout_16 = QHBoxLayout(self.horizontalWidget8)
        self.horizontalLayout_16.setObjectName(u"horizontalLayout_16")
        self.horizontalLayout_16.setContentsMargins(0, 0, 0, 0)
        self.hideNamesBtn = QToolButton(self.horizontalWidget8)
        self.hideNamesBtn.setObjectName(u"hideNamesBtn")
        sizePolicy2.setHeightForWidth(self.hideNamesBtn.sizePolicy().hasHeightForWidth())
        self.hideNamesBtn.setSizePolicy(sizePolicy2)

        self.horizontalLayout_16.addWidget(self.hideNamesBtn)

        self.borderAllBtn = QToolButton(self.horizontalWidget8)
        self.borderAllBtn.setObjectName(u"borderAllBtn")
        sizePolicy2.setHeightForWidth(self.borderAllBtn.sizePolicy().hasHeightForWidth())
        self.borderAllBtn.setSizePolicy(sizePolicy2)

        self.horizontalLayout_16.addWidget(self.borderAllBtn)

        self.addAllBtn = QToolButton(self.horizontalWidget8)
        self.addAllBtn.setObjectName(u"addAllBtn")
        sizePolicy2.setHeightForWidth(self.addAllBtn.sizePolicy().hasHeightForWidth())
        self.addAllBtn.setSizePolicy(sizePolicy2)

        self.horizontalLayout_16.addWidget(self.addAllBtn)


        self.verticalLayout_22.addWidget(self.horizontalWidget8)


        self.verticalLayout_23.addWidget(self.themesPageContent)

        self.pages.addWidget(self.themingPage)

        self._3.addWidget(self.pages)


        self.horizontalLayout_18.addWidget(self.main)


        self.verticalLayout_11.addWidget(self.body)

        Nugget.setCentralWidget(self.centralwidget)

        self.retranslateUi(Nugget)

        self.devicePicker.setCurrentIndex(-1)
        self.pages.setCurrentIndex(6)
        self.dynamicIslandDrp.setCurrentIndex(0)
        self.spoofedModelDrp.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(Nugget)
    # setupUi

    def retranslateUi(self, Nugget):
        Nugget.setWindowTitle(QCoreApplication.translate("Nugget", u"Nugget", None))
        self.centralwidget.setProperty(u"cls", QCoreApplication.translate("Nugget", u"central", None))
        self.devicePicker.setPlaceholderText(QCoreApplication.translate("Nugget", u"None", None))
        self.refreshBtn.setProperty(u"cls", QCoreApplication.translate("Nugget", u"btn", None))
        self.titleBar.setText(QCoreApplication.translate("Nugget", u"Nugget", None))
        self.homePageBtn.setText(QCoreApplication.translate("Nugget", u"\u4e3b\u9875", None))
        self.homePageBtn.setProperty(u"cls", QCoreApplication.translate("Nugget", u"sidebarBtn", None))
        self.explorePageBtn.setText(QCoreApplication.translate("Nugget", u"\u63a2\u7d22", None))
        self.explorePageBtn.setProperty(u"cls", QCoreApplication.translate("Nugget", u"sidebarBtn", None))
        self.gestaltPageBtn.setText(QCoreApplication.translate("Nugget", u"     Mobile Gestalt(\u5f00\u5c9b\u4e4b\u7c7b\u8fd9\u91cc\u770b~)", None))
        self.gestaltPageBtn.setProperty(u"cls", QCoreApplication.translate("Nugget", u"sidebarBtn", None))
        self.featureFlagsPageBtn.setText(QCoreApplication.translate("Nugget", u"\u7279\u6b8a\u529f\u80fd", None))
        self.featureFlagsPageBtn.setProperty(u"cls", QCoreApplication.translate("Nugget", u"sidebarBtn", None))
        self.euEnablerPageBtn.setText(QCoreApplication.translate("Nugget", u"\u8bbe\u5907\u4fe1\u606f\u4f2a\u9020(\u5f00AI\u7684\u770b\u770b\u8fd9\u91cc~)", None))
        self.euEnablerPageBtn.setProperty(u"cls", QCoreApplication.translate("Nugget", u"sidebarBtn", None))
        self.springboardOptionsPageBtn.setText(QCoreApplication.translate("Nugget", u"    Springboard\u8bbe\u7f6e", None))
        self.springboardOptionsPageBtn.setProperty(u"cls", QCoreApplication.translate("Nugget", u"sidebarBtn", None))
        self.internalOptionsPageBtn.setText(QCoreApplication.translate("Nugget", u"\u5185\u7f6e\u529f\u80fd", None))
        self.internalOptionsPageBtn.setProperty(u"cls", QCoreApplication.translate("Nugget", u"sidebarBtn", None))
        self.advancedPageBtn.setText(QCoreApplication.translate("Nugget", u"\u9ad8\u98ce\u9669\u529f\u80fd", None))
        self.advancedPageBtn.setProperty(u"cls", QCoreApplication.translate("Nugget", u"sidebarBtn", None))
        self.applyPageBtn.setText(QCoreApplication.translate("Nugget", u"\u5e94\u7528", None))
        self.applyPageBtn.setProperty(u"cls", QCoreApplication.translate("Nugget", u"sidebarBtn", None))
        self.settingsPageBtn.setText(QCoreApplication.translate("Nugget", u"\u8bbe\u7f6e", None))
        self.settingsPageBtn.setProperty(u"cls", QCoreApplication.translate("Nugget", u"sidebarBtn", None))
        self.phoneNameLbl.setText(QCoreApplication.translate("Nugget", u"\u8bbe\u5907\u540d", None))
        self.phoneVersionLbl.setText(QCoreApplication.translate("Nugget", u"<html><head/><body><p>iOS\u7248\u672c</p></body></html>", None))
        self.bigNuggetBtn.setText(QCoreApplication.translate("Nugget", u"...", None))
        self.label_2.setText(QCoreApplication.translate("Nugget", u"Nugget", None))
        self.discordBtn.setText(QCoreApplication.translate("Nugget", u"\u52a0\u5165Discord", None))
        self.starOnGithubBtn.setText(QCoreApplication.translate("Nugget", u"\u53bbGithub\u70b9\u4e2a\u661f\u661f\u5427", None))
        self.leminBtn.setText(QCoreApplication.translate("Nugget", u"  LeminLimez", None))
        self.leminTwitterBtn.setText(QCoreApplication.translate("Nugget", u"...", None))
        self.leminGithubBtn.setText(QCoreApplication.translate("Nugget", u"...", None))
        self.leminKoFiBtn.setText(QCoreApplication.translate("Nugget", u"...", None))
        self.toolButton_14.setText(QCoreApplication.translate("Nugget", u"\u4e3b\u5f00\u53d1\u8005", None))
        self.helpFromBtn.setText(QCoreApplication.translate("Nugget", u"\u529f\u80fd\u5b9e\u73b0", None))
        self.jjtechBtn.setText(QCoreApplication.translate("Nugget", u"JJTech\n"
"TrollStore", None))
        self.disfordottieBtn.setText(QCoreApplication.translate("Nugget", u"disfordottie\n"
"\u65f6\u949f\u52a8\u753b,\u65e7\u76f8\u518cUI", None))
        self.lrdsnowBtn.setText(QCoreApplication.translate("Nugget", u"lrdsnow\n"
"\u8bbe\u5907\u4fe1\u606f\u4f2a\u9020", None))
        self.toolButton_15.setText(QCoreApplication.translate("Nugget", u"\u7279\u522b\u611f\u8c22", None))
        self.libiBtn.setText(QCoreApplication.translate("Nugget", u"pymobiledevice3", None))
        self.qtBtn.setText(QCoreApplication.translate("Nugget", u"Qt Creator", None))
        self.label.setText(QCoreApplication.translate("Nugget", u"Nugget GUI - Version 4.1 \u6c49\u5316BY Bennett", None))
        self.statusBarLbl.setText(QCoreApplication.translate("Nugget", u"Mobile Gestalt", None))
        self.mgaWarningLbl.setText(QCoreApplication.translate("Nugget", u"!\u4e0b\u5217\u4fee\u6539\u9700\u8981MobileGestalt\u6587\u4ef6 \u8bf7\u5728\u5e94\u7528\u9009\u9879\u5361\u9009\u62e9 !", None))
        self.label_9.setText(QCoreApplication.translate("Nugget", u"\u578b\u53f7\u9009\u62e9", None))
        self.dynamicIslandDrp.setItemText(0, QCoreApplication.translate("Nugget", u"None", None))
        self.dynamicIslandDrp.setItemText(1, QCoreApplication.translate("Nugget", u"2436 (SE\u7cfb\u5217\u5f00X\u624b\u52bf)", None))
        self.dynamicIslandDrp.setItemText(2, QCoreApplication.translate("Nugget", u"2556 (iPhone 14 Pro \u7075\u52a8\u5c9b)", None))
        self.dynamicIslandDrp.setItemText(3, QCoreApplication.translate("Nugget", u"2796 (iPhone 14 Pro Max \u7075\u52a8\u5c9b)", None))
        self.dynamicIslandDrp.setItemText(4, QCoreApplication.translate("Nugget", u"2976 (iPhone 15 Pro Max \u7075\u52a8\u5c9b)", None))
        self.dynamicIslandDrp.setItemText(5, QCoreApplication.translate("Nugget", u"2622 (iPhone 16 Pro \u7075\u52a8\u5c9b)", None))
        self.dynamicIslandDrp.setItemText(6, QCoreApplication.translate("Nugget", u"2868 (iPhone 16 Pro Max \u7075\u52a8\u5c9b)", None))

        self.dynamicIslandDrp.setCurrentText(QCoreApplication.translate("Nugget", u"None", None))
        self.rdarFixChk.setText(QCoreApplication.translate("Nugget", u"\u4fee\u590dRDAR(\u7ea2\u6761)", None))
        self.modelNameChk.setText(QCoreApplication.translate("Nugget", u"\u4fee\u6539\u8bbe\u5907\u578b\u53f7\u540d\u79f0", None))
        self.modelNameTxt.setText(QCoreApplication.translate("Nugget", u"\u578b\u53f7\u540d\u79f0", None))
        self.modelNameTxt.setPlaceholderText(QCoreApplication.translate("Nugget", u"Model Name", None))
        self.bootChimeChk.setText(QCoreApplication.translate("Nugget", u"\u542f\u7528\u542f\u52a8\u97f3(\u8c8c\u4f3c\u6ca1\u7528)", None))
        self.chargeLimitChk.setText(QCoreApplication.translate("Nugget", u"\u542f\u52a8\u5145\u7535\u9650\u5236", None))
        self.tapToWakeChk.setText(QCoreApplication.translate("Nugget", u"\u542f\u7528\u53cc\u51fb\u5524\u9192(SE\u7528)", None))
        self.iphone16SettingsChk.setText(QCoreApplication.translate("Nugget", u"\u542f\u7528iPhone 16\u8bbe\u7f6e", None))
        self.parallaxChk.setText(QCoreApplication.translate("Nugget", u"\u7981\u7528\u58c1\u7eb8\u89c6\u5dee", None))
        self.stageManagerChk.setText(QCoreApplication.translate("Nugget", u"\u542f\u7528\u53f0\u524d\u8c03\u5ea6 (WARNING: \u5bb9\u6613\u51fa\u95ee\u9898,\u5c24\u5176iPhone\u8bbe\u5907)", None))
        self.enableMedusaChk.setText(QCoreApplication.translate("Nugget", u"\u542f\u7528 Medusa (iPad \u591a\u4efb\u52a1) (WARNING: \u5bb9\u6613\u51fa\u95ee\u9898,\u5c24\u5176iPhone\u8bbe\u5907)", None))
        self.ipadAppsChk.setText(QCoreApplication.translate("Nugget", u"\u5141\u8bb8iPad\u5e94\u7528\u5728iPhone", None))
        self.shutterChk.setText(QCoreApplication.translate("Nugget", u"\u7981\u7528\u5730\u533a\u9650\u5236\u529f\u80fd (\u5982 \u62cd\u7167\u97f3)", None))
        self.findMyFriendsChk.setText(QCoreApplication.translate("Nugget", u"\u542f\u7528\u67e5\u627e\u6211\u7684\u670b\u53cb", None))
        self.pencilChk.setText(QCoreApplication.translate("Nugget", u"\u542f\u7528 Apple Pencil \u8bbe\u7f6e(\u8c8c\u4f3c\u6ca1\u7528,\u662f\u7a7a\u58f3\uff09", None))
        self.actionButtonChk.setText(QCoreApplication.translate("Nugget", u"\u542f\u52a8 Action Button \u8bbe\u7f6e\u83dc\u5355(\u6ca1\u6709\u6309\u952e\u7684\u8bbe\u5907\u5c31\u4e00\u4e2aUI\u6ca1\u7528)", None))
        self.internalInstallChk.setText(QCoreApplication.translate("Nugget", u"\u8bbe\u7f6eApple Internal \u5b89\u88c5 (\u6240\u6709\u8f6f\u4ef6\u652f\u6301HUD)(\u4e0d\u5efa\u8bae,\u5c0f\u5fc3\u83b7\u5f97\u5e38\u9a7b\u76ae\u80a4)", None))
        self.internalStorageChk.setText(QCoreApplication.translate("Nugget", u"\u542f\u7528\u5185\u7f6e\u50a8\u5b58 (WARNING: \u5bb9\u6613\u51fa\u95ee\u9898,\u5c24\u5176iPad\u8bbe\u5907)", None))
        self.collisionSOSChk.setText(QCoreApplication.translate("Nugget", u"\u542f\u7528\u78b0\u649e SOS", None))
        self.aodChk.setText(QCoreApplication.translate("Nugget", u"\u542f\u7528\u5168\u5929\u5019\u663e\u793a(AOD)", None))
        self.label_10.setText(QCoreApplication.translate("Nugget", u"\u81ea\u5b9a\u4e49\u5bc6\u94a5", None))
        self.addGestaltKeyBtn.setText(QCoreApplication.translate("Nugget", u"  Add Key", None))
        self.label_12.setText(QCoreApplication.translate("Nugget", u"\u8b66\u544a\uff1a \u9519\u8bef\u5730\u4f7f\u7528\u6b64\u529f\u80fd\u53ef\u80fd\u4f1a\u767d\u82f9\u679c\u3002\n"
"\u53ea\u6709\u5728\u60a8\u77e5\u9053\u81ea\u5df1\u5728\u505a\u4ec0\u4e48\u65f6\u624d\u4f7f\u7528\u3002", None))
        self.internalOptionsLbl.setText(QCoreApplication.translate("Nugget", u"\u7279\u6b8a\u529f\u80fd", None))
        self.clockAnimChk.setText(QCoreApplication.translate("Nugget", u"\u542f\u7528\u9501\u5c4f\u65f6\u949f\u52a8\u753b", None))
        self.lockscreenChk.setText(QCoreApplication.translate("Nugget", u"\u542f\u7528\u91cd\u590d\u7684\u9501\u5c4f\u6309\u94ae\u548c\u9501\u5c4f\u5feb\u901f\u5f00\u5173(\u8fd9\u5565?)", None))
        self.photosChk.setText(QCoreApplication.translate("Nugget", u"\u542f\u7528\u65e7\u76f8\u518cUI", None))
        self.aiChk.setText(QCoreApplication.translate("Nugget", u"\u542f\u7528Apple Intelligence", None))
        self.eligibilityLbl.setText(QCoreApplication.translate("Nugget", u"Eligibility Tweaks", None))
        self.euEnablerEnabledChk.setText(QCoreApplication.translate("Nugget", u"\u5730\u533a\u4fee\u6539\u5668", None))
        self.label_5.setText(QCoreApplication.translate("Nugget", u"\u4fee\u6539\u65b9\u5f0f", None))
        self.methodChoiceDrp.setItemText(0, QCoreApplication.translate("Nugget", u"Method 1", None))
        self.methodChoiceDrp.setItemText(1, QCoreApplication.translate("Nugget", u"Method 2", None))

        self.label_6.setText(QCoreApplication.translate("Nugget", u"\u5730\u533a\u7b26\u53f7(\u4f8b:US)", None))
        self.regionCodeTxt.setPlaceholderText(QCoreApplication.translate("Nugget", u"Region Code (Default: US)", None))
        self.mgaWarningLbl2.setText(QCoreApplication.translate("Nugget", u"!\u4e0b\u5217\u4fee\u6539\u9700\u8981MobileGestalt\u6587\u4ef6 \u8bf7\u5728\u5e94\u7528\u9009\u9879\u5361\u9009\u62e9 !", None))
        self.enableAIChk.setText(QCoreApplication.translate("Nugget", u"\u542f\u7528Apple Intelligence (\u5bf9\u4e8e\u4e0d\u652f\u6301\u7684\u8bbe\u5907)", None))
        self.eligFileChk.setText(QCoreApplication.translate("Nugget", u"\u4f2a\u9020\u5730\u533a\u4fe1\u606f", None))
        self.languageLbl.setText(QCoreApplication.translate("Nugget", u"\u5730\u533a\u7b26\u53f7:", None))
        self.languageTxt.setPlaceholderText(QCoreApplication.translate("Nugget", u"Language Code (i.e. en)", None))
        self.aiInfoLabel.setText(QCoreApplication.translate("Nugget", u"\u4e3a\u4e86\u4e0b\u8f7d AI \u6a21\u578b\uff0c\u60a8\u5fc5\u987b\u4f2a\u9020\u60a8\u7684\u8bbe\u5907\u6a21\u578b\u3002\u4f46\u662f\uff0c\u8fd9\u53ef\u80fd\u4f1a\u7834\u574f Face ID\uff0c\u76f4\u5230\u60a8\u6062\u590d\u4fee\u6539\u3002\n"
"\u8b66\u544a\uff1a\u53d6\u6d88\u4f2a\u9020\u540e\uff0c\u8bf7\u52ff\u8f6c\u5230\u201c\u8bbe\u7f6e\u201d\u5e94\u7528\u4e2d\u7684 Apple Intelligence \u83dc\u5355\u3002\n"
"\u5728\u539f\u59cb\u8bbe\u5907\u578b\u53f7\u4e0a\u8fdb\u5165\u8be5\u83dc\u5355\u5c06\u5bfc\u81f4\u91cd\u65b0\u4e0b\u8f7d\uff0c\u5e76\u53ef\u80fd\u9700\u8981\u5b8c\u5168\u6062\u590d\u624d\u80fd\u4fee\u590d\u3002\n"
"\u6b64\u5916\uff0c\u5982\u679c\u60a8\u5728\u578b\u53f7\u4e4b\u95f4\u5207\u6362\uff0c\u4f8b\u5982\u4ece iPhone 16\u5230 iPhone 15 Pro \u7cfb\u5217\u7684\u4f2a\u9020\uff0c\u4e5f\u53ef\u80fd\u4f1a\u91cd\u65b0\u4e0b\u8f7d\u3002\n"
"\u8bf7\u5c0f\u5fc3\uff01", None))
        self.label_8.setText(QCoreApplication.translate("Nugget", u"\u4f2a\u9020\u673a\u578b", None))
        self.spoofedModelDrp.setItemText(0, QCoreApplication.translate("Nugget", u"Original", None))
        self.spoofedModelDrp.setItemText(1, QCoreApplication.translate("Nugget", u"iPhone 15 Pro (iPhone16,1)", None))
        self.spoofedModelDrp.setItemText(2, QCoreApplication.translate("Nugget", u"iPhone 15 Pro Max (iPhone16,2)", None))
        self.spoofedModelDrp.setItemText(3, QCoreApplication.translate("Nugget", u"iPhone 16 (iPhone17,3)", None))
        self.spoofedModelDrp.setItemText(4, QCoreApplication.translate("Nugget", u"iPhone 16 Plus (iPhone17,4)", None))
        self.spoofedModelDrp.setItemText(5, QCoreApplication.translate("Nugget", u"iPhone 16 Pro (iPhone17,1)", None))
        self.spoofedModelDrp.setItemText(6, QCoreApplication.translate("Nugget", u"iPhone 16 Pro Max (iPhone17,2)", None))
        self.spoofedModelDrp.setItemText(7, QCoreApplication.translate("Nugget", u"iPad Mini (A17 Pro) (W) (iPad16,1)", None))
        self.spoofedModelDrp.setItemText(8, QCoreApplication.translate("Nugget", u"iPad Mini (A17 Pro) (C) (iPad16,2)", None))
        self.spoofedModelDrp.setItemText(9, QCoreApplication.translate("Nugget", u"iPad Pro (13-inch) (M4) (W) (iPad16,5)", None))
        self.spoofedModelDrp.setItemText(10, QCoreApplication.translate("Nugget", u"iPad Pro (13-inch) (M4) (C) (iPad16,6)", None))
        self.spoofedModelDrp.setItemText(11, QCoreApplication.translate("Nugget", u"iPad Pro (11-inch) (M4) (W) (iPad16,3)", None))
        self.spoofedModelDrp.setItemText(12, QCoreApplication.translate("Nugget", u"iPad Pro (11-inch) (M4) (C) (iPad16,4)", None))
        self.spoofedModelDrp.setItemText(13, QCoreApplication.translate("Nugget", u"iPad Pro (12.9-inch) (M2) (W) (iPad14,5)", None))
        self.spoofedModelDrp.setItemText(14, QCoreApplication.translate("Nugget", u"iPad Pro (12.9-inch) (M2) (C) (iPad14,6)", None))
        self.spoofedModelDrp.setItemText(15, QCoreApplication.translate("Nugget", u"iPad Pro (11-inch) (M2) (W) (iPad14,3)", None))
        self.spoofedModelDrp.setItemText(16, QCoreApplication.translate("Nugget", u"iPad Pro (11-inch) (M2) (C) (iPad14,4)", None))
        self.spoofedModelDrp.setItemText(17, QCoreApplication.translate("Nugget", u"iPad Air (13-inch) (M2) (W) (iPad14,10)", None))
        self.spoofedModelDrp.setItemText(18, QCoreApplication.translate("Nugget", u"iPad Air (13-inch) (M2) (C) (iPad14,11)", None))
        self.spoofedModelDrp.setItemText(19, QCoreApplication.translate("Nugget", u"iPad Air (11-inch) (M2) (W) (iPad14,8)", None))
        self.spoofedModelDrp.setItemText(20, QCoreApplication.translate("Nugget", u"iPad Air (11-inch) (M2) (C) (iPad14,9)", None))
        self.spoofedModelDrp.setItemText(21, QCoreApplication.translate("Nugget", u"iPad Pro (11-inch) (M1) (W) (iPad13,4)", None))
        self.spoofedModelDrp.setItemText(22, QCoreApplication.translate("Nugget", u"iPad Pro (11-inch) (M1) (C) (iPad13,5)", None))
        self.spoofedModelDrp.setItemText(23, QCoreApplication.translate("Nugget", u"iPad Pro (12.9-inch) (M1) (W) (iPad13,8)", None))
        self.spoofedModelDrp.setItemText(24, QCoreApplication.translate("Nugget", u"iPad Pro (12.9-inch) (M1) (C) (iPad13,9)", None))
        self.spoofedModelDrp.setItemText(25, QCoreApplication.translate("Nugget", u"iPad Air (M1) (W) (iPad13,16)", None))
        self.spoofedModelDrp.setItemText(26, QCoreApplication.translate("Nugget", u"iPad Air (M1) (C) (iPad13,17)", None))

        self.spoofedModelDrp.setCurrentText(QCoreApplication.translate("Nugget", u"Original", None))
        self.springboardOptionsLbl.setText(QCoreApplication.translate("Nugget", u"Springboard Options", None))
        self.label_13.setText(QCoreApplication.translate("Nugget", u"Lock Screen Footnote Text", None))
        self.footnoteTxt.setPlaceholderText(QCoreApplication.translate("Nugget", u"Footnote Text", None))
        self.disableLockRespringChk.setText(QCoreApplication.translate("Nugget", u"Disable Lock After Respring", None))
        self.disableDimmingChk.setText(QCoreApplication.translate("Nugget", u"Disable Screen Dimming While Charging", None))
        self.disableBatteryAlertsChk.setText(QCoreApplication.translate("Nugget", u"Disable Low Battery Alerts", None))
        self.disableCrumbChk.setText(QCoreApplication.translate("Nugget", u"Disable Breadcrumbs", None))
        self.enableSupervisionTextChk.setText(QCoreApplication.translate("Nugget", u"Show Supervision Text on Lock Screen", None))
        self.enableAirPlayChk.setText(QCoreApplication.translate("Nugget", u"Enable AirPlay support for Stage Manager", None))
        self.internalOptionsLbl1.setText(QCoreApplication.translate("Nugget", u"Internal Options", None))
        self.buildVersionChk.setText(QCoreApplication.translate("Nugget", u"Show Build Version in Status Bar", None))
        self.RTLChk.setText(QCoreApplication.translate("Nugget", u"Force Right-to-Left Layout", None))
        self.metalHUDChk.setText(QCoreApplication.translate("Nugget", u"Enable Metal HUD Debug", None))
        self.iMessageChk.setText(QCoreApplication.translate("Nugget", u"Enable iMessage Debugging", None))
        self.IDSChk.setText(QCoreApplication.translate("Nugget", u"Enable Continuity Debugging", None))
        self.VCChk.setText(QCoreApplication.translate("Nugget", u"Enable FaceTime Debugging", None))
        self.appStoreChk.setText(QCoreApplication.translate("Nugget", u"Enable App Store Debug Gesture", None))
        self.notesChk.setText(QCoreApplication.translate("Nugget", u"Enable Notes Debug Mode", None))
        self.showTouchesChk.setText(QCoreApplication.translate("Nugget", u"Show Touches With Debug Info", None))
        self.hideRespringChk.setText(QCoreApplication.translate("Nugget", u"Hide Respring Icon", None))
        self.enableWakeVibrateChk.setText(QCoreApplication.translate("Nugget", u"Vibrate on Raise-to-Wake", None))
        self.pasteSoundChk.setText(QCoreApplication.translate("Nugget", u"Play Sound on Paste", None))
        self.notifyPastesChk.setText(QCoreApplication.translate("Nugget", u"Show Notifications for System Pastes", None))
        self.advancedOptionsLbl.setText(QCoreApplication.translate("Nugget", u"\u9ad8\u98ce\u9669\u529f\u80fd", None))
        self.label_17.setText(QCoreApplication.translate("Nugget", u"\u544a\u77e5:\n"
"\n"
"\u8fd9\u91cc\u7684\u9009\u9879\u53ef\u80fd\u4f1a\u5bfc\u81f4\u4e0b\u5217\u95ee\u9898(\u5305\u62ec\u4f46\u4e0d\u9650\u4e8e):\n"
"1.\u767d\u82f9\u679c\n"
"2.\u624b\u673a\u53d1\u70eb\n"
"3.SpringBoard\u5d29\u6e83\n"
"4.\u559c\u63d0\u677f\u7816\n"
"5.\u7b2c\u4e09\u6b21\u4e16\u754c\u5927\u6218\u7b49\n"
"Nugget\u4e0d\u5bf9\u4e0b\u5217\u95ee\u9898\u5bfc\u81f4\u7684\u635f\u5931\u8d1f\u8d23", None))
        self.disableOTAChk.setText(QCoreApplication.translate("Nugget", u"\u7981\u7528\u7cfb\u7edfOTA", None))
        self.enableResolutionChk.setText(QCoreApplication.translate("Nugget", u"\u81ea\u5b9a\u4e49\u5206\u8fa8\u7387", None))
        self.resHeightLbl.setText(QCoreApplication.translate("Nugget", u"\u9ad8:", None))
        self.resHeightTxt.setText(QCoreApplication.translate("Nugget", u"\u5206\u8fa8\u7387:", None))
        self.resHeightTxt.setPlaceholderText(QCoreApplication.translate("Nugget", u"Resolution Height", None))
        self.resHeightWarningLbl.setText(QCoreApplication.translate("Nugget", u"!", None))
        self.resWidthLbl.setText(QCoreApplication.translate("Nugget", u"\u5bbd:", None))
        self.resWidthTxt.setText(QCoreApplication.translate("Nugget", u"\u5206\u8fa8\u7387:", None))
        self.resWidthTxt.setPlaceholderText(QCoreApplication.translate("Nugget", u"Resolution Width", None))
        self.resWidthWarningLbl.setText(QCoreApplication.translate("Nugget", u"!", None))
        self.statusBarLbl_5.setText(QCoreApplication.translate("Nugget", u"Apply", None))
        self.label_16.setText("")
        self.modifiedTweaksLbl.setText(QCoreApplication.translate("Nugget", u"\u5df2\u9009\u62e9\u7684\u4fee\u6539", None))
        self.gestaltLocationLbl.setText(QCoreApplication.translate("Nugget", u"None", None))
        self.chooseGestaltBtn.setText(QCoreApplication.translate("Nugget", u"\u9009\u62e9\u6587\u4ef6", None))
        self.applyTweaksBtn.setText(QCoreApplication.translate("Nugget", u"\u5e94\u7528\u4fee\u6539", None))
        self.statusLbl.setText(QCoreApplication.translate("Nugget", u"\u51c6\u5907\u597d\u4e86\uff0c\u7b49\u5f85\u8d70\u8d77", None))
        self.removeTweaksBtn.setText(QCoreApplication.translate("Nugget", u"\u79fb\u9664\u6240\u6709\u4fee\u6539", None))
        self.resetGestaltBtn.setText(QCoreApplication.translate("Nugget", u"\u91cd\u7f6e Mobile Gestalt", None))
        self.springboardOptionsLbl1.setText(QCoreApplication.translate("Nugget", u"Nugget Settings", None))
        self.allowWifiApplyingChk.setText(QCoreApplication.translate("Nugget", u"\u5141\u8bb8\u901a\u8fc7WIFI\u8bbe\u7f6e", None))
        self.autoRebootChk.setText(QCoreApplication.translate("Nugget", u"\u5e94\u7528\u540e\u81ea\u52a8\u91cd\u542f", None))
        self.showRiskyChk.setText(QCoreApplication.translate("Nugget", u"\u5c55\u793a\u9ad8\u98ce\u9669\u529f\u80fd", None))
        self.skipSetupChk.setText(QCoreApplication.translate("Nugget", u"\u8df3\u8fc7\u6fc0\u6d3b\u8bbe\u7f6e", None))
        self.supervisionChk.setText(QCoreApplication.translate("Nugget", u"\u542f\u7528\u76d1\u7ba1(\u9700\u8981\u6fc0\u6d3b)", None))
        self.supervisionOrganization.setText(QCoreApplication.translate("Nugget", u"\u7ec4\u7ec7\u540d\u79f0", None))
        self.supervisionOrganization.setPlaceholderText(QCoreApplication.translate("Nugget", u"Enter Organization Name", None))
        self.label_15.setText(QCoreApplication.translate("Nugget", u"* Note: Skip Setup may cause issues with configuration profiles. Turn it off if you need that.", None))
        self.resetPairBtn.setText(QCoreApplication.translate("Nugget", u"\u91cd\u65b0\u914d\u5bf9\u8bbe\u5907", None))
        self.statusBarLbl_2.setText(QCoreApplication.translate("Nugget", u"Location Simulation", None))
        self.label_4.setText("")
        self.loadLocSimBtn.setText(QCoreApplication.translate("Nugget", u"Start Location Simulation", None))
        self.label_7.setText(QCoreApplication.translate("Nugget", u"Latitude", None))
        self.latitudeTxt.setPlaceholderText(QCoreApplication.translate("Nugget", u"XXX.XXXXX", None))
        self.label_11.setText(QCoreApplication.translate("Nugget", u"Longitude", None))
        self.longitudeTxt.setPlaceholderText(QCoreApplication.translate("Nugget", u"XXX.XXXXX", None))
        self.setLocationBtn.setText(QCoreApplication.translate("Nugget", u"Set Location", None))
        self.resetLocationBtn.setText(QCoreApplication.translate("Nugget", u"Reset Location", None))
        self.customOperationsLbl.setText(QCoreApplication.translate("Nugget", u"Custom Operations", None))
        self.label_14.setText("")
        self.importOperationBtn.setText(QCoreApplication.translate("Nugget", u"  Import .cowperation", None))
        self.newOperationBtn.setText(QCoreApplication.translate("Nugget", u"  New Operation", None))
        self.exploreLbl.setText(QCoreApplication.translate("Nugget", u"Explore", None))
        self.exploreSubLbl.setText("")
        self.themesLbl.setText(QCoreApplication.translate("Nugget", u"Mobile Gestalt Modifications", None))
        self.importThemeBtn.setText(QCoreApplication.translate("Nugget", u"Import Theme:", None))
        self.importThemeFolderBtn.setText(QCoreApplication.translate("Nugget", u"...", None))
        self.importThemeZipBtn.setText(QCoreApplication.translate("Nugget", u"...", None))
        self.label_3.setText(QCoreApplication.translate("Nugget", u"Customize Individual Apps", None))
        self.hideNamesBtn.setText(QCoreApplication.translate("Nugget", u"Hide/Show All App Names", None))
        self.borderAllBtn.setText(QCoreApplication.translate("Nugget", u"Toggle All \"Border\"", None))
        self.addAllBtn.setText(QCoreApplication.translate("Nugget", u"Toggle All \"Add to Device\"", None))
    # retranslateUi

