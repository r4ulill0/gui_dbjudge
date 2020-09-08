from view.new_scene.data_generation.table_data_generation_tab import Table_data_generation_tab
from control.new_scene_controller import New_scene_controller
from model.scene import Scene

from dbjudge.connection_manager.manager import Manager
from dbjudge import squema_recollector
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

        self.view_questions.add_question_button.clicked.connect(
            self.add_question)
        self.view_questions.keywords_edition_popped_up.connect(
            self.keywords_edition)
        self.view_questions.scenario_changed.connect(
            self.update_current_scenario)

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
        self.manager.delete_database(self.current_scenario)

    def delete_data(self):
        self.manager.delete_database_data()

    # DATAGEN
    def generate_extra_data(self):
        pass

    def load_datagen_data(self):
        manager = Manager.singleton_instance
        manager.select_database(self.model.name)
        conn = manager.selected_db_connection

        if not self.model.context:
            self.model.context = squema_recollector.create_context(conn)

        self.view_data_gen.tabWidget.clear()
        custom_types = self.manager.get_fake_types()
        for _, table in enumerate(self.model.context.tables):
            new_tab_page = Table_data_generation_tab(
                table, custom_types)
            new_tab_page.table_data_modified.connect(self.update_type)
            self.view_data_gen.tabWidget.addTab(new_tab_page, table.name)

    # QUESTIONS
    def load_questions_data(self):
        pass

    def save_questions(self):
        pass
