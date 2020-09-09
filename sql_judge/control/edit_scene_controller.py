from view.new_scene.data_generation.table_data_generation_tab import Table_data_generation_tab
from control.new_scene_controller import New_scene_controller
from model.scene import Scene

from dbjudge import filler
from dbjudge.structures.fake_types import Regex, Custom, Default
from dbjudge.connection_manager.manager import Manager
from dbjudge import squema_recollector
from dbjudge.questions.generation import generator
from PyQt5.QtCore import QObject, pyqtSlot


class Edit_scene_controller(New_scene_controller, QObject):
    def __init__(self, config_view, datagen_view, questions_view):
        QObject.__init__(self)

        self.view_config = config_view
        self.view_data_gen = datagen_view
        self.view_questions = questions_view

        self.model = Scene()
        self.manager = Manager.singleton_instance
        self.current_scenario = self.manager.get_databases()[0]

        self.view_config.scenario_changed.connect(self.update_current_scenario)
        self.view_config.delete_data_button.clicked.connect(self.delete_data)
        self.view_config.delete_scenario_button.clicked.connect(
            self.delete_scenario)

        self.view_data_gen.scenario_changed.connect(
            self.update_current_scenario)
        self.view_data_gen.comboBox.currentTextChanged.connect(
            self.load_datagen_data)
        self.view_data_gen.generate_data_button.clicked.connect(
            self.generate_data)

        self.view_questions.add_question_button.clicked.connect(
            self.add_question)
        self.view_questions.keywords_edition_popped_up.connect(
            self.keywords_edition)
        self.view_questions.scenario_changed.connect(
            self.update_current_scenario)
        self.view_questions.comboBox.currentTextChanged.connect(
            self.load_questions_data)
        self.view_questions.save_questions_button.clicked.connect(
            self.save_questions)

    def load_scenarios(self):
        combo_list = self.manager.get_databases()
        self.view_config.load_scenarios(combo_list)
        self.view_data_gen.load_scenarios(combo_list)
        self.view_questions.load_scenarios(combo_list)

    @pyqtSlot(str)
    def update_current_scenario(self, scenario):
        self.current_scenario = scenario
        self.model.name = scenario
        self.view_config.setCurrentScenario(scenario)
        self.view_data_gen.setCurrentScenario(scenario)
        self.view_questions.setCurrentScenario(scenario)

    # CONFIG

    def delete_scenario(self):
        self.manager.selected_db_connection.close()
        self.manager.selected_db_connection = None
        self.manager.delete_database(self.current_scenario)
        self.load_scenarios()

    def delete_data(self):
        self.manager.delete_database_data()

    # DATAGEN
    @pyqtSlot(str, str, str, tuple)
    def update_type(self, table_name, column_name, fake_name, extra_data):
        table = self.model.context.get_table_by_name(table_name)
        column = table.columns[column_name]
        del column.fake_type
        column.max_char_len = None
        fake_type = None
        if fake_name == 'regex':
            fake_type = Regex(extra_data[0])
            column.max_char_len = int(extra_data[1]) if extra_data[1] else None
        elif fake_name == 'custom':
            fake_type = Custom(extra_data[0])
        else:
            fake_type = Default()
            max_value = extra_data[0]
            min_value = extra_data[1]
            max_char_len = extra_data[2]
            column.max_value = max_value if max_value else None
            column.min_value = min_value if min_value else None
            column.max_char_len = max_char_len if max_char_len else None

        column.fake_type = fake_type

    @pyqtSlot(bool)
    def generate_data(self):
        manager = Manager.singleton_instance
        manager.select_database(self.model.name)
        filler.generate_fake_data(
            self.model.context, manager.selected_db_connection)

    def load_datagen_data(self):
        if self.model.name:
            manager = Manager.singleton_instance
            manager.select_database(self.model.name)
            conn = manager.selected_db_connection

            self.model.context = squema_recollector.create_context(conn)

            self.view_data_gen.tabWidget.clear()
            custom_types = self.manager.get_fake_types()
            for _, table in enumerate(self.model.context.tables):
                new_tab_page = Table_data_generation_tab(
                    table, custom_types)
                new_tab_page.table_data_modified.connect(self.update_type)
                self.view_data_gen.tabWidget.addTab(new_tab_page, table.name)

    # QUESTIONS
    def add_question(self, question_input=None, answer_input=None):
        question = question_input if question_input else self.view_questions.get_question_text()
        answer = answer_input if answer_input else self.view_questions.get_answer_text()
        self.model.add_question(question, answer)
        self.view_questions.add_question(question, answer)

    def load_questions_data(self):
        if self.model.name:
            self.model.questions = []
            self.model.keywords = []
            self.view_questions.reset_questions()
            self.manager.select_database(self.model.name)
            questions = self.manager.get_questions()
            for question in questions:
                answer = self.manager.get_correct_answer(question)
                self.add_question(question, answer)

    def save_questions(self):
        for index, (question, query) in enumerate(self.model.questions):
            generator.create_question(
                self.model.name,
                query,
                question,
                self.model.context,
                self.model.get_formatted_keywords(index))
