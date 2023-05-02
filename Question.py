from abc import abstractmethod
from word2number import w2n
import random
from NLGFunctions import *


def getNumber(phrase):
    number = None

    if phrase.__len__() == 0:
        return None
    elif phrase.__len__() == 1:
        try:
            number = w2n.word_to_num(phrase[0])
            return number
        except:
            return None

    for index in range(0, phrase.__len__() - 1):
        first_num = None
        second_num = None
        try:
            first_num = w2n.word_to_num(phrase[index])
            if number is None:
                number = first_num
            else:
                return "more_than_one_number"
            second_num = w2n.word_to_num(phrase[index + 1])
            return "composite_number"
        except:
            if number is not None and second_num is not None:
                return "composite_number"

    try:
        first_num = w2n.word_to_num(phrase[phrase.__len__() - 1])
        if number is None:
            number = first_num
        else:
            return "more_than_one_number"
    except:
        pass

    return number


class Question:
    category = None
    weight = 0
    responses = None
    isPartiallyCorrect = False
    score = 0
    maxAttempt = 1
    numberAttempt = 0

    def __init__(self, category, responses):
        self.category = category
        self.responses = responses

    @abstractmethod
    def getScore(self, phrase_token):
        pass

    @abstractmethod
    def getTheQuestion(self):
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

    def getTheQuestion(self):
        return SpecifyAllElements(self.category, self.numberAttempt)


class QuestionEnumerateElements(Question):
    def __init__(self, category, responses):
        super().__init__(category, responses)
        self.weight = 3

    def getScore(self, number_of_elements):
        self.isPartiallyCorrect = False
        number_of_responses = self.responses.__len__()
        number_of_elements = getNumber(number_of_elements)
        if number_of_elements is None:
            raise Exception("There isn't a number")
        elif number_of_elements == "more_than_one_number":
            raise Exception("Too many numbers")
        elif number_of_elements == "composite_number":
            self.score = 0
            return 0

        if number_of_elements >= 2 * number_of_responses or number_of_elements <= 0:
            self.score = 0
        else:
            self.isPartiallyCorrect = True
            self.score = round(
                self.weight * (1 - (abs(number_of_responses - number_of_elements) / number_of_responses)))
        return self.score

    def getNumber(self, phrase):
        number = None
        for index in range(0, phrase.__len__() - 2):
            try:
                temp = w2n.word_to_num(phrase[index])
                if number == None:
                    number = temp
                else:
                    return -1  # More than one number
                temp = w2n.word_to_num(phrase[index + 1])
                return -2  # composite number
            except:
                pass
        return number

    def getTheQuestion(self):
        return EnumerateAllElements(self.category)


class QuestionYesOrNo(Question):
    negation = False
    elementToAsk = None

    def __init__(self, category, real_responses, possible_responses):
        super().__init__(category, real_responses)
        self.weight = 2
        self.negation = random.choice([True, False])
        difference = list(set(possible_responses) - set(real_responses))
        if random.choice([True, False]):
            self.elementToAsk = random.choice(real_responses)
        else:
            self.elementToAsk = random.choice(difference)

    def getScore(self, response):
        self.isPartiallyCorrect = False
        if response.count("yes") > 0 or response.count("true") > 0:
            if response.count("no") > 0 or response.count("false") > 0:
                raise Exception("The list contains both yes and no")
            response = "yes"
        elif response.count("no") > 0 or response.count("false") > 0:
            if response.count("yes") > 0 or response.count("true") > 0:
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

    def getTheQuestion(self):
        return ContainingYesOrNo(self.category, self.elementToAsk, self.negation)
