from view.qt_view.questions.question_row import Ui_QuestionRow

from PyQt5.QtWidgets import QWidget
from PyQt5.QtCore import pyqtSignal


class QuestionRow(QWidget, Ui_QuestionRow):
    row_deletion = pyqtSignal(int)
    keywords_button_clicked = pyqtSignal(int)

    def __init__(self, question, answer, index):
        super().__init__()
        self.setupUi(self)
        self.index = int(index)
        self.question_label.setText(question)
        self.answer_label.setText(answer)
        self.delete_button.clicked.connect(self.delete_click_redirection)
        self.keywords_button.clicked.connect(self.manage_keywords_button)

    def delete_click_redirection(self):
        self.row_deletion.emit(self.index)

    def manage_keywords_button(self):
        self.keywords_button_clicked.emit(self.index)
