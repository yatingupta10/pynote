# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'edytor.ui'
#
# Created: Sat May  5 18:01:07 2007
#      by: PyQt4 UI code generator 4.1.1
#
# WARNING! All changes made in this file will be lost!

# Created by Yatin Gupta
# github username : yatingupta10
# website : http://www.yatingupta.me/

import sys
from PyQt4 import QtCore, QtGui

class Ui_notepad(object):
    def setupUi(self, notepad):
        notepad.setObjectName("notepad")
        notepad.resize(QtCore.QSize(QtCore.QRect(0,0,560,336).size()).expandedTo(notepad.minimumSizeHint()))

        self.centralwidget = QtGui.QWidget(notepad)
        self.centralwidget.setObjectName("centralwidget")

        self.gridlayout = QtGui.QGridLayout(self.centralwidget)
        self.gridlayout.setMargin(9)
        self.gridlayout.setSpacing(6)
        self.gridlayout.setObjectName("gridlayout")

        self.editor_window = QtGui.QTextEdit(self.centralwidget)
        self.editor_window.setObjectName("editor_window")
        self.gridlayout.addWidget(self.editor_window,1,0,1,3)

        self.pushButton_2 = QtGui.QPushButton(self.centralwidget)
        self.pushButton_2.setObjectName("pushButton_2")
        self.gridlayout.addWidget(self.pushButton_2,0,2,1,1)

        self.button_save = QtGui.QPushButton(self.centralwidget)
        self.button_save.setObjectName("button_save")
        self.gridlayout.addWidget(self.button_save,0,1,1,1)

        self.button_open = QtGui.QPushButton(self.centralwidget)
        self.button_open.setObjectName("button_open")
        self.gridlayout.addWidget(self.button_open,0,0,1,1)
        notepad.setCentralWidget(self.centralwidget)

        self.menubar = QtGui.QMenuBar(notepad)
        self.menubar.setGeometry(QtCore.QRect(0,0,560,26))
        self.menubar.setObjectName("menubar")
        notepad.setMenuBar(self.menubar)

        self.statusbar = QtGui.QStatusBar(notepad)
        self.statusbar.setObjectName("statusbar")
        notepad.setStatusBar(self.statusbar)

        self.retranslateUi(notepad)
        QtCore.QObject.connect(self.pushButton_2,QtCore.SIGNAL("clicked()"),notepad.close)
        QtCore.QMetaObject.connectSlotsByName(notepad)

    def retranslateUi(self, notepad):
        notepad.setWindowTitle(QtGui.QApplication.translate("notepad", "notepad", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton_2.setText(QtGui.QApplication.translate("notepad", "Close", None, QtGui.QApplication.UnicodeUTF8))
        self.button_save.setText(QtGui.QApplication.translate("notepad", "Save", None, QtGui.QApplication.UnicodeUTF8))
        self.button_open.setText(QtGui.QApplication.translate("notepad", "Open", None, QtGui.QApplication.UnicodeUTF8))

