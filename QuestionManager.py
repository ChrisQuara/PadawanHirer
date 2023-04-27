
class QuestionManager:
    _instance = None
    questions = []
    categories = []

    def __init__(self):
        raise RuntimeError('Call instance() instead')

    @classmethod
    def instance(cls):
        if cls._instance is None:
            cls._instance = cls.__new__(cls)
            # Put any initialization here.
        return cls._instance

    def addCategory(self, category):
        if not self.categories.__contains__(category): self.categories.append(category)

    def getIndexCategory(self, category):
        for i in range(0, self.categories.__sizeof__() - 1):
            if category == self.categories[i]: return i
        raise RuntimeError('The category is unknown, add it with addCategories()')

    def getCategoryByIndex(self, index):
        if self.categories.__len__() - 1 >= index: return self.categories[index]
        return None

    def addQuestion(self, question):
        if not self.categories.__contains__(question.category): raise RuntimeError(
            'The question\'s category is unknown, add it with addCategories().')
        self.questions.append(question)

    def removeQuestion(self, question):
        self.questions.remove(question)

    def printQuestions(self):
        print(self.questions)

    def getNumberOfQuestions(self):
        return self.questions.__len__()

    def getQuestions(self):
        return self.questions.copy()

    def getQuestionsWithWeightCriteria(self, criteria):
        return [question for question in self.questions if criteria(question.weight)]

    def getQuestionsWithCategoryCriteria(self, criteria):
        return [question for question in self.questions if criteria(question.category)]

    def getAllResponses(self):
        to_return = []
        for question in self.questions:
            to_return += question.responses
        return to_return

    @staticmethod
    def getExplicitQuestionsWithCategoryCriteria(questions, criteria):
        return [question for question in questions if criteria(question.category)]

    @staticmethod
    def getExplicitQuestionsWithWeightCriteria(questions, criteria):
        return [question for question in questions if criteria(question.weight)]

    @staticmethod
    def getComparisonWeightQuestion(questions, comparison):
        lowest_question = questions[0]
        for question in questions:
            if comparison(question.weight, lowest_question.weight): lowest_question = question
        return lowest_question
