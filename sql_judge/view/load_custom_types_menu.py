import asyncio

from view.qt_view.load_sql_view import Ui_LoadSqlView
from PyQt5.QtWidgets import QWidget
from PyQt5.QtWidgets import QFileDialog
from PyQt5.QtCore import pyqtSlot


class Load_custom_types_menu(QWidget, Ui_LoadSqlView):
    def __init__(self):
        super().__init__()

        self.selected_files = None
        self.setupUi(self)

        self.load_file_button.clicked.connect(self.file_load)

    @pyqtSlot(bool)
    def file_load(self):
        file_selector = QFileDialog(
            self, 'Open file', "/", "Csv files (*.csv)")

        if file_selector.exec_():
            self.selected_files = file_selector.selectedFiles()

            for file_name in self.selected_files:
                print(file_name)
                # customloader.loadfakes(filename)

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
