from view.qt_view.data_generation.data_generation_view import Ui_DataGeneration
from .data_generation.table_data_generation_tab import Table_data_generation_tab

from dbjudge.structures.context import Context
from PyQt5.QtWidgets import QWidget
from PyQt5.QtCore import pyqtSlot


class Data_generation_menu(Ui_DataGeneration, QWidget):
    def __init__(self):
        super().__init__()

        self.setupUi(self)
