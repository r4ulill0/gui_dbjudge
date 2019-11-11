from view.qt_view.modify_scene_menu_view import Ui_ModifySceneMenu
from PyQt5.QtWidgets import QWidget


class Modify_scene_menu(Ui_ModifySceneMenu, QWidget):
    def __init__(self, parent=None):
        super().__init__()

        self.setupUi(parent)
        self.gridLayoutWidget.hide()

    def load_scenes_combo_box(self, items):
        self.scene_combo_box.clear()
        self.scene_combo_box.addItems(items)
