from PyQt5.QtWidgets import QProgressDialog


class ProgressDialog(QProgressDialog):
    def __init__(self):
        super().__init__()
        self.setupUi()

    def setupUi(self):
        self.setModal(True)
        self.setCancelButtonText("Interrumpir")
