
from view.qt_view.admin_menu_view import Ui_AdminMenu

from PyQt5.QtWidgets import QWidget


class Admin_menu(Ui_AdminMenu, QWidget):
    def __init__(self, parent):
        super(Admin_menu, self).__init__()

        self.setupUi(parent)
        self.gridLayoutWidget.hide()
