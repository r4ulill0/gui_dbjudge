from PyQt5.QtWidgets import QMainWindow
from PyQt5.QtWidgets import QStackedWidget
from PyQt5.QtCore import pyqtSlot
from PyQt5.QtCore import pyqtSignal

from view.qt_view.main_window_view import Ui_MainWindow
from view.main_menu import Main_menu
from view.admin_menu import Admin_menu
from view.new_scene_menu import New_scene_menu
from view.load_sql_menu import Load_sql_menu
from view.load_custom_types_menu import Load_custom_types_menu
from view.modify_scene_menu import Modify_scene_menu
from view.data_generation_menu import Data_generation_menu
from control.main_controller import Main_controller
from control.load_custom_types_controller import Load_custom_types_controller
from control.load_sql_controller import Load_sql_controller
from control.new_scene_controller import New_scene_controller
from control.modify_scene_controller import Modify_scene_controller
from control.data_generation_controller import Data_generation_controller


class Main_window(QMainWindow, Ui_MainWindow):
    # define signals
    arrived_at_modify_scene = pyqtSignal()
    arrived_at_data_generation = pyqtSignal()
    moved_with_selected_scene = pyqtSignal(str)

    def __init__(self):
        super(Main_window, self).__init__()

        self.setupUi(self)

        # define views
        self.main_menu = Main_menu()
        self.admin_menu = Admin_menu()
        self.load_custom_types_menu = Load_custom_types_menu()
        self.modify_scene_menu = Modify_scene_menu()
        self.new_scene_menu = New_scene_menu()
        self.load_sql_menu = Load_sql_menu()
        self.data_generation_menu = Data_generation_menu()

        # load views in the QStackedWidget
        self.views_stack = QStackedWidget(self)

        self.views_stack.addWidget(self.main_menu)
        self.views_stack.addWidget(self.admin_menu)
        self.views_stack.addWidget(self.load_custom_types_menu)
        self.views_stack.addWidget(self.modify_scene_menu)
        self.views_stack.addWidget(self.new_scene_menu)
        self.views_stack.addWidget(self.load_sql_menu)
        self.views_stack.addWidget(self.data_generation_menu)

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
        self.load_custom_types_controller = Load_custom_types_controller(
            self.load_custom_types_menu)
        self.modify_scene_controller = Modify_scene_controller(
            self.modify_scene_menu)
        self.data_generation_controller = Data_generation_controller(
            self.data_generation_menu)

        # connect signals
        self.arrived_at_modify_scene.connect(
            self.modify_scene_controller.load_scenes)
        self.arrived_at_data_generation.connect(
            self.data_generation_controller.load_scene_data)
        self.moved_with_selected_scene.connect(
            self.load_sql_controller.load_scene_name)
        self.moved_with_selected_scene.connect(
            self.data_generation_controller.load_scene_name)

        # connect transition elements
        self.main_menu.admin_menu_button.clicked.connect(
            self.main_menu_to_admin_menu)
        # self.main_menu.user_menu_button.clicked.connect()
        # self.admin_menu.add_questions_button.clicked.connect()
        # self.admin_menu.administrate_users_button.clicked.connect()
        self.admin_menu.load_custom_fakes_button.clicked.connect(
            self.admin_menu_to_load_custom_types_menu)
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
        self.modify_scene_menu.generate_data_button.clicked.connect(
            self.modify_scene_to_data_generation)
        self.load_sql_menu.return_button.clicked.connect(
            self.load_sql_menu_to_modify_scene)
        self.data_generation_menu.return_button.clicked.connect(
            self.data_generation_to_modify_scene)

        # set first menu visible
        self.setCentralWidget(self.views_stack)
        self.views_stack.setCurrentWidget(self.main_menu)

    @pyqtSlot(bool)
    def main_menu_to_admin_menu(self):
        self.views_stack.setCurrentWidget(self.admin_menu)

    @pyqtSlot(bool)
    def admin_menu_to_main_menu(self):
        self.views_stack.setCurrentWidget(self.main_menu)

    @pyqtSlot(bool)
    def admin_menu_to_new_scene(self):
        self.views_stack.setCurrentWidget(self.new_scene_menu)

    @pyqtSlot(bool)
    def admin_menu_to_load_custom_types_menu(self):
        self.views_stack.setCurrentWidget(self.load_custom_types_menu)

    @pyqtSlot(bool)
    def admin_menu_to_modify_scene_menu(self):
        self.arrived_at_modify_scene.emit()
        self.views_stack.setCurrentWidget(self.modify_scene_menu)

    @pyqtSlot(bool)
    def modify_scene_to_admin_menu(self):
        self.views_stack.setCurrentWidget(self.admin_menu)

    @pyqtSlot(bool)
    def new_scene_to_admin_menu(self):
        self.views_stack.setCurrentWidget(self.admin_menu)

    def new_scene_to_modify_scene(self):
        self.arrived_at_modify_scene.emit()
        self.views_stack.setCurrentWidget(self.modify_scene_menu)

    @pyqtSlot(bool)
    def modify_scene_to_load_sql(self):
        self.moved_with_selected_scene.emit(
            self.modify_scene_menu.get_selected_scene())
        self.views_stack.setCurrentWidget(self.load_sql_menu)

    def modify_scene_to_data_generation(self):
        self.moved_with_selected_scene.emit(
            self.modify_scene_menu.get_selected_scene())
        self.arrived_at_data_generation.emit()
        self.views_stack.setCurrentWidget(self.data_generation_menu)

    def load_sql_menu_to_modify_scene(self):
        self.views_stack.setCurrentWidget(self.modify_scene_menu)

    def data_generation_to_modify_scene(self):
        self.views_stack.setCurrentWidget(self.modify_scene_menu)
