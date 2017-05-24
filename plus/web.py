# -*-coding: utf-8 -*-
import logging
from PyQt5.QtWebKitWidgets import QWebView, QWebPage, QWebInspector
from PyQt5.QtWebKit import QWebSettings
from PyQt5.QtWidgets import QShortcut, QDialog, QGridLayout, QWidget
from PyQt5.QtCore import Qt, QDir


class WebViewPlus(QWebView):
    """
    WebView 커스터마이징
     - inspector 추가
     - jsconsole 로그 추가
     - webview에서 document로 이벤트를 발생함.
    """

    customEvent = """
    var event = document.createEvent("CustomEvent");
    event.initCustomEvent("{type}", true, true, {detail} );
    document.dispatchEvent(event);
    """

    def __init__(self):
        super().__init__()
        self.setPage(WebPagePlus())
        self._setupWebview()

    def _setupWebview(self):
        settings = self.settings()
        currentPath = QDir.currentPath()
        settings.setAttribute(QWebSettings.LocalStorageEnabled, True)
        settings.setAttribute(QWebSettings.OfflineStorageDatabaseEnabled, True)
        settings.setAttribute(QWebSettings.OfflineWebApplicationCacheEnabled, True)
        settings.setAttribute(QWebSettings.DnsPrefetchEnabled, True)
        settings.setAttribute(QWebSettings.CSSGridLayoutEnabled, True)
        settings.setAttribute(QWebSettings.JavascriptCanOpenWindows, True)
        settings.setAttribute(QWebSettings.JavascriptCanCloseWindows, True)
        settings.setAttribute(QWebSettings.JavascriptCanAccessClipboard, True)
        settings.setAttribute(QWebSettings.DeveloperExtrasEnabled, True)
        settings.setOfflineStoragePath(currentPath + "/storage/offline")
        settings.setOfflineWebApplicationCachePath(currentPath + "/storage/webcache")
        settings.setLocalStoragePath(currentPath + "/storage/local")
        settings.setOfflineStorageDefaultQuota(5 * 1024 * 1024)
        settings.setOfflineWebApplicationCacheQuota(5 * 1024 * 1024)
        settings.enablePersistentStorage()
        
        """
        F12키를 누르면 "개발자 도구"가 노출됨
        """
        # webinspector
        self.webInspector = QWebInspector(self)
        self.webInspector.setPage(self.page())

        #Keyboard shortcuts
        shortcut = {}
        shortcut['F4'] = QShortcut(self)
        shortcut['F4'].setContext(Qt.ApplicationShortcut)
        shortcut['F4'].setKey(Qt.Key_F4)
        shortcut['F4'].activated.connect(self._toggleInspector)
        #F5 - Page reloading
        shortcut['F5'] = QShortcut(self)
        shortcut['F5'].setKey(Qt.Key_F5)
        shortcut['F5'].activated.connect(self.reload)

        # Devtools
        self.webInspector.setVisible(True)
        self.devTool = QDialog(self)
        self.devTool.setWindowTitle("Development Tool")
        self.devTool.resize(950, 400)
        layout = QGridLayout()
        layout.setContentsMargins(0,0,0,0)
        layout.addWidget(self.webInspector)
        self.devTool.setLayout(layout)

    def _toggleInspector(self):
        """
        F4키를 다시 누르면 "개발자 도구"가 토글됨.
        """
        self.devTool.setVisible(not self.devTool.isVisible())

    # webview의 document에 이벤트를 발생함.
    def fireEvent(self, type, detail):
        self.page().mainFrame().evaluateJavaScript(WebViewPlus.customEvent.format(type=type, detail=detail))


class WebPagePlus(QWebPage):
    """
    javascript 콘솔 메시지를 python logger에 출력
    http://pyqt.sourceforge.net/Docs/PyQt4/qwebpage.html
    """

    def __init__(self, logger=None):
        super().__init__()
        if not logger:
            logger = logging
        self.logger = logger

    def javaScriptConsoleMessage(self, msg, lineNumber, sourceID):
        self.logger.warning("console(%s:%d): %s" % (sourceID, lineNumber, msg))