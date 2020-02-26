
import numpy as np
from multiprocessing import Pool, cpu_count
import math 
from numpy import log, sin, cos, exp
# from sklearn.metrics import r2_score

import constants
from individual import Individual
from tree import Tree
import utils
from genom_transaltor import Genom_Translator

class Evaluator():

    def __init__(self, X, y, column_names):
        self.X = X
        self.y = y
        self.column_names = column_names
        self.preprocess_x()
        self.genom_transaltor = Genom_Translator(self.column_names)

    def preprocess_x(self):
        self.X = self.X.astype(complex)

    def evaluate_population_paralal(self, population):
        fitness_array = np.empty([len(population)])
        p = Pool(constants.NUM_POOL)
        paralal_input = zip(range(len(population)),population)
        paralal_result = p.map(self.evaluate_individual_paralal, paralal_input)
        p.close()
        p.join()
        for i, fitness in paralal_result:
            fitness_array[i] = fitness
        return fitness_array

    def evaluate_individual_paralal(self, paralal_input):
        i, individual = paralal_input
        return i, self.evaluate_individual(individual)

    def evaluate_population(self, population):
        fitness_array = np.empty([len(population)])
        for i, individual in enumerate(population):
            fitness_array[i] = self.evaluate_individual(individual)
        return fitness_array

    def evaluate_individual(self, individual):
        # self.transalete_genotype(individual)
        expression_str = self.genom_transaltor.get_raw_fenotype(individual)
        X = self.X ## for short string on eval
        valid_math_expression = self.build_math_evaluation(expression_str)
        # try:
        y_pred = eval(valid_math_expression).real
        y_pred = np.nan_to_num(y_pred) # replace nan values with 0
        return utils.r2_score(self.y, y_pred)
        # return r2_score(self.y, y_pred)
        # except: ## TODO change system division so division by 0 is 0
        #     return -float('inf')
          
    def build_math_evaluation(self, expression):
        split_expression = expression.split('_')
        math_str = ''
        for split in split_expression:
            if split.isnumeric():
                math_str += self.get_string_data_column(int(split))
            else:
                math_str += split
        return math_str

    def get_string_data_column(self, column_number):
        return 'X[:,{}]'.format(column_number)

def absln(x):
    return log(abs(x))