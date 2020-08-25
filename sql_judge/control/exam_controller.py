from model.exam import ExamData

from dbjudge.connection_manager.manager import Manager
from dbjudge import squema_recollector
from PyQt5.QtCore import pyqtSlot


class Exam_controller():
    def __init__(self, selection_view, exam_view):
        self.selection_view = selection_view
        self.exam_view = exam_view
        self.model = ExamData()
        self.manager = Manager.singleton_instance

        self.selection_view.scenario_selection.currentTextChanged.connect(
            self.update_scenario_data)

    def load_avaiable_scenarios(self):
        self.model.scenarios = self.manager.get_databases()
        self.selection_view.load_scenarios(self.model.scenarios)

    def update_scenario_data(self, scenario):
        if (scenario):
            self.manager.select_database(scenario)
            questions = self.manager.get_questions()
            tables = self.manager.get_tables()
            tuples = self.manager.get_total_data_count()
            total_tables = len(tables)
            total_questions = len(questions)
            total_rows = tuples
            self.selection_view.update_scenario_data(
                total_tables, total_questions, total_rows)
