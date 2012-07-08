import sys

from PyQt4 import QtGui

from .library import add_file_to_library

APP_TITLE = 'omnmeta'


class AppWindow(QtGui.QWidget):
    def __init__(self, *args, **kwargs):
        super(AppWindow, self).__init__(*args, **kwargs)
        self.setAcceptDrops(True)
        self.initUI()

    def dragEnterEvent(self, evt):
        if evt.mimeData().hasUrls:
            evt.accept()
        else:
            evt.ignore()

    def dropEvent(self, evt):
        if evt.mimeData().hasUrls:
            links = [x.toLocalFile() for x in evt.mimeData().urls()]
            for link in links:
                add_file_to_library(link)
            evt.accept()
        else:
            evt.ignore()

    def initUI(self):
        self.setWindowTitle(APP_TITLE)
        self.show()


def main():
    app = QtGui.QApplication(sys.argv)
    app_window = AppWindow()
    print app_window
    sys.exit(app.exec_())
