from view.qt_view.new_scene_menu_datagen_view import Ui_NewSceneMenuDatagen
from PyQt5.QtWidgets import QWidget


class New_scene_menu_datagen(Ui_NewSceneMenuDatagen, QWidget):
    def __init__(self):
        super().__init__()

        self.setupUi(self)

    # TODO check if this method is used
    def get_scene_name_text(self):
        return self.scene_name_input_text.text()
