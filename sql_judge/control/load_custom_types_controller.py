import sys
import csv

from dbjudge import squema_recollector
from dbjudge.connection_manager.manager import Manager
from dbjudge.custom_fakes import custom_loader

from model.load_types import LoadTypesProcess
from view.load_sql_menu import Load_sql_menu

from PyQt5.QtCore import QObject, pyqtSlot, QModelIndex


class Load_custom_types_controller(QObject):
    def __init__(self, view):
        super().__init__()
        self.main_view = view
        self.model = LoadTypesProcess()
        self.main_view.table.setModel(self.model)

        self.main_view.load_file_button.clicked.connect(self.import_csv_types)

    @pyqtSlot(bool)
    def import_csv_types(self):
        file_selector = self.main_view.get_import_file_selector()

        if file_selector.exec_():
            for file_name in file_selector.selectedFiles():
                with open(file_name) as csv_file:
                    values = csv.reader(csv_file)
                    for row_id, row in enumerate(values):
                        for col_id, value in enumerate(row):
                            index = self.model.createIndex(row_id, col_id)
                            self.model.setData(index, value)
