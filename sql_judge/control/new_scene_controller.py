from PyQt5.QtCore import QObject, pyqtSlot
from dbjudge.connection_manager.manager import Manager
from dbjudge import filler
from dbjudge import squema_recollector
from dbjudge.structures.fake_types import Regex, Custom, Default
from view.new_scene_menu_schema import New_scene_menu_schema
from view.data_generation.table_data_generation_tab import Table_data_generation_tab
from model.scene import Scene


class New_scene_controller(QObject):
    def __init__(self, controller, view_schema, view_data_gen, view_questions):
        super().__init__()
        self.main_controller = controller
        self.view_schema = view_schema
        self.view_data_gen = view_data_gen
        self.view_questions = view_questions
        self.manager = Manager.singleton_instance
        self.model = Scene()

        self.view_schema.confirm_button.clicked.connect(self.create_new_scene)
        self.view_questions.add_question_button.clicked.connect(
            self.add_question)
        self.view_questions.finish_button.clicked.connect(
            self.finish_scene_creation)
        self.new_scene_event()

    def new_scene_event(self):
        self.view_schema.navbar_gen_data.setEnabled(False)

# SCHEMA
    @pyqtSlot(bool)
    def create_new_scene(self):
        scene_name = self.view_schema.get_scene_name_text()
        scene_ddl = self.view_schema.get_ddl_text()
        self.model.name = scene_name
        self.model.loaded_sql = scene_ddl

        self.manager.create_database(scene_name)
        self.manager.select_database(scene_name)
        self.manager.execute_sql(scene_ddl)
        self.manager.selected_db_connection.commit()
        self.view_schema.navbar_gen_data.setEnabled(True)

# DATA GENERATION
    @pyqtSlot(str, str, str, str)
    def update_type(self, table_name, column_name, fake_name, extra_data):
        table = self.model.context.get_table_by_name(table_name)
        column = table.columns[column_name]
        del column.fake_type
        fake_type = None
        if fake_name == 'regex':
            fake_type = Regex(extra_data)
        elif fake_name == 'custom':
            fake_type = Custom(extra_data)
        else:
            fake_type = Default()
        column.fake_type = fake_type

    @pyqtSlot(bool)
    def generate_data(self):
        manager = Manager.singleton_instance
        manager.select_database(self.model.name)
        filler.generate_fake_data(
            self.model.context, manager.selected_db_connection)

    def load_scene_data(self):

        manager = Manager.singleton_instance
        manager.select_database(self.model.name)
        conn = manager.selected_db_connection

        if not self.model.context:
            self.model.context = squema_recollector.create_context(conn)

        self.view_data_gen.tabWidget.clear()
        for index, table in enumerate(self.model.context.tables):
            new_tab_page = Table_data_generation_tab(
                table)
            new_tab_page.table_data_modified.connect(self.update_type)
            self.view_data_gen.tabWidget.addTab(new_tab_page, table.name)

# QUESTIONS

    def add_question(self):
        question = self.view_questions.get_question_text()
        answer = self.view_questions.get_answer_text()
        self.model.questions.append((question, answer))
        self.view_questions.add_question(question, answer)

    def finish_scene_creation(self):
        # TODO progress popup
        filler.generate_fake_data(
            self.model.context, self.manager.selected_db_connection)
