
import random
###################################
import numbers_generator as ng
import constants
###################################

class Individual():
    def __init__(self, num_features, max_individual_size, num_actions = 5):
        self.num_features = num_features
        self.max_individual_size = max_individual_size
        self.num_actions = num_actions
        
    def be_born(self):
        self.individual_size = ng.generate_gaussian_integers(mu=3, sigma=1, lower_limit=1, upper_limit=5)[0]
        self.feature_indices = ng.generate_n_uniform_random_integers(min_val=0, max_val = self.num_features, size = self.individual_size)
        self.weights = ng.generate_n_uniform_random_values(self.individual_size)
        self.parentheses_binary_vec = ng.generate_n_binary_numbers(size=self.individual_size)
        self.actions = ng.generate_n_uniform_random_integers(min_val=0 , max_val = self.num_actions , size = self.individual_size)
        self.wl_scalars = ng.generate_gaussian(mu=1, sigma = 0.5, size = self.individual_size)
        return self.create_dna_dictionary()

    def create_dna_dictionary(self):
        self.dna_dict = {}
        self.dna_dict[constants.DNA_SIZE_STR] = self.individual_size
        self.dna_dict[constants.DNA_WEIGHTS_STR] = self.weights
        self.dna_dict[constants.DNA_FEATURES_STR] = self.feature_indices
        self.dna_dict[constants.DNA_PARENTHESES_STR] = self.parentheses_binary_vec
        self.dna_dict[constants.DNA_ACTIONS_STR] = self.actions
        self.dna_dict[constants.DNA_WL_SCALAR] = self.wl_scalars

        return self.dna_dict
    
    @staticmethod
    def merge_dna_data(dna_dict):
        tree_values = dna_dict[constants.DNA_WEIGHTS_STR]
        feature_values = dna_dict[constants.DNA_FEATURES_STR]
        parentheses_values = dna_dict[constants.DNA_PARENTHESES_STR]
        actions_values = dna_dict[constants.DNA_ACTIONS_STR]
        wl_scalars = dna_dict[constants.DNA_WL_SCALAR]
        return list(zip(tree_values, feature_values, parentheses_values, actions_values, wl_scalars))
    
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
    def get_all_merged_values(merged):
        return merged[1], merged[2] ,merged[3], merged[4]

        

    

