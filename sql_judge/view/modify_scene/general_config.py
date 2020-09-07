from view.qt_view.modify_scene.general_config_view import Ui_ModifySceneMenuConfig
from PyQt5.QtWidgets import QWidget
from PyQt5.QtCore import pyqtSignal


class Modify_scene_general_config(QWidget, Ui_ModifySceneMenuConfig):
    scenario_changed = pyqtSignal(str)

    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.comboBox.currentTextChanged.connect(self.handle_scenario_change)

    def load_scenarios(self, scenarios):
        self.comboBox.clear()
        for scenario in scenarios:
            self.comboBox.addItem(scenario)

    def handle_scenario_change(self):
        scenario = self.comboBox.currentText()
        self.scenario_changed.emit(scenario)

    def setCurrentScenario(self, scenario):
        index = self.comboBox.findText(scenario)
        self.comboBox.setCurrentIndex(index)
