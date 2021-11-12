#!/usr/bin/env pythonw
# -*-coding: utf-8 -*-
import sys
import os.path
import re
from optparse import OptionParser
from PyQt5.QtCore import QUrl
from PyQt5.QtWidgets import QApplication, QMainWindow, QStatusBar
from plus.widget import MainWidget


class Window(QMainWindow):
    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        self.main = MainWidget()
        self.setMinimumSize(1024, 640)
        self.setWindowTitle("QWebview-plus for Kiwoom")
        self.setGeometry(800, 200, 300, 100)
        self.setCentralWidget(self.main)

        self.statusbar = QStatusBar()
        self.setStatusBar(self.statusbar)
        self.statusbar.showMessage("[F5키] 화면 Refresh, [F12] 개발자 도구")


def main():
    parser = OptionParser()
    parser.add_option(
        "-f",
        "--file",
        action="store",
        type="string",
        dest="file",
        help="시작 파일 경로",
        default="./index.html",
    )
    (opt, args) = parser.parse_args()

    if os.path.isfile(opt.file):
        # application 이 실행하기 전에 port 가 처리되어야 한다.
        os.environ["QTWEBENGINE_REMOTE_DEBUGGING"] = "0.0.0.0:9222"

        app = QApplication(sys.argv)
        window = Window()
        window.main.webview.load(
            QUrl.fromLocalFile(
                os.path.join(os.path.dirname(os.path.abspath(__file__)), opt.file)
            )
        )
        window.show()
        sys.exit(app.exec_())
    else:
        parser.print_help()
        sys.exit()


if __name__ == "__main__":
    main()
