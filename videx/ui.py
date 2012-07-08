import sys

from PyQt4 import QtGui

APP_TITLE = 'videx'


class AppWindow(QtGui.QWidget):
    def __init__(self):
        super(AppWindow, self).__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle(APP_TITLE)
        self.show()


def main():
    app = QtGui.QApplication(sys.argv)
    app_window = AppWindow()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
