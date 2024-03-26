def championship_reproduction(population: list, capacity: int = None) -> list:
    if not capacity:
        capacity = len(population) // 4

    population.sort(key=lambda x: x[1])

    new_population = [population[i][0] for i in range(capacity)]
    return new_population


def meritocratic_reproduction(population: list, capacity: int = None):
    pass


reproduction_types = {
    'championship': championship_reproduction
}
