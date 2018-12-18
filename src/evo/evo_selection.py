import random as rand
import pandas as pd


def selection(population_df, selection_func):
    return selection_func(population_df)
    # population_fit = []
    # print(f'Running Objective Function on Population: ', end='', flush=True)
    # for idx, member in enumerate(population):
    #     print(f'{idx} ', end='', flush=True)
    #     fitness = objective_func(member)
    #     population_fit.append(fitness)
    # print('\nCompleted Objective Function Calculations')
    # df = pd.DataFrame({'population': population, 'fitness': population_fit})
    # population, population_fit = selection_func(df)
    # return population, population_fit


def elitism_selection(population_df, elite_percent=0.1):
    elite_num = int(len(population_df) * elite_percent)
    elite_df = population_df.sort_values(
        by=['fitness'], ascending=False).head(elite_num)
    sample_num = len(population_df) - elite_num
    elite_df = elite_df.append(
        population_df.sample(n=sample_num, replace=True), ignore_index=True)
    return elite_df


def fitness_proportional_selection(population, population_fit):
    sample_prob = []
    cdf = []
    fitness_sum = sum(population_fit)
    for idx, fitness in enumerate(population_fit):
        sample_prob_fitness = fitness / fitness_sum
        sample_prob.append(sample_prob_fitness)
        cdf.append(cdf[idx - 1] +
                   sample_prob[idx] if idx > 0 else sample_prob[idx])
    population_sel = population.copy()
    for i in range(len(population)):
        ran = rand.uniform(0, 1)
        for k in range(len(population)):
            if ran > cdf[k]:
                population_sel[i] = population[k]
                break
    return population_sel
