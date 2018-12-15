import spacy

from evo_mutation import mutate, mutate_synonym, mutate_token_synonym
from evo_objective import objective
from evo_recombination import recombine, recombine_words
from evo_selection import fitness_proportional_selection


def evolve(original_text: str, n: int = 25, max_generations: int = 35):
    nlp = spacy.load('en_core_web_sm')

    def fitness_objective(member):
        return objective(nlp, member, original_text)

    # Initialize Population
    population = [original_text] * n

    generations = 0
    max_fitness_generation = 100
    curr_max_fitness = 0

    best_fitnesses = []
    worst_fitnesses = []
    mean_fitnesses = []

    while generations < max_fitness_generation * 2 and generations < max_generations:
        generations += 1
        print(f'Recombining for Generation: {generations}')
        population = recombine(nlp, population, recombine_words)
        print(f'Mutating for Generation: {generations}')
        population = mutate(nlp, population, mutate_token_synonym)

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