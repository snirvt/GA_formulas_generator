
import random

###################################
import numbers_generator as ng
# import mutatation_handler as mh
###################################

class Individual():
    def __init__(self, num_features, max_individual_size, num_actions = 6):
        self.num_features = num_features
        self.max_individual_size = max_individual_size
        self.num_actions = num_actions
        self.be_born()
        
    def be_born(self):
        self.individual_size = ng.generate_gaussian_integers(mu=3, sigma=1, lower_limit=1, upper_limit=5)[0]
        self.feature_indices = ng.generate_n_uniform_random_integers(min_val=0, max_val = self.num_features, size = self.individual_size)
        self.weights = ng.generate_n_uniform_random_values(self.individual_size)
        self.parentheses_binary_vec = ng.generate_n_uniform_random_integers(min_val=0 , max_val=2 , size=self.individual_size)
        self.actions = ng.generate_n_uniform_random_integers(min_val=0 , max_val = self.num_actions , size = self.individual_size)
        return self.creat_dna_dictionary()

    def creat_dna_dictionary(self):
        self.dna_dict = {}
        self.dna_dict['size'] = self.individual_size
        self.dna_dict['weights'] = self.weights
        self.dna_dict['feature_indices'] = self.feature_indices
        self.dna_dict['parentheses_binary_vec'] = self.parentheses_binary_vec
        self.dna_dict['actions'] = self.actions
        return self.dna_dict

        

    

