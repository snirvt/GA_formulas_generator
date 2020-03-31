
import numpy as np
import random

class Mating_Handler():

    def __init__(self, num_offsprings_per_parent):
        self.num_offsprings_per_parent = num_offsprings_per_parent
    
    def choose_parents(self, population, population_fitness):
        sorted_population = self.sort_by_fitness(population, population_fitness)
        num_parents = int( len(population) / self.num_offsprings_per_parent )
        sampled_population = random.choices(sorted_population[int(num_parents/2):], k = int(num_parents/2))
        sorted_population[int(num_parents/2):num_parents] = sampled_population ## keep the best num_parents/2 parents, the rest are random
        return sorted_population, num_parents

    def sort_by_fitness(self, population, population_fitness):
        fitness_sorting_index = np.argsort(population_fitness)
        # return population[fitness_sorting_index[::-1]] # reverse sort population by fitness
        return population[fitness_sorting_index] # reverse sort population by fitness