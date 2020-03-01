
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

    def __init__(self, X, X_test, y, y_test, column_names):
        self.X = X
        self.X_test = X_test
        self.y = y
        self.y_test = y_test
        self.column_names = column_names
        self.preprocess_x()
        self.genom_transaltor = Genom_Translator(self.column_names)

    def preprocess_x(self):
        self.X = self.X.astype(complex)

    def evaluate_population_paralal(self, population):
        fitness_array_train = np.empty([len(population)])
        fitness_array_test = np.empty([len(population)])
        p = Pool(constants.NUM_POOL)
        paralal_input = zip(range(len(population)),population)
        paralal_result = p.map(self.evaluate_individual_paralal, paralal_input)
        p.close()
        p.join()
        for i, fitness_train, fitness_test in paralal_result:
            fitness_array_train[i] = fitness_train
            fitness_array_test[i] = fitness_test
        return fitness_array_train, fitness_array_test


    def evaluate_individual_paralal(self, paralal_input):
        i, individual = paralal_input
        train_res, test_res = self.evaluate_individual(individual)
        return i, train_res, test_res

    def evaluate_population(self, population):
        fitness_array_train = np.empty([len(population)])
        fitness_array_test = np.empty([len(population)])
        for i, individual in enumerate(population):
            fitness_array_train[i], fitness_array_test[i] = self.evaluate_individual(individual)
        return fitness_array_train, fitness_array_test

    def evaluate_individual(self, individual): 
        expression_str = self.genom_transaltor.get_raw_fenotype(individual)
        valid_math_expression = self.build_math_evaluation(expression_str)

        y_pred_train = self.fixed_eval(self.X, valid_math_expression) 
        y_pred_test = self.fixed_eval(self.X_test, valid_math_expression)

        return utils.r2_score(self.y, y_pred_train), utils.r2_score(self.y_test, y_pred_test)

    def fixed_eval(self,X, valid_math_expression): ## X is for eval
        y_pred = eval(valid_math_expression).real
        return np.nan_to_num(y_pred)

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