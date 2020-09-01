from view.qt_view.new_scene_menu_schema_view import Ui_NewSceneMenuSchema
from PyQt5.QtWidgets import QWidget
from PyQt5.QtCore import pyqtSlot


class New_scene_menu_schema(Ui_NewSceneMenuSchema, QWidget):
    def __init__(self):
        super().__init__()

        self.setupUi(self)

    def set_files_selected(self, text):
        self.files_selected_label.setText(text)

    def get_scene_name_text(self):
        return self.scene_name_input.text()

    def get_ddl_text(self):
        return self.text_editor.toPlainText()
