import sys
import os
import configparser
from PyQt5.QtCore import QObject, pyqtSlot
from dbjudge.connection_manager.manager import Manager


class Main_controller(QObject):
    def __init__(self, view):
        super().__init__()

        self.main_window = view
        config = configparser.ConfigParser()
        dir_cfg = os.path.join(
            sys.path[0],
            'config.ini'
        )
        config.read(dir_cfg)
        self.connection_manager = Manager(
            user=config['DATABASE']['user'],
            password=config['DATABASE']['pass'],
            host=config['DATABASE']['host'],
            database_name=config['DATABASE']['dbname'],
            port=config['DATABASE']['port']
        )
