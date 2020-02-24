
import numpy as np
import pandas as pd
import copy
###################################
from population_handler import Population_Handler
from probability_handler import Probability_Handler
import constants
from evaluator import Evaluator
from data_parser import Data_Parser
from mating_handler import Mating_Handler
from generation_creator import Generation_Creator
from result_handler import Result_Handler
from genom_transaltor import Genom_Translator
###################################

class GA():
    def __init__(self, X, y, column_names, parlal = False):
        self.X = X
        self.y = y
        self.column_names = column_names
        self.paralal = parlal
        self.top_score = float('-inf')
        # self.top_individual = None
        self.top_fenotype = None

        self.probability_handler = None
        self.population_handler = None
        self.mating_handler = None
        self.generation_creator = None
        self.result_handler = None
        self.genom_translator = None
        
        self.setup()

    def setup(self):
        self.probability_handler = Probability_Handler(max_feature_number = len(self.column_names))
        self.population_handler = Population_Handler(probability_handler = self.probability_handler, max_individual_size = 10)
        self.evaluator = Evaluator(X = self.X, y = self.y, column_names = self.column_names)
        self.mating_handler = Mating_Handler(num_offsprings_per_parent = constants.NUM_OFFSPRINGS_PER_PARENT)
        self.generation_creator = Generation_Creator()
        self.result_handler = Result_Handler()
        self.genom_translator = Genom_Translator(column_names = self.column_names)

    def create_population(self, population_size = 10):
        self.population_handler.create_population(population_size = population_size)
    
    def get_population(self):
        return self.population_handler.get_population()

    def save_results(self,fenotype, score):
        if score > self.top_score:
            print('new best:')
            self.top_score = score
            self.top_fenotype = copy.deepcopy(fenotype)
            df = pd.DataFrame([fenotype, score])
            df = df.T
            df.columns = ['formula', 'r2_score']
            self.result_handler.save_to_file(path = 'results/results.xlsx', sheetName = 'results',df = df.T, append = True, header=True)
    
    def natural_selection(self): # fitness -> mating_pool -> create_new_generation -> mutate -> crossover
        self.create_population(population_size = 1000)
        for _ in range(100):
            fitness_vec = self.fitness()
            fittest_individual = self.get_population()[np.argmax(fitness_vec)]
            best_generation_fenotype = self.genom_translator.translate_genotype(fittest_individual)
            self.save_results(best_generation_fenotype, fitness_vec.max())
            print('best of generation: {}, fenotype: {}'.format(np.round(np.max(fitness_vec),3), best_generation_fenotype))
            parents_front, num_parents = self.mating_pool(fitness_vec = fitness_vec)
            self.create_new_generation(parents_front = parents_front, num_parents = num_parents)
            self.mutate_population()
            
    def fitness(self):
        population = self.get_population()
        if self.paralal:
            return self.evaluator.evaluate_population_paralal(population)
        return self.evaluator.evaluate_population(population)

    def mating_pool(self, fitness_vec):
        population = self.get_population()
        # if self.paralal:
        #     parents_front, num_parents = self.mating_handler.choose_parents_paralal(population, fitness_vec)
        # else:
        parents_front, num_parents = self.mating_handler.choose_parents(population, fitness_vec)
        return parents_front, num_parents
        
    def create_new_generation(self, parents_front, num_parents):
        # if self.paralal:
        #     new_generation = self.generation_creator.replicate_parents_paralal(parents_front = parents_front, num_parents = num_parents)
        # else:
        new_generation = self.generation_creator.replicate_parents(parents_front = parents_front, num_parents = num_parents)
        self.population_handler.set_population(new_generation = new_generation)

    def mutate_population(self):
        if self.paralal:
            self.population_handler.mutate_population_paralal()
            return
        self.population_handler.mutate_population()
    
    def crossover_population(self):
        pass
        












