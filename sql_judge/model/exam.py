from PyQt5.QtCore import QAbstractListModel, QAbstractItemModel
from PyQt5.QtCore import Qt, QModelIndex, pyqtSlot


class ExamData:
    def __init__(self):
        self.data = None
        self.selected_scenario = None
        self.scenarios = None
        self._questions = QuestionSet()

    @property
    def questions(self):
        return self._questions

    @questions.setter
    def questions(self, value):
        self._questions.question_list = value


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
