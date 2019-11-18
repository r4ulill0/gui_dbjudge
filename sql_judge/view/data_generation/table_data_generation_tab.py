from view.qt_view.data_generation.tables_data_generation_tab_view import Ui_TablesDataGenerationTab
from .column_data_generation_row import Column_data_generation_row

from dbjudge.structures.table import Table
from PyQt5.QtWidgets import QWidget
from PyQt5.QtCore import pyqtSlot, pyqtSignal


class Table_data_generation_tab(Ui_TablesDataGenerationTab, QWidget):
    table_data_modified = pyqtSignal(str, str, str, str)

    def __init__(self, table):
        super().__init__()

        self.setupUi(self)
        self.table = table
        self.rows = []
        self._load_table(table)

    def _load_table(self, table):
        intermediate_widget = QWidget()
        dark_background = False
        for _, column in table.columns.items():
            new_row = Column_data_generation_row(
                column, dark_background)
            new_row.type_info_modified.connect(self.update_table)
            self.rows.append(new_row)
            self.verticalLayout.addWidget(new_row)
            dark_background = not dark_background

        intermediate_widget.setLayout(self.verticalLayout)
        self.scrollArea.setWidget(intermediate_widget)

    @pyqtSlot(str, str, str)
    def update_table(self, column, ctype, extra_data):
        table = self.table.name
        self.table_data_modified.emit(table, column, ctype, extra_data)
