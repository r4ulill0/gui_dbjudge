from view.qt_view.exam.results_view import Ui_Results
from PyQt5.QtWidgets import QWidget


class Results(Ui_Results, QWidget):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
