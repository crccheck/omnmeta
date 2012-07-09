import sys

from PyQt4 import QtGui

from . import library

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
                obj, created = library.add(link)
                if created:
                    self.main_list.addItem(str(obj))
                # from pdb4qt import set_trace; set_trace()
            evt.accept()
        else:
            evt.ignore()

    def initUI(self):
        hbox = QtGui.QHBoxLayout(self)
        w = self.init_main_list()
        hbox.addWidget(w)
        self.setLayout(hbox)
        self.setWindowTitle(APP_TITLE)
        self.show()

    def init_main_list(self):
        file_list = QtGui.QListWidget()
        for f in library.get():
            file_list.addItem("%s" % f)
        self.main_list = file_list
        return file_list


def main():
    app = QtGui.QApplication(sys.argv)
    app_window = AppWindow()
    print app_window
    sys.exit(app.exec_())
