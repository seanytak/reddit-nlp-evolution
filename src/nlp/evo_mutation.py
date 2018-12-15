import random as rand
import nltk 
from nltk.corpus import wordnet 

import language_check

import numpy as np
import pandas as pd


def mutate(nlp, population, mutate_func, mutation_rate=0.5):
    """Mutates a member of the population using mutate_func with probability mutation_rate 
    """
    population_mut = []
    for member in population:
        offspring = member
        if rand.uniform(0, 1) <= mutation_rate:
            offspring = mutate_func(nlp, member)
        population_mut.append(offspring)
    return population_mut

def mutate_verb(nlp, member: str):
    doc = nlp(member)
    verbs = []
    for idx in range(1, len(doc)):
        if doc[idx].pos_ == 'VERB' and doc[idx - 1].pos_ != 'ADV':
            verbs.append((doc[idx].text, idx))
    
    



def mutate_token_synonym(nlp, member: str):

    # Pick a random word
    words = member.split(' ')
    locus = rand.randrange(0, len(words))

    # Tokenize the words
    doc = nlp(member)
    rand_token = doc[locus]
    # print(rand_token.text)
    # print(doc)

    # Find a synonym to replace the word that matches the part of speech
    synonyms = list(set([l.name() for syn in wordnet.synsets(rand_token.text) for l in syn.lemmas()]))
    if synonyms:
        pos = None
        trials = 0
        max_trials = 15
        print(f'Chosen Word: {rand_token.text} | Part-of-Speech: {rand_token.pos_}')
        while trials < max_trials and pos != rand_token.pos_:
            words[locus] = synonyms[rand.randrange(0, len(synonyms))]
            member = ' '.join(words)
            # member = ' '.join(token.text_with_ws for token in doc)
            doc = nlp(member)
            pos = doc[locus].pos_
            print(f'Trying Replacement Word: {doc[locus].text} | Part-of-Speech: {doc[locus].pos_}')
            trials += 1
    print(member)

    # Grammar Fixer
    tool = language_check.LanguageTool('en-US')
    matches = tool.check(member)
    member = language_check.correct(member, matches)
    # if member != corrected_text:
    #     member = corrected_text
    #     print(f'Corrected Text: {corrected_text} | Original Text: {member}')

    return member


def mutate_synonym(nlp, member: str):
    # nltk.download('wordnet')
    words = member.split(' ')

    # Pick a random word in the text
    locus = rand.randrange(0, len(words))
    rand_word = words[locus]

    # Get a unique list of synonyms to rand_word
    synonyms = list(set([l.name() for syn in wordnet.synsets(rand_word) for l in syn.lemmas()]))
    if synonyms:
        words[locus] = synonyms[rand.randrange(0, len(synonyms))]

    # Grammar Checking
    text = ' '.join(words)
    tool = language_check.LanguageTool('en-US')
    matches = tool.check(text)
    corrected_text = language_check.correct(text, matches)
    if text != corrected_text:
        print(f'Corrected Text: {corrected_text} | Original Text: {text}')

    return text

