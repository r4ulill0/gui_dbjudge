from PyQt5.QtWidgets import QMainWindow
from PyQt5.QtWidgets import QStackedWidget
from PyQt5.QtCore import pyqtSlot
from PyQt5.QtCore import pyqtSignal

from view.qt_view.main_window_view import Ui_MainWindow
from view.main_menu import Main_menu
from view.user_menu import User_menu
from view.exam import Exam
from view.results import Results
from view.admin_menu import Admin_menu
from view.new_scene.new_scene_menu_schema import New_scene_menu_schema
from view.new_scene.new_scene_menu_datagen import New_scene_menu_datagen
from view.new_scene.new_scene_menu_questions import New_scene_menu_questions
from view.load_custom_types_menu import Load_custom_types_menu
from control.main_controller import Main_controller
from control.exam_controller import Exam_controller
from control.load_custom_types_controller import Load_custom_types_controller
from control.new_scene_controller import New_scene_controller


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
        self.user_menu = User_menu()
        self.exam = Exam()
        self.results = Results()
        self.admin_menu = Admin_menu()
        self.load_custom_types_menu = Load_custom_types_menu()
        self.new_scene_menu_schema = New_scene_menu_schema()
        self.new_scene_menu_datagen = New_scene_menu_datagen()
        self.new_scene_menu_questions = New_scene_menu_questions()

        # load views in the QStackedWidget
        self.views_stack = QStackedWidget(self)

        self.views_stack.addWidget(self.main_menu)
        self.views_stack.addWidget(self.user_menu)
        self.views_stack.addWidget(self.exam)
        self.views_stack.addWidget(self.results)
        self.views_stack.addWidget(self.admin_menu)
        self.views_stack.addWidget(self.load_custom_types_menu)
        self.views_stack.addWidget(self.new_scene_menu_schema)
        self.views_stack.addWidget(self.new_scene_menu_datagen)
        self.views_stack.addWidget(self.new_scene_menu_questions)

        # load controllers
        self.main_controller = Main_controller(self)
        self.exam_controller = Exam_controller(
            self.user_menu, self.exam, self.results)
        self.new_scene_controller = New_scene_controller(
            self.main_controller, self.new_scene_menu_schema, self.new_scene_menu_datagen, self.new_scene_menu_questions)
        self.load_custom_types_controller = Load_custom_types_controller(
            self.load_custom_types_menu)

        # connect signals
        self.arrived_at_data_generation.connect(
            self.new_scene_controller.load_scene_data)

        # connect transition elements
        self.main_menu.user_menu_button.clicked.connect(
            self.main_menu_to_user_menu)
        self.user_menu.access_button.clicked.connect(
            self.user_menu_to_exam)
        self.user_menu.return_button.clicked.connect(
            self.user_menu_to_main_menu)
        self.exam.exit_button.clicked.connect(
            self.exam_to_user_menu)
        self.exam.generate_report_button.clicked.connect(
            self.exam_to_results)
        self.results.return_button.clicked.connect(
            self.results_to_user_menu)
        self.main_menu.admin_menu_button.clicked.connect(
            self.main_menu_to_admin_menu)
        self.admin_menu.create_scene_button.clicked.connect(
            self.admin_menu_to_new_scene)
        self.admin_menu.load_custom_fakes_button.clicked.connect(
            self.admin_menu_to_load_custom_types_menu)
        self.admin_menu.edit_custom_fakes_button.clicked.connect(
            self.admin_menu_to_edit_custom_types_menu)
        self.admin_menu.return_button.clicked.connect(
            self.admin_menu_to_main_menu)
        self.new_scene_menu_schema.return_button.clicked.connect(
            self.new_scene_to_admin_menu)
        self.new_scene_menu_schema.navbar_gen_data.clicked.connect(
            self.news_scene_schema_to_new_scene_datagen)
        self.new_scene_menu_datagen.return_button.clicked.connect(
            self.new_scene_to_admin_menu)
        self.new_scene_menu_datagen.navbar_schema.clicked.connect(
            self.new_scene_menu_datagen_to_schema)
        self.new_scene_menu_datagen.navbar_questions.clicked.connect(
            self.new_scene_menu_datagen_to_questions)
        self.new_scene_menu_questions.navbar_schema.clicked.connect(
            self.new_scene_menu_questions_to_schema)
        self.new_scene_menu_questions.navbar_gen_data.clicked.connect(
            self.new_scene_menu_questions_to_datagen)
        self.new_scene_menu_questions.return_button.clicked.connect(
            self.new_scene_to_admin_menu)
        self.new_scene_menu_questions.finish_button.clicked.connect(
            self.finish_scene_transition)
        self.load_custom_types_menu.return_button.clicked.connect(
            self.load_custom_types_menu_to_admin_menu)

        # set first menu visible
        self.setCentralWidget(self.views_stack)
        self.views_stack.setCurrentWidget(self.main_menu)

    @pyqtSlot(bool)
    def main_menu_to_user_menu(self):
        self.views_stack.setCurrentWidget(self.user_menu)
        self.exam_controller.load_avaiable_scenarios()

    @pyqtSlot(bool)
    def user_menu_to_exam(self):
        self.views_stack.setCurrentWidget(self.exam)

    @pyqtSlot(bool)
    def user_menu_to_main_menu(self):
        self.views_stack.setCurrentWidget(self.main_menu)

    @pyqtSlot(bool)
    def exam_to_user_menu(self):
        self.exam.clear_ui()
        self.views_stack.setCurrentWidget(self.user_menu)

    @pyqtSlot(bool)
    def exam_to_results(self):
        self.views_stack.setCurrentWidget(self.results)

    @pyqtSlot(bool)
    def results_to_user_menu(self):
        self.views_stack.setCurrentWidget(self.user_menu)

    @pyqtSlot(bool)
    def main_menu_to_admin_menu(self):
        self.views_stack.setCurrentWidget(self.admin_menu)

    @pyqtSlot(bool)
    def admin_menu_to_main_menu(self):
        self.views_stack.setCurrentWidget(self.main_menu)

    @pyqtSlot(bool)
    def admin_menu_to_new_scene(self):
        self.views_stack.setCurrentWidget(self.new_scene_menu_schema)

    @pyqtSlot(bool)
    def news_scene_schema_to_new_scene_datagen(self):
        self.arrived_at_data_generation.emit()
        self.views_stack.setCurrentWidget(self.new_scene_menu_datagen)

    @pyqtSlot(bool)
    def admin_menu_to_load_custom_types_menu(self):
        self.load_custom_types_controller.editMode(False)
        self.views_stack.setCurrentWidget(self.load_custom_types_menu)

    @pyqtSlot(bool)
    def admin_menu_to_edit_custom_types_menu(self):
        self.load_custom_types_controller.editMode(True)
        self.views_stack.setCurrentWidget(self.load_custom_types_menu)

    @pyqtSlot(bool)
    def admin_menu_to_create_scene_menu(self):
        self.views_stack.setCurrentWidget(self.modify_scene_menu)

    @pyqtSlot(bool)
    def modify_scene_to_admin_menu(self):
        self.views_stack.setCurrentWidget(self.admin_menu)

    @pyqtSlot(bool)
    def new_scene_to_admin_menu(self):
        self.views_stack.setCurrentWidget(self.admin_menu)

    @pyqtSlot(bool)
    def new_scene_menu_datagen_to_schema(self):
        self.views_stack.setCurrentWidget(self.new_scene_menu_schema)

    @pyqtSlot(bool)
    def new_scene_menu_datagen_to_questions(self):
        self.arrived_at_data_generation.emit()
        self.views_stack.setCurrentWidget(self.new_scene_menu_questions)

    @pyqtSlot(bool)
    def new_scene_menu_questions_to_schema(self):
        self.views_stack.setCurrentWidget(self.new_scene_menu_schema)

    @pyqtSlot(bool)
    def new_scene_menu_questions_to_datagen(self):
        self.views_stack.setCurrentWidget(self.new_scene_menu_datagen)

    @pyqtSlot(bool)
    def finish_scene_transition(self):
        self.new_scene_controller.finish_scene_creation()
        self.views_stack.setCurrentWidget(self.admin_menu)

    def load_custom_types_menu_to_admin_menu(self):
        self.views_stack.setCurrentWidget(self.admin_menu)
