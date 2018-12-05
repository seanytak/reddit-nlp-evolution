import matplotlib
matplotlib.use('pdf')
import matplotlib.pyplot as plt
import numpy as np

from mutate import mutate, mutate_synonym
from objective import objective
from evo_select import fitness_proportional_selection


def evolve(original_text: str, n: int):
    def fitness_objective(member):
        return objective(member, original_text)

    # Initialize Population
    population = [original_text] * n

    generations = 0
    max_fitness_generation = 100
    curr_max_fitness = 0

    best_fitnesses = []
    worst_fitnesses = []
    mean_fitnesses = []

    while generations < 20:#max_fitness_generation * 2:
        generations += 1
        print(f'Mutating for Generation: {generations}')
        population = mutate(population, mutate_synonym)

        print(f'Selection for Generation: {generations}')
        population, population_fit = fitness_proportional_selection(population,
                                                    fitness_objective)
        

        # population_fit = [fitness_objective(member) for member in population]
        best_fitnesses.append(max(population_fit))
        worst_fitnesses.append(min(population_fit))
        mean_fitnesses.append(sum(population_fit) / len(population_fit))

        if curr_max_fitness < best_fitnesses[generations - 1]:
            max_fitness_generation = generations if generations > 100 else 100
            curr_max_fitness = best_fitnesses[generations - 1]

        print(f'''
        Generation: {generations}\t
        Best: {best_fitnesses[generations - 1]}\t
        Worst: {worst_fitnesses[generations - 1]}\t
        Mean: {mean_fitnesses[generations - 1]}\t
        Population: {population}
        ''')

    return best_fitnesses, worst_fitnesses, mean_fitnesses


best, worst, mean = evolve(
    "People driving around town with their GD high beams on makes me crazy.",
    n=10)
x = np.arange(0, len(best))

plt.scatter(x, y=np.array(best), label='Best')
plt.scatter(x, y=np.array(worst), label='Worst')
plt.scatter(x, y=np.array(mean), label='Mean')
plt.xlabel('Generations')
plt.ylabel('Fitness')
plt.title('Objective Function on the Best Individual in the Population')
plt.legend()
plt.savefig('results.pdf')
