from PyQt5.QtWidgets import QMainWindow
from PyQt5.QtCore import pyqtSlot

from view.qt_view.main_window_view import Ui_MainWindow
from view.main_menu import Main_menu
from view.admin_menu import Admin_menu
from view.new_scene_menu import New_scene_menu
from view.load_sql_menu import Load_sql_menu
from view.modify_scene_menu import Modify_scene_menu
from control.main_controller import Main_controller
from control.load_sql_controller import Load_sql_controller
from control.new_scene_controller import New_scene_controller


class Main_window(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super(Main_window, self).__init__()

        self.setupUi(self)

        # load views
        self.main_menu = Main_menu(self.frame)
        self.admin_menu = Admin_menu(self.frame)
        self.modify_scene_menu = Modify_scene_menu(self.frame)
        self.new_scene_menu = New_scene_menu(self.frame)
        self.load_sql_menu = Load_sql_menu(self.frame)

        # load controllers
        self.main_controller = Main_controller(self,
                                               'conexion',
                                               'plsL3tM3in',
                                               'localhost',
                                               'main_tfg'
                                               )
        self.load_sql_controller = Load_sql_controller(self.load_sql_menu)
        self.new_scene_controller = New_scene_controller(
            self.main_controller, self.new_scene_menu)

        # connect transition elements
        self.main_menu.admin_menu_button.clicked.connect(
            self.main_menu_to_admin_menu)
        # self.main_menu.user_menu_button.clicked.connect()
        # self.admin_menu.add_questions_button.clicked.connect()
        # self.admin_menu.administrate_users_button.clicked.connect()
        self.admin_menu.administrate_scenes_button.clicked.connect(
            self.admin_menu_to_modify_scene_menu)
        self.admin_menu.return_button.clicked.connect(
            self.admin_menu_to_main_menu)
        self.admin_menu.new_scene_button.clicked.connect(
            self.admin_menu_to_new_scene)
        self.new_scene_menu.return_button.clicked.connect(
            self.new_scene_to_admin_menu)
        self.modify_scene_menu.return_button.clicked.connect(
            self.modify_scene_to_admin_menu)
        self.modify_scene_menu.load_sql_button.clicked.connect(
            self.modify_scene_to_load_sql)

        # set first menu visible
        self.main_menu.gridLayoutWidget.show()

    @pyqtSlot(bool)
    def main_menu_to_admin_menu(self):
        self.main_menu.gridLayoutWidget.hide()
        self.admin_menu.gridLayoutWidget.show()

    @pyqtSlot(bool)
    def admin_menu_to_main_menu(self):
        self.admin_menu.gridLayoutWidget.hide()
        self.main_menu.gridLayoutWidget.show()

    @pyqtSlot(bool)
    def admin_menu_to_new_scene(self):
        self.admin_menu.gridLayoutWidget.hide()
        self.new_scene_menu.gridLayoutWidget.show()

    @pyqtSlot(bool)
    def admin_menu_to_modify_scene_menu(self):
        self.admin_menu.gridLayoutWidget.hide()
        self.modify_scene_menu.gridLayoutWidget.show()

    @pyqtSlot(bool)
    def modify_scene_to_admin_menu(self):
        self.modify_scene_menu.gridLayoutWidget.hide()
        self.admin_menu.gridLayoutWidget.show()

    @pyqtSlot(bool)
    def new_scene_to_admin_menu(self):
        self.new_scene_menu.gridLayoutWidget.hide()
        self.admin_menu.gridLayoutWidget.show()

    def new_scene_to_modify_scene(self):
        self.new_scene_menu.gridLayoutWidget.hide()
        self.modify_scene_menu.gridLayoutWidget.show()

    @pyqtSlot(bool)
    def modify_scene_to_load_sql(self):
        self.modify_scene_menu.gridLayoutWidget.hide()
        self.load_sql_menu.gridLayoutWidget.show()
