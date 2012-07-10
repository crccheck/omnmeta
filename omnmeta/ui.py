import sys

from PySide import QtGui

from . import library

APP_TITLE = 'omnmeta'


class ListWidget(QtGui.QListWidget):
    def __init__(self, *args, **kwargs):
        super(ListWidget, self).__init__(*args, **kwargs)
        for f in library.get():
            self.addItem(f)

    def addItem(self, obj):
        super(ListWidget, self).addItem("{0.name} - {0.path}".format(obj))


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
                    self.main_widget.addItem(obj)
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
        main_widget = ListWidget()
        self.main_widget = main_widget
        return main_widget


def main():
    app = QtGui.QApplication(sys.argv)
    app_window = AppWindow()
    print app_window
    sys.exit(app.exec_())
