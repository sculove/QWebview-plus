from PyQt5.QtWebEngineWidgets import QWebEngineView, QWebEnginePage, QWebEngineSettings
from PyQt5.QtCore import QUrl

class DevtoolView(QWebEngineView):
    """
    QWebEngineView 커스터마이징
    """
    def __init__(self, port):
        super().__init__()
        self.setPage(QWebEnginePage(self))
        self.load(QUrl("http://127.0.0.1:"+ port))

    def show(self):
        loadScript = """
        document.body.style.visibility = "hidden";
        var items = Array.prototype.slice.call(document.querySelectorAll(".item"));
        var targets = items.filter(v => {
            if(v.title === "Inspectable pages") {
                v.style.display = "none";
                return false;
            } else {
                return true;
            }
        });
        if(targets.length === 1) {
            location.href = targets[0].href;
        } else {
            document.body.style.visibility = "visible";
        }
        """
        self.page().runJavaScript(loadScript)