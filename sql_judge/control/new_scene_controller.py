from dbjudge.connection_manager.manager import Manager
from PyQt5.QtCore import QObject, pyqtSlot
from view.new_scene_menu_schema import New_scene_menu_schema


class New_scene_controller(QObject):
    def __init__(self, controller, view):
        super().__init__()
        self.main_controller = controller
        self.main_view = view
        self.manager = Manager.singleton_instance

        # view.create_button.clicked.connect(self.create_new_scene)

    @pyqtSlot(bool)
    def create_new_scene(self):
        scene_name = self.main_view.get_scene_name_text()
        self.manager.create_database(scene_name)
        self.main_controller.main_window.new_scene_to_modify_scene()
