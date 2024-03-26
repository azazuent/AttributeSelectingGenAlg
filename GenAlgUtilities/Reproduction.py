from math import ceil


def championship_reproduction(evaluated_population: list, reduction_rate: int = 0.5) -> list:
    capacity = ceil(len(evaluated_population) * reduction_rate)

    evaluated_population.sort(key=lambda x: x[1], reverse=True)

    new_population = [evaluated_population[i][0] for i in range(capacity)]
    return new_population


def meritocratic_reproduction(population: list, capacity: int = None):
    pass


reproduction_types = {
    'championship': championship_reproduction
}
