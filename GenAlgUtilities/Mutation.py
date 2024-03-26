from random import randint, choice


def bit_mutation(population: list, target_amount: int = 1):
    population_copy = population.copy()
    population_size = len(population_copy)

    for _ in range(target_amount):
        individual_index = randint(0, population_size - 1)
        mutating_bit = randint(0, len(population_copy[0]) - 1)

        population_copy[individual_index][mutating_bit] = \
            not population_copy[individual_index][mutating_bit]

    return population_copy


mutation_types = {
    "bit": bit_mutation
}
