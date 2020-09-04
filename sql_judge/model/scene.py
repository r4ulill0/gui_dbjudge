
class Scene():
    def __init__(self):
        self.name = None
        self.loaded_sql = None
        self.context = None
        self.questions = []
        self.keywords = []

    def add_question(self, question_text, proposed_answer):
        question = (question_text, proposed_answer)
        self.questions.append(question)
        if len(self.questions) > len(self.keywords):
            self.keywords.append(([], []))

    def update_question(self, index, question_text, proposed_answer):
        self.questions[index] = (question_text, proposed_answer)

    def update_keywords(self, index, keywords):
        self.keywords[index] = keywords

    def delete_questions_and_keywords_row(self, index):
        self.questions.pop(index)
        self.keywords.pop(index)

    def get_formatted_keywords(self, index):
        allowance = self.keywords[index][0]
        keywords = self.keywords[index][1]
        result = {}
        for index in range(len(keywords)):
            formatted_allowance = allowance[index] == 'Obligatorio'
            key = keywords[index]
            result[key] = formatted_allowance

        return result
