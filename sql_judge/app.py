import sys

from view.main_window import Main_window

from PyQt5 import QtWidgets
from PyQt5 import uic

app = QtWidgets.QApplication(sys.argv)

mw = Main_window()
mw.show()

app.exit(app.exec())
