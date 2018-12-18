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

    # Initialize Population
    population_df = pd.DataFrame({
        'text': [original_text] * population_size
    })
    results_df = pd.DataFrame(columns=['generation', 'best', 'worst', 'mean', 'best_text', 'worst_text'])

    nlp = spacy.load('en_core_web_lg')
    def obj(population_df):
        objective_func = np.vectorize(objective)
        return objective_func(population_df, original_text, nlp)

    generation = 0
    max_fitness_generation = 100
    curr_max_fitness = 0

    while generation < max_fitness_generation * 2 and generation < max_generation:
        generation += 1

        print(f'Recombining for Generation: {generation}')
        population_df = recombine(population_df, recombine_words, obj, nlp)

        print(f'Mutating for Generation: {generation}')
        population_df = mutate(population_df, mutate_token_synonym, obj, nlp)

        print(f'Selection for Generation: {generation}')
        population_df = selection(population_df, elitism_selection, obj)

        df = pd.DataFrame({
            'generation': generation,
            'best': population_df['fitness'].max(),
            'mean': population_df['fitness'].mean(),
            'worst': population_df['fitness'].min(),
            'best_text': population_df.loc[population_df['fitness'].idxmax(), 'text'],
            'worst_text': population_df.loc[population_df['fitness'].idxmin(), 'text'],
        })

        results_df.append(df)

        if curr_max_fitness < df['best']:
            max_fitness_generation = generation if generation > 100 else 100
            curr_max_fitness = df['best']

        print(f'''
        Generation: {df['Generation']}\t
        best: {df['best']} | {df['best_text']}\t
        worst: {df['worst']} | {df['worst_text']}\t
        mean: {df['mean']}\t
        ''')

    return results_df