from model.exam import ExamData


class Exam_controller():
    def __init__(self, selection_view, exam_view):
        self.selection_view = selection_view
        self.exam_view = exam_view
        self.model = ExamData()
