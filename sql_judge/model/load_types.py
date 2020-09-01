from PyQt5.QtCore import QAbstractTableModel, QAbstractItemModel
from PyQt5.QtCore import Qt, QModelIndex, pyqtSlot


class LoadTypesProcess(QAbstractTableModel):
    def __init__(self):
        super().__init__()
        self.csv_values = []
        self.header_model = HeaderModel()

    def index(self, row, column, parent=QModelIndex()):
        return self.createIndex(row, column)

    def rowCount(self, parent=QModelIndex()):
        return len(self.csv_values)

    def columnCount(self, parent=QModelIndex()):
        count = 0
        if len(self.csv_values):
            count = len(self.csv_values[0])

        return count

    def data(self, index, role=Qt.DisplayRole):
        if role == Qt.DisplayRole:
            return self.csv_values[index.row()][index.column()]

    def setData(self, index, value, role=Qt.EditRole):

        if index.isValid() and role == Qt.EditRole:
            if index.column() >= self.columnCount():
                self.insertColumns(index.column(), 1)
            if index.row() >= self.rowCount():
                self.insertRows(index.row(), 1)
            self.csv_values[index.row()][index.column()] = value
            self.dataChanged.emit(index, index)
            return True

        return False

    def flags(self, index):

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

    def removeRows(self, position, rows, index=QModelIndex()):
        self.beginRemoveRows(index, position, position+rows-1)
        for row in reversed(range(position, position+rows)):
            self.csv_values.pop(row)
        self.endRemoveRows()

    def removeColumns(self, position, columns, index=QModelIndex()):
        self.beginRemoveColumns(index, position, position+columns-1)
        delete_list = reversed(range(position, position+columns))
        for row in self.csv_values:
            for column in delete_list:
                row.pop(column)


class HeaderModel(QAbstractItemModel):
    def __init__(self):
        super().__init__()
        self.values = []

    def index(self, row, column, parent=QModelIndex()):
        return self.createIndex(row, column)

    def columnCount(self, parent=QModelIndex()):
        return len(self.values)

    def rowCount(self, parent=QModelIndex()):
        return 1

    def headerData(self, section, orientation, role=Qt.DisplayRole):
        if role == Qt.DisplayRole:
            return self.values[section]

    def setHeaderData(self, section, orientation, value, role=Qt.EditRole):
        if role == Qt.EditRole:
            self.values[section] = value

    def removeColumn(self, column, index=QModelIndex()):
        self.beginRemoveColumns(index, column, column)
        self.values.pop(column)
        self.endRemoveColumns()

    def insertColumns(self, column, amount, index=QModelIndex()):
        self.beginInsertColumns(index, column, column+amount-1)
        for idx in range(amount):
            self.values.append(str(self.columnCount()+idx))
        self.endInsertColumns()
