from PyQt5.QtCore import QAbstractListModel, QAbstractItemModel
from PyQt5.QtCore import Qt, QModelIndex, pyqtSlot

from dbjudge.judge.judge import Judge


class ExamData:
    def __init__(self):
        self.data = None
        self.selected_scenario = None
        self.scenarios = None
        self.current_question = 0
        self._judge = Judge()
        self._questions = QuestionSet()
        self.report = {}

    @property
    def questions(self):
        return self._questions

    @questions.setter
    def questions(self, value):
        self._judge.start_session(value)
        self.questions.beginResetModel()
        self._questions.question_list = value
        self.questions.endResetModel()

    @property
    def answers(self):
        if self._judge.session:
            return self._judge.session.mapped_answers
        else:
            return {}

    def generate_report(self):
        self.report = self._judge.generate_report()


class QuestionSet(QAbstractListModel):
    def __init__(self, questions=[]):
        super().__init__()
        self.question_list = questions

    def rowCount(self, parent=QModelIndex()):
        return len(self.question_list)

    def data(self, index, role=Qt.DisplayRole):
        if role == Qt.DisplayRole:
            displayed_data = "Pregunta "+str(index.row())
            return displayed_data

    def flags(self, index):
        return Qt.ItemIsEnabled | Qt.ItemIsSelectable

    def __len__(self):
        return len(self.question_list)
