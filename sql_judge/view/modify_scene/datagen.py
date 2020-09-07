from view.qt_view.modify_scene.modify_scene_menu_datagen_view import Ui_ModifySceneMenuDatagen
from PyQt5.QtWidgets import QWidget
from PyQt5.QtCore import pyqtSignal


class Modify_scene_datagen(QWidget, Ui_ModifySceneMenuDatagen):
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
