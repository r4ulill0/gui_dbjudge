import sys

from dbjudge import squemaGetter
from dbjudge.connection_manager.manager import Manager

from PyQt5.QtCore import QObject, pyqtSlot
from view.load_sql_menu import Load_sql_menu


class Load_sql_controller(QObject):
    def __init__(self, view):
        super().__init__()
        self.main_view = view

        self.named = False
        self.sql_loaded = False
        self.scene_name = None

        view.confirm_button.clicked.connect(self.load_sql_event)

    @pyqtSlot(bool)
    def load_sql_event(self):
        manager = Manager.singleton_instance
        sql = self.main_view.get_sql_text()

        try:
            manager.select_database(self.scene_name)
            manager.execute_sql(sql)
            manager.selected_db_connection.commit()
            self.main_view.set_status_text(
                "Exito! cargado en {}".format(self.scene_name), True)
        except:
            self.main_view.set_status_text(
                "Ocurrió un error inesperado: {}".format(sys.exc_info()), False)

    @pyqtSlot(str)
    def load_scene_name(self, name):
        self.scene_name = name
