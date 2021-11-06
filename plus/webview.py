# -*-coding: utf-8 -*-
import logging
from PyQt5.QtWebEngineWidgets import QWebEngineScript, QWebEngineView, QWebEnginePage, QWebEngineSettings
from PyQt5.QtWebChannel import QWebChannel
from plus.kiwoom import Kiwoom
from plus import util

class QWebEngineViewPlus(QWebEngineView):
    """
    QWebEngineView 커스터마이징
    """
    def __init__(self):
        super().__init__()
        self.kiwoom = Kiwoom()
        self.setPage(QWebEnginePagePlus())
        self.loadQwebchannelJs()
        self.setupWebview()
        self.urlChanged.connect(self.OnUrlChanged)

    def OnUrlChanged(self):
        webchannel = QWebChannel(self.page())
        self.page().setWebChannel(webchannel)
        webchannel.registerObject("kiwoom", self.kiwoom)

    def setupWebview(self):
        settings = self.settings()
        settings.setAttribute(QWebEngineSettings.LocalContentCanAccessRemoteUrls, True)
        settings.setAttribute(QWebEngineSettings.SpatialNavigationEnabled, True)
        settings.setAttribute(QWebEngineSettings.HyperlinkAuditingEnabled, True)
        settings.setAttribute(QWebEngineSettings.ScrollAnimatorEnabled, True)
        settings.setAttribute(QWebEngineSettings.PluginsEnabled, True)
        settings.setAttribute(QWebEngineSettings.FullScreenSupportEnabled, True)
        settings.setAttribute(QWebEngineSettings.ScreenCaptureEnabled, True)
        settings.setAttribute(QWebEngineSettings.TouchIconsEnabled, True)
        settings.setAttribute(QWebEngineSettings.FocusOnNavigationEnabled, True)
        settings.setAttribute(QWebEngineSettings.AllowRunningInsecureContent, True)
        settings.setAttribute(QWebEngineSettings.AllowGeolocationOnInsecureOrigins, True)
        settings.setAttribute(QWebEngineSettings.PlaybackRequiresUserGesture, True)
        settings.setAttribute(QWebEngineSettings.JavascriptCanPaste, True)
        settings.setAttribute(QWebEngineSettings.WebRTCPublicInterfacesOnly, True)
        settings.setAttribute(QWebEngineSettings.DnsPrefetchEnabled, True)

    def loadQwebchannelJs(self):
        qwebchannel_js = util.readFile('./js/qwebchannel.js')
        qwebchannel_plus_js = util.readFile('./js/qwebchannel_plus.js')
        script = util.createScript(qwebchannel_js)
        script_plus = util.createScript(qwebchannel_plus_js, QWebEngineScript.DocumentReady)
        self.page().scripts().insert(script)
        self.page().scripts().insert(script_plus)
    
class QWebEnginePagePlus(QWebEnginePage):
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

