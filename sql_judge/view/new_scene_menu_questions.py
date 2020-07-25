from view.qt_view.new_scene_menu_questions_view import Ui_NewSceneMenuQuestions
from view.questions.question_row import QuestionRow
from PyQt5.QtWidgets import QWidget


class New_scene_menu_questions(Ui_NewSceneMenuQuestions, QWidget):
    def __init__(self):
        super().__init__()

        self.setupUi(self)

    def add_question(self, question, answer):
        new_row = QuestionRow(question, answer)
        self.verticalLayout.addWidget(new_row)

    def get_question_text(self):
        return self.question_input.toPlainText()

    def get_answer_text(self):
        return self.answer_input.toPlainText()
