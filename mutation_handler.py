
import numpy as np

##################################
import constants
import numbers_generator as ng
import utils
##################################

class Mutation_Handler():
    def __init__(self, probability_handler, values_handler):
        self.probability_handler = probability_handler
        self.vh = values_handler

    def mutate_paralal(self, dna_dict):
        self.mutate(dna_dict)
        return dna_dict

    def mutate(self, dna_dict):
        for key in dna_dict:
            mutation_chance = self.probability_handler.get_probability_dict()[key]
            if key == constants.DNA_SIZE_STR:
                self.mutate_size(dna_dict, mutation_chance)
                continue
            self.vector_mutation(dna_dict, key, mutation_chance)

    def vector_mutation(self, dna_dict, key, mutation_chance):
        gen = dna_dict[key]
        for i in range(len(gen)):
            if np.random.rand() < mutation_chance:
                gen[i] = self.vh.create_scalar_values(key = key, previous_value = gen[i])

    def mutate_size(self, dna_dict, mutation_chance):
        if np.random.rand() > mutation_chance:
            return
        individual_size = dna_dict[constants.DNA_SIZE_STR]
        new_size = self.vh.create_scalar_values(key = constants.DNA_SIZE_STR, previous_value = individual_size)
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
        for key in dna_dict:
            if key == constants.DNA_SIZE_STR:
                continue
            dna_dict[key].insert(index,  self.vh.create_scalar_values(key = key))
        dna_dict[constants.DNA_SIZE_STR] += 1




