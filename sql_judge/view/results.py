from view.qt_view.exam.results_view import Ui_Results
from PyQt5.QtWidgets import QWidget, QListWidgetItem
from PyQt5.QtGui import QIcon


class Results(Ui_Results, QWidget):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

    def update_total_count(self, correct_count, total_count):
        text = '{}/{}'.format(correct_count, total_count)
        self.total_result_label.setText(text)

    def update_current_question(self, new_question):
        self.question.setText(new_question)

    def update_correct_result(self, result):
        text = 'Correcto' if result else 'Incorrecto'
        color = 'green' if result else 'red'
        self.correct_result_label.setStyleSheet('color: {}'.format(color))
        self.correct_result_label.setText(text)

    def update_correct_answer(self, result):
        text = 'Si' if result else 'No'
        color = 'green' if result else 'red'
        self.correct_answer_label.setStyleSheet('color: {}'.format(color))
        self.correct_answer_label.setText(text)

    def update_excess_tables(self, tables):
        self.excess_tables_list.clear()
        for table in tables:
            self.excess_tables_list.addItem(table)

    def update_keywords(self, expected_keywords, used_keywords):

        yes_icon = QIcon(':/icons/yes-64.png')
        no_icon = QIcon(':/icons/no-48.png')
        for keyword, expected in expected_keywords.items():
            requirement_type = 'Requerido' if expected else 'Prohibido'
            text = '{}: {}'.format(requirement_type, keyword)

            if expected == (keyword in used_keywords):
                icon = yes_icon
            else:
                icon = no_icon

            new_keyword_entry = QListWidgetItem(icon, text)
            new_keyword_entry.setIcon(icon)

            self.keywords_list.addItem(new_keyword_entry)
