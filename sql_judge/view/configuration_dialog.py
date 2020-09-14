from view.qt_view.configuration_dialog_view import Ui_ConfigurationDialog


from PyQt5.QtWidgets import QDialog


class ConfigDialog(Ui_ConfigurationDialog, QDialog):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.save_button.clicked.connect(self.accept)

    def get_user(self):
        return self.user_input.text()

    def get_pass(self):
        return self.pass_input.text()

    def get_host(self):
        return self.host_input.text()

    def get_dbname(self):
        return self.dbname_input.text()

    def get_port(self):
        return self.port_input.text()
