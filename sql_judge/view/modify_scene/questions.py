from view.qt_view.modify_scene.modify_scene_menu_questions_view import Ui_ModifySceneMenuQuestions
from view.new_scene.questions.question_row import QuestionRow
from PyQt5.QtWidgets import QWidget
from PyQt5.QtCore import pyqtSlot, Qt, pyqtSignal
from PyQt5.QtGui import QPalette


class Modify_scene_questions(QWidget, Ui_ModifySceneMenuQuestions):
    updated_question_data = pyqtSignal(str, str)
    keywords_edition_popped_up = pyqtSignal(int)
    scenario_changed = pyqtSignal(str)

    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.comboBox.currentTextChanged.connect(self.handle_scenario_change)

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

    def load_scenarios(self, scenarios):
        self.comboBox.clear()
        for scenario in scenarios:
            self.comboBox.addItem(scenario)

    def handle_scenario_change(self):
        scenario = self.comboBox.currentText()
        self.scenario_changed.emit(scenario)

    def setCurrentScenario(self, scenario):
        index = self.comboBox.findText(scenario)
        self.comboBox.setCurrentIndex(index)
