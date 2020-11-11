
import numpy as np
from multiprocessing import Pool, cpu_count
import math 
from numpy import log, sin, cos, exp
from sklearn.metrics import mean_squared_error as mse
from sklearn.metrics import r2_score

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
        self.X_test = self.X_test.astype(complex)

    def evaluate_population_paralal(self, population):
        fitness_array_train_mse = np.empty([len(population)])
        fitness_array_test_mse = np.empty([len(population)])
        fitness_array_train_r2 = np.empty([len(population)])
        fitness_array_test_r2 = np.empty([len(population)])

        p = Pool(constants.NUM_POOL)
        paralal_input = zip(range(len(population)),population)
        paralal_result = p.map(self.evaluate_individual_paralal, paralal_input)
        p.close()
        p.join()
        for i, fitness_train_mse, fitness_test_mse, fitness_train_r2, fitness_test_r2 in paralal_result:
            fitness_array_train_mse[i] = fitness_train_mse
            fitness_array_test_mse[i] = fitness_test_mse
            fitness_array_train_r2[i] = fitness_train_r2
            fitness_array_test_r2[i] = fitness_test_r2
        return fitness_array_train_mse, fitness_array_test_mse, fitness_array_train_r2, fitness_array_test_r2


    def evaluate_individual_paralal(self, paralal_input):
        i, individual = paralal_input
        train_res_mse, test_res_mse, train_res_r2, test_res_r2 = self.evaluate_individual(individual)
        return i, train_res_mse, test_res_mse, train_res_r2, test_res_r2

    def evaluate_population(self, population):
        fitness_array_train = np.empty([len(population)])
        fitness_array_test = np.empty([len(population)])
        fitness_array_train_r2 = np.empty([len(population)])
        fitness_array_test_r2 = np.empty([len(population)])

        for i, individual in enumerate(population):
            fitness_array_train[i], fitness_array_test[i],fitness_array_train_r2[i], fitness_array_test_r2[i] = self.evaluate_individual(individual)
        return fitness_array_train, fitness_array_test, fitness_array_train_r2, fitness_array_test_r2

# math.isnan(self.evaluate_individual(individual))
    def evaluate_individual(self, individual): 
        y_pred_train, y_pred_test = self.make_prediction(individual)
        return mse(self.y, y_pred_train), mse(self.y_test, y_pred_test), r2_score(self.y, y_pred_train), r2_score(self.y_test, y_pred_test) 
    

    def make_prediction(self, individual): 
        expression_str = self.genom_transaltor.get_raw_fenotype(individual)
        valid_math_expression = self.build_math_evaluation(expression_str)

        y_pred_train = self.fixed_eval(self.X, valid_math_expression) 
        y_pred_test = self.fixed_eval(self.X_test, valid_math_expression)

        Q = np.hstack((np.reshape(y_pred_train, (-1, 1)), np.ones((len(y_pred_train), 1))))
        (a, b), _, _, _ = np.linalg.lstsq(Q, self.y, rcond=None)   
        y_pred_train = y_pred_train*a + b
        y_pred_test = y_pred_test*a + b


        # return utils.r2_score(self.y, y_pred_train), utils.r2_score(self.y_test, y_pred_test)
        return y_pred_train, y_pred_test


    
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
    return log(abs(x)).astype(complex)