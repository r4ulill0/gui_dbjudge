from view.qt_view.modify_scene_menu_view import Ui_ModifySceneMenu
from PyQt5.QtWidgets import QWidget


class Modify_scene_menu(Ui_ModifySceneMenu, QWidget):
    def __init__(self):
        super().__init__()

        self.setupUi(self)

    def load_scenes_combo_box(self, items):
        self.scene_combo_box.clear()
        self.scene_combo_box.addItems(items)

    def get_selected_scene(self):
        scene_name = self.scene_combo_box.currentText()
        return scene_name
