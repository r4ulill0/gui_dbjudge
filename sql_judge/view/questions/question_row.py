from view.qt_view.questions.question_row import Ui_QuestionRow

from PyQt5.QtWidgets import QWidget
from PyQt5.QtCore import pyqtSignal


class QuestionRow(QWidget, Ui_QuestionRow):
    row_deletion = pyqtSignal(int)

    def __init__(self, question, answer, index):
        super().__init__()
        self.setupUi(self)
        self.index = int(index)
        self.question_label.setText(question)
        self.answer_label.setText(answer)
        self.delete_button.clicked.connect(self.delete_click_redirection)

    def delete_click_redirection(self):
        self.row_deletion.emit(self.index)
