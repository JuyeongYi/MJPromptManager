from PySide6 import QtWidgets
from MJPromptMaker.MainWindow import MjPrmptBuilder

if __name__ == '__main__':
    # show the window
    app = QtWidgets.QApplication([])

    window = MjPrmptBuilder()
    window.showMaximized()
    app.exec()
