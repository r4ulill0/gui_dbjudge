from view.qt_view.new_scene_menu_view import Ui_NewSceneMenu
from PyQt5.QtWidgets import QWidget


class New_scene_menu(Ui_NewSceneMenu, QWidget):
    def __init__(self):
        super().__init__()

        self.setupUi(self)

    def get_scene_name_text(self):
        return self.scene_name_input_text.text()
