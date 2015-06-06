#!/usr/bin/env python
import sys
import re
from PyQt4 import QtCore, QtGui
from PyQt4.QtCore import QObject

from neptuneinstaller_ui import Ui_MainWindow
from os import popen, path, popen2, system

global usernameok, userpwok, rootpwok, errormsg, cusernameOk
usernameok = False
userpwok = False
rootpwok = False
cusernameOk = False
pwerrormsg = "Password missmatch"

global curLang
curLang = QtCore.QLocale.system().name()

class MyForm(QtGui.QMainWindow):
    def __init__(self, parent=None):
        QtGui.QWidget.__init__(self, parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.center()
        self.ui.tabWidget.setCurrentIndex(0)
        self.ui.steps.setText("1/4")
        self.getLinuxPartitions()
        self.connect(self.ui.quitbtn, QtCore.SIGNAL('clicked()'), self.quitbtnClicked)
        self.connect(self.ui.nextbtn, QtCore.SIGNAL('clicked()'), self.nextbtnClicked)
        self.connect(self.ui.nextbtn_2, QtCore.SIGNAL('clicked()'), self.nextbtnClicked)
        self.connect(self.ui.backbtn, QtCore.SIGNAL('clicked()'), self.backbtnClicked)
        self.connect(self.ui.backbtn_2, QtCore.SIGNAL('clicked()'), self.backbtnClicked)
        self.connect(self.ui.partedbtn, QtCore.SIGNAL('clicked()'), self.partedbtnClicked)
        self.connect(self.ui.backbtn_3, QtCore.SIGNAL('clicked()'), self.backbtnClicked)
        self.connect(self.ui.nextbtn_3, QtCore.SIGNAL('clicked()'), self.nextbtnClicked)
        self.connect(self.ui.nextbtn_4, QtCore.SIGNAL('clicked()'), self.installbtnClicked)
        self.connect(self.ui.ch_rootPart, QtCore.SIGNAL('clicked()'), self.backbtnClicked)
        self.connect(self.ui.ch_homePart, QtCore.SIGNAL('clicked()'), self.backbtnClicked)
        self.connect(self.ui.refreshBtn, QtCore.SIGNAL('clicked()'), self.getLinuxPartitions)
        self.connect(self.ui.ch_username, QtCore.SIGNAL('clicked()'), lambda arg=1: self.goToPage(arg))
        self.connect(self.ui.ch_lang, QtCore.SIGNAL('clicked()'), self.languageSelector)
        self.ui.formatRootCheck.stateChanged.connect(self.formatRootClicked)
        self.ui.sudoEnabled.stateChanged.connect(self.sudoEnabledClicked)
        self.ui.formatCombo.currentIndexChanged.connect(self.formatComboChanged)
        #self.connect(self.ui.rootpw3, QtCore.SIGNAL('textChanged()'), self.rootpwCheck) # This does not seem to work why the heck !?
        self.ui.rootpw2.textChanged.connect(self.rootpwCheck)
        self.ui.userpw2.textChanged.connect(self.userpwCheck)
        self.ui.username.textChanged.connect(self.usernameCheck)
        self.ui.cusername.textChanged.connect(self.cusernameCheck)
        self.ui.nextbtn_2.setEnabled(False)
        self.ui.formatRootCheck.setCheckState(QtCore.Qt.Checked)
        
            
    def quitbtnClicked(self):
        sys.exit(0)
        
    def goToPage(self, arg):
        self.ui.tabWidget.setCurrentIndex(arg)
        self.ui.steps.setText(str(arg+1)+"/4")

    def languageSelector(self):
        popen("/usr/bin/language-selector &")

    def formatRootClicked(self, state):
        if state == QtCore.Qt.Checked:
            popen("touch /tmp/neptune-installer-formatRoot.tmp")
        else:
            popen("rm /tmp/neptune-installer-formatRoot.tmp")
            
    def sudoEnabledClicked(self, state):
        if state == QtCore.Qt.Checked:
            popen("rm /tmp/neptune-installer-sudoDisabled.tmp")
        else:
            popen("touch /tmp/neptune-installer-sudoDisabled.tmp")
            
    def formatComboChanged(self, state):
        print state ## DEBUG state = 0 means btrfs, 1 = ext4 state = 2 means f2fs
        if state == 1:
            popen("touch /tmp/neptune-installer-formatRootExt4.tmp")
        elif state == 2:
            popen("touch /tmp/neptune-installer-formatRootF2FS.tmp")
        else:
            popen("rm /tmp/neptune-installer-formatRootF2FS.tmp")
            popen("rm /tmp/neptune-installer-formatRootExt4.tmp")

    def isFormatRootChecked(self):
        if self.ui.formatRootCheck.checkState() == QtCore.Qt.Checked:
            return True
        else:
            return False

    def getLinuxPartitions(self):
	self.ui.targetbox.clear()
	self.ui.homebox.clear()
	self.ui.grubbox.clear()
        self.ui.grubbox.addItem("MBR/EFI", userData = None)
        self.ui.homebox.addItem(QtGui.QApplication.translate("MainWindow", "same as target", None, QtGui.QApplication.UnicodeUTF8))
        linpart = popen("sudo partitions list_possible_root_partitions").readlines()
        for s in linpart:
	  self.ui.targetbox.addItem(s.strip(), userData = None)
	  self.ui.homebox.addItem(s.strip(), userData = None)
	  self.ui.grubbox.addItem(s.strip(), userData = None)

    def cusernameCheck(self):
        global cusernameOk
        new_username = self.ui.cusername.text().split(' ')[0]
        new_username = new_username.toLower()
        new_username = new_username.replace(QtCore.QRegExp('^[^a-z]+'), '')
        new_username = new_username.replace(QtCore.QRegExp('[^-a-z0-9_]'), '')
        self.ui.username.setText(new_username)
        if self.ui.cusername.text().isEmpty() != True:
             cusernameOk = True
    
    def usernameCheck(self):
        global usernameok, userpwok, rootpwok
        rx = QtCore.QRegExp("\\w+");
        validator = QtGui.QRegExpValidator(rx, None);
        self.ui.username.setValidator(validator)
        if self.ui.username.text() == "root":
             pal = QtGui.QPalette(self.ui.username.palette())
             pal.setColor(QtGui.QPalette.Base,QtGui.QColor('red'))
             self.ui.username.setPalette(pal)
             self.ui.nextbtn_2.setEnabled(False)
        elif self.ui.username.text().isEmpty() != True:
             usernameok = True
        else:
             pal = QtGui.QPalette(self.ui.username.palette())
             pal.setColor(QtGui.QPalette.Base,QtGui.QColor('white'))
             self.ui.username.setPalette(pal)
             self.ui.nextbtn_2.setEnabled(True)
             self.installok()

    def rootpwCheck(self):
        global usernameok, userpwok, rootpwok
        if self.ui.rootpw1.text() != self.ui.rootpw2.text():
             pal = QtGui.QPalette(self.ui.rootpw2.palette())
             pal.setColor(QtGui.QPalette.Base,QtGui.QColor('red'))
             self.ui.rootpw2.setPalette(pal)
             self.ui.rootpw2.setToolTip(pwerrormsg)
             #self.ui.rootpw2.palette().setColor(QtGui.QPalette.Base,QtGui.QColor('red')) This does not seem to work, or is buggy or whatever. 
             self.ui.nextbtn_2.setEnabled(False)
        else:
             pal = QtGui.QPalette(self.ui.rootpw2.palette())
             pal.setColor(QtGui.QPalette.Base,QtGui.QColor('white'))
             self.ui.rootpw2.setPalette(pal)
             self.ui.rootpw2.setToolTip("")
             #self.ui.rootpw2.palette().setColor(QtGui.QPalette.Base,QtGui.QColor('white'))
             self.ui.nextbtn_2.setEnabled(True)
             rootpwok = True
             self.installok()

    def userpwCheck(self):
        global usernameok, userpwok, rootpwok
        if self.ui.userpw1.text() != self.ui.userpw2.text():
             pal = QtGui.QPalette(self.ui.userpw2.palette())
             pal.setColor(QtGui.QPalette.Base,QtGui.QColor('red'))
             self.ui.userpw2.setPalette(pal)
             self.ui.userpw2.setToolTip(pwerrormsg)
             #self.ui.userpw2.palette().setColor(QtGui.QPalette.Base,QtGui.QColor('red')) This does not seem to work, or is buggy or whatever. 
             self.ui.nextbtn_2.setEnabled(False)
        else:
             pal = QtGui.QPalette(self.ui.userpw2.palette())
             pal.setColor(QtGui.QPalette.Base,QtGui.QColor('white'))
             self.ui.userpw2.setPalette(pal)
             self.ui.userpw2.setToolTip("")
             #self.ui.userpw2.palette().setColor(QtGui.QPalette.Base,QtGui.QColor('white'))
             self.ui.nextbtn_2.setEnabled(True)
             userpwok = True
             self.installok()

    def installok(self):
        if userpwok == True and rootpwok == True and usernameok == True and cusernameOk == True:
            self.ui.nextbtn_2.setEnabled(True)
        else:
            self.ui.nextbtn_2.setEnabled(False)

    def nextbtnClicked(self):
        CurrentIndex = self.ui.tabWidget.currentIndex()
        self.ui.tabWidget.setCurrentIndex(CurrentIndex + 1)
        self.ui.steps.setText(str(CurrentIndex+2)+"/4")
	if CurrentIndex == 2:   # Load summary page here
            # Load languages from language selector if available
	    if path.exists("/usr/share/language-selector/languages"):
                languages_rev = {}
		file = open('/usr/share/language-selector/languages', "r")
                for line in file:
                    line = line.strip()
                    split = line.split("=")
                    if len(split) == 2:
                        languages_rev[split[0]] = split[1]
                file.close()

                for key in languages_rev.keys():
                    if key.startswith(curLang):
                        lang = languages_rev[key]
            else:
                # Display localization string if we don't have access to languages file
                lang = popen("echo $LANG").readline().strip('\n')
            target = self.ui.targetbox.currentText()
            homepart = self.ui.homebox.currentText()
            tar_part_size = popen("sudo sfdisk -luM | grep " + str(target) + "| awk '{print $4}'").readline().strip('\n')
            tar_fs = "ext4"
            if "ext4" in self.ui.formatCombo.currentText():
                tar_fs = "ext4"
            elif "f2fs" in self.ui.formatCombo.currentText():
                tar_fs = "f2fs"
            elif "btrfs" in self.ui.formatCombo.currentText():
                tar_fs = "btrfs"
	    if self.isFormatRootChecked():
	        self.ui.target_part_summary.setText(QtGui.QApplication.translate("MainWindow", "Format and install onto ", None, QtGui.QApplication.UnicodeUTF8) + str(target) + " (" + tar_part_size + " MB)" + "(" + tar_fs + ")")
            else:
	        self.ui.target_part_summary.setText(QtGui.QApplication.translate("MainWindow", "Install onto ", None, QtGui.QApplication.UnicodeUTF8) + str(target) + " (" + tar_part_size + " MB)")
            if homepart != QtGui.QApplication.translate("MainWindow", "same as target", None, QtGui.QApplication.UnicodeUTF8):
                home_part_size = popen("sudo sfdisk -luM | grep " + str(homepart) + "| awk '{print $4}'").readline().strip('\n')
	        self.ui.home_part_summary.setText(QtGui.QApplication.translate("MainWindow", "Install onto ", None, QtGui.QApplication.UnicodeUTF8) + homepart + " (" + home_part_size + " MB)")
	    else:
	        self.ui.home_part_summary.setText(QtGui.QApplication.translate("MainWindow", "Install onto ", None, QtGui.QApplication.UnicodeUTF8) + target + " (" + tar_part_size + " MB)")
	    self.ui.lang_summary.setText(QtGui.QApplication.translate("MainWindow", "Use language ", None, QtGui.QApplication.UnicodeUTF8) + lang)
	    username = self.ui.cusername.text()
	    self.ui.user_summary.setText(QtGui.QApplication.translate("MainWindow", "Create user ", None, QtGui.QApplication.UnicodeUTF8) + username)
	    self.ui.nextbtn_4.setText(self.tr("Install"))
	    
    def backbtnClicked(self):
        CurrentIndex = self.ui.tabWidget.currentIndex()
        self.ui.tabWidget.setCurrentIndex(CurrentIndex - 1)
        self.ui.steps.setText(str(CurrentIndex)+"/4")
        self.ui.nextbtn_4.setText(self.tr("Next"))

    def installbtnClicked(self):
        target = self.ui.targetbox.currentText()
        grubpart = self.ui.grubbox.currentText()
        homepart = self.ui.homebox.currentText()
        pwd = self.ui.rootpw1.text().toUtf8()
        cuser = self.ui.cusername.text().toUtf8()
        user = self.ui.username.text().toUtf8()
        userpwd = self.ui.userpw1.text().toUtf8()
        if target.length() != 0:
            print "Targetpartition: " + str(target) + "\nGrubpartition: " + str(grubpart) + "\nHomepartition: " + str(homepart) + "\nRootpw: " + str(pwd) + "\nUsername: " + str(user) + "\nUserpw: " + str(userpwd)
            popen("mkdir -p /tmp/neptune-installer/")
            popen("echo '" + str(pwd) + "' > /tmp/neptune-installer/tmp.pwd") 
            popen("echo '" + str(user) +"' > /tmp/neptune-installer/tmp.user")
            popen("echo '" + str(cuser) +"' > /tmp/neptune-installer/tmp.cuser")
            popen("echo '" + str(userpwd) + "' > /tmp/neptune-installer/tmp.userpwd")
            popen("echo '" + str(target) + "' > /tmp/neptune-installer/tmp.hd")
            if homepart != QtGui.QApplication.translate("MainWindow", "same as target", None, QtGui.QApplication.UnicodeUTF8):
                popen("echo '" + str(homepart) + "' > /tmp/neptune-installer/tmp.home")
            if grubpart != "MBR/EFI" and grubpart != "":
                popen("echo '" + str(grubpart) + "' > /tmp/neptune-installer/tmp.grubpart")
            elif grubpart == "":
                popen("touch /tmp/neptune-installer/tmp.grubskip")
            # Disabled for debugging
            if path.exists("/usr/bin/kdialog"):
                print "kdialog available"
                popen("kdesudo /usr/bin/neptune-install.sh &") # 2>&1 | tee -i /tmp/neptune-installer.log &")
            else:
                print "kdialog not available"
                popen2("xhost + && xterm -e '/usr/bin/neptune-install.sh'") # 2>&1 | tee -i /tmp/neptune-installer.log' ")
            sys.exit(0)
        else:
            QtGui.QMessageBox.critical(self, "No Target", self.tr("You need to enter a target for installation"),QtGui.QMessageBox.Ok)
        
    def center(self):
        screen = QtGui.QDesktopWidget().screenGeometry()
        size =  self.geometry()
        self.move((screen.width()-size.width())/2, (screen.height()-size.height())/2)
        
    def partedbtnClicked(self):
        try:
            ramcmd = popen("cat /proc/meminfo | grep MemTotal | cut -d ':' -f 2 | cut -d 'k' -f 1 | sed 's/ //g'")
            ram = str(int(float(ramcmd.readline())/1024))
            if int(ram) < 1000:
                foo = QtGui.QMessageBox.information(self, 'SWAP Warning', self.tr("You are running low on memory we recommened you to create a swap partition"), QtGui.QMessageBox.Ok)
        except:
            print "Could not read memory size. Skipping SWAP Warning test."
        popen("kdesudo gparted")

        

if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)
    translator=QtCore.QTranslator()
    directory="/usr/bin"
    translator.load(directory+"/neptune-installer_ui-"+unicode(QtCore.QLocale.system().name()[:2])+u".qm")
    print ("trying to load localization file "+ directory+"/neptune-installer_ui-"+unicode(QtCore.QLocale.system().name())[:2]+".qm") # Debug only
    app.installTranslator(translator)
    myapp = MyForm()
    myapp.show()
    sys.exit(app.exec_())
