import sys
import os
import configparser
from psycopg2 import Error
from PyQt5.QtCore import QObject, pyqtSlot
from dbjudge.connection_manager.manager import Manager

from view.configuration_dialog import ConfigDialog


class Main_controller(QObject):
    def __init__(self, view):
        super().__init__()

        if getattr(sys, 'frozen', False):
            base_path = os.path.dirname(sys.executable)
        else:
            base_path = sys.path[0]

        self.main_window = view
        config = configparser.ConfigParser()
        dir_cfg = os.path.join(
            base_path,
            'config.ini'
        )

        if not os.path.exists(dir_cfg):
            self.create_config_file(dir_cfg)

        correct_config = False
        first_loop = True

        while not correct_config:
            config.read(dir_cfg)
            if not first_loop:
                config_dialog = ConfigDialog()

                if config_dialog.exec():
                    config['DATABASE']['user'] = config_dialog.get_user()
                    config['DATABASE']['pass'] = config_dialog.get_pass()
                    config['DATABASE']['host'] = config_dialog.get_host()
                    config['DATABASE']['dbname'] = config_dialog.get_dbname()
                    config['DATABASE']['port'] = config_dialog.get_port()
                    config.write(open(dir_cfg, 'w'))
                else:
                    break

            first_loop = False
            try:
                self.connection_manager = Manager(
                    user=config['DATABASE']['user'],
                    password=config['DATABASE']['pass'],
                    host=config['DATABASE']['host'],
                    database_name=config['DATABASE']['dbname'],
                    port=config['DATABASE']['port']
                )
                correct_config = True
            except Error:
                correct_config = False

    def create_config_file(self, path):
        config_file = configparser.ConfigParser()
        config_file['DATABASE'] = {
            'user': '',
            'pass': '',
            'host': '',
            'dbname': '',
            'port': ''
        }
        config_file.write(open(path, 'w'))
