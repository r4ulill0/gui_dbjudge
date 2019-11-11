
from PyQt5.QtCore import QObject, pyqtSlot
from dbjudge.connection_manager.manager import Manager


class Main_controller(QObject):
    def __init__(self, view, con_user, con_password, con_host, con_database, con_port=None):
        super().__init__()

        self.main_window = view
        self.connection_manager = Manager(
            user=con_user, password=con_password,
            host=con_host, database_name=con_database, port=con_port)

    
