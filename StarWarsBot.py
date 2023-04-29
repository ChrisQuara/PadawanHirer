import json
import random
import Question
import QuestionManager
from nltk.tokenize import MWETokenizer, word_tokenize
from NLGFunctions import *

manager = QuestionManager.QuestionManager.instance()
tokenizer = MWETokenizer()


def AvgWeightedSumOfQuestions(questions):
    sum_of_weights = 0
    for question in questions:
        sum_of_weights += question.weight
    return sum_of_weights / questions.__len__()


def getQuestionsScore(questions):
    total_scores = 0
    total_weights = 0
    for question in questions:
        total_scores += question.score
        total_weights += question.weight
    return total_scores / total_weights


def getCategoriesToAdd(number_of_questions):
    if number_of_questions > manager.getNumberOfQuestions():
        raise RuntimeError('number_of_questions must be <=  manager.getNumberOfQuestions()')
    categories_to_add = []

    for categories_added in manager.categories:
        categories_to_add.append(0)

    question_to_add = 0
    offset = 0
    while (question_to_add - offset) < number_of_questions:
        index = question_to_add % manager.categories.__len__()
        if manager.getQuestionsWithCategoryCriteria((lambda x: x == manager.getCategoryByIndex(index))).__len__() > \
                categories_to_add[index]:
            categories_to_add[index] += 1
        else:
            offset += 1
        question_to_add += 1

    return categories_to_add


def extractQuestions(number_of_questions, avg_weighted_sum):
    questions = manager.getQuestions()
    questions_extracted = []
    categories_to_add = getCategoriesToAdd(number_of_questions)

    last_extracted_weight = 1
    questions_added = 0
    while questions_added < number_of_questions:
        question_extracted = question_extracted = QuestionManager.QuestionManager.getComparisonWeightQuestion(questions,
                                                                                                              (lambda x,
                                                                                                                      y: x > y))
        if questions_added % 2 == 0:
            admissible_questions = QuestionManager.QuestionManager.getExplicitQuestionsWithWeightCriteria(questions, (
                lambda x: x >= avg_weighted_sum))
            if admissible_questions.__len__() > 0:
                question_extracted = random.choice(admissible_questions)

        else:
            questions_to_extract = QuestionManager.QuestionManager.getExplicitQuestionsWithWeightCriteria(questions, (
                lambda x: x >= 2 * avg_weighted_sum - last_extracted_weight))
            if questions_to_extract.__len__() > 0:
                question_extracted = QuestionManager.QuestionManager.getComparisonWeightQuestion(questions_to_extract,
                                                                                                 (lambda x, y: x < y))

        if categories_to_add[manager.getIndexCategory(question_extracted.category)] > 0:
            questions_added += 1
            questions_extracted.append(question_extracted)
            last_extracted_weight = question_extracted.weight
            categories_to_add[manager.getIndexCategory(question_extracted.category)] = categories_to_add[
                                                                                           manager.getIndexCategory(
                                                                                               question_extracted.category)] - 1
        questions.remove(question_extracted)

    return questions_extracted


def generateQuestions():
    data = json.load(open("KB.json"))
    all_possible_responses = []
    for category, answers in data.items():
        all_possible_responses += answers

    for category, answers in data.items():
        manager.addCategory(category)
        answers = list(answers)
        manager.addQuestion(Question.QuestionSpecifyAllElements(category, answers))
        manager.addQuestion(Question.QuestionEnumerateElements(category, answers))
        manager.addQuestion(Question.QuestionYesOrNo(category, answers, all_possible_responses))


'''def create_f(q):
    frame["category"] = q.category
    for responses in q.responses:
        frame[responses] = False
    return frame'''


def main():
    for sentence in PrimaFrase(random.choice([0, 1, 2])):
        print(sentence)
    name = input()
    print("Well " + name + "...")
    generateQuestions()
    questions = extractQuestions(5, 2.5)
    for question in questions:
        counter = 0
        counter_err = 0
        loop = True
        while loop and counter < question.maxAttempt and counter_err < 3:
            print(question.getTheQuestion())
            user_ans = tokenizer.tokenize(word_tokenize(input().lower()))
            try:
                score = question.getScore(user_ans)
                counter += 1
                print(correctAns(question, score))
                if score == question.weight:
                    loop = False
            except:
                print("Input error!")
                loop = True
                counter -= 1
                counter_err += 1
        if loop:
            print(endquestioning())

    print("AvgWeightedSumOfQuestions:" + str(AvgWeightedSumOfQuestions(questions)))
    print(scorecomment(getQuestionsScore(questions)))


main()
