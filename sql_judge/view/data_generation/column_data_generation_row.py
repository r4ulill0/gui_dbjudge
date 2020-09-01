from view.qt_view.data_generation.column_data_generation_row_view import Ui_ColumnDataGenerationRow

from dbjudge.connection_manager.manager import Manager
from dbjudge.structures.column import Column

from PyQt5.QtWidgets import QWidget
from PyQt5.QtWidgets import QLineEdit, QComboBox
from PyQt5.QtCore import Qt, pyqtSignal, pyqtSlot
from PyQt5.QtGui import QColor


class Column_data_generation_row(Ui_ColumnDataGenerationRow, QWidget):
    type_info_modified = pyqtSignal(str, str, tuple)

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
        self.custom_type_input.currentIndexChanged.connect(
            self.update_type_for_combo)
        self.regex_input.editingFinished.connect(
            self.update_type_for_input_line)
        self.regex_max_len_input.editingFinished.connect(
            self.update_type_for_input_line)

        self._current_input = 'default'

        self._load_custom_types()
        self.setLayout(self.gridLayout)

    def _load_custom_types(self):
        self.custom_type_input.clear()
        types = Manager.singleton_instance.get_fake_types()
        for fake_type in types:
            self.custom_type_input.addItem(fake_type[0])

    @pyqtSlot(int)
    def update_type_for_combo(self):
        self.update_type()

    @pyqtSlot(str)
    def update_type_for_input_line(self):
        self.update_type()

    @pyqtSlot(bool)
    def update_type(self):
        mapped_buttons_and_type_info = {
            self.regex_radio_button: self.regex_input,
            self.default_type_radio_button: None,
            self.custom_type_radio_button: self.custom_type_input
        }

        for button, input_element in mapped_buttons_and_type_info.items():
            if button.isChecked():
                self._disable_current_input()
                column = self.column.name
                current_type = self._get_button_type(button)
                self._current_input = current_type
                self._enable_current_input()
                extra_data = self._get_extra_data_from(self._current_input)
                self.type_info_modified.emit(column, current_type, extra_data)
                break

    def _disable_current_input(self):
        if self._current_input == 'regex':
            self.regex_input.setEnabled(False)
            self.regex_max_len_input.setEnabled(False)
            self.max_len_label.setEnabled(False)
        elif self._current_input == 'custom':
            self.custom_type_input.setEnabled(False)

    def _enable_current_input(self):
        if self._current_input == 'regex':
            self.regex_input.setEnabled(True)
            self.regex_max_len_input.setEnabled(True)
            self.max_len_label.setEnabled(True)
        elif self._current_input == 'custom':
            self.custom_type_input.setEnabled(True)

    def _get_button_type(self, button):
        mapped_types = {
            self.regex_radio_button: 'regex',
            self.default_type_radio_button: 'default',
            self.custom_type_radio_button: 'custom'
        }
        return mapped_types[button]

    def _get_extra_data_from(self, current_input):
        data = ('', 0)
        if current_input == 'custom':
            data = (self.custom_type_input.currentText(),)
        elif current_input == 'regex':
            data = (self.regex_input.text(), self.regex_max_len_input.text())

        return data
