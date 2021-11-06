

from PyQt5.QtWidgets import QHBoxLayout, QShortcut, QWidget
from plus.webview import WebViewPlus
from plus.devtoolView import DevtoolView
from PyQt5.QtCore import Qt

class MainWidget(QWidget):
    def __init__(self):
        super().__init__()
        self.webview = WebViewPlus()
        self.devtool = DevtoolView()
        self.initUI()
        self.setShortcut()
        
    def initUI(self):
        layout = QHBoxLayout()
        layout.setContentsMargins(0, 0, 0, 0)
        layout.addWidget(self.webview)
        layout.addWidget(self.devtool)
        self.setLayout(layout)

    def setShortcut(self):
        #Keyboard shortcuts
        shortcut = {}
        
        #F5 - Page reloading
        shortcut['F5'] = QShortcut(self)
        shortcut['F5'].setKey(Qt.Key_F5)
        shortcut['F5'].activated.connect(self.webview.reload)
        
        shortcut['F12'] = QShortcut(self)
        shortcut['F12'].setKey(Qt.Key_F12)
        shortcut['F12'].activated.connect(self.toggleDevTool)


    def toggleDevTool(self):
        """
        F12키를 다시 누르면 "개발자 도구"가 사라짐
        """
        if not self.devtool.isVisible():
            self.devtool.show()
        self.devtool.setVisible(not self.devtool.isVisible())