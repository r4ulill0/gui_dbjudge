import asyncio

from view.qt_view.custom_types.load_custom_types_view import Ui_LoadCustomTypesView
from view.load_types.types_table import TypesTable
from PyQt5.QtWidgets import QWidget
from PyQt5.QtWidgets import QFileDialog
from PyQt5.QtCore import pyqtSlot


class Load_custom_types_menu(QWidget, Ui_LoadCustomTypesView):
    def __init__(self):
        super().__init__()

        self.setupUi(self)
        self.table = TypesTable()
        self.table_container.addWidget(self.table)

    @pyqtSlot(bool)
    def file_load(self):
        file_selector = QFileDialog(
            self, 'Open file', "/", "Csv files (*.csv)")

        if file_selector.exec_():
            for file_name in file_selector.selectedFiles():
                with open(file_name) as csv_file:
                    reader = csv_file.read()

    def set_status_text(self, text, success):
        self.status_label.setText(text)
        # TODO COLOR DEL TEXTO
        if success:
            self._temp_format_text()
        else:
            self.status_label.textFormat()

    async def _temp_format_text(self):
        await asyncio.sleep(5)
        self.status_label.textFormat()

    def get_import_file_selector(self):
        file_selector = QFileDialog(
            self, 'Open file', "/", "Csv files (*.csv)")

        return file_selector

    def load_table_values(self, values, number_of_rows, number_of_cols):
        del self.table

        self.table = TypesTable(number_of_rows, number_of_cols)
        self.type_column_container.addWidget(self.table)
        for row, values in enumerate(values):
            for column, cell_value in enumerate(values):
                # self.table.itemAt(row, column).setText(cell_value)
                pass
