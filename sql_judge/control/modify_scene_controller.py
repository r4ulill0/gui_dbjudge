from dbjudge.connection_manager.manager import Manager
from PyQt5.QtCore import QObject, pyqtSlot
from view.modify_scene_menu import Modify_scene_menu


class Modify_scene_controller(QObject):
    def __init__(self, view):
        super().__init__()
        self.main_view = view
        self.manager = Manager.singleton_instance

    def load_scenes(self):
        print("dentro!")
        databases = self.manager.get_databases()
        self.main_view.load_scenes_combo_box(databases)
