import numpy as np
import pandas as pd
import spacy

from evo_mutation import mutate, mutate_synonym, mutate_token_synonym
from evo_objective import objective
from evo_recombination import recombine, recombine_words
from evo_selection import selection, elitism_selection, fitness_proportional_selection


def evolve(original_text: str,
           population_size: int = 25,
           max_generation: int = 35) -> pd.DataFrame:

    # Construct Objective Function
    nlp = spacy.load('en_core_web_sm')
    def evo_objective(row):
        return objective(row, original_text, nlp)

    # Initialize Population
    population_df = pd.DataFrame({
        'text': [original_text] * population_size
    })
    population_df['fitness'] = population_df['text'].apply(evo_objective)

    # Construct Results DataFrame
    results_df = pd.DataFrame(columns=['generation', 'best', 'worst', 'mean', 'best_text', 'worst_text'])

    generation = 0
    max_fitness_generation = 100
    curr_max_fitness = 0

    while generation < max_fitness_generation * 2 and generation < max_generation:
        generation += 1

        print(f'Recombining for Generation: {generation}')
        # population_df = recombine(population_df, recombine_words, evo_objective, nlp)

        print(f'Mutating for Generation: {generation}')
        population_df = mutate(population_df, mutate_token_synonym, evo_objective, nlp)
        # print(population_df)

        print(f'Selection for Generation: {generation}')
        population_df = selection(population_df, elitism_selection)
        # print(population_df)

        new_generation = {
            'generation': generation,
            'best': population_df['fitness'].max(),
            'mean': population_df['fitness'].mean(),
            'worst': population_df['fitness'].min(),
            'best_text': population_df.loc[population_df['fitness'].idxmax(), 'text'],
            'worst_text': population_df.loc[population_df['fitness'].idxmin(), 'text'],
        }

        results_df.append(pd.DataFrame(new_generation, index=[0]))

        if curr_max_fitness < new_generation['best']:
            max_fitness_generation = generation if generation > 100 else 100
            curr_max_fitness = new_generation['best']

        print(f'''
        Generation: {new_generation['generation']}\t
        Best: {new_generation['best']} | {new_generation['best_text']}\t
        Worst: {new_generation['worst']} | {new_generation['worst_text']}\t
        Mean: {new_generation['mean']}\t
        ''')

    return results_df