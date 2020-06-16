from view.qt_view.new_scene_menu_questions_view import Ui_NewSceneMenuQuestions
from PyQt5.QtWidgets import QWidget


class New_scene_menu_questions(Ui_NewSceneMenuQuestions, QWidget):
    def __init__(self):
        super().__init__()

        self.setupUi(self)

    # TODO check if this method is used
    def get_scene_name_text(self):
        return self.scene_name_input_text.text()
