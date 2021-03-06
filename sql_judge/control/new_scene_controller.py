import os

from PyQt5.QtCore import QObject, pyqtSlot, pyqtSignal
from PyQt5.QtWidgets import QFileDialog
from dbjudge.connection_manager.manager import Manager
from dbjudge import squema_recollector
from dbjudge.structures.fake_types import Regex, Custom, Default
from view.new_scene.new_scene_menu_schema import New_scene_menu_schema
from view.new_scene.data_generation.table_data_generation_tab import Table_data_generation_tab
from view.new_scene.questions.keywords_popup import KeywordsPopup
from view.progress_dialog import ProgressDialog
from model.scene import Scene
from model.popup_keywords import KeyWordsPopupModel
from control.threading import FinishSceneThread


class New_scene_controller(QObject):
    finished_scene = pyqtSignal()

    def __init__(self, view_schema, view_data_gen, view_questions):
        super().__init__()
        self.view_schema = view_schema
        self.view_data_gen = view_data_gen
        self.view_questions = view_questions
        self.manager = Manager.singleton_instance
        self.model = Scene()
        self.working_thread = None

        self.view_schema.load_file_button.clicked.connect(self.file_load)
        self.view_schema.confirm_button.clicked.connect(self.create_new_scene)
        self.view_questions.add_question_button.clicked.connect(
            self.add_question)
        self.view_questions.keywords_edition_popped_up.connect(
            self.keywords_edition)
        self.new_scene_event()

    def new_scene_event(self):
        self.view_schema.clear()
        self.view_schema.navbar_gen_data.setEnabled(False)
        self.model = Scene()

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

    @pyqtSlot(bool)
    def file_load(self):
        file_selector = QFileDialog(
            self.view_schema, 'Open DDL file', "/", "Sql files (*.sql)")

        if file_selector.exec_():
            file_names = file_selector.selectedFiles()
            base_names = []
            for file_name in file_names:
                base_names.append(os.path.basename(file_name))
                with open(file_name) as sql:
                    for line in sql.readlines():
                        self.view_schema.text_editor.appendPlainText(line)

            if base_names:
                label_text = ', '.join(base_names)
            else:
                label_text = 'Ningún archivo seleccionado'

            self.view_schema.set_files_selected(label_text)

# DATA GENERATION
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

    def load_scene_data(self):

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

    def add_question(self):
        question = self.view_questions.get_question_text()
        answer = self.view_questions.get_answer_text()
        self.model.add_question(question, answer)
        self.view_questions.add_question(question, answer)

    def finish_scene_creation(self):
        self.manager.select_database(self.model.name)
        progress_popup = ProgressDialog()
        self.working_thread = FinishSceneThread(
            self.model, self.manager)
        self.working_thread.progression_made.connect(progress_popup.setValue)
        self.working_thread.category_update.connect(
            progress_popup.setLabelText)
        progress_popup.canceled.connect(self.working_thread.quit)
        self.working_thread.start()
        if progress_popup.exec():
            self.finished_scene.emit()

    @pyqtSlot(int)
    def keywords_edition(self, index):
        keyword_options = ['Obligatorio', 'Prohibido']
        selectable_keywords = self.manager.get_all_keywords()
        popup = KeywordsPopup(keyword_options, selectable_keywords)
        if popup.exec():
            self.model.update_keywords(index, popup.model.return_data())
