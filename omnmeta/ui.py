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


class MainWindow(QtGui.QMainWindow):
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)

        self.main_widget = ListWidget()
        self.setCentralWidget(self.main_widget)
        self.setAcceptDrops(True)
        self.setWindowTitle(APP_TITLE)

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


def main():
    import sys
    app = QtGui.QApplication(sys.argv)
    mw = MainWindow()
    mw.show()
    sys.exit(app.exec_())
