import numpy as np

###################################
from individual import Individual
###################################

"""This class is responsible for creating the population and applying actions upon the individuals"""
class Population_Handler():
    def __init__(self, num_features, probability_handler, max_individual_size = 10):
        self.num_features = num_features
        self.probability_handler = probability_handler
        self.max_individual_size = max_individual_size
        self.population = []
        self.individual = Individual(self.num_features, self.max_individual_size)
        
    def create_individual(self):
        return self.individual.be_born()

    def create_population(self, population_size = 10): 
        self.population = np.empty([population_size]).astype(object)
        for i in range(population_size):
            self.population[i]=self.create_individual()

    def mutate(self):
        pass
    def cross_over(self):
        pass



