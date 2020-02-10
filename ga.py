
import numpy as np
import pandas as pd

###################################
from population_handler import Population_Handler
from probability_handler import Probability_Handler
import constants
from evaluator import Evaluator
from data_parser import Data_Parser
###################################


class GA():

    def __init__(self, X, y, column_names):
        self.X = X
        self.y = y
        self.column_names = column_names

        self.probability_handler = []
        self.population_handler = []
        self.setup()

    def setup(self):
        self.probability_handler = Probability_Handler(max_feature_number = len(self.column_names))
        self.population_handler = Population_Handler(probability_handler = self.probability_handler, max_individual_size = 10)
        self.evaluator = Evaluator(X = self.X, y = self.y, column_names = self.column_names)

    def create_population(self, population_size = 10):
        self.population_handler.create_population(population_size = population_size)
    
    def get_population(self):
        return self.population_handler.get_population()

    def natural_selection(self): # fitness -> mating_pool -> create_new_generation -> mutate -> crossover
        pass

    def fitness(self):
        population = self.population_handler.get_population()
        return self.evaluator.evaluate_population(population)

    def mating_pool(self):
        pass

    def create_new_generation(self):
        pass

    def mutate_population(self):
        self.population_handler.mutate_population()

    def crossover_population(self):
        pass
    
    def translate_genotype(self):
        pass














