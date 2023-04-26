import random,json

from QuestionManager import QuestionManager
from Question import Question

manager = QuestionManager.instance()


def AvgWeightedSumOfQuestions(questions):
    sum_of_weights = 0
    for question in questions:
        sum_of_weights += question.weight
    return sum_of_weights / questions.__len__()


def getQuestionsScore(questions):
    total_scores = 0
    total_weights = 0
    for question in questions:
        total_scores += question.getScore()
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
        question_extracted = question_extracted = QuestionManager.getComparisonWeightQuestion(questions,
                                                                                              (lambda x,
                                                                                                      y: x > y))
        if questions_added % 2 == 0:
            admissible_questions = QuestionManager.getExplicitQuestionsWithWeightCriteria(questions, (
                lambda x: x >= avg_weighted_sum))
            if admissible_questions.__len__() > 0:
                question_extracted = random.choice(admissible_questions)

        else:
            questions_to_extract = QuestionManager.getExplicitQuestionsWithWeightCriteria(questions, (lambda x: x >= 2*avg_weighted_sum-last_extracted_weight))
            if questions_to_extract.__len__() > 0:
                question_extracted = QuestionManager.getComparisonWeightQuestion(questions_to_extract,
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

# __________________tests__________________
def testQuestionExtraction():

    manager.addCategory("jedi basics")
    manager.addCategory("sith")
    manager.addCategory("the force")

    manager.addQuestion(Question("jedi basics", 5, "1"))
    manager.addQuestion(Question("jedi basics", 4, "2"))
    manager.addQuestion(Question("jedi basics", 3, "3"))
    manager.addQuestion(Question("jedi basics", 2, "4"))
    manager.addQuestion(Question("jedi basics", 1, "5"))

    manager.addQuestion(Question("sith", 5, "6"))
    manager.addQuestion(Question("sith", 4, "7"))
    manager.addQuestion(Question("sith", 2, "8"))
    manager.addQuestion(Question("sith", 1, "9"))

    manager.addQuestion(Question("the force", 5, "10"))
    manager.addQuestion(Question("the force", 4, "11"))
    manager.addQuestion(Question("the force", 3, "12"))

    questions = extractQuestions(8, 2.5)

    print("[")
    for question in questions:
        print(question.toString())
    print("]")
    print("AvgWeightedSumOfQuestions:" + str(AvgWeightedSumOfQuestions(questions)))
    print("Score (per il momento deve dare sempre 1):" + str(getQuestionsScore(questions)))

#_____________________Main______________________
def knowledgebuilder():
    kb = json.load(open("KB.json"))
    return kb

manager = QuestionManager.instance()
data = knowledgebuilder()
frame = {}
for category, answers in data.items():
    manager.addCategory(category)
    answers = list(answers)
    manager.addQuestion(Question(category, 5, answers))
    manager.addQuestion(Question(category, 3, random.choice(answers)))
    bool_answer = ["yes", "no"] 
    manager.addQuestion(Question(category, 2, random.choice(bool_answer)))

def create_f(q):
        frame["category"] = q.category
        for responses in q.responses:
            frame[responses] = False
        return frame


def main():
    print("Saluto")
    questions = extractQuestions(3, 2.5)
    print("[")
    for question in questions:
        create_f(question)
        user_ans = input().lower()
    print("]")
    print("AvgWeightedSumOfQuestions:" + str(AvgWeightedSumOfQuestions(questions)))
    print("Score (per il momento deve dare sempre 1):" + str(getQuestionsScore(questions)))
    
main()

