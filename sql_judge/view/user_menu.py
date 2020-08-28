from view.qt_view.pre_evaluation_view import Ui_PreEvaluationView
from PyQt5.QtWidgets import QWidget


class User_menu(Ui_PreEvaluationView, QWidget):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

    def get_current_scenario(self):
        return self.scenario_selection.currentText()

    def load_scenarios(self, scenarios):
        self.scenario_selection.clear()
        for scenario in scenarios:
            self.scenario_selection.addItem(scenario)

    def update_scenario_data(self, total_tables, total_questions, total_rows):
        self.data_table.item(0, 1).setText(str(total_tables))
        self.data_table.item(1, 1).setText(str(total_questions))
        self.data_table.item(2, 1).setText(str(total_rows))
