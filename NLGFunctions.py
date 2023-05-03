from simplenlg.framework import *
from simplenlg.realiser.english import *
from simplenlg.features import *
from simplenlg.phrasespec import *
import json
import random

lexicon = Lexicon.getDefaultLexicon()
nlgFactory = NLGFactory(lexicon)
realiser = Realiser(lexicon)

'''
def dizionario():
    dizionario = json.load(open("dizionario.json"))
    return dizionario


data = dizionario()'''


def PrimaFrase(n):
    n = [0, 1, 2]
    m = random.choice(n)
    if (m == 0):
        array = []
        phrase1 = nlgFactory.createClause()
        phrase1.setSubject("You")
        phrase1.setVerb("be")
        phrase1.addComplement("brave")
        phrase1.addComplement("my little Padawan")
        phrase1.setPlural(True)
        sentence = realiser.realiseSentence(phrase1)
        array.append(sentence)
        breath = nlgFactory.createClause()
        breath.addPreModifier("hhhhh...")
        array.append(realiser.realiseSentence(breath))
        phrase2 = nlgFactory.createClause("Now", "prove", "your knowledge")
        phrase2.setSubject("you")
        phrase2.addFrontModifier("Now")
        phrase2.setFeature(Feature.MODAL, "have to")
        phrase3 = nlgFactory.createClause("so, tell me your name")
        phrase2.addPostModifier(phrase3)
        sentence = realiser.realiseSentence(phrase2)
        array.append(sentence)
        return array
    elif (m == 1):
        array = []
        phrase1 = nlgFactory.createClause()
        phrase1.setSubject("I")
        phrase1.setVerb("be tired")
        phrase1.addComplement("today")
        phrase1.addComplement("my little Padawan")
        sentence = realiser.realiseSentence(phrase1)
        array.append(sentence)
        breath = nlgFactory.createClause()
        breath.addPreModifier("hhhhh...")
        array.append(realiser.realiseSentence(breath))
        phrase2 = nlgFactory.createAdjectivePhrase("That's a bad day")
        phrase3 = nlgFactory.createClause("so, tell me your name")
        phrase2.addPostModifier(phrase3)
        array.append(realiser.realiseSentence(phrase2))
        return array
    elif (m == 2):
        array = []
        phrase1 = nlgFactory.createClause()
        phrase1.setSubject("I")
        phrase1.setVerb("want")
        phrase1.setFeature(Feature.NEGATED, True)
        object1 = nlgFactory.createClause("to loose my time")
        object2 = nlgFactory.createNounPhrase("patience")
        obj = nlgFactory.createCoordinatedPhrase(object1, object2)
        phrase1.addPostModifier(obj)
        sentence = realiser.realiseSentence(phrase1)
        array.append(sentence)
        breath = nlgFactory.createClause()
        breath.addPreModifier("hhhhh...")
        array.append(realiser.realiseSentence(breath))
        phrase2 = nlgFactory.createAdjectivePhrase("Maybe this is your lucky day")
        phrase3 = nlgFactory.createClause("so, tell me your name")
        phrase2.addPostModifier(phrase3)
        array.append(realiser.realiseSentence(phrase2))
        return array


def ResponseToInput(name):
    array = []
    if name == "luke":
        p = nlgFactory.createClause()
        subj = nlgFactory.createNounPhrase("Your name")
        verb = nlgFactory.createVerbPhrase("suppose that")
        obj = nlgFactory.createNounPhrase("the force")
        subordinate = nlgFactory.createClause("is strong with you")
        p.addFrontModifier("Nice Luke!")
        p.setSubject(subj)
        p.setVerb(verb)
        p.setObject(obj)
        p.addPostModifier(subordinate)
        sentence = realiser.realiseSentence(p)
        breath = nlgFactory.createClause("hhhhh...")
        array.append(realiser.realiseSentence(breath))
        array.append(sentence)
        p2 = nlgFactory.createClause("like a perfect Skywalker...")
        array.append(realiser.realiseSentence(p2))
        return array
    else:
        n = [0, 1, 2]
        m = random.choice(n)
        if (m == 0):
            p2 = nlgFactory.createClause()
            p2.addFrontModifier("Mmm...")
            p2.addFrontModifier(name)
            p2.addPostModifier(",")
            p2.setSubject("I")
            p2.setVerb("be sure")
            p2.setFeature(Feature.NEGATED, True)
            prep = nlgFactory.createPrepositionPhrase("that you are good enough")
            p2.addPostModifier(prep)
            sentence2 = realiser.realiseSentence(p2)
            breath = nlgFactory.createClause()
            breath.addPreModifier("hhhhh...")
            array.append(realiser.realiseSentence(breath))
            array.append(sentence2)
            p3 = nlgFactory.createClause("But... let's start!")
            sentence3 = realiser.realiseSentence(p3)
            array.append(sentence3)
        elif (m == 1):
            p = nlgFactory.createClause()
            intro = nlgFactory.createNounPhrase("Well", name)
            intro.addPostModifier("...")
            p3 = realiser.realiseSentence(intro)
            p.setSubject("you")
            verb = nlgFactory.createVerbPhrase("be ready for the challenge")
            p.setVerbPhrase(verb)
            p.setFeature(Feature.INTERROGATIVE_TYPE, InterrogativeType.YES_NO)
            sentence = realiser.realiseSentence(p)
            p2 = nlgFactory.createClause("C'mon let's start! The Dark can't wait")
            sentence2 = realiser.realiseSentence(p2)
            array.append(p3)
            array.append(sentence)
            array.append(sentence2)
        elif (m == 2):
            p = nlgFactory.createClause()
            p.addFrontModifier(name)
            p.setSubject("you")
            verb = nlgFactory.createVerbPhrase("be ready to test")
            p.setVerbPhrase(verb)
            p.setComplement("your Dark... sorry, competence")
            p.setFeature(Feature.INTERROGATIVE_TYPE, InterrogativeType.YES_NO)
            sentence = realiser.realiseSentence(p)
            p2 = nlgFactory.createClause("C'mon let's start! The Dark can't wait")
            sentence2 = realiser.realiseSentence(p2)
            array.append(sentence)
            array.append(sentence2)
        return array


def SpecifyAllElements(category, attempt):
    array = []
    if (attempt == 0):
        p = nlgFactory.createClause()
        p.setSubject("you")
        p.setVerb("specify")
        p.setFeature(Feature.MODAL, "can")
        obj = nlgFactory.createNounPhrase(category)
        preposition = nlgFactory.createPrepositionPhrase(preposition="about")
        preposition.addComplement(obj)
        p.addPostModifier(preposition)
        p.setFeature(Feature.INTERROGATIVE_TYPE, InterrogativeType.WHAT_OBJECT)
        question_done = realiser.realiseSentence(p)
        breath = nlgFactory.createClause("Hhhhh...")
        array.append(realiser.realiseSentence(breath))
        array.append(question_done)
        return array
    elif (attempt == 1):
        p1 = nlgFactory.createClause("I", "need", "more precision")
        sentence = realiser.realiseSentence(p1)
        array.append(sentence)
        p = nlgFactory.createClause()
        p.setSubject("you")
        p.setVerb("specify")
        p.setFeature(Feature.MODAL, "can")
        obj = nlgFactory.createNounPhrase(category)
        preposition = nlgFactory.createPrepositionPhrase(preposition="something else about")
        preposition.addComplement(obj)
        p.addPostModifier(preposition)
        p.setFeature(Feature.INTERROGATIVE_TYPE, InterrogativeType.YES_NO)
        question_done = realiser.realiseSentence(p)
        array.append(question_done)
        return array
    elif (attempt == 2):
        p = nlgFactory.createClause("This is not enough for me!")
        sentence = realiser.realiseSentence(p)
        breath = nlgFactory.createClause("Hhhhh...")
        array.append(realiser.realiseSentence(breath))
        array.append(sentence)
        p1 = nlgFactory.createClause("say", "something about")
        p1.addFrontModifier("Please,")
        p1.setComplement(category)
        sentence2 = realiser.realiseSentence(p1)
        array.append(sentence2)
        return array


def EnumerateAllElements(category):
    p = nlgFactory.createClause("you tell me", "how many notions", "do you know")
    p.setFeature(Feature.MODAL, "Can")
    obj = nlgFactory.createNounPhrase(category)
    preposition = nlgFactory.createPrepositionPhrase(preposition="about")
    preposition.addComplement(obj)
    p.addPostModifier(preposition)
    p.setFeature(Feature.INTERROGATIVE_TYPE, InterrogativeType.YES_NO)
    question_done = realiser.realiseSentence(p)
    return question_done


def ContainingYesOrNo(category, element, negated):
    p = nlgFactory.createClause()
    subj = nlgFactory.createNounPhrase("it")
    if negated:
        verb = nlgFactory.createVerbPhrase("be false that")
    else:
        verb = nlgFactory.createVerbPhrase("be true that")
    obj1 = nlgFactory.createNounPhrase(element)
    complement = nlgFactory.createPrepositionPhrase("belongs to", category)
    obj2 = nlgFactory.createNounPhrase(complement)
    p.setSubject(subj)
    p.setVerbPhrase(verb)
    p.setObject(obj1)
    p.setComplement(obj2)
    p.setFeature(Feature.INTERROGATIVE_TYPE, InterrogativeType.YES_NO)
    question_done = realiser.realiseSentence(p)
    return question_done


# risposta di Darth Vader a domande che richiedono all'utente di rispondere Yes or No
def ResponseToYesOrNo(question, score):
    category = question.category
    if score == question.weight:  # risposta corretta
        p = nlgFactory.createClause("The Force", "seems to be", "on your side")
        p.addFrontModifier("Good!")
        p.addPostModifier(",")
        p2 = nlgFactory.createClause("you", "know", "something about")
        p2.setPlural(True)
        p.addPostModifier(p2)
        p3 = nlgFactory.createNounPhrase(category)
        p3.addPostModifier("...")
        p2.addPostModifier(p3)
        response_done = realiser.realiseSentence(p)
    else:
        p = nlgFactory.createClause("You", "be", "wrong!")
        p.setPlural(True)
        p.addFrontModifier("Damn!")
        subj = nlgFactory.createNounPhrase("You")
        subj.setFeature(Feature.ELIDED, True)
        p2 = nlgFactory.createClause(subj, "Need to study more about")
        p2.setPlural(True)
        p2.addPostModifier(category)
        p.addPostModifier(p2)
        response_done = realiser.realiseSentence(p)
    return response_done


# dopo un tot di risposte "bad" generiamo casualmente una risposta cuscinetto
def SafeQuestion(category):
    subj = nlgFactory.createNounPhrase("You")
    subj.setFeature(Feature.ELIDED, True)
    p = nlgFactory.createClause(subj, "be", "focused")
    p.setPlural(True)
    p.setFeature(Feature.MODAL, "have to")
    p.addPostModifier("we were talking about")
    p.addPostModifier(category)
    p.addPostModifier("wake up!")
    sentence = nlgFactory.createClause(subj, p)
    sentence1 = realiser.realiseSentence(sentence)
    return sentence1


# risposte per quando si risponde male a Darth Vader per 3 volte
# se è maggiore di 3 chiamiamo la domanda "cuscinetto"  SafeQuestion
def BadResponse(badInput, question):
    if (badInput == 0):
        array = []
        p = nlgFactory.createClause()
        p.setSubject("I")
        verb = nlgFactory.createVerbPhrase("find your lack of faith disturbing...")
        p.setVerbPhrase(verb)
        array.append(realiser.realiseSentence(p))
        breath = nlgFactory.createClause("Hhhhh...")
        array.append(realiser.realiseSentence(breath))
        p2 = nlgFactory.createClause("The light", "confuses you")
        p2.setFeature(Feature.TENSE, Tense.PAST)
        array.append(realiser.realiseSentence(p2))
        p4 = nlgFactory.createClause("Try to say", "something good")
        p4.setPlural(True)
        p5 = nlgFactory.createClause("don't waste my time with your incompetence")
        p6 = nlgFactory.createCoordinatedPhrase(p4, p5)
        array.append(realiser.realiseSentence(p6))
    elif (badInput == 1):
        array = []
        p = nlgFactory.createClause("Your lack of control", "is disturbing")
        adv = nlgFactory.createAdverbPhrase("Very bad!")
        p.addFrontModifier(adv)
        array.append(realiser.realiseSentence(p))
        breath = nlgFactory.createClause("Hhhhh...")
        array.append(realiser.realiseSentence(breath))
        p2 = nlgFactory.createClause("you", "don't know", "the power of Dark Side")
        p2.addFrontModifier("Maybe")
        p2.setPlural(True)
        array.append(realiser.realiseSentence(p2))
    elif (badInput == 2):
        array = []
        p = nlgFactory.createClause("You", "fail me", "yet again")
        p.setFeature(Feature.TENSE, Tense.PAST)
        array.append(realiser.realiseSentence(p))
        breath = nlgFactory.createClause("Hhhhh...")
        array.append(realiser.realiseSentence(breath))
        p2 = nlgFactory.createClause("I", "tolerate", "such arrogance")
        p2.setFeature(Feature.NEGATED, True)
        p2.setFeature(Feature.MODAL, "can")
        subordinate = nlgFactory.createNounPhrase("from a simple initiated rookie")
        p2.addPostModifier(subordinate)
        array.append(realiser.realiseSentence(p2))
        p3 = nlgFactory.createClause("you", "wish experience", "the full power of the Dark Side")
        p4 = nlgFactory.createVerbPhrase("feel the sting of my lightsaber")
        p4.setPlural(True)
        p3.addPostModifier("and")
        p3.addPostModifier(p4)
        p3.setFeature(Feature.INTERROGATIVE_TYPE, InterrogativeType.YES_NO)
        array.append(realiser.realiseSentence(p3))
        array.append(SafeQuestion(question.category))
    return array


def endquestioning():
    react = nlgFactory.createClause("You", "exhausted", "my patience")
    react.setFeature(Feature.PERFECT, True)
    react1 = nlgFactory.createClause("I", "ask anymore", " about this question")
    react1.setFeature(Feature.TENSE, Tense.FUTURE)
    react1.setFeature(Feature.NEGATED, True)
    react.setPlural(True)
    react1.setPlural(True)
    c = nlgFactory.createCoordinatedPhrase(react, react1)
    reaction = realiser.realiseSentence(c)
    return reaction


def correctAns(question, score):
    if type(question).__name__ == "QuestionYesOrNo":
        return ResponseToYesOrNo(question, score)
    p = nlgFactory.createClause()
    subj = nlgFactory.createNounPhrase("your answer")
    comp = ""
    if score == question.weight:
        verb = nlgFactory.createVerbPhrase("be correct")
        p2 = nlgFactory.createClause("let's go to another question")
        p.addPostModifier(p2)
    elif question.isPartiallyCorrect:
        verb = nlgFactory.createVerbPhrase("be partially correct")
        # p2 = nlgFactory.createClause("You", "know", "something else about")
        # p2.addPostModifier(category)
        # p.addPostModifier(p2)
        # comp = nlgFactory.createStringElement(", tell me more about it")
    else:
        verb = nlgFactory.createVerbPhrase("be not correct")
    p.setSubject(subj)
    p.setVerbPhrase(verb)
    p.setComplement(comp)
    reaction = realiser.realiseSentence(p)
    return reaction


def scorecomment(score):
    array = []
    if score < 0.6:
        p = nlgFactory.createClause("Your lack of preparation and focus", "be", "a clear indication")
        subordinate = nlgFactory.createPrepositionPhrase("of your weakness")
        p.addPostModifier(subordinate)
        reaction = realiser.realiseSentence(p)
        p2 = nlgFactory.createClause("You", "squander", "your potential")
        p2.setPlural(True)
        subordinate2 = nlgFactory.createClause("with careless mistakes")
        p2.addPostModifier(subordinate2)
        p3 = nlgFactory.createClause("You failed a simple test...")
        array.append(reaction)
        array.append(realiser.realiseSentence(p2))
        array.append(realiser.realiseSentence(p3))
        subordinate3 = nlgFactory.createPrepositionPhrase("in the greater challenges that lie ahead")
        p4 = nlgFactory.createClause("you", "expect to succeed", subordinate3)
        p4.setFeature(Feature.MODAL, "can")
        p4.setFeature(Feature.INTERROGATIVE_TYPE, InterrogativeType.HOW)
        array.append(realiser.realiseSentence(p4))
        p5 = nlgFactory.createClause("You must do better or face the consequences,")
        p6 = nlgFactory.createClause("come back when you really know the jedi art")
        p5.addPostModifier(p6)
        array.append(realiser.realiseSentence(p5))
    if score >= 0.6:
        breath = nlgFactory.createClause("Hhhhh...")
        array.append(realiser.realiseSentence(breath))
        p = nlgFactory.createClause("Now, the last question if you want to be my Padawan")
        array.append(FinalQuestion())
    return array


def FinalQuestion():
    subordinate = nlgFactory.createPrepositionPhrase("ready to embrace the Dark Side of the force")
    p = nlgFactory.createClause("you", "be", subordinate)
    p.setPlural(True)
    p.setFeature(Feature.INTERROGATIVE_TYPE, InterrogativeType.YES_NO)
    response = realiser.realiseSentence(p)
    return response


def ChooseTheDark(user_answer):
    array = []
    if user_answer.count("yes") > 0 or user_answer.count("sure") > 0 or user_answer.count("okay"):
        s = nlgFactory.createClause("This", "be", "the right choice")
        array.append(realiser.realiseSentence(s))
        p = nlgFactory.createClause("Your performance", "has impressed", "me")
        array.append(realiser.realiseSentence(p))
        p2 = nlgFactory.createClause("Your mastery of the Force")
        p3 = nlgFactory.createClause("is evident in your precise and efficient execution")
        p2.addPostModifier(p3)
        array.append(realiser.realiseSentence(p2))
        breath = nlgFactory.createClause("Hhhhh...")
        array.append(realiser.realiseSentence(breath))
        p4 = nlgFactory.createClause("There is no power in light,")
        p5 = nlgFactory.createClause("only weakness and submission")
        p4.addPostModifier(p5)
        p6 = nlgFactory.createClause("You", "can be", "my Padawan")
        p6.setPlural(True)
        p7 = nlgFactory.createClause("rule the darkness with me")
        coord = nlgFactory.createCoordinatedPhrase(p6, p7)
        p8 = nlgFactory.createClause("The Dark Side", "be", "the path to true power,")
        p9 = nlgFactory.createPrepositionPhrase("to bring order to chaos")
        p10 = nlgFactory.createPrepositionPhrase("to shape galaxy as we see fit")
        coord2 = nlgFactory.createCoordinatedPhrase(p9, p10)
        p8.addPostModifier(coord2)
        array.append(realiser.realiseSentence(p8))
        array.append(realiser.realiseSentence(p4))
        array.append(realiser.realiseSentence(coord))
    else:
        p = nlgFactory.createClause("Your performance", "has impressed", "me")
        array.append(realiser.realiseSentence(p))
        p2 = nlgFactory.createClause("Your mastery of the Force")
        p3 = nlgFactory.createClause("is evident in your precise and efficient execution")
        p2.addPostModifier(p3)
        array.append(realiser.realiseSentence(p2))
        breath = nlgFactory.createClause("Hhhhh...")
        array.append(realiser.realiseSentence(breath))
        p4 = nlgFactory.createClause("the light", "is never", "a good way")
        p4.addFrontModifier("But")
        p5 = nlgFactory.createPrepositionPhrase("just a consolation")
        p4.addPostModifier(p5)
        array.append(realiser.realiseSentence(p4))
        p6 = nlgFactory.createClause("I", "to suppose")
        p6.setFeature(Feature.MODAL, "have")
        subordinate2 = nlgFactory.createClause("you", "be", "follower of Obi-Wan")
        subordinate2.addFrontModifier("that")
        p6.addPostModifier(subordinate2)
        array.append(realiser.realiseSentence(p6))
        p7 = nlgFactory.createClause("You can be a Padawan, but not mine")
        array.append(realiser.realiseSentence(p7))
    return array