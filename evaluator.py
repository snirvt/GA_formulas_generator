
import numpy as np

import constants
from individual import Individual
from tree import Tree
import utils

class Evaluator():

    def __init__(self, X, y, column_names):
        self.X = X
        self.y = y
        self.column_names = column_names
        self.tree = Tree()
        self.expression_str = ''

    def evaluate_population(self, population):
        fitness_array = np.empty([len(population)])
        for i, individual in enumerate(population):
            fitness_array[i] = self.evaluate_individual(individual)
        return fitness_array

    def evaluate_individual(self, individual):
        self.build_individual_binary_tree(individual)
        self.expression_str = ''
        self.extract_tree_expression(self.tree.node, index_mark = '_')
        self.fix_expression()
        X = self.X ## for short string on eval
        return utils.r2_score(self.y, eval(self.build_math_evaluation(self.expression_str)))

    def build_individual_binary_tree(self, individual):
        merged_values = Individual.merge_dna_data(individual)
        self.tree.delete_tree()
        for value in merged_values:
            self.tree.insert(value)

    def extract_tree_expression(self, node, index_mark = '_'):
        if node == None or node.data == None:
            return self.expression_str
        feature, parentheses, action = Individual.get_all_merged_values(node.data)
        
        if parentheses == 1:
            self.expression_str += '('

        self.expression_str += '{}{}{}'.format(index_mark, feature, index_mark)
        self.expression_str += utils.get_action(action)

        self.expression_str = self.extract_tree_expression(node.left, index_mark)
        self.expression_str = self.extract_tree_expression(node.right, index_mark)

        if parentheses == 1:
            self.expression_str = self.expression_str[:-1] + ')' + self.expression_str[-1] ## put closing parentesis before action
        return self.expression_str

    def fix_expression(self):
        self.expression_str = self.expression_str[:-1] ## remove the last action

    
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






