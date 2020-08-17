from model.exam import ExamData

from dbjudge.connection_manager.manager import Manager


class Exam_controller():
    def __init__(self, selection_view, exam_view):
        self.selection_view = selection_view
        self.exam_view = exam_view
        self.model = ExamData()
        self.manager = Manager.singleton_instance

    def load_avaiable_scenarios(self):
        self.model.scenarios = self.manager.get_databases()
        self.selection_view.load_scenarios(self.model.scenarios)
