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
@click.option('-d', '--debug', is_flag=True, help='Invoke Debug Mode.')
def main(text: str, population_size: int, generations: int, max_generations: int, debug: bool):
    """CLI tool to invoke an NLP processor to syntactically modify a sentence while keeping it semantically intact.
    Converges to a solution using evolutionary algorithm approach."""
    best, worst, mean = evolve(text, population_size, max_generations)
    x = np.arange(0, len(best))
    plt.scatter(x, y=np.array(best), label='Best')
    plt.scatter(x, y=np.array(worst), label='Worst')
    plt.scatter(x, y=np.array(mean), label='Mean')
    plt.xlabel('Generations')
    plt.ylabel('Fitness')
    plt.title('Objective Function on the Best Individual in the Population')
    plt.legend()
    plt.savefig(f'results/results_{datetime.now()}.pdf')

if __name__ == '__main__':
    main()



