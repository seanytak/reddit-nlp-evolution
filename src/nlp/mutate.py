import random as rand
import nltk 
from nltk.corpus import wordnet 

import numpy as np
import pandas as pd


def mutate(population, mutate_func, mutation_rate=0.5):
    """Mutates a member of the population using mutate_func with probability mutation_rate 
    """
    population_mut = []
    for member in population:
        offspring = member
        if rand.uniform(0, 1) <= mutation_rate:
            offspring = mutate_func(member)
        population_mut.append(offspring)
    return population_mut

def mutate_synonym(member: str):
    # nltk.download('wordnet')
    words = member.split(' ')

    # Pick a random word in the text
    locus = rand.randrange(0, len(words))
    rand_word = words[locus]

    # Get a unique list of synonyms to rand_word
    synonyms = list(set([l.name() for syn in wordnet.synsets(rand_word) for l in syn.lemmas()]))
    if synonyms:
        words[locus] = synonyms[rand.randrange(0, len(synonyms))]
    return ' '.join(words)

