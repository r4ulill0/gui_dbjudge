from view.qt_view.modify_scene.modify_scene_menu_datagen_view import Ui_ModifySceneMenuDatagen
from PyQt5.QtWidgets import QWidget


class Modify_scene_datagen(QWidget, Ui_ModifySceneMenuDatagen):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
