#!/usr/bin/env python
#-*-coding: utf-8 -*-
import sys
import os.path
from optparse import OptionParser
from PyQt5.QtCore import QUrl
from PyQt5.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QSplitter, QMessageBox
from plus.kiwoom import KiwoomWebViewPlus

class Window(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setMinimumSize(1024, 640)
        self.setWindowTitle("QWebview-plus for Kiwoom")
        self.view = KiwoomWebViewPlus()
        self.setCentralWidget(self.view)

        self.view.devTool.setVisible(True)

        # view split
        # self.splitter = QSplitter(self)
        # self.splitter.setOrientation(Qt.Horizontal)
        # layout = QVBoxLayout(self)
        # layout.setContentsMargins(0,0,0,0)
        # layout.addWidget(self.splitter)
        # self.splitter.addWidget(self.view)
        # self.splitter.addWidget(self.view.webInspector)
        # self.view.webInspector.setVisible(True)
        # self.splitter.setSizes([640,640])

if __name__ == "__main__":
    #parsing command line arguments
    parser = OptionParser()
    parser.add_option("-f", "--file", action="store", type="string", dest="file", help="시작 파일 경로", default="./index.html")
    (opt, args) = parser.parse_args()

    if os.path.isfile(opt.file):
        app = QApplication(sys.argv)
        window = Window()
        window.view.load(QUrl.fromLocalFile(os.path.join(os.path.dirname( os.path.abspath( __file__ ) ), opt.file)))
        window.show()
        sys.exit(app.exec_())
    else:
        parser.print_help()
        sys.exit()
