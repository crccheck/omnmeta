from PySide.QtCore import (Qt, QAbstractTableModel, QModelIndex)
from PySide import QtGui

from . import library

APP_TITLE = 'omnmeta'


class FileModel(QAbstractTableModel):
    items = []
    list_display = ('name', 'path', 'hash')

    def rowCount(self, index=QModelIndex()):
        return len(self.items)

    def columnCount(self, index=QModelIndex()):
        return len(self.list_display)

    def data(self, index, role=Qt.DisplayRole):
        if not index.isValid():
            return None
        if not 0 <= index.row() < len(self.items):
            return None
        if role == Qt.DisplayRole:
            item = self.items[index.row()]
            return item.get(self.list_display[index.column()])
        return None

    def setData(self, index, value, role=Qt.EditRole):
        if role != Qt.EditRole:
            return False
        if index.isValid and 0 <= index.row() < len(self.items):
            item = self.items[index.row()]
            item[self.list_display[index.column()]] = value
        self.dataChanged.emit(index, index)
        return True

    def headerData(self, section, orientation, role=Qt.DisplayRole):
        if role != Qt.DisplayRole:
            return None
        if orientation == Qt.Horizontal:
            return self.list_display[section]
        return None

    def insertRows(self, position, rows=1, index=QModelIndex()):
        self.beginInsertRows(QModelIndex(), position, position + rows - 1)
        for row in range(rows):
            self.items.insert(position + row, {})
        self.endInsertRows()
        return True

    def removeRows(self, position, rows=1, index=QModelIndex()):
        self.beginRemoveRows(QModelIndex(), position, position + rows - 1)
        del self.items[position:position + rows]
        self.endRemoveRows()
        return True

    # custom methods
    def setItem(self, position, obj):
        """ set item in `position` to correspond to `obj` object """
        for col_idx, label in enumerate(self.list_display):
            ix = self.index(position, col_idx)
            self.setData(ix, getattr(obj, label))

    def insertItem(self, obj):
        """ appends the `obj` to rows """
        row_idx = self.rowCount()
        self.insertRows(row_idx)
        self.setItem(row_idx, obj)


class FileView(QtGui.QTableView):
    def __init__(self, *args, **kwargs):
        super(FileView, self).__init__(*args, **kwargs)
        self.model = FileModel()
        self.setModel(self.model)
        self.verticalHeader().hide()
        self.setSortingEnabled(True)
        self.setSelectionBehavior(QtGui.QAbstractItemView.SelectionBehavior.SelectRows)
        self.resetDisplay()

    def addItem(self, obj):
        self.model.insertItem(obj)

    def resetDisplay(self):
        """ clear all rows and reload data """
        # FIXME conflicts with sorting
        # self.clearContents()
        # self.setRowCount(0)  # not sure why clearContents doesn't also do this
        for f in library.get():
            self.addItem(f)
        self.resizeColumnsToContents()


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
        exitAction.triggered.connect(library.update_hashes)

        reloadAction = QtGui.QAction('Reload', self)
        exitAction.setShortcut('Ctrl+R')
        reloadAction.triggered.connect(self.main_widget.resetDisplay)

        self.toolbar = self.addToolBar('Exit')
        self.toolbar.addAction(exitAction)
        self.toolbar.addAction(reloadAction)

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
