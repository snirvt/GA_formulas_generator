
import numpy as np

##################################
import constants
import numbers_generator as ng
import utils
##################################

class Mutation_Handler():

    def __init__(self, probability_handler):
        self.probability_handler = probability_handler

    def mutate(self, dna_dict):
        for key in dna_dict:
            if key == constants.DNA_SIZE_STR:
                self.mutate_size(dna_dict)
                continue
            self.apply_vector_mutation(dna_dict[key], key)


    def apply_vector_mutation(self, gen, key): #todo create switch case
        mutator_function = []
        if key == constants.DNA_PARENTHESES_STR:
            mutator_function = lambda : ng.generate_n_uniform_random_integers(min_val=0 , max_val=2 , size=1)[0]
        if key == constants.DNA_WEIGHTS_STR:
            mutator_function = lambda : ng.generate_n_uniform_random_values(n=1)[0]
        if key == constants.DNA_ACTIONS_STR:
            mutator_function = lambda : ng.generate_n_uniform_random_integers(min_val=0 , max_val = constants.NUM_ACTIONS , size=1)[0]
        if key == constants.DNA_FEATURES_STR:
            mutator_function = lambda : ng.generate_n_uniform_random_integers(min_val=0, max_val = constants.MAX_NUM_OF_FEATURES, size = 1)[0]
            
        mutation_chance = self.probability_handler.get_probability_dict()[key]
        self.vector_mutation(gen, mutation_chance, mutator_function)


    def vector_mutation(self, gen, mutation_chance, mutator_function):
        for i in range(len(gen)):
            if np.random.rand() < mutation_chance:
                gen[i] = mutator_function()


    def mutate_size(self, dna_dict):
        individual_size = dna_dict[constants.DNA_SIZE_STR]
        new_size = ng.generate_gaussian_integers(mu=individual_size, sigma=1, lower_limit=1, upper_limit=constants.MAX_SIZE_INDIVIDUAL)[0]    
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
        dna_dict[constants.DNA_FEATURES_STR].insert(index , ng.generate_n_uniform_random_integers(min_val=0, max_val = constants.MAX_NUM_OF_FEATURES, size = 1)[0])
        dna_dict[constants.DNA_WEIGHTS_STR].insert(index, ng.generate_n_uniform_random_values(1)[0])
        dna_dict[constants.DNA_PARENTHESES_STR].insert(index, ng.generate_n_uniform_random_integers(min_val=0 , max_val=2 , size=1)[0])
        dna_dict[constants.DNA_ACTIONS_STR].insert(index, ng.generate_n_uniform_random_integers(min_val = 0 , max_val = constants.NUM_ACTIONS, size = 1)[0])
        dna_dict[constants.DNA_SIZE_STR] += 1






