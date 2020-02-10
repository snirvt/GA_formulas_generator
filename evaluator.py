
import numpy as np

import constants
from individual import Individual
from tree import Tree

class Evaluator():

    def __init__(self, X, y, column_names):
        self.X = X
        self.y = y
        self.column_names = column_names

    def evaluate_population(self, population):
        fitness_array = np.empty([len(population)])
        for i, individual in enumerate(population):
            fitness_array[i] = self.evaluate_individual(individual)
        return fitness_array

    def evaluate_individual(self, individual):
        tree = self.create_individual_binary_tree(individual)
        return 0

    def create_individual_binary_tree(self, individual):
        merged_values = Individual.merge_dna_data(individual)
        tree = Tree()
        for value in merged_values:
            tree.insert(value)
        return tree












