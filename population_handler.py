import numpy as np

###################################
from individual import Individual
from mutation_handler import Mutation_Handler
###################################

"""This class is responsible for creating the population and applying actions upon the individuals"""
class Population_Handler():
    def __init__(self, probability_handler, max_individual_size = 10):
        self.probability_handler = probability_handler
        self.max_individual_size = max_individual_size
        self.population = []
        self.individual = Individual(self.probability_handler.max_feature_number, self.max_individual_size)
        self.mh = Mutation_Handler(self.probability_handler)
        
    def create_individual(self):
        return self.individual.be_born()

    def create_population(self, population_size = 10): 
        self.population = np.empty([population_size]).astype(object)
        for i in range(population_size):
            self.population[i]=self.create_individual()

    def mutate_population(self):
        for individual in self.population:
            self.mh.mutate(individual)

    def cross_over_population(self):
        pass

    def get_population(self):
        return self.population
