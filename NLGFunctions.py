from simplenlg.framework import *
from simplenlg.realiser.english import *
from simplenlg.features import *
from simplenlg.phrasespec import *
import json

lexicon = Lexicon.getDefaultLexicon()
nlgFactory = NLGFactory(lexicon)
realiser = Realiser(lexicon)

'''
def dizionario():
    dizionario = json.load(open("dizionario.json"))
    return dizionario


data = dizionario()'''


def PrimaFrase(n):
    if (n == 0):
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
    elif (n == 1):
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
    elif (n == 2):
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


def SpecifyAllElements(category):
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
    return question_done


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


def correctAns(question, score):
    p = nlgFactory.createClause()
    subj = nlgFactory.createNounPhrase("your answer")
    comp = ""
    if score == question.weight:
        verb = nlgFactory.createVerbPhrase("be correct")
    elif question.isPartiallyCorrect:
        verb = nlgFactory.createVerbPhrase("be partially correct")
        #comp = nlgFactory.createStringElement(", tell me more about it")
    else:
        verb = nlgFactory.createVerbPhrase("be not correct")
    p.setSubject(subj)
    p.setVerbPhrase(verb)
    p.setComplement(comp)
    reaction = realiser.realiseSentence(p)
    return reaction


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


# Ho solo implementato la parte in cui l'utente viene bocciato, non so nulla di star wars lol
def scorecomment(score):
    reaction = "Empty reaction"
    if score < 0.6:
        p = nlgFactory.createClause("You", "are", "probably a true sith")
        p.setPlural(True)
        reaction = realiser.realiseSentence(p)
    return reaction
