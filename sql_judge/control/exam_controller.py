from model.exam import ExamData

from dbjudge.connection_manager.manager import Manager
from dbjudge import squema_recollector, exceptions
from PyQt5.QtCore import pyqtSlot, QItemSelectionModel


class Exam_controller():
    def __init__(self, selection_view, exam_view, results_view):
        self.selection_view = selection_view
        self.exam_view = exam_view
        self.results_view = results_view
        self.model = ExamData()
        self.manager = Manager.singleton_instance

        self.selection_view.scenario_selection.currentTextChanged.connect(
            self.update_scenario_data)
        self.selection_view.access_button.clicked.connect(
            self.update_scenario_data)

        self.exam_view.test_button.clicked.connect(self.try_answer)
        self.exam_view.question_list.setModel(self.model.questions)
        self.exam_view.question_list.selectionModel().currentRowChanged.connect(
            self.update_current_exam_question)

        self.exam_view.generate_report_button.clicked.connect(
            self.finish_exam)

        self.results_view.question_list.setModel(self.model.questions)
        self.results_view.question_list.selectionModel().currentRowChanged.connect(
            self.update_current_results_question)

    def load_avaiable_scenarios(self):
        self.model.scenarios = self.manager.get_databases()
        self.selection_view.load_scenarios(self.model.scenarios)

    def update_scenario_data(self, scenario):
        scenario = self.selection_view.get_current_scenario()
        if scenario:
            self.manager.select_database(scenario)
            self.model.questions = self.manager.get_questions()
            tables = self.manager.get_tables()
            tuples = self.manager.get_total_data_count()
            total_tables = len(tables)
            total_questions = len(self.model.questions)
            total_rows = tuples
            self.selection_view.update_scenario_data(
                total_tables, total_questions, total_rows)
            self.selection_view.access_button.setEnabled(total_questions > 0)
        preselected_index = self.model.questions.index(0, 0)
        self.exam_view.question_list.selectionModel().setCurrentIndex(
            preselected_index, QItemSelectionModel.SelectionFlag.ClearAndSelect)

    def update_current_exam_question(self, index):
        self.model.answers[self.model.questions.question_list[self.model.current_question]
                           ] = self.exam_view.get_answer_text()
        self.exam_view.update_current_question(
            self.model.questions.question_list[index.row()])
        self.exam_view.set_answer_text(
            self.model.answers[self.model.questions.question_list[index.row()]])
        self.model.current_question = index.row()

    def try_answer(self):
        answer = self.exam_view.get_answer_text()
        try:
            response = self.manager.execute_in_readonly(answer)
            for row in response:
                complete_row = ''
                for element in row:
                    complete_row += ' '+str(element)
                self.exam_view.set_console_output(complete_row)
        except exceptions.ReadOnlyError:
            error_message = 'Error sintáctico detectado, revisa tu consulta'
            self.exam_view.set_console_output(error_message)

    def finish_exam(self):
        self.model.answers[self.model.questions.question_list[self.model.current_question]
                           ] = self.exam_view.get_answer_text()
        self.exam_view.clear_ui()
        self.model.generate_report()
        preselected_index = self.model.questions.index(0, 0)
        self.results_view.question_list.selectionModel().setCurrentIndex(
            preselected_index, QItemSelectionModel.SelectionFlag.ClearAndSelect)

    def update_current_results_question(self, index):
        correct_answers_count = 0
        total_count = 0
        for question, analysis in self.model.report.items():
            if analysis.is_correct():
                correct_answers_count += 1
            total_count += 1

        question = self.model.questions.question_list[index.row()]
        self.results_view.update_total_count(
            correct_answers_count, total_count)
        self.results_view.update_current_question(question)
        self.results_view.update_correct_result(
            self.model.report[question].correct_result)
        self.results_view.update_correct_answer(
            self.model.report[question].is_correct())
        self.results_view.update_excess_tables(
            self.model.report[question].excess_tables_used)
        self.results_view.update_keywords(
            self.model.report[question].expected_keywords, self.model.report[question].used_keywords)
        self.model.current_question = index.row()
