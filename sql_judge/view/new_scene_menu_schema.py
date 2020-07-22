from view.qt_view.new_scene_menu_schema_view import Ui_NewSceneMenuSchema
from PyQt5.QtWidgets import QWidget
from PyQt5.QtWidgets import QFileDialog
from PyQt5.QtCore import pyqtSlot


class New_scene_menu_schema(Ui_NewSceneMenuSchema, QWidget):
    def __init__(self):
        super().__init__()

        self.setupUi(self)
        self.load_file_button.clicked.connect(self.file_load)

    def get_scene_name_text(self):
        return self.scene_name_input.text()

    @pyqtSlot(bool)
    def file_load(self):
        file_selector = QFileDialog(
            self, 'Open DDL file', "/", "Sql files (*.sql)")

        if file_selector.exec_():
            file_names = file_selector.selectedFiles()

            for file_name in file_names:
                with open(file_name) as sql:
                    for line in sql.readlines():
                        self.text_editor.appendPlainText(line)

    def get_ddl_text(self):
        return self.text_editor.toPlainText()
