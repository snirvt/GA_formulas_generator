
import random
###################################
import numbers_generator as ng
import constants
import features_generator as fg
###################################

class Individual():
    def __init__(self, num_features, max_individual_size, num_actions = 5):
        self.num_features = num_features
        self.max_individual_size = max_individual_size
        self.num_actions = num_actions
        
    def be_born(self):
        self.individual_size = fg.create_size_feature()
        self.feature_indices = fg.create_feature_index_vector(self.num_features, self.individual_size)
        self.weights = fg.create_weight_vector(self.individual_size)
        self.parentheses_binary_vec = fg.create_parentheses_vector(size = self.individual_size )
        self.actions = fg.create_action_vector(size = self.individual_size)
        self.wl_scalars = fg.create_wl_scalars_vector(mu=1, sigma = 0.5, size = self.individual_size)
        self.wl_powers = fg.create_wl_scalars_vector(mu=1, sigma = 0.5, size = self.individual_size)
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
        return self.dna_dict
    
    @staticmethod
    def merge_dna_data(dna_dict):
        tree_values = dna_dict[constants.DNA_WEIGHTS_STR]
        feature_values = dna_dict[constants.DNA_FEATURES_STR]
        parentheses_values = dna_dict[constants.DNA_PARENTHESES_STR]
        actions_values = dna_dict[constants.DNA_ACTIONS_STR]
        wl_scalars = dna_dict[constants.DNA_WL_SCALAR]
        wl_powers = dna_dict[constants.DNA_WL_POWER]
        return list(zip(tree_values, feature_values, parentheses_values, actions_values, wl_scalars, wl_powers))
    
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
    def get_all_merged_values(merged):
        return merged[1], merged[2] ,merged[3], merged[4], merged[5]

        

    

