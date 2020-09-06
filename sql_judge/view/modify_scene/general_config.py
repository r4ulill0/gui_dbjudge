from view.qt_view.modify_scene.general_config_view import Ui_ModifySceneMenuConfig
from PyQt5.QtWidgets import QWidget


class Modify_scene_general_config(QWidget, Ui_ModifySceneMenuConfig):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
