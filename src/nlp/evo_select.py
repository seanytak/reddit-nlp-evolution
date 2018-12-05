import random as rand

def fitness_proportional_selection(population, objective):
    population_fit = []
    fitness_sum = 0
    print(f'Running Objective Function on Population: ', end='', flush=True)
    for idx, member in enumerate(population):
        print(f'{idx} ', end='', flush=True)
        fitness = objective(member)
        fitness_sum += fitness
        population_fit.append(fitness)
    print('\nCompleted Objective Function Calculations')
    sample_prob = []
    cdf = []
    for idx, fitness in enumerate(population_fit):
        sample_prob_fitness = fitness / fitness_sum
        sample_prob.append(sample_prob_fitness)
        cdf.append(cdf[idx - 1] + sample_prob[idx] if idx > 0 else sample_prob[idx])
    population_sel = population.copy()
    for i in range(len(population)):
        ran = rand.uniform(0, 1)
        for k in range(len(population)):
            if ran > cdf[k]:
                population_sel[i] = population[k]
                break
    return population_sel, population_fit

        