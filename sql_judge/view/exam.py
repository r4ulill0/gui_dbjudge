from view.qt_view.exam.exam_view import Ui_Exam
from PyQt5.QtWidgets import QWidget


class Exam(Ui_Exam, QWidget):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

    def update_current_question(self, question_text):
        self.question.setText(question_text)

    def get_answer_text(self):
        return self.plainTextEdit.toPlainText()

    def set_answer_text(self, text):
        self.plainTextEdit.setPlainText(text)

    def set_console_output(self, text):
        self.database_output.append(text)
