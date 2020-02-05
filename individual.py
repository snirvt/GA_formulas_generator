
import random

###################################
# import numbers_generator as ng
from numbers_generator import Numbers_Generator as ng

###################################

class Individual():
    def __init__(self, num_features, max_individual_size, probability_handler, num_actions = 6):
        self.dna_list = []
        self.probability_handler = probability_handler
        self.individual_size = ng.generate_gaussian_integers(mu=3, sigma=1, lower_limit=1, upper_limit=5)[0]
        
        self.feature_indices = ng.generate_n_uniform_random_integers(min_val=0, max_val = num_features, size = max_individual_size)
        self.tree_values = ng.generate_n_unique_random_integers(self.individual_size)
        self.parentheses_binary_vec = ng.generate_n_uniform_random_integers(min_val=0 , max_val=2 , size=self.individual_size)
        self.action_vector = ng.generate_n_uniform_random_integers(min_val=0 , max_val = num_actions , size = self.individual_size)
        self.insert_to_dna_list()

    def insert_to_dna_list(self):
        self.dna_list.append(self.feature_indices)
        self.dna_list.append(self.tree_values)
        self.dna_list.append(self.parentheses_binary_vec)
        self.dna_list.append(self.action_vector)

    def mutate(self):
        self.mutate_size()
        return self.probability_handler.get_probability_list()[0]
        
    def mutate_size(self):
        new_size = ng.generate_gaussian_integers(mu=self.individual_size, sigma=1, lower_limit=1, upper_limit=10)[0]    
        if new_size == self.individual_size:
            return
        if new_size < self.individual_size:
            self.remove_genotype_parts(new_size)
            return

    def remove_genotype_parts(self, new_size):
        while self.individual_size > new_size and self.individual_size > 0:
            index_to_remove = ng.generate_n_uniform_random_integers(min_val = 0 , max_val = self.individual_size , size = 1 )[0]
            for i in range(len(self.dna_list)):
                del self.dna_list[i][index_to_remove]
            self.individual_size -= 1

        

