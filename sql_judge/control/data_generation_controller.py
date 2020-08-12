from view.data_generation.table_data_generation_tab import Table_data_generation_tab

from dbjudge import squema_recollector
from dbjudge import filler
from dbjudge.connection_manager.manager import Manager
from dbjudge.structures.fake_types import Regex, Default, Custom

from PyQt5.QtCore import QObject, pyqtSlot


class Data_generation_controller(QObject):
    def __init__(self, view):
        super().__init__()

        self.main_view = view
        self.scene_name = None
        self.context = None

        # TODO enable data generation confirmation with navigation button
        # self.main_view.navbar_questions.clicked.connect(self.generate_data)

    @pyqtSlot(str, str, str, str)
    def update_type(self, table_name, column_name, fake_name, extra_data):
        table = self.context.get_table_by_name(table_name)
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

    @pyqtSlot(str)
    def load_scene_name(self, scene_name):
        self.scene_name = scene_name

    @pyqtSlot(bool)
    def generate_data(self):
        manager = Manager.singleton_instance
        manager.select_database(self.scene_name)
        filler.generate_fake_data(self.context, manager.selected_db_connection)

    def load_scene_data(self):
        Manager.singleton_instance.select_database(self.scene_name)
        conn = Manager.singleton_instance.selected_db_connection
        self.context = squema_recollector.create_context(conn)
        self.main_view.tabWidget.clear()
        for _, table in enumerate(self.context.tables):
            new_tab_page = Table_data_generation_tab(
                table)
            new_tab_page.table_data_modified.connect(self.update_type)
            self.main_view.tabWidget.addTab(new_tab_page, table.name)
