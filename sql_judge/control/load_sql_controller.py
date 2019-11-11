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

        view.confirm_button.clicked.connect(self.load_sql_event)

    @pyqtSlot(bool)
    def load_sql_event(self):
        manager = Manager.singleton_instance
        sql = self.main_view.get_sql_text()
        print(sql)
        # context = squemaGetter.create_context(
        #     Manager.singleton_instance.selected_db_connection)
