import sys
import csv

from dbjudge import squemaGetter
from dbjudge.connection_manager.manager import Manager
from dbjudge.custom_fakes import custom_loader

from PyQt5.QtCore import QObject, pyqtSlot
from view.load_sql_menu import Load_sql_menu


class Load_custom_types_controller(QObject):
    def __init__(self, view):
        super().__init__()
        self.main_view = view
        # TODO conectar con el menu y cargar desde dbjudge.customfakesloader el csv
        # view.confirm_button.clicked.connect(self.load_csv_types)

    @pyqtSlot(bool)
    def load_csv_types(self):
        for file_path in self.main_view.selected_files:
            print("loading types from {}".format(file_path))
            results = custom_loader.load_csv_fakes(file_path)
            custom_loader.save_to_database(results)
