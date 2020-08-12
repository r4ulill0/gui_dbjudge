from model.exam import ExamData


class Exam_controller():
    def __init__(self, view):
        self.exam_view = view
        self.model = ExamData()
