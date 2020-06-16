from view.qt_view.new_scene_menu_schema_view import Ui_NewSceneMenuSchema
from PyQt5.QtWidgets import QWidget


class New_scene_menu_schema(Ui_NewSceneMenuSchema, QWidget):
    def __init__(self):
        super().__init__()

        self.setupUi(self)

    def get_scene_name_text(self):
        return self.scene_name_input_text.text()
