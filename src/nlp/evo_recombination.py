import random as rand
import nltk 
from nltk.corpus import wordnet 

import language_check

import numpy as np
import pandas as pd

# def recombine(nlp, population, recombine_func):
#     """Mutates a member of the population using mutate_func with probability mutation_rate 
#     """
#     population_mut = []
#     for member in population:
#         offspring = member
#         if rand.uniform(0, 1) <= mutation_rate:
#             offspring = recombine_func(nlp, member)
#         population_mut.append(offspring)
#     return population_mut