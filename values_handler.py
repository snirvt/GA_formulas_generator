

import numbers_generator as ng
import constants
import numpy as np
class Values_Handler():

    def __init__(self, probability_handler):
        self.probability_handler = probability_handler
        self.dict = {}
        self.setup_functions()
        self.setup_inputs()

    def setup_inputs(self):
        self.dict[constants.DNA_ACTIONS_STR + 'input'] = [0, constants.NUM_ACTIONS]
        self.dict[constants.DNA_FEATURES_STR + 'input'] = [0, self.probability_handler.max_feature_number]
        self.dict[constants.DNA_WEIGHTS_STR + 'input']  = []
        self.dict[constants.DNA_PARENTHESES_STR + 'input'] = [0, 2]
        self.dict[constants.DNA_WL_ACTIVATION + 'input'] = self.create_activation_input()
        self.dict[constants.DNA_PARENTHESES_ACTIVATION + 'input'] = self.create_activation_input()

        ## normaly distributed
        self.dict[constants.DNA_SIZE_STR + 'input'] = [3, 1, constants.MIN_SIZE_INDIVIDUAL, constants.MAX_SIZE_INDIVIDUAL]
        self.dict[constants.DNA_WL_SCALAR + 'input'] = [1, 0.5]
        self.dict[constants.DNA_WL_POWER + 'input'] = [1, 0.5]
        self.dict[constants.DNA_PARENTHESES_BIAS + 'input'] = [0, 0.5]
        self.dict[constants.DNA_WL_BIAS + 'input'] = [0, 0.5]
        self.dict[constants.DNA_PARENTHESES_POWER + 'input'] = [1, 0.5]

        self.dict['normaly distributed'] = []
        self.dict['normaly distributed'].append(constants.DNA_SIZE_STR)
        self.dict['normaly distributed'].append(constants.DNA_WL_SCALAR)
        self.dict['normaly distributed'].append(constants.DNA_WL_POWER)
        self.dict['normaly distributed'].append(constants.DNA_PARENTHESES_BIAS)
        self.dict['normaly distributed'].append(constants.DNA_WL_BIAS)
        self.dict['normaly distributed'].append(constants.DNA_PARENTHESES_POWER)

    def create_activation_input(self, id_chance = 0.5):
        num_activation = constants.NUM_WL_ACTIVATION
        return [list(np.arange(num_activation))] + [[id_chance] + [id_chance/(num_activation-1)]*(num_activation-1)]

    def setup_functions(self):
        self.dict[constants.DNA_SIZE_STR] = lambda list_input: ng.generate_gaussian_integers(list_input[0], list_input[1], list_input[2], list_input[3], list_input[4])
        self.dict[constants.DNA_ACTIONS_STR] = lambda list_input: ng.generate_n_uniform_random_integers(list_input[0], list_input[1], list_input[2])
        self.dict[constants.DNA_FEATURES_STR] = lambda list_input: ng.generate_n_uniform_random_integers(list_input[0], list_input[1], list_input[2])
        self.dict[constants.DNA_WEIGHTS_STR] = lambda list_input: ng.generate_n_uniform_random_values(list_input[0])
        self.dict[constants.DNA_PARENTHESES_STR] = lambda list_input: ng.generate_n_uniform_random_integers(list_input[0], list_input[1], list_input[2])
        self.dict[constants.DNA_WL_SCALAR] = lambda list_input: ng.generate_gaussian(list_input[0], list_input[1], list_input[2])
        self.dict[constants.DNA_WL_POWER] = lambda list_input: ng.generate_gaussian(list_input[0], list_input[1], list_input[2])
        self.dict[constants.DNA_PARENTHESES_BIAS] = lambda list_input: ng.generate_gaussian(list_input[0], list_input[1], list_input[2])
        self.dict[constants.DNA_WL_ACTIVATION] = lambda list_input: ng.generate_non_uniform_integers(list_input[0], list_input[1], list_input[2])
        self.dict[constants.DNA_PARENTHESES_ACTIVATION] = lambda list_input: ng.generate_non_uniform_integers(list_input[0], list_input[1], list_input[2])
        self.dict[constants.DNA_WL_BIAS] = lambda list_input: ng.generate_gaussian(list_input[0], list_input[1], list_input[2])
        self.dict[constants.DNA_PARENTHESES_POWER] = lambda list_input: ng.generate_gaussian(list_input[0], list_input[1], list_input[2])

    def get_dict(self):
        return self.dict

    def create_vector_values(self, key, size):
        list_input = self.dict[key + 'input'] + [size]
        return self.dict[key](list_input)

    def create_scalar_values(self, key, previous_value = None):
        list_input = self.dict[key + 'input'] + [1]
        if key in self.dict['normaly distributed'] and previous_value != None:
            if np.random.rand() < self.probability_handler.independent_update_chance:
                list_input[0] = previous_value
            
        return self.dict[key](list_input)[0]
