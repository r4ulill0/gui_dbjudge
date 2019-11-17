import asyncio

from view.qt_view.load_sql_view import Ui_LoadSqlView
from PyQt5.QtWidgets import QWidget
from PyQt5.QtWidgets import QFileDialog
from PyQt5.QtCore import pyqtSlot


class Load_sql_menu(QWidget, Ui_LoadSqlView):
    def __init__(self):
        super().__init__()

        self.setupUi(self)

        self.load_file_button.clicked.connect(self.file_load)

    @pyqtSlot(bool)
    def file_load(self):
        file_selector = QFileDialog(
            self, 'Open file', "/", "Sql files (*.sql)")

        if file_selector.exec_():
            file_names = file_selector.selectedFiles()

            for file_name in file_names:
                with open(file_name) as sql:
                    for line in sql.readlines():
                        self.sql_text_input.appendPlainText(line)

    def get_sql_text(self):
        return self.sql_text_input.toPlainText()

    def set_status_text(self, text, success):
        self.status_label.setText(text)
        # COLOR DEL TEXTO
        if success:
            self._temp_format_text()
        else:
            self.status_label.textFormat()

    async def _temp_format_text(self):
        await asyncio.sleep(5)
        self.status_label.textFormat()
