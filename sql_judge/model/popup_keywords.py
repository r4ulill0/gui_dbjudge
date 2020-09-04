from PyQt5.QtCore import QAbstractListModel, QAbstractItemModel
from PyQt5.QtCore import Qt, QModelIndex, pyqtSlot


class KeyWordsPopupModel(QAbstractListModel):
    def __init__(self):
        super().__init__()
        self.allowance = []
        self.keyword = []

    def return_data(self):
        return (self.allowance, self.keyword)

    def index(self, row, column=0, parent=QModelIndex()):
        return self.createIndex(row, column)

    def rowCount(self, parent=QModelIndex()):
        return len(self.keyword)

    def data(self, index, role=Qt.DisplayRole):
        if role == Qt.DisplayRole:
            option = '' if self.allowance[index.row(
            )] == 'Obligatorio' else 'evitar '
            text = 'Se debe {}usar {}'.format(
                option, self.keyword[index.row()])
            return text

    def insertRows(self, position, rows, index=QModelIndex()):
        self.beginInsertRows(index, position, position+rows-1)
        for _ in range(rows):
            new_keyword = False
            new_allowance = ''
            self.keyword.append(new_keyword)
            self.allowance.append(new_allowance)
        self.endInsertRows()
        return True

    def setData(self, index, value, role=Qt.EditRole):

        if index.isValid() and role == Qt.EditRole:
            if index.row() >= self.rowCount():
                self.insertRows(index.row(), 1)
            self.allowance[index.row()] = value[0]
            self.keyword[index.row()] = value[1]
            self.dataChanged.emit(index, index)
            return True

        return False

    def removeRows(self, position, rows, index=QModelIndex()):
        self.beginRemoveRows(index, position, position+rows-1)
        for row in reversed(range(position, position+rows)):
            self.keyword.pop(row)
            self.allowance.pop(row)
        self.endRemoveRows()
