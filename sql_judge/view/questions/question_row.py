from view.qt_view.questions.question_row import Ui_QuestionRow

from PyQt5.QtWidgets import QWidget


class QuestionRow(QWidget, Ui_QuestionRow):
    def __init__(self, question, answer):
        super().__init__()
        self.setupUi(self)

        self.question_label.setText(question)
        self.answer_label.setText(answer)
