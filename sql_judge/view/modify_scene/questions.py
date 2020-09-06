from view.qt_view.modify_scene.modify_scene_menu_questions_view import Ui_ModifySceneMenuQuestions
from PyQt5.QtWidgets import QWidget


class Modify_scene_questions(QWidget, Ui_ModifySceneMenuQuestions):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
