from PySide import QtGui

from . import library

APP_TITLE = 'omnmeta'


class FileView(QtGui.QTableWidget):
    def __init__(self, *args, **kwargs):
        super(FileView, self).__init__(*args, **kwargs)
        self.setColumnCount(2)
        for idx, f in enumerate(library.get()):
            # TODO merge functionality with self.addItem()
            self.insertRow(idx)
            self.setItem(idx, 0, QtGui.QTableWidgetItem(f.name))
            self.setItem(idx, 1, QtGui.QTableWidgetItem(f.path))
        self.horizontalHeader().setStretchLastSection(True)
        self.verticalHeader().hide()

    def addItem(self, obj):
        idx = self.rowCount()
        self.insertRow(idx)
        self.setItem(idx, 0, QtGui.QTableWidgetItem(obj.name))
        self.setItem(idx, 1, QtGui.QTableWidgetItem(obj.path))


class MainWindow(QtGui.QMainWindow):
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)

        self.main_widget = FileView()
        self.setCentralWidget(self.main_widget)
        self.createMenus()
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
