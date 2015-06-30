# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainwindow.ui'
#
# Created: Thu Apr  2 13:16:51 2015
#      by: PyQt4 UI code generator 4.9.6
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(578, 398)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setLocale(QtCore.QLocale(QtCore.QLocale.English, QtCore.QLocale.UnitedStates))
        self.centralWidget = QtGui.QWidget(MainWindow)
        self.centralWidget.setObjectName(_fromUtf8("centralWidget"))
        self.Banner = QtGui.QLabel(self.centralWidget)
        self.Banner.setGeometry(QtCore.QRect(0, 0, 591, 91))
        self.Banner.setLocale(QtCore.QLocale(QtCore.QLocale.English, QtCore.QLocale.UnitedStates))
        self.Banner.setText(_fromUtf8(""))
        self.Banner.setPixmap(QtGui.QPixmap(_fromUtf8(":/data/img/neptune-banner.png")))
        self.Banner.setScaledContents(False)
        self.Banner.setAlignment(QtCore.Qt.AlignCenter)
        self.Banner.setObjectName(_fromUtf8("Banner"))
        self.tabWidget = QtGui.QTabWidget(self.centralWidget)
        self.tabWidget.setGeometry(QtCore.QRect(0, 90, 591, 349))
        self.tabWidget.setTabPosition(QtGui.QTabWidget.South)
        self.tabWidget.setObjectName(_fromUtf8("tabWidget"))
        self.welcometab = QtGui.QWidget()
        self.welcometab.setObjectName(_fromUtf8("welcometab"))
        self.layoutWidget = QtGui.QWidget(self.welcometab)
        self.layoutWidget.setGeometry(QtCore.QRect(0, 260, 571, 41))
        self.layoutWidget.setObjectName(_fromUtf8("layoutWidget"))
        self.horizontalLayout = QtGui.QHBoxLayout(self.layoutWidget)
        self.horizontalLayout.setMargin(0)
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.quitbtn = QtGui.QPushButton(self.layoutWidget)
        self.quitbtn.setMinimumSize(QtCore.QSize(0, 24))
        icon = QtGui.QIcon.fromTheme(_fromUtf8("exit"))
        self.quitbtn.setIcon(icon)
        self.quitbtn.setObjectName(_fromUtf8("quitbtn"))
        self.horizontalLayout.addWidget(self.quitbtn)
        spacerItem = QtGui.QSpacerItem(358, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.nextbtn = QtGui.QPushButton(self.layoutWidget)
        self.nextbtn.setMinimumSize(QtCore.QSize(0, 24))
        icon = QtGui.QIcon.fromTheme(_fromUtf8("next"))
        self.nextbtn.setIcon(icon)
        self.nextbtn.setObjectName(_fromUtf8("nextbtn"))
        self.horizontalLayout.addWidget(self.nextbtn)
        self.logo = QtGui.QLabel(self.welcometab)
        self.logo.setGeometry(QtCore.QRect(20, 0, 61, 71))
        self.logo.setText(_fromUtf8(""))
        self.logo.setPixmap(QtGui.QPixmap(_fromUtf8(":/data/img/drive-harddisk.png")))
        self.logo.setObjectName(_fromUtf8("logo"))
        self.layoutWidget_2 = QtGui.QWidget(self.welcometab)
        self.layoutWidget_2.setGeometry(QtCore.QRect(110, 0, 461, 251))
        self.layoutWidget_2.setObjectName(_fromUtf8("layoutWidget_2"))
        self.verticalLayout = QtGui.QVBoxLayout(self.layoutWidget_2)
        self.verticalLayout.setMargin(0)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.title = QtGui.QLabel(self.layoutWidget_2)
        self.title.setTextFormat(QtCore.Qt.AutoText)
        self.title.setObjectName(_fromUtf8("title"))
        self.verticalLayout.addWidget(self.title)
        self.msg = QtGui.QLabel(self.layoutWidget_2)
        self.msg.setWordWrap(True)
        self.msg.setObjectName(_fromUtf8("msg"))
        self.verticalLayout.addWidget(self.msg)
        self.tabWidget.addTab(self.welcometab, _fromUtf8(""))
        self.usertab = QtGui.QWidget()
        self.usertab.setObjectName(_fromUtf8("usertab"))
        self.layoutWidget_3 = QtGui.QWidget(self.usertab)
        self.layoutWidget_3.setGeometry(QtCore.QRect(0, 260, 571, 41))
        self.layoutWidget_3.setObjectName(_fromUtf8("layoutWidget_3"))
        self.horizontalLayout_2 = QtGui.QHBoxLayout(self.layoutWidget_3)
        self.horizontalLayout_2.setMargin(0)
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.backbtn = QtGui.QPushButton(self.layoutWidget_3)
        self.backbtn.setMinimumSize(QtCore.QSize(0, 24))
        icon = QtGui.QIcon.fromTheme(_fromUtf8("back"))
        self.backbtn.setIcon(icon)
        self.backbtn.setObjectName(_fromUtf8("backbtn"))
        self.horizontalLayout_2.addWidget(self.backbtn)
        spacerItem1 = QtGui.QSpacerItem(358, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem1)
        self.nextbtn_2 = QtGui.QPushButton(self.layoutWidget_3)
        self.nextbtn_2.setMinimumSize(QtCore.QSize(0, 24))
        icon = QtGui.QIcon.fromTheme(_fromUtf8("next"))
        self.nextbtn_2.setIcon(icon)
        self.nextbtn_2.setObjectName(_fromUtf8("nextbtn_2"))
        self.horizontalLayout_2.addWidget(self.nextbtn_2)
        self.logo_2 = QtGui.QLabel(self.usertab)
        self.logo_2.setGeometry(QtCore.QRect(20, 0, 61, 71))
        self.logo_2.setText(_fromUtf8(""))
        self.logo_2.setPixmap(QtGui.QPixmap(_fromUtf8(":/data/img/system-users.png")))
        self.logo_2.setObjectName(_fromUtf8("logo_2"))
        self.title_2 = QtGui.QLabel(self.usertab)
        self.title_2.setGeometry(QtCore.QRect(111, 10, 119, 23))
        self.title_2.setTextFormat(QtCore.Qt.AutoText)
        self.title_2.setObjectName(_fromUtf8("title_2"))
        self.layoutWidget1 = QtGui.QWidget(self.usertab)
        self.layoutWidget1.setGeometry(QtCore.QRect(111, 40, 451, 76))
        self.layoutWidget1.setObjectName(_fromUtf8("layoutWidget1"))
        self.verticalLayout_7 = QtGui.QVBoxLayout(self.layoutWidget1)
        self.verticalLayout_7.setMargin(0)
        self.verticalLayout_7.setObjectName(_fromUtf8("verticalLayout_7"))
        self.msg_2 = QtGui.QLabel(self.layoutWidget1)
        self.msg_2.setWordWrap(True)
        self.msg_2.setObjectName(_fromUtf8("msg_2"))
        self.verticalLayout_7.addWidget(self.msg_2)
        self.horizontalLayout_3 = QtGui.QHBoxLayout()
        self.horizontalLayout_3.setObjectName(_fromUtf8("horizontalLayout_3"))
        self.verticalLayout_3 = QtGui.QVBoxLayout()
        self.verticalLayout_3.setObjectName(_fromUtf8("verticalLayout_3"))
        self.label = QtGui.QLabel(self.layoutWidget1)
        self.label.setObjectName(_fromUtf8("label"))
        self.verticalLayout_3.addWidget(self.label)
        self.label_2 = QtGui.QLabel(self.layoutWidget1)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.verticalLayout_3.addWidget(self.label_2)
        self.horizontalLayout_3.addLayout(self.verticalLayout_3)
        self.verticalLayout_2 = QtGui.QVBoxLayout()
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.rootpw1 = QtGui.QLineEdit(self.layoutWidget1)
        self.rootpw1.setText(_fromUtf8(""))
        self.rootpw1.setEchoMode(QtGui.QLineEdit.Password)
        self.rootpw1.setObjectName(_fromUtf8("rootpw1"))
        self.verticalLayout_2.addWidget(self.rootpw1)
        self.rootpw2 = QtGui.QLineEdit(self.layoutWidget1)
        self.rootpw2.setText(_fromUtf8(""))
        self.rootpw2.setEchoMode(QtGui.QLineEdit.Password)
        self.rootpw2.setObjectName(_fromUtf8("rootpw2"))
        self.verticalLayout_2.addWidget(self.rootpw2)
        self.horizontalLayout_3.addLayout(self.verticalLayout_2)
        self.verticalLayout_7.addLayout(self.horizontalLayout_3)
        self.layoutWidget2 = QtGui.QWidget(self.usertab)
        self.layoutWidget2.setGeometry(QtCore.QRect(111, 117, 451, 141))
        self.layoutWidget2.setObjectName(_fromUtf8("layoutWidget2"))
        self.verticalLayout_6 = QtGui.QVBoxLayout(self.layoutWidget2)
        self.verticalLayout_6.setMargin(0)
        self.verticalLayout_6.setObjectName(_fromUtf8("verticalLayout_6"))
        self.label_4 = QtGui.QLabel(self.layoutWidget2)
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.verticalLayout_6.addWidget(self.label_4)
        self.sudoEnabled = QtGui.QCheckBox(self.layoutWidget2)
        self.sudoEnabled.setEnabled(True)
        self.sudoEnabled.setChecked(True)
        self.sudoEnabled.setObjectName(_fromUtf8("sudoEnabled"))
        self.verticalLayout_6.addWidget(self.sudoEnabled)
        self.horizontalLayout_4 = QtGui.QHBoxLayout()
        self.horizontalLayout_4.setObjectName(_fromUtf8("horizontalLayout_4"))
        self.verticalLayout_5 = QtGui.QVBoxLayout()
        self.verticalLayout_5.setObjectName(_fromUtf8("verticalLayout_5"))
        self.label_cusername = QtGui.QLabel(self.layoutWidget2)
        self.label_cusername.setObjectName(_fromUtf8("label_cusername"))
        self.verticalLayout_5.addWidget(self.label_cusername)
        self.label_3 = QtGui.QLabel(self.layoutWidget2)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.verticalLayout_5.addWidget(self.label_3)
        self.label_5 = QtGui.QLabel(self.layoutWidget2)
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.verticalLayout_5.addWidget(self.label_5)
        self.label_6 = QtGui.QLabel(self.layoutWidget2)
        self.label_6.setObjectName(_fromUtf8("label_6"))
        self.verticalLayout_5.addWidget(self.label_6)
        self.horizontalLayout_4.addLayout(self.verticalLayout_5)
        self.verticalLayout_4 = QtGui.QVBoxLayout()
        self.verticalLayout_4.setObjectName(_fromUtf8("verticalLayout_4"))
        self.cusername = QtGui.QLineEdit(self.layoutWidget2)
        self.cusername.setText(_fromUtf8(""))
        self.cusername.setObjectName(_fromUtf8("cusername"))
        self.verticalLayout_4.addWidget(self.cusername)
        self.username = QtGui.QLineEdit(self.layoutWidget2)
        self.username.setText(_fromUtf8(""))
        self.username.setObjectName(_fromUtf8("username"))
        self.verticalLayout_4.addWidget(self.username)
        self.userpw1 = QtGui.QLineEdit(self.layoutWidget2)
        self.userpw1.setText(_fromUtf8(""))
        self.userpw1.setEchoMode(QtGui.QLineEdit.Password)
        self.userpw1.setObjectName(_fromUtf8("userpw1"))
        self.verticalLayout_4.addWidget(self.userpw1)
        self.userpw2 = QtGui.QLineEdit(self.layoutWidget2)
        self.userpw2.setText(_fromUtf8(""))
        self.userpw2.setEchoMode(QtGui.QLineEdit.Password)
        self.userpw2.setObjectName(_fromUtf8("userpw2"))
        self.verticalLayout_4.addWidget(self.userpw2)
        self.horizontalLayout_4.addLayout(self.verticalLayout_4)
        self.verticalLayout_6.addLayout(self.horizontalLayout_4)
        self.tabWidget.addTab(self.usertab, _fromUtf8(""))
        self.parttab = QtGui.QWidget()
        self.parttab.setObjectName(_fromUtf8("parttab"))
        self.logo_3 = QtGui.QLabel(self.parttab)
        self.logo_3.setGeometry(QtCore.QRect(20, 0, 61, 71))
        self.logo_3.setText(_fromUtf8(""))
        self.logo_3.setPixmap(QtGui.QPixmap(_fromUtf8(":/data/img/partitionmanager.png")))
        self.logo_3.setObjectName(_fromUtf8("logo_3"))
        self.layoutWidget_4 = QtGui.QWidget(self.parttab)
        self.layoutWidget_4.setGeometry(QtCore.QRect(0, 260, 571, 41))
        self.layoutWidget_4.setObjectName(_fromUtf8("layoutWidget_4"))
        self.horizontalLayout_5 = QtGui.QHBoxLayout(self.layoutWidget_4)
        self.horizontalLayout_5.setMargin(0)
        self.horizontalLayout_5.setObjectName(_fromUtf8("horizontalLayout_5"))
        self.backbtn_2 = QtGui.QPushButton(self.layoutWidget_4)
        self.backbtn_2.setMinimumSize(QtCore.QSize(0, 24))
        icon = QtGui.QIcon.fromTheme(_fromUtf8("back"))
        self.backbtn_2.setIcon(icon)
        self.backbtn_2.setObjectName(_fromUtf8("backbtn_2"))
        self.horizontalLayout_5.addWidget(self.backbtn_2)
        spacerItem2 = QtGui.QSpacerItem(358, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_5.addItem(spacerItem2)
        self.nextbtn_3 = QtGui.QPushButton(self.layoutWidget_4)
        self.nextbtn_3.setMinimumSize(QtCore.QSize(0, 24))
        icon = QtGui.QIcon.fromTheme(_fromUtf8("next"))
        self.nextbtn_3.setIcon(icon)
        self.nextbtn_3.setObjectName(_fromUtf8("nextbtn_3"))
        self.horizontalLayout_5.addWidget(self.nextbtn_3)
        self.layoutWidget3 = QtGui.QWidget(self.parttab)
        self.layoutWidget3.setGeometry(QtCore.QRect(110, 10, 461, 251))
        self.layoutWidget3.setObjectName(_fromUtf8("layoutWidget3"))
        self.verticalLayout_9 = QtGui.QVBoxLayout(self.layoutWidget3)
        self.verticalLayout_9.setMargin(0)
        self.verticalLayout_9.setObjectName(_fromUtf8("verticalLayout_9"))
        self.verticalLayout_8 = QtGui.QVBoxLayout()
        self.verticalLayout_8.setObjectName(_fromUtf8("verticalLayout_8"))
        self.gridLayout = QtGui.QGridLayout()
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.title_3 = QtGui.QLabel(self.layoutWidget3)
        self.title_3.setTextFormat(QtCore.Qt.AutoText)
        self.title_3.setObjectName(_fromUtf8("title_3"))
        self.gridLayout.addWidget(self.title_3, 0, 0, 1, 1)
        self.msg_3 = QtGui.QLabel(self.layoutWidget3)
        self.msg_3.setWordWrap(True)
        self.msg_3.setObjectName(_fromUtf8("msg_3"))
        self.gridLayout.addWidget(self.msg_3, 1, 0, 1, 1)
        self.verticalLayout_8.addLayout(self.gridLayout)
        self.horizontalLayout_6 = QtGui.QHBoxLayout()
        self.horizontalLayout_6.setObjectName(_fromUtf8("horizontalLayout_6"))
        spacerItem3 = QtGui.QSpacerItem(128, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_6.addItem(spacerItem3)
        self.partedbtn = QtGui.QPushButton(self.layoutWidget3)
        self.partedbtn.setMinimumSize(QtCore.QSize(188, 24))
        icon = QtGui.QIcon.fromTheme(_fromUtf8("gparted"))
        self.partedbtn.setIcon(icon)
        self.partedbtn.setObjectName(_fromUtf8("partedbtn"))
        self.horizontalLayout_6.addWidget(self.partedbtn)
        spacerItem4 = QtGui.QSpacerItem(108, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_6.addItem(spacerItem4)
        self.refreshBtn = QtGui.QPushButton(self.layoutWidget3)
        self.refreshBtn.setMinimumSize(QtCore.QSize(0, 24))
        icon = QtGui.QIcon.fromTheme(_fromUtf8("reload"))
        self.refreshBtn.setIcon(icon)
        self.refreshBtn.setObjectName(_fromUtf8("refreshBtn"))
        self.horizontalLayout_6.addWidget(self.refreshBtn)
        spacerItem5 = QtGui.QSpacerItem(108, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_6.addItem(spacerItem5)
        self.verticalLayout_8.addLayout(self.horizontalLayout_6)
        self.verticalLayout_9.addLayout(self.verticalLayout_8)
        spacerItem6 = QtGui.QSpacerItem(20, 5, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout_9.addItem(spacerItem6)
        self.horizontalLayout_7 = QtGui.QHBoxLayout()
        self.horizontalLayout_7.setObjectName(_fromUtf8("horizontalLayout_7"))
        self.label_7 = QtGui.QLabel(self.layoutWidget3)
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        self.label_7.setFont(font)
        self.label_7.setObjectName(_fromUtf8("label_7"))
        self.horizontalLayout_7.addWidget(self.label_7)
        self.targetbox = QtGui.QComboBox(self.layoutWidget3)
        self.targetbox.setEditable(True)
        self.targetbox.setObjectName(_fromUtf8("targetbox"))
        self.horizontalLayout_7.addWidget(self.targetbox)
        self.verticalLayout_9.addLayout(self.horizontalLayout_7)
        self.horizontalLayout_20 = QtGui.QHBoxLayout()
        self.horizontalLayout_20.setObjectName(_fromUtf8("horizontalLayout_20"))
        self.formatRootCheck = QtGui.QCheckBox(self.layoutWidget3)
        self.formatRootCheck.setObjectName(_fromUtf8("formatRootCheck"))
        self.horizontalLayout_20.addWidget(self.formatRootCheck)
        self.formatCombo = QtGui.QComboBox(self.layoutWidget3)
        self.formatCombo.setObjectName(_fromUtf8("formatCombo"))
        icon = QtGui.QIcon.fromTheme(_fromUtf8("harddrive"))
        self.formatCombo.addItem(icon, _fromUtf8(""))
        icon = QtGui.QIcon.fromTheme(_fromUtf8("harddrive"))
        self.formatCombo.addItem(icon, _fromUtf8(""))
        self.horizontalLayout_20.addWidget(self.formatCombo)
        self.verticalLayout_9.addLayout(self.horizontalLayout_20)
        spacerItem7 = QtGui.QSpacerItem(20, 2, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout_9.addItem(spacerItem7)
        self.horizontalLayout_8 = QtGui.QHBoxLayout()
        self.horizontalLayout_8.setObjectName(_fromUtf8("horizontalLayout_8"))
        self.label_8 = QtGui.QLabel(self.layoutWidget3)
        self.label_8.setObjectName(_fromUtf8("label_8"))
        self.horizontalLayout_8.addWidget(self.label_8)
        self.grubbox = QtGui.QComboBox(self.layoutWidget3)
        self.grubbox.setEditable(True)
        self.grubbox.setObjectName(_fromUtf8("grubbox"))
        self.horizontalLayout_8.addWidget(self.grubbox)
        self.verticalLayout_9.addLayout(self.horizontalLayout_8)
        spacerItem8 = QtGui.QSpacerItem(20, 2, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout_9.addItem(spacerItem8)
        self.horizontalLayout_9 = QtGui.QHBoxLayout()
        self.horizontalLayout_9.setObjectName(_fromUtf8("horizontalLayout_9"))
        self.label_9 = QtGui.QLabel(self.layoutWidget3)
        self.label_9.setObjectName(_fromUtf8("label_9"))
        self.horizontalLayout_9.addWidget(self.label_9)
        self.homebox = QtGui.QComboBox(self.layoutWidget3)
        self.homebox.setEditable(True)
        self.homebox.setObjectName(_fromUtf8("homebox"))
        self.horizontalLayout_9.addWidget(self.homebox)
        self.verticalLayout_9.addLayout(self.horizontalLayout_9)
        self.tabWidget.addTab(self.parttab, _fromUtf8(""))
        self.summaryTab = QtGui.QWidget()
        self.summaryTab.setObjectName(_fromUtf8("summaryTab"))
        self.layoutWidget_5 = QtGui.QWidget(self.summaryTab)
        self.layoutWidget_5.setGeometry(QtCore.QRect(0, 260, 571, 41))
        self.layoutWidget_5.setObjectName(_fromUtf8("layoutWidget_5"))
        self.horizontalLayout_10 = QtGui.QHBoxLayout(self.layoutWidget_5)
        self.horizontalLayout_10.setMargin(0)
        self.horizontalLayout_10.setObjectName(_fromUtf8("horizontalLayout_10"))
        self.backbtn_3 = QtGui.QPushButton(self.layoutWidget_5)
        self.backbtn_3.setMinimumSize(QtCore.QSize(0, 24))
        icon = QtGui.QIcon.fromTheme(_fromUtf8("back"))
        self.backbtn_3.setIcon(icon)
        self.backbtn_3.setObjectName(_fromUtf8("backbtn_3"))
        self.horizontalLayout_10.addWidget(self.backbtn_3)
        spacerItem9 = QtGui.QSpacerItem(358, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_10.addItem(spacerItem9)
        self.nextbtn_4 = QtGui.QPushButton(self.layoutWidget_5)
        self.nextbtn_4.setMinimumSize(QtCore.QSize(0, 24))
        icon = QtGui.QIcon.fromTheme(_fromUtf8("down"))
        self.nextbtn_4.setIcon(icon)
        self.nextbtn_4.setObjectName(_fromUtf8("nextbtn_4"))
        self.horizontalLayout_10.addWidget(self.nextbtn_4)
        self.layoutWidget_6 = QtGui.QWidget(self.summaryTab)
        self.layoutWidget_6.setGeometry(QtCore.QRect(110, 10, 461, 251))
        self.layoutWidget_6.setObjectName(_fromUtf8("layoutWidget_6"))
        self.verticalLayout_12 = QtGui.QVBoxLayout(self.layoutWidget_6)
        self.verticalLayout_12.setMargin(0)
        self.verticalLayout_12.setObjectName(_fromUtf8("verticalLayout_12"))
        self.verticalLayout_13 = QtGui.QVBoxLayout()
        self.verticalLayout_13.setObjectName(_fromUtf8("verticalLayout_13"))
        self.gridLayout_3 = QtGui.QGridLayout()
        self.gridLayout_3.setSpacing(6)
        self.gridLayout_3.setObjectName(_fromUtf8("gridLayout_3"))
        self.horizontalLayout_11 = QtGui.QHBoxLayout()
        self.horizontalLayout_11.setSpacing(6)
        self.horizontalLayout_11.setContentsMargins(-1, 0, -1, -1)
        self.horizontalLayout_11.setObjectName(_fromUtf8("horizontalLayout_11"))
        self.label_10 = QtGui.QLabel(self.layoutWidget_6)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Maximum, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_10.sizePolicy().hasHeightForWidth())
        self.label_10.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        font.setKerning(True)
        self.label_10.setFont(font)
        self.label_10.setObjectName(_fromUtf8("label_10"))
        self.horizontalLayout_11.addWidget(self.label_10)
        self.target_part_summary = QtGui.QLabel(self.layoutWidget_6)
        self.target_part_summary.setWordWrap(True)
        self.target_part_summary.setObjectName(_fromUtf8("target_part_summary"))
        self.horizontalLayout_11.addWidget(self.target_part_summary)
        self.gridLayout_3.addLayout(self.horizontalLayout_11, 1, 0, 1, 1)
        self.horizontalLayout_15 = QtGui.QHBoxLayout()
        self.horizontalLayout_15.setObjectName(_fromUtf8("horizontalLayout_15"))
        self.verticalLayout_15 = QtGui.QVBoxLayout()
        self.verticalLayout_15.setObjectName(_fromUtf8("verticalLayout_15"))
        self.horizontalLayout_15.addLayout(self.verticalLayout_15)
        spacerItem10 = QtGui.QSpacerItem(128, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_15.addItem(spacerItem10)
        self.ch_rootPart = QtGui.QPushButton(self.layoutWidget_6)
        self.ch_rootPart.setObjectName(_fromUtf8("ch_rootPart"))
        self.horizontalLayout_15.addWidget(self.ch_rootPart)
        self.gridLayout_3.addLayout(self.horizontalLayout_15, 4, 0, 1, 1)
        self.title_5 = QtGui.QLabel(self.layoutWidget_6)
        self.title_5.setTextFormat(QtCore.Qt.AutoText)
        self.title_5.setObjectName(_fromUtf8("title_5"))
        self.gridLayout_3.addWidget(self.title_5, 0, 0, 1, 1)
        self.verticalLayout_13.addLayout(self.gridLayout_3)
        self.gridLayout_5 = QtGui.QGridLayout()
        self.gridLayout_5.setObjectName(_fromUtf8("gridLayout_5"))
        self.horizontalLayout_16 = QtGui.QHBoxLayout()
        self.horizontalLayout_16.setObjectName(_fromUtf8("horizontalLayout_16"))
        self.verticalLayout_16 = QtGui.QVBoxLayout()
        self.verticalLayout_16.setObjectName(_fromUtf8("verticalLayout_16"))
        self.horizontalLayout_16.addLayout(self.verticalLayout_16)
        spacerItem11 = QtGui.QSpacerItem(128, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_16.addItem(spacerItem11)
        self.ch_lang = QtGui.QPushButton(self.layoutWidget_6)
        self.ch_lang.setObjectName(_fromUtf8("ch_lang"))
        self.horizontalLayout_16.addWidget(self.ch_lang)
        self.gridLayout_5.addLayout(self.horizontalLayout_16, 2, 0, 1, 1)
        self.horizontalLayout_12 = QtGui.QHBoxLayout()
        self.horizontalLayout_12.setObjectName(_fromUtf8("horizontalLayout_12"))
        self.label_11 = QtGui.QLabel(self.layoutWidget_6)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Maximum, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_11.sizePolicy().hasHeightForWidth())
        self.label_11.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        self.label_11.setFont(font)
        self.label_11.setObjectName(_fromUtf8("label_11"))
        self.horizontalLayout_12.addWidget(self.label_11)
        self.lang_summary = QtGui.QLabel(self.layoutWidget_6)
        self.lang_summary.setWordWrap(True)
        self.lang_summary.setObjectName(_fromUtf8("lang_summary"))
        self.horizontalLayout_12.addWidget(self.lang_summary)
        self.gridLayout_5.addLayout(self.horizontalLayout_12, 0, 0, 1, 1)
        self.verticalLayout_13.addLayout(self.gridLayout_5)
        self.gridLayout_7 = QtGui.QGridLayout()
        self.gridLayout_7.setObjectName(_fromUtf8("gridLayout_7"))
        self.horizontalLayout_18 = QtGui.QHBoxLayout()
        self.horizontalLayout_18.setObjectName(_fromUtf8("horizontalLayout_18"))
        self.verticalLayout_18 = QtGui.QVBoxLayout()
        self.verticalLayout_18.setObjectName(_fromUtf8("verticalLayout_18"))
        self.horizontalLayout_18.addLayout(self.verticalLayout_18)
        spacerItem12 = QtGui.QSpacerItem(128, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_18.addItem(spacerItem12)
        self.ch_username = QtGui.QPushButton(self.layoutWidget_6)
        self.ch_username.setObjectName(_fromUtf8("ch_username"))
        self.horizontalLayout_18.addWidget(self.ch_username)
        self.gridLayout_7.addLayout(self.horizontalLayout_18, 3, 0, 1, 1)
        self.horizontalLayout_14 = QtGui.QHBoxLayout()
        self.horizontalLayout_14.setObjectName(_fromUtf8("horizontalLayout_14"))
        self.label_13 = QtGui.QLabel(self.layoutWidget_6)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Maximum, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_13.sizePolicy().hasHeightForWidth())
        self.label_13.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        self.label_13.setFont(font)
        self.label_13.setObjectName(_fromUtf8("label_13"))
        self.horizontalLayout_14.addWidget(self.label_13)
        self.user_summary = QtGui.QLabel(self.layoutWidget_6)
        self.user_summary.setWordWrap(True)
        self.user_summary.setObjectName(_fromUtf8("user_summary"))
        self.horizontalLayout_14.addWidget(self.user_summary)
        self.gridLayout_7.addLayout(self.horizontalLayout_14, 0, 0, 1, 1)
        self.verticalLayout_13.addLayout(self.gridLayout_7)
        self.gridLayout_6 = QtGui.QGridLayout()
        self.gridLayout_6.setContentsMargins(-1, -1, -1, 10)
        self.gridLayout_6.setObjectName(_fromUtf8("gridLayout_6"))
        self.horizontalLayout_17 = QtGui.QHBoxLayout()
        self.horizontalLayout_17.setObjectName(_fromUtf8("horizontalLayout_17"))
        self.verticalLayout_17 = QtGui.QVBoxLayout()
        self.verticalLayout_17.setObjectName(_fromUtf8("verticalLayout_17"))
        self.horizontalLayout_17.addLayout(self.verticalLayout_17)
        spacerItem13 = QtGui.QSpacerItem(128, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_17.addItem(spacerItem13)
        self.ch_homePart = QtGui.QPushButton(self.layoutWidget_6)
        self.ch_homePart.setObjectName(_fromUtf8("ch_homePart"))
        self.horizontalLayout_17.addWidget(self.ch_homePart)
        self.gridLayout_6.addLayout(self.horizontalLayout_17, 3, 0, 1, 1)
        self.horizontalLayout_13 = QtGui.QHBoxLayout()
        self.horizontalLayout_13.setObjectName(_fromUtf8("horizontalLayout_13"))
        self.label_12 = QtGui.QLabel(self.layoutWidget_6)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Maximum, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_12.sizePolicy().hasHeightForWidth())
        self.label_12.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        self.label_12.setFont(font)
        self.label_12.setObjectName(_fromUtf8("label_12"))
        self.horizontalLayout_13.addWidget(self.label_12)
        self.home_part_summary = QtGui.QLabel(self.layoutWidget_6)
        self.home_part_summary.setWordWrap(True)
        self.home_part_summary.setObjectName(_fromUtf8("home_part_summary"))
        self.horizontalLayout_13.addWidget(self.home_part_summary)
        self.gridLayout_6.addLayout(self.horizontalLayout_13, 0, 0, 1, 1)
        self.verticalLayout_13.addLayout(self.gridLayout_6)
        self.verticalLayout_12.addLayout(self.verticalLayout_13)
        self.logo_4 = QtGui.QLabel(self.summaryTab)
        self.logo_4.setGeometry(QtCore.QRect(20, 0, 61, 71))
        self.logo_4.setText(_fromUtf8(""))
        self.logo_4.setPixmap(QtGui.QPixmap(_fromUtf8(":/data/img/step.png")))
        self.logo_4.setScaledContents(True)
        self.logo_4.setObjectName(_fromUtf8("logo_4"))
        self.tabWidget.addTab(self.summaryTab, _fromUtf8(""))
        self.steps = QtGui.QLabel(self.centralWidget)
        self.steps.setGeometry(QtCore.QRect(550, 70, 21, 16))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(255, 243, 230))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 243, 230))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 243, 230))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 243, 230))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.ToolTipText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 243, 230))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 243, 230))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 243, 230))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 243, 230))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.ToolTipText, brush)
        brush = QtGui.QBrush(QtGui.QColor(146, 145, 144))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(165, 164, 164))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(151, 150, 149))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 243, 230))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.ToolTipText, brush)
        self.steps.setPalette(palette)
        self.steps.setText(_fromUtf8(""))
        self.steps.setObjectName(_fromUtf8("steps"))
        MainWindow.setCentralWidget(self.centralWidget)

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(1)
        self.grubbox.setCurrentIndex(-1)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "Neptune Installer", None))
        self.quitbtn.setText(_translate("MainWindow", "Quit", None))
        self.nextbtn.setText(_translate("MainWindow", "Next", None))
        self.title.setText(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'DejaVu Sans\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<table style=\"-qt-table-type: root; margin-top:4px; margin-bottom:4px; margin-left:4px; margin-right:4px;\">\n"
"<tr>\n"
"<td style=\"border: none;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:14pt; font-weight:600;\">Welcome</span></p></td></tr></table></body></html>", None))
        self.msg.setText(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Ubuntu\'; font-size:10pt; font-weight:400; font-style:normal;\">\n"
"<table border=\"0\" style=\"-qt-table-type: root; margin-top:4px; margin-bottom:4px; margin-left:4px; margin-right:4px;\">\n"
"<tr>\n"
"<td style=\"border: none;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'DejaVu Sans\'; font-size:9pt;\">This is the Installer for Neptune that allows you to install the system onto your harddrive. </span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:\'DejaVu Sans\'; font-size:9pt;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'DejaVu Sans\'; font-size:11pt; font-weight:600;\">Systemrequirements:</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:\'DejaVu Sans\'; font-size:9pt;\"><br /></p>\n"
"<p align=\"justify\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'DejaVu Sans\'; font-size:9pt;\"> </span><img src=\":/data/img/drive-harddisk32.png\" /><span style=\" font-family:\'DejaVu Sans\'; font-size:9pt;\">    8 GB free disk space</span></p>\n"
"<p align=\"justify\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'DejaVu Sans\'; font-size:9pt;\"> </span><img src=\":/data/img/battery-charging.png\" /><span style=\" font-family:\'DejaVu Sans\'; font-size:9pt;\">    Plugged in power source</span></p>\n"
"<p align=\"justify\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'DejaVu Sans\'; font-size:9pt;\"> </span><img src=\":/data/img/kthesaurus.png\" /><span style=\" font-family:\'DejaVu Sans\'; font-size:9pt;\">    Knowledge about partitioning</span></p></td></tr></table></body></html>", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.welcometab), _translate("MainWindow", "Tab 1", None))
        self.backbtn.setText(_translate("MainWindow", "Back", None))
        self.nextbtn_2.setText(_translate("MainWindow", "Next", None))
        self.title_2.setText(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'DejaVu Sans\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<table border=\"0\" style=\"-qt-table-type: root; margin-top:4px; margin-bottom:4px; margin-left:4px; margin-right:4px;\">\n"
"<tr>\n"
"<td style=\"border: none;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:14pt; font-weight:600;\">User Setup</span></p></td></tr></table></body></html>", None))
        self.msg_2.setText(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'DejaVu Sans\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<table border=\"0\" style=\"-qt-table-type: root; margin-top:4px; margin-bottom:4px; margin-left:4px; margin-right:4px;\">\n"
"<tr>\n"
"<td style=\"border: none;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Please enter the password for the root user.</p></td></tr></table></body></html>", None))
        self.label.setText(_translate("MainWindow", "root password:", None))
        self.label_2.setText(_translate("MainWindow", "confirm root password:", None))
        self.label_4.setText(_translate("MainWindow", "Create a new default user.", None))
        self.sudoEnabled.setText(_translate("MainWindow", "with Super User rights", None))
        self.label_cusername.setText(_translate("MainWindow", "Full Name:", None))
        self.label_3.setText(_translate("MainWindow", "Username:", None))
        self.label_5.setText(_translate("MainWindow", "user password:", None))
        self.label_6.setText(_translate("MainWindow", "confirm user password:", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.usertab), _translate("MainWindow", "Tab 2", None))
        self.backbtn_2.setText(_translate("MainWindow", "Back", None))
        self.nextbtn_3.setText(_translate("MainWindow", "Next", None))
        self.title_3.setText(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'DejaVu Sans\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<table border=\"0\" style=\"-qt-table-type: root; margin-top:4px; margin-bottom:4px; margin-left:4px; margin-right:4px;\">\n"
"<tr>\n"
"<td style=\"border: none;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:14pt; font-weight:600;\">Partitioning</span></p></td></tr></table></body></html>", None))
        self.msg_3.setText(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'DejaVu Sans\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<table border=\"0\" style=\"-qt-table-type: root; margin-top:4px; margin-bottom:4px; margin-left:4px; margin-right:4px;\">\n"
"<tr>\n"
"<td style=\"border: none;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">You need at least 1 partition with 8 GB free disk space formatted in a linux filesystem (ext2/3/4/xfs/jfs).</p></td></tr></table></body></html>", None))
        self.partedbtn.setText(_translate("MainWindow", "Start manual partitioning", None))
        self.refreshBtn.setText(_translate("MainWindow", "Refresh", None))
        self.label_7.setText(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'DejaVu Sans\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<table style=\"-qt-table-type: root; margin-top:4px; margin-bottom:4px; margin-left:4px; margin-right:4px;\">\n"
"<tr>\n"
"<td style=\"border: none;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:600;\">Target Partition:</span></p></td></tr></table></body></html>", None))
        self.formatRootCheck.setText(_translate("MainWindow", "Format target partition", None))
        self.formatCombo.setItemText(0, _translate("MainWindow", "New default (btrfs)", None))
        self.formatCombo.setItemText(1, _translate("MainWindow", "Old default (ext4)", None))
        self.label_8.setText(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'DejaVu Sans\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<table style=\"-qt-table-type: root; margin-top:4px; margin-bottom:4px; margin-left:4px; margin-right:4px;\">\n"
"<tr>\n"
"<td style=\"border: none;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:600;\">Bootloader Target:</span></p></td></tr></table></body></html>", None))
        self.label_9.setText(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'DejaVu Sans\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<table border=\"0\" style=\"-qt-table-type: root; margin-top:4px; margin-bottom:4px; margin-left:4px; margin-right:4px;\">\n"
"<tr>\n"
"<td style=\"border: none;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:600;\">Home Partition:</span></p></td></tr></table></body></html>", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.parttab), _translate("MainWindow", "Seite", None))
        self.backbtn_3.setText(_translate("MainWindow", "Back", None))
        self.nextbtn_4.setText(_translate("MainWindow", "Install", None))
        self.label_10.setText(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'DejaVu Sans\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<table style=\"-qt-table-type: root; margin-top:4px; margin-bottom:4px; margin-left:4px; margin-right:4px;\">\n"
"<tr>\n"
"<td style=\"border: none;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:600;\">Target Partition:</span></p></td></tr></table></body></html>", None))
        self.target_part_summary.setText(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Ubuntu\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<table border=\"0\" style=\"-qt-table-type: root; margin-top:4px; margin-bottom:4px; margin-left:4px; margin-right:4px;\">\n"
"<tr>\n"
"<td style=\"border: none;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'DejaVu Sans\';\">Install onto </span></p></td></tr></table></body></html>", None))
        self.ch_rootPart.setText(_translate("MainWindow", "Change", None))
        self.title_5.setText(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Ubuntu\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<table border=\"0\" style=\"-qt-table-type: root; margin-top:4px; margin-bottom:4px; margin-left:4px; margin-right:4px;\">\n"
"<tr>\n"
"<td style=\"border: none;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'DejaVu Sans\'; font-size:14pt; font-weight:600;\">Summary</span></p></td></tr></table></body></html>", None))
        self.ch_lang.setText(_translate("MainWindow", "Change", None))
        self.label_11.setText(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'DejaVu Sans\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<table style=\"-qt-table-type: root; margin-top:4px; margin-bottom:4px; margin-left:4px; margin-right:4px;\">\n"
"<tr>\n"
"<td style=\"border: none;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:600;\">Language :</span></p></td></tr></table></body></html>", None))
        self.lang_summary.setText(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Ubuntu\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<table border=\"0\" style=\"-qt-table-type: root; margin-top:4px; margin-bottom:4px; margin-left:4px; margin-right:4px;\">\n"
"<tr>\n"
"<td style=\"border: none;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'DejaVu Sans\';\">Use language</span></p></td></tr></table></body></html>", None))
        self.ch_username.setText(_translate("MainWindow", "Change", None))
        self.label_13.setText(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Ubuntu\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<table border=\"0\" style=\"-qt-table-type: root; margin-top:4px; margin-bottom:4px; margin-left:4px; margin-right:4px;\">\n"
"<tr>\n"
"<td style=\"border: none;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'DejaVu Sans\'; font-weight:600;\">User:</span></p></td></tr></table></body></html>", None))
        self.user_summary.setText(_translate("MainWindow", "Create user", None))
        self.ch_homePart.setText(_translate("MainWindow", "Change", None))
        self.label_12.setText(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'DejaVu Sans\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<table border=\"0\" style=\"-qt-table-type: root; margin-top:4px; margin-bottom:4px; margin-left:4px; margin-right:4px;\">\n"
"<tr>\n"
"<td style=\"border: none;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:600;\">Home Partition:</span></p></td></tr></table></body></html>", None))
        self.home_part_summary.setText(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Ubuntu\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<table border=\"0\" style=\"-qt-table-type: root; margin-top:4px; margin-bottom:4px; margin-left:4px; margin-right:4px;\">\n"
"<tr>\n"
"<td style=\"border: none;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'DejaVu Sans\';\">Install onto </span></p></td></tr></table></body></html>", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.summaryTab), _translate("MainWindow", "Seite", None))

import neptuneinstaller_images_rc
