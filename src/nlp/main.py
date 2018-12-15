from datetime import datetime
import sys

import click
import matplotlib
import matplotlib.pyplot as plt
matplotlib.use('pdf')
import numpy as np

from evo import evolve

@click.command()
@click.option('-t', '--text', default='I am really hungry in the daytime but not the nighttime.', help='Base text to modify.')
@click.option('-n', '--population-size', default=25, help='Number of members in the population.')
@click.option('-g', '--generations', default=25, help='Minimum number of generations.')
@click.option('-m', '--max-generations', default=35, help='Maximum number of generations.')
def main(text: str, population_size: int, generations: int, max_generations: int):
    """Driver code for the evolve program"""
    best, worst, mean = evolve(text, population_size, max_generations)
    x = np.arange(0, len(best))
    plt.scatter(x, y=np.array(best), label='Best')
    plt.scatter(x, y=np.array(worst), label='Worst')
    plt.scatter(x, y=np.array(mean), label='Mean')
    plt.xlabel('Generations')
    plt.ylabel('Fitness')
    plt.title('Objective Function on the Best Individual in the Population')
    plt.legend()
    plt.savefig(f'results_{datetime.now()}.pdf')

if __name__ == '__main__':
    main()



