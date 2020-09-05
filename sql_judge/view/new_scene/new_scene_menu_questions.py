from view.qt_view.new_scene.new_scene_menu_questions_view import Ui_NewSceneMenuQuestions
from view.new_scene.questions.question_row import QuestionRow
from PyQt5.QtWidgets import QWidget
from PyQt5.QtCore import pyqtSlot, Qt, pyqtSignal
from PyQt5.QtGui import QPalette


class New_scene_menu_questions(Ui_NewSceneMenuQuestions, QWidget):
    updated_question_data = pyqtSignal(str, str)
    keywords_edition_popped_up = pyqtSignal(int)

    def __init__(self):
        super().__init__()
        self._rows = []
        self._base_color = Qt.gray
        self._dark_color = QPalette().window().color()
        self.setupUi(self)

    def add_question(self, question, answer):
        new_row = QuestionRow(question, answer, len(self._rows))
        new_row.row_deletion.connect(self.delete_question)
        new_row.keywords_button_clicked.connect(self.redirect_keywords_signal)
        self._rows.append(new_row)
        self.verticalLayout.addWidget(new_row)
        self._update_background()

    def _update_background(self):
        dark_background = True
        for row in self._rows:
            row.setAutoFillBackground(True)
            palette = row.palette()
            if dark_background:
                palette.setColor(row.backgroundRole(), self._dark_color)
                row.setPalette(palette)
            else:
                palette.setColor(row.backgroundRole(), self._base_color)
                row.setPalette(palette)
            dark_background = not dark_background

    @pyqtSlot(int)
    def redirect_keywords_signal(self, index):
        self.keywords_edition_popped_up.emit(index)

    @pyqtSlot(int)
    def delete_question(self, index):
        deletion = None
        for idx, row in enumerate(self._rows):
            if idx > index:
                row.index -= 1
            elif idx < index:
                pass
            elif idx == index:
                deletion = idx

        self._rows.pop(deletion)
        self.verticalLayout.takeAt(deletion)
        self._update_background()

    def get_question_text(self):
        return self.question_input.toPlainText()

    def get_answer_text(self):
        return self.answer_input.toPlainText()
