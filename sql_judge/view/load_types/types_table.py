from PyQt5.QtWidgets import QTableView, QPushButton, QTableWidgetItem
from PyQt5 import Qt, QtCore, QtWidgets


class TypesTable(QTableView):
    def __init__(self):
        super().__init__()
        self.setHorizontalHeader(MetaHeaderView(QtCore.Qt.Horizontal))


class MetaHeaderView(Qt.QHeaderView):

    def __init__(self, orientation, parent=None):
        super(MetaHeaderView, self).__init__(orientation, parent)
        self.setSectionsMovable(True)
        self.setSectionsClickable(True)
        self.line = QtWidgets.QLineEdit(parent=self.viewport())
        self.line.setAlignment(QtCore.Qt.AlignTop)
        self.line.setHidden(True)
        self.line.blockSignals(True)
        self.sectionedit = 0
        self.sectionDoubleClicked.connect(self.editHeader)
        self.line.editingFinished.connect(self.doneEditing)

    def doneEditing(self):
        self.line.blockSignals(True)
        self.line.setHidden(True)
        newname = str(self.line.text())
        self.model().values[self.sectionedit] = newname
        self.line.setText('')
        self.setCurrentIndex(QtCore.QModelIndex())

    def editHeader(self, section):
        edit_geometry = self.line.geometry()
        edit_geometry.setWidth(self.sectionSize(section))
        edit_geometry.moveLeft(self.sectionViewportPosition(section))
        self.line.setGeometry(edit_geometry)

        self.line.setText(self.model().values[section])
        self.line.setHidden(False)
        self.line.blockSignals(False)
        self.line.setFocus()
        self.line.selectAll()
        self.sectionedit = section
