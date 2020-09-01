import os
import csv

from dbjudge import squema_recollector
from dbjudge.custom_fakes import custom_loader

from model.load_types import LoadTypesProcess
from view.load_sql_menu import Load_sql_menu

from PyQt5.QtCore import QObject, pyqtSlot, QModelIndex, Qt


class Load_custom_types_controller(QObject):
    def __init__(self, view):
        super().__init__()
        self.main_view = view
        self.model = LoadTypesProcess()
        self.main_view.table.setModel(self.model)
        self.main_view.table.horizontalHeader().setModel(self.model.header_model)

        self.main_view.load_file_button.clicked.connect(self.import_csv_types)
        self.main_view.add_button.clicked.connect(self.add_row)
        self.main_view.delete_button.clicked.connect(self.delete_selection)
        self.main_view.save_button.clicked.connect(self.save_custom_types)

    def _manage_file_open(self, files):
        if not files:
            text = 'Ningún archivo seleccionado'
        else:
            text = os.path.basename(files[0])
        self.main_view.label.setText(text)

    @pyqtSlot(bool)
    def import_csv_types(self):
        file_selector = self.main_view.get_import_file_selector()

        if file_selector.exec_():
            self.model.beginResetModel()
            self.model.csv_values.clear()
            files = file_selector.selectedFiles()
            self._manage_file_open(files)
            for file_name in files:
                with open(file_name) as csv_file:
                    values = csv.reader(csv_file)
                    for idx, row in enumerate(values):
                        if idx == 0:
                            self.model.header_model.beginResetModel()
                            self.model.header_model.values = row
                            self.model.header_model.endResetModel()
                        else:
                            self.model.csv_values.append(row)
            self.model.endResetModel()

    def add_row(self):
        last_row = self.model.rowCount()
        self.model.insertRows(last_row+1, 1)

    def delete_selection(self):
        selection = self.main_view.table.selectionModel()
        if selection.hasSelection():
            for column in reversed(range(self.model.columnCount())):
                if selection.isColumnSelected(column):
                    self.model.removeColumns(column, 1)
                    self.model.header_model.removeColumn(column)

            for row in reversed(range(self.model.rowCount())):
                if selection.isRowSelected(row):
                    self.model.removeRows(row, 1)

            for cell in selection.selectedIndexes():
                self.model.setData(cell, '', Qt.EditRole)

    def save_custom_types(self):
        custom_loader.save_to_database(
            self.model.csv_values, selected_names=self.model.header_model.values)
        self.model.beginResetModel()
        self.model.header_model.beginResetModel()
        self.model.header_model.values.clear()
        self.model.csv_values.clear()
        self.model.header_model.endResetModel()
        self.model.endResetModel()
        self._manage_file_open(None)
