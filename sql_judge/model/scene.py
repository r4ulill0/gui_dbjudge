
class Scene():
    def __init__(self):
        self.name =
        self.loaded_sql =
        self.questions = []

    def add_question(self, question_text, proposed_answer):
        question = (question_text, proposed_answer)
        self.questions.append(question)
