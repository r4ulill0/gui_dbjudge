from PyQt5.QtWidgets import QDialog
from view.qt_view.questions.keywords_popup import Ui_KeywordsPopup
from model.popup_keywords import KeyWordsPopupModel


class KeywordsPopup(QDialog, Ui_KeywordsPopup):
    def __init__(self, options, keywords):
        super().__init__()
        self.setupUi(self)
        self.model = KeyWordsPopupModel()
        self.listView.setModel(self.model)

        self.allowance_combobox.addItems(options)
        self.keyword_combobox.addItems(keywords)
        self.confirm_button.clicked.connect(self.accept)
        self.cancel_button.clicked.connect(self.reject)
        self.add_button.clicked.connect(self.add_new_row)
        self.delete_button.clicked.connect(self.delete_selected_rows)

    def add_new_row(self):
        index = self.model.rowCount()
        value = [
            self.allowance_combobox.currentText(),
            self.keyword_combobox.currentText()
        ]
        qt_index = self.model.createIndex(index, 0)
        self.model.setData(qt_index, value)

    def delete_selected_rows(self):
        selection = self.listView.selectionModel()
        if selection.hasSelection():
            for row in reversed(range(self.model.rowCount())):
                if selection.isRowSelected(row):
                    self.model.removeRows(row, 1)
