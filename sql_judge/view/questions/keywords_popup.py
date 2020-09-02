from view.qt_view.questions.keywords_popup import Ui_KeywordsPopup
from PyQt5.QtWidgets import QDialog


class KeywordsPopup(QDialog, Ui_KeywordsPopup):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

    def accept(self):
        pass

    def reject(self):
        pass
