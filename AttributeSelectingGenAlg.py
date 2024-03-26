from random import random, choice
from bitarray import bitarray
from tqdm import tqdm
import pandas as pd

from GenAlgUtilities.Crossover import crossover_types
from GenAlgUtilities.Reproduction import reproduction_types
from GenAlgUtilities.Mutation import mutation_types

from MLModels import model_types


def hit_prob(prob: float) -> bool:
    return random() <= prob


def generate_individual(length: int, weight_of_1) -> (list, float):
    while True:
        individual = bitarray(hit_prob(weight_of_1) for _ in range(length))
        if individual.any():
            return individual


def AttributeSelectingGenAlg(data: pd.DataFrame, target: pd.Series,
                             model_type: str = "bayesian",
                             test_ratio: float = 0.33,
                             population_power: int = 100,
                             population_cap: int = 50,
                             iteration_amount: int = 100,
                             reproduction_type: str = "championship",
                             reduction_rate: float = 0.5,
                             crossover_type: str = "uniform",
                             crossover_p: float = 0.4,
                             mutation_type: str = "bit",
                             mutation_p: float = 0.1,
                             weight_of_1: float = 0.5):

    def evaluate_population():
        evaluated_population = []
        for individual in population:
            if not individual.any():
                individual = generate_individual(attribute_amount, weight_of_1)
            mask = [bool(bit) for bit in individual]
            cut_data = data.loc[:, mask]
            evaluated_population.append((individual, model_f(cut_data, target, test_ratio)))
        return evaluated_population

    model_f = model_types[model_type]

    reproduction_f = reproduction_types[reproduction_type]
    crossover_f = crossover_types[crossover_type]
    mutation_f = mutation_types[mutation_type]

    attribute_amount = len(data.axes[1])
    population = [generate_individual(attribute_amount, weight_of_1)
                  for _ in range(population_power)]
    for _ in tqdm(range(iteration_amount)):

        evaluated_population = evaluate_population()

        population = reproduction_f(evaluated_population, reduction_rate)

        while len(population) < population_cap:
            population.append(generate_individual(attribute_amount, weight_of_1))

        if hit_prob(crossover_p):
            individual_1 = choice(population)
            while True:
                individual_2 = choice(population)
                if individual_2 != individual_1:
                    break

            population += crossover_f(individual_1, individual_2)

        if hit_prob(mutation_p):
            population = mutation_f(population)

    evaluated_population = evaluate_population()
    evaluated_population.sort(key=lambda x: x[1], reverse=True)

    possible_solutions = [evaluated_population[0][0]]
    target_score = evaluated_population[0][1]
    evaluated_population.pop(0)
    for individual in evaluated_population:
        if individual[1] != target_score:
            return target_score, possible_solutions
        if individual[0] not in possible_solutions:
            possible_solutions.append(individual[0])

    return target_score, possible_solutions