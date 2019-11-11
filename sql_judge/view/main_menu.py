from view.qt_view.main_menu_view import Ui_MainMenu

from PyQt5.QtWidgets import QWidget


class Main_menu(Ui_MainMenu, QWidget):
    def __init__(self, parent=None):
        super(Main_menu, self).__init__()

        self.setupUi(parent)
        self.gridLayoutWidget.hide()
