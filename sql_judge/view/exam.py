from view.qt_view.exam.exam_view import Ui_Exam
from PyQt5.QtWidgets import QWidget


class Exam(Ui_Exam, QWidget):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

    def update_current_question(self, question_text):
        self.question.setText(question_text)
