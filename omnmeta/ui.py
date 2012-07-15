from PySide import QtGui

from . import library

APP_TITLE = 'omnmeta'


class FileView(QtGui.QTableWidget):
    list_display = ('name', 'path', 'hash')

    def __init__(self, *args, **kwargs):
        super(FileView, self).__init__(*args, **kwargs)
        self.setColumnCount(len(self.list_display))
        for f in library.get():
            self.addItem(f)
        self.horizontalHeader().setStretchLastSection(True)
        self.verticalHeader().hide()
        self.setHorizontalHeaderLabels(self.list_display)
        self.setSortingEnabled(True)
        self.setSelectionBehavior(QtGui.QAbstractItemView.SelectionBehavior.SelectRows)

    def addItem(self, obj):
        idx = self.rowCount()
        self.insertRow(idx)
        for col_i, label in enumerate(self.list_display):
            self.setItem(idx, col_i, QtGui.QTableWidgetItem(getattr(obj, label)))


class MainWindow(QtGui.QMainWindow):
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)

        self.main_widget = FileView()
        self.setCentralWidget(self.main_widget)
        self.createMenus()
        self.createToolbars()
        self.setAcceptDrops(True)
        self.setWindowTitle(APP_TITLE)
        self.resize(640, 480)

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

    def createMenus(self):
        # Create the main menuBar menu items
        fileMenu = self.menuBar().addMenu("&File")

        # Populate the File menu
        # fileMenu.addSeparator()
        self.createAction("E&xit", fileMenu, self.close)

    def createToolbars(self):
        exitAction = QtGui.QAction('Rescan MD5', self)
        # exitAction = QtGui.QAction(QtGui.QIcon('exit24.png'), 'Exit', self)
        # exitAction.setShortcut('Ctrl+R')
        exitAction.triggered.connect(library.update_hashes)

        self.toolbar = self.addToolBar('Exit')
        self.toolbar.addAction(exitAction)

    def createAction(self, text, menu, slot):
        """ Helper function to save typing when populating menus
            with action.
        """
        action = QtGui.QAction(text, self)
        menu.addAction(action)
        action.triggered.connect(slot)
        return action


def main():
    import sys
    app = QtGui.QApplication(sys.argv)
    mw = MainWindow()
    mw.show()
    sys.exit(app.exec_())
