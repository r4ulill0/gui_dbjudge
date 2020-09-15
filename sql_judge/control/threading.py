from PyQt5.QtCore import QThread
from PyQt5.QtCore import pyqtSignal
from dbjudge import filler
from dbjudge.questions.generation import generator
from psycopg2 import Error


class FinishSceneThread(QThread):
    progression_made = pyqtSignal(int)
    category_update = pyqtSignal(str)

    def __init__(self, model, manager):
        super().__init__()
        self.model = model
        self.manager = manager
        self.progress = 0

    def run(self):
        try:
            self.progression_made.emit(self.progress)
            self.category_update.emit("Generando datos...")
            filler.generate_fake_data(
                self.model.context, self.manager.selected_db_connection, self.process_filler_progress)

            self.category_update.emit(
                "Generando datos adicionales para las preguntas...")
            progress_unit = int(50/len(self.model.questions)
                                ) if self.model.questions else 0
            for index, (question, query) in enumerate(self.model.questions):
                self.progress += progress_unit if self.progress+progress_unit < 100 else 0
                self.progression_made.emit(self.progress)
                generator.create_question(
                    self.model.name,
                    query,
                    question,
                    self.model.context,
                    self.model.get_formatted_keywords(index))

            self.progression_made.emit(100)
        except Error:
            pass

    def process_filler_progress(self, filler_progress):
        increase = int(filler_progress/2)
        increase = increase if increase > 0 else 1
        self.progress += increase if self.progress+increase < 50 else 0

        self.progression_made.emit(self.progress)

    def exit(self, return_code):
        self._clean_conn()
        super().exit(return_code)

    def quit(self):
        self._clean_conn()
        super().quit()

    def _clean_conn(self):
        self.manager.selected_db_connection.cancel()
        self.manager.selected_db_connection.rollback()
        self.manager.selected_db_connection.close()
        self.manager.selected_db_connection = None
