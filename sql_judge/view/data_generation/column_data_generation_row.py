from view.qt_view.data_generation.column_data_generation_row_view import Ui_ColumnDataGenerationRow

from dbjudge.connection_manager.manager import Manager
from dbjudge.structures.column import Column

from PyQt5.QtWidgets import QWidget
from PyQt5.QtWidgets import QLineEdit, QComboBox
from PyQt5.QtCore import Qt, pyqtSignal, pyqtSlot
from PyQt5.QtGui import QColor


class Column_data_generation_row(Ui_ColumnDataGenerationRow, QWidget):
    type_info_modified = pyqtSignal(str, str, str)

    def __init__(self, column, dark_background):
        super().__init__()

        self.setupUi(self)

        if dark_background:
            self.setAutoFillBackground(True)
            palette = self.palette()
            palette.setColor(self.backgroundRole(), Qt.gray)
            self.setPalette(palette)

        self.column_name_label.setText(column.name)
        self.column = column
        self.itemAt = self.gridLayout.itemAt
        self.sizeHint = self.gridLayout.sizeHint

        self.regex_radio_button.toggled.connect(self.update_type)
        self.default_type_radio_button.toggled.connect(self.update_type)
        self.custom_type_radio_button.toggled.connect(self.update_type)

        self._load_custom_types()
        self.setLayout(self.gridLayout)

    def _load_custom_types(self):
        self.custom_type_input.clear()
        types = Manager.singleton_instance.get_custom_fakes(
            self.column.ctype)
        self.custom_type_input.addItems(types)

    @pyqtSlot(bool)
    def update_type(self):
        mapped_buttons_and_type_info = {
            self.regex_radio_button: self.regex_input,
            self.default_type_radio_button: None,
            self.custom_type_radio_button: self.custom_type_input
        }

        for button, input_element in mapped_buttons_and_type_info.items():
            if button.isChecked():
                column = self.column.name
                current_type = self._get_button_type(button)
                extra_data = self._get_extra_data_from(input_element)
                self.type_info_modified.emit(column, current_type, extra_data)
                break

    def _get_button_type(self, button):
        mapped_types = {
            self.regex_radio_button: 'regex',
            self.default_type_radio_button: 'default',
            self.custom_type_radio_button: 'custom'
        }
        return mapped_types[button]

    def _get_extra_data_from(self, input_element):
        input_type = type(input_element)
        data = None
        if input_type == QLineEdit:
            data = input_element.text()
        elif input_type == QLineEdit:
            data = input_element.currentText()

        return data
