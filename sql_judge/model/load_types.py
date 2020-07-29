from PyQt5.QtCore import QAbstractTableModel, QAbstractItemModel
from PyQt5.QtCore import Qt, QModelIndex, pyqtSlot


class LoadTypesProcess(QAbstractTableModel):
    def __init__(self):
        super().__init__()
        self.csv_values = [['a', 'b'], ['c', 'd']]

    def rowCount(self, parent=QModelIndex()):
        return len(self.csv_values)

    def columnCount(self, parent=QModelIndex()):
        max_len = 0
        for row in self.csv_values:
            max_len = len(row) if len(row) > max_len else max_len
        return max_len

    def data(self, index, role=Qt.DisplayRole):
        return self.csv_values[index.row()][index.column()]

    def setData(self, index, value, role=Qt.EditRole):

        if index.isValid() and role == Qt.EditRole:
            if index.column() >= self.columnCount():
                self.insertColumns(index.column(), 1)
            if index.row() >= self.rowCount():
                self.insertRows(index.row(), 1)
            print(" ".join((str(index.row()), str(index.column()))))
            self.csv_values[index.row()][index.column()] = value
            self.dataChanged.emit(index, index)
            return True

        return False

    def flags(self, index):
        if not index.isValid():
            return Qt.ItemIsEnabled

        return QAbstractTableModel.flags(self, index) | Qt.ItemIsEditable

    def insertRows(self, position, rows, index=QModelIndex()):
        self.beginInsertRows(index, position, position+rows-1)
        for _ in range(rows):
            new_row = []
            for _ in range(self.columnCount()):
                new_row.append("")
            self.csv_values.append(new_row)
        self.endInsertRows()
        return True

    def insertColumns(self, position, columns, index=QModelIndex()):
        self.beginInsertColumns(index, position, position+columns-1)
        for row in self.csv_values:
            for _ in range(columns):
                row.append("")
        self.endInsertColumns()
        return True
