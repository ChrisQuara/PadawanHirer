from abc import abstractmethod
import random


class Question:
    category = None
    weight = 0
    responses = None
    isPartiallyCorrect = False
    score = 0
    maxAttempt = 1

    def __init__(self, category, responses):
        self.category = category
        self.responses = responses

    @abstractmethod
    def getScore(self, phrase_token):
        pass

    @abstractmethod
    def askTheQuestion(self):
        pass

    def toString(self):
        return "<Category:" + str(self.category) + ", Weight:" + str(self.weight) + ", Responses:" + str(
            self.responses) + ">"


class QuestionSpecifyAllElements(Question):

    def __init__(self, category, responses):
        super().__init__(category, responses)
        self.weight = 5
        self.maxAttempt = 3

    def getScore(self, phrase_words):
        self.isPartiallyCorrect = False
        to_respond = self.responses.copy()
        for word in phrase_words:
            if word in to_respond:
                self.isPartiallyCorrect = True
                to_respond.remove(word)
        if (self.responses.__len__() - to_respond.__len__()) / self.responses.__len__() > 1 / 2:
            self.score = self.weight
        else:
            self.score = 0
        return self.score

    def askTheQuestion(self):
        print("Elenca tutte gli elementi della categoria '" + str(self.category) + "':")
        return "Da implementare"


class QuestionEnumerateElements(Question):
    def __init__(self, category, responses):
        super().__init__(category, responses)
        self.weight = 3

    def getScore(self, number_of_elements):
        self.isPartiallyCorrect = False
        if number_of_elements.__len__() > 1:
            raise Exception("The list contains more than one element")
        number_of_elements = int(number_of_elements[0])
        number_of_responses = self.responses.__len__()
        if number_of_elements >= 2 * number_of_responses or number_of_elements <= 0:
            self.score = 0
        else:
            self.isPartiallyCorrect = True
            self.score = round(
                self.weight * (1 - (abs(number_of_responses - number_of_elements) / number_of_responses)))
        return self.score

    def askTheQuestion(self):
        print("Quanti elementi contiene la categoria '" + str(self.category) + "':")
        return "Da implementare"


class QuestionYesOrNo(Question):
    negation = False
    elementToAsk = None

    def __init__(self, category, real_responses, possible_responses):
        super().__init__(category, real_responses)
        self.weight = 2
        self.negation = random.choice([True, False])
        self.elementToAsk = random.choice(possible_responses)

    def getScore(self, response):
        self.isPartiallyCorrect = False
        if response.count("yes") > 0:
            if response.count("no") > 0:
                raise Exception("The list contains both yes and no")
            response = "yes"
        elif response.count("no") > 0:
            if response.count("yes") > 0:
                raise Exception("The list contains both yes and no")
            response = "no"
        else:
            raise Exception("The list does not contains yes or no")

        if (response.lower() == "yes" and not self.negation) or (response.lower() == "no" and self.negation):
            for element in self.responses:
                if element.lower() == self.elementToAsk.lower():
                    self.isPartiallyCorrect = True
                    self.score = self.weight
                    return self.weight
            return 0
        elif (response.lower() == "no" and not self.negation) or (response.lower() == "yes" and self.negation):
            for element in self.responses:
                if element.lower() == self.elementToAsk.lower():
                    self.score = 0
                    return 0
            self.isPartiallyCorrect = True
            self.score = self.weight
            return self.weight
        else:
            self.score = 0
            return 0

    def askTheQuestion(self):
        negate = ""
        if self.negation:
            negate = " non "
        print("E' vero che '" + self.elementToAsk + "'" + negate + "è membro della categoria '" + self.category + "':")
        return "Da implementare"
