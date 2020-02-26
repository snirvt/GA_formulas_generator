import numpy as np
from multiprocessing import Pool, cpu_count

###################################
from individual import Individual
from mutation_handler import Mutation_Handler
import constants
from values_handler import Values_Handler
###################################

"""This class is responsible for creating the population and applying actions upon the individuals"""
class Population_Handler():
    def __init__(self, probability_handler, max_individual_size = 10):
        self.probability_handler = probability_handler
        self.max_individual_size = max_individual_size
        self.population = []
        self.values_handler = Values_Handler(probability_handler)
        self.individual = Individual(self.probability_handler.max_feature_number, self.max_individual_size, self.values_handler)
        self.mh = Mutation_Handler(self.probability_handler, self.values_handler)
        
    def create_individual(self):
        return self.individual.be_born()

    def create_population(self, population_size = 10): 
        self.population = np.empty([population_size]).astype(object)
        for i in range(population_size):
            self.population[i] = self.create_individual()

    def mutate_population(self):
        for individual in self.population[1:]: ## dont mutate the top best
            self.mh.mutate(individual)

    def mutate_population_paralal(self):
        p = Pool(constants.NUM_POOL)
        paralal_input = list(self.population)
        paralal_result = p.map(self.mh.mutate_paralal, paralal_input)
        p.close()
        p.join()
        self.population = np.array(paralal_result)

    def cross_over_population(self):
        pass

    def get_population(self):
        return self.population

    def set_population(self, new_generation):
        self.population = new_generation
