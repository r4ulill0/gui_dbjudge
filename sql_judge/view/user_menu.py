from view.qt_view.pre_evaluation_view import Ui_PreEvaluationView
from PyQt5.QtWidgets import QWidget


class User_menu(Ui_PreEvaluationView, QWidget):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

    def load_scenarios(self, scenarios):
        self.scenario_selection.clear()
        for scenario in scenarios:
            self.scenario_selection.addItem(scenario)
