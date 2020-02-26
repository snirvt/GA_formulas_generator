
import random
###################################
import numbers_generator as ng
import constants
import features_generator as fg
from values_handler import Values_Handler
###################################

class Individual():
    def __init__(self, num_features, max_individual_size, values_handler):
        self.num_features = num_features
        self.max_individual_size = max_individual_size
        self.vh = values_handler

    def be_born(self):
        self.individual_size =  self.vh.create_scalar_values(key = constants.DNA_SIZE_STR)
        self.feature_indices = self.vh.create_vector_values(key = constants.DNA_FEATURES_STR, size = self.individual_size)
        self.weights = self.vh.create_vector_values(key = constants.DNA_WEIGHTS_STR, size = self.individual_size)
        self.parentheses_binary_vec = self.vh.create_vector_values(key = constants.DNA_PARENTHESES_STR, size = self.individual_size)
        self.actions = self.vh.create_vector_values(key = constants.DNA_ACTIONS_STR, size = self.individual_size)
        self.wl_scalars = self.vh.create_vector_values(key = constants.DNA_WL_SCALAR, size = self.individual_size)
        self.wl_powers = self.vh.create_vector_values(key = constants.DNA_WL_POWER, size = self.individual_size)
        self.parentheses_bias = self.vh.create_vector_values(key = constants.DNA_PARENTHESES_BIAS, size = self.individual_size)
        self.wl_activation = self.vh.create_vector_values(key = constants.DNA_WL_ACTIVATION, size = self.individual_size)
        self.parentheses_activation = self.vh.create_vector_values(key = constants.DNA_PARENTHESES_ACTIVATION, size = self.individual_size)

        return self.create_dna_dictionary()

    def create_dna_dictionary(self):
        self.dna_dict = {}
        self.dna_dict[constants.DNA_SIZE_STR] = self.individual_size
        self.dna_dict[constants.DNA_WEIGHTS_STR] = self.weights
        self.dna_dict[constants.DNA_FEATURES_STR] = self.feature_indices
        self.dna_dict[constants.DNA_PARENTHESES_STR] = self.parentheses_binary_vec
        self.dna_dict[constants.DNA_ACTIONS_STR] = self.actions
        self.dna_dict[constants.DNA_WL_SCALAR] = self.wl_scalars
        self.dna_dict[constants.DNA_WL_POWER] = self.wl_powers
        self.dna_dict[constants.DNA_PARENTHESES_BIAS] = self.parentheses_bias
        self.dna_dict[constants.DNA_WL_ACTIVATION] = self.wl_activation
        self.dna_dict[constants.DNA_PARENTHESES_ACTIVATION] = self.parentheses_activation
        return self.dna_dict
    
    @staticmethod
    def merge_dna_data(dna_dict):
        tree_values = dna_dict[constants.DNA_WEIGHTS_STR]
        feature_values = dna_dict[constants.DNA_FEATURES_STR]
        parentheses_values = dna_dict[constants.DNA_PARENTHESES_STR]
        actions_values = dna_dict[constants.DNA_ACTIONS_STR]
        wl_scalars = dna_dict[constants.DNA_WL_SCALAR]
        wl_powers = dna_dict[constants.DNA_WL_POWER]
        parentheses_bias = dna_dict[constants.DNA_PARENTHESES_BIAS]
        wl_activation = dna_dict[constants.DNA_WL_ACTIVATION]
        wl_parentheses = dna_dict[constants.DNA_PARENTHESES_ACTIVATION]

        return list(zip(tree_values, feature_values, parentheses_values, actions_values, wl_scalars, wl_powers, parentheses_bias, wl_activation, wl_parentheses))
    
    @staticmethod
    def get_merged_feature_values(merged):
        return merged[1]

    @staticmethod
    def get_merged_parentheses_values(merged):
        return merged[2]

    @staticmethod
    def get_merged_actions_values(merged):
        return merged[3]
    
    @staticmethod
    def get_merged_wl_scalars(merged):
        return merged[4]

    @staticmethod
    def get_merged_wl_powers(merged):
        return merged[5]

    @staticmethod
    def get_merged_parentheses_bias(merged):
        return merged[6]

    @staticmethod
    def get_all_merged_values(merged):
        return merged[1], merged[2] ,merged[3], merged[4], merged[5], merged[6], merged[7], merged[8]

        

    

