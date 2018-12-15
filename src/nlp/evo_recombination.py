import random as rand
import nltk 
from nltk.corpus import wordnet 

import language_check

import numpy as np
import pandas as pd

def recombine(nlp, population, recombine_func, recombination_rate=0.05):
    """Mutates a member of the population using mutate_func with probability mutation_rate 
    """
    population_mut = []
    for member in population:
        offspring = member
        if rand.uniform(0, 1) <= recombination_rate:
            offspring = recombine_func(nlp, member, population[rand.randrange(0, len(population))])
        population_mut.append(offspring)
    return population_mut

def recombine_words(nlp, parent_one: str, parent_two: str):
    words_one = parent_one.split(' ')
    words_two = parent_two.split(' ')
    xo_one = rand.randrange(0, len(words_two))
    xo_two = rand.randrange(0, len(words_two))
    for i in range(min(xo_one, xo_two), max(xo_one, xo_two)):
        words_one[i] = words_two[i]
    return ' '.join(words_one)


