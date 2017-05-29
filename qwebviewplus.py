#!/usr/bin/env pythonw
#-*-coding: utf-8 -*-
import sys
import os.path
import re
from optparse import OptionParser
from PyQt5.QtCore import QUrl
from PyQt5.QtWidgets import QApplication, QFileDialog, qApp, QAction, QMainWindow, QStatusBar, QVBoxLayout, QSplitter, QMessageBox, QInputDialog, QLineEdit
from plus.kiwoom import KiwoomWebViewPlus

class Window(QMainWindow):
    def __init__(self):
        super().__init__()
        self.view = KiwoomWebViewPlus()
        self.initUI()

    def menuUI(self):
        openfile_action = QAction('&Open File', self)
        openfile_action.setShortcut('Ctrl+O') 
        openfile_action.setStatusTip('Open files')
        openfile_action.triggered.connect(self.onOpenFile)

        openurl_action = QAction('Open &Url', self)
        openurl_action.setShortcut('Ctrl+U') 
        openurl_action.setStatusTip('Open URL')
        openurl_action.triggered.connect(self.onOpenUrl)
        # exit_action = QAction(QIcon('exit.png'), "&Exit", self)
        
        quit_action = QAction('&Quit', self)
        quit_action.setShortcut('Ctrl+Q') 
        quit_action.setStatusTip('Exit application')
        quit_action.triggered.connect(qApp.quit)

        fileMenu = self.menuBar().addMenu('Menu')
        fileMenu.addAction(openfile_action)
        fileMenu.addAction(openurl_action)
        fileMenu.addAction(quit_action)

    def initUI(self):
        self.setMinimumSize(1024, 640)
        self.setWindowTitle("QWebview-plus for Kiwoom")
        self.setCentralWidget(self.view)

        self.view.statusbar = QStatusBar()
        self.setStatusBar(self.view.statusbar)
        self.view.statusbar.showMessage("[F4키] 개발자 도구, [F5키] 화면 Refresh")
        # self.view.devTool.setVisible(True)
        
        self.menuUI()
        

    def onOpenFile(self, event):
        vOpenfilename = QFileDialog.getOpenFileName(self, 'Open File', filter="*.*")
        if vOpenfilename == "":
            return
        if os.path.isfile(vOpenfilename[0]):
            window.view.load(QUrl.fromLocalFile(vOpenfilename[0]))         

    def onOpenUrl(self, event):
        url, okPressed = QInputDialog.getText(self, "Open URL","인터넷 주소를 입력해주세요", QLineEdit.Normal, "")
        if okPressed and url != "":
            prefix = "" if bool(re.match('^(?:http)s?://', url)) else "http://"
            window.view.load(QUrl(prefix + url))


if __name__ == "__main__":
    #parsing command line arguments
    app = QApplication(sys.argv)
    window = Window()
    window.show()
    sys.exit(app.exec_())
    