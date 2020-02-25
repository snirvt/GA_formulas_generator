
import numpy as np

##################################
import constants
import numbers_generator as ng
import utils
import features_generator as fg
##################################

class Mutation_Handler():

    def __init__(self, probability_handler):
        self.probability_handler = probability_handler

    def mutate_paralal(self, dna_dict):
        self.mutate(dna_dict)
        return dna_dict

    def mutate(self, dna_dict):
        for key in dna_dict:
            if key == constants.DNA_SIZE_STR:
                mutation_chance = self.probability_handler.get_probability_dict()[key]
                if np.random.rand() < mutation_chance:
                    self.mutate_size(dna_dict)
                continue
            self.apply_vector_mutation(dna_dict[key], key)

    def apply_vector_mutation(self, gen, key): #todo create switch case
        mutator_function = []
        if key == constants.DNA_PARENTHESES_STR:
            mutator_function = lambda : fg.sample_parentheses()
        if key == constants.DNA_WEIGHTS_STR:
            mutator_function = lambda : fg.sample_weight()
        if key == constants.DNA_ACTIONS_STR:
            mutator_function = lambda : fg.sample_action()
        if key == constants.DNA_FEATURES_STR:
            mutator_function = lambda : fg.sample_feature_index(num_features=self.probability_handler.max_feature_number)
        if key == constants.DNA_WL_SCALAR:
            mutator_function = lambda : fg.sample_wl_scalars(mu = 1, sigma = 0.5)
        if key == constants.DNA_WL_POWER:
            mutator_function = lambda : fg.sample_wl_powers(mu = 1, sigma = 0.5)
    

        mutation_chance = self.probability_handler.get_probability_dict()[key]
        self.vector_mutation(gen, mutation_chance, mutator_function)


    def vector_mutation(self, gen, mutation_chance, mutator_function):
        for i in range(len(gen)):
            if np.random.rand() < mutation_chance:
                gen[i] = mutator_function()

    def mutate_size(self, dna_dict):
        individual_size = dna_dict[constants.DNA_SIZE_STR]
        new_size = fg.sample_size(mu = individual_size)
        if new_size == individual_size:
            return
        if new_size < individual_size:
            self.remove_genotype_parts(new_size, dna_dict)
        if new_size > individual_size:
            self.add_genotype_parts(new_size, dna_dict)
            
    def remove_genotype_parts(self, new_size, dna_dict):
        while dna_dict[constants.DNA_SIZE_STR] > new_size and dna_dict[constants.DNA_SIZE_STR] > 1:
            index_to_remove = ng.generate_n_uniform_random_integers(min_val = 0 , max_val = dna_dict[constants.DNA_SIZE_STR] , size = 1 )[0]
            
            for key in dna_dict:
                if key == constants.DNA_SIZE_STR:
                    continue
                del dna_dict[key][index_to_remove]
            dna_dict[constants.DNA_SIZE_STR] -= 1
    
    def add_genotype_parts(self, new_size, dna_dict):
        while dna_dict[constants.DNA_SIZE_STR] < new_size:
            index_to_add = ng.generate_n_uniform_random_integers(min_val = 0 , max_val = dna_dict[constants.DNA_SIZE_STR] , size = 1 )[0]
            self.insert_new_values_to_dna(index_to_add, dna_dict)

    def insert_new_values_to_dna(self, index, dna_dict):
        dna_dict[constants.DNA_FEATURES_STR].insert(index , fg.sample_feature_index(num_features = self.probability_handler.max_feature_number))
        dna_dict[constants.DNA_WEIGHTS_STR].insert(index, fg.sample_weight())
        dna_dict[constants.DNA_PARENTHESES_STR].insert(index, ng.generate_n_binary_numbers(size=1)[0])
        dna_dict[constants.DNA_ACTIONS_STR].insert(index, fg.sample_action())
        dna_dict[constants.DNA_WL_SCALAR].insert(index, fg.sample_wl_scalars(mu=1, sigma=0.5))
        dna_dict[constants.DNA_WL_POWER].insert(index, fg.sample_wl_powers(mu=1, sigma=0.5))

        dna_dict[constants.DNA_SIZE_STR] += 1




