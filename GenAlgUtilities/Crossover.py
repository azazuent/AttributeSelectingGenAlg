from bitarray import bitarray
from random import randint, random


def one_point_crossover(individual1: bitarray, individual2: bitarray):
    crossover_point = randint(1, len(individual1) - 1)

    child_1 = individual1[:crossover_point] + \
              individual2[crossover_point:]

    child_2 = individual2[:crossover_point] + \
              individual1[crossover_point:]

    return [child_1, child_2]


def two_point_crossover(individual1: bitarray, individual2: bitarray):
    crossover_point_1 = randint(1, len(individual1) - 2)
    crossover_point_2 = randint(crossover_point_1 + 1, len(individual1) - 1)

    child_1 = individual1[:crossover_point_1] + \
              individual2[crossover_point_1:crossover_point_2] + \
              individual1[crossover_point_2:]

    child_2 = individual2[:crossover_point_1] + \
              individual1[crossover_point_1:crossover_point_2] + \
              individual2[crossover_point_2:]

    return [child_1, child_2]


def uniform_crossover(individual1: bitarray, individual2: bitarray):
    child_1 = bitarray()
    child_2 = bitarray()

    for i in range(len(individual1)):
        if random() < 0.5:
            child_1.append(individual1[i])
            child_2.append(individual2[i])
        else:
            child_1.append(individual2[i])
            child_2.append(individual1[i])

    return [child_1, child_2]


crossover_types = {
    "one_point": one_point_crossover,
    "two_point": two_point_crossover,
    "uniform": uniform_crossover
}
