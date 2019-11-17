import sys
from view.data_generation.table_data_generation_tab import Table_data_generation_tab

from dbjudge import squemaGetter
from dbjudge.connection_manager.manager import Manager

from PyQt5.QtCore import QObject, pyqtSlot


class Data_generation_controller(QObject):
    def __init__(self, view):
        super().__init__()

        self.main_view = view
        self.scene_name = None
        self.context = None

    @pyqtSlot()
    def update_type(self, table, column, new_type):
        self.main_view

    @pyqtSlot(str)
    def load_scene_name(self, scene_name):
        self.scene_name = scene_name

    def load_scene_data(self):
        Manager.singleton_instance.select_database(self.scene_name)
        conn = Manager.singleton_instance.selected_db_connection
        self.context = squemaGetter.create_context(conn)
        self.main_view.tabWidget.clear()
        for index, table in enumerate(self.context.tables):
            new_tab_page = Table_data_generation_tab(
                table)
            self.main_view.tabWidget.addTab(new_tab_page, table.name)
