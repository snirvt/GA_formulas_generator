
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import copy
###################################
from population_handler import Population_Handler
from probability_handler import Probability_Handler
import constants
from evaluator import Evaluator
from mating_handler import Mating_Handler
from generation_creator import Generation_Creator
from result_handler import Result_Handler
from genom_transaltor import Genom_Translator
###################################

class GA():
    def __init__(self, X, X_test, y, y_test, column_names,output_path, parlal = False):
        self.X = X
        self.X_test = X_test
        self.y = y
        self.y_test = y_test
        self.column_names = column_names
        self.output_path = output_path
        self.paralal = parlal
        self.top_global_score = float('-inf')
        self.top_global_score_test = float('-inf')

        self.top_individual = None
        self.a = None
        self.b = None

        self.top_fenotype = None
        self.no_imrovment_counter = 0
        self.prev_top_score = float('-inf')

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
        self.evaluator = Evaluator(X = self.X,X_test=self.X_test, y = self.y,y_test=self.y_test, column_names = self.column_names)
        self.mating_handler = Mating_Handler(num_offsprings_per_parent = constants.NUM_OFFSPRINGS_PER_PARENT)
        self.generation_creator = Generation_Creator()
        self.result_handler = Result_Handler()
        self.genom_translator = Genom_Translator(column_names = self.column_names)


    def plot_res(self):
        y_pred_train, y_pred_test = self.evaluator.make_prediction(self.top_individual)  

        
        plt.figure(1)
        plt.subplot(211)
        plt.plot(self.y)
        plt.plot(y_pred_train)
        plt.title('train')
        plt.subplot(212)
        plt.plot(self.y_test)
        plt.plot(y_pred_test)
        plt.title('test')
        plt.show(block=False)

        plt.figure(2)
        plt.subplot(211)
        plt.scatter(self.y, y_pred_train)
        plt.title('train')
        plt.subplot(212)
        plt.scatter(self.y_test, y_pred_test)
        plt.title('test')
        plt.show(block=False)

    def create_population(self, population_size = 10):
        self.population_handler.create_population(population_size = population_size)
    
    def get_population(self):
        return self.population_handler.get_population()

    def save_results(self, fenotype, score_test, score_train):
        df = pd.DataFrame([fenotype,'{}/{}'.format(self.a,self.b), score_test, score_train])
        df = df.T
        df.columns = ['formula','slope/bias', 'r2_score_test', 'r2_score_train']
        self.result_handler.save_to_file(path =self.output_path , sheetName = 'results',df = df, append = True, header=True)

    def restart_population(self):
        self.create_population(population_size = 1000)
        print('---------restart population---------')
        self.no_imrovment_counter = 1
        self.prev_top_score = float('-inf')

    def examine_generation(self, fitness_vec_train, fitness_vec_test,fitness_vec_train_r2, fitness_vec_test_r2):
        fittest_index_train = np.argmin(fitness_vec_train)
        fittest_index_test = np.argmin(fitness_vec_test)
        fittest_individual_train = self.get_population()[fittest_index_train]
        fittest_individual_test = self.get_population()[fittest_index_test]
        best_fenotype_train = self.genom_translator.translate_genotype(fittest_individual_train)
        best_fenotype_test = self.genom_translator.translate_genotype(fittest_individual_test)
        best_score_test = fitness_vec_test_r2[fittest_index_test]
        # best_score_train = fitness_vec_train_r2[fittest_index_train]
        best_score_train = fitness_vec_train_r2[fittest_index_test]
        print('best of generation train: r2: {}, mse: {}'.format(np.round(best_score_train,3), np.round(fitness_vec_train[fittest_index_train],3)))
        print('best of generation test: r2: {}, mse: {}'.format(np.round(best_score_test,3), np.round(fitness_vec_test[fittest_index_test],3)))

        return best_score_train, best_score_test, best_fenotype_test, fittest_individual_test

    def update_global_best(self, best_score_test, best_score_train, best_fenotype_test, fittest_individual_test):
        print('new best:')
        self.top_global_score_test = best_score_test
        self.top_global_score = best_score_train
        self.top_fenotype = copy.deepcopy(best_fenotype_test)
        self.top_individual = fittest_individual_test

        y_pred_train, _ = self.evaluator.make_prediction(self.top_individual)
        Q = np.hstack((np.reshape(y_pred_train, (-1, 1)), np.ones((len(y_pred_train), 1))))
        (a, b), _, _, _ = np.linalg.lstsq(Q, self.y, rcond=None)   

        self.a = a
        self.b = b


    def natural_selection(self, iterations=50, patience = 10): # fitness -> mating_pool -> create_new_generation -> mutate -> crossover
        for _ in range(iterations):
            if self.no_imrovment_counter % patience == 0:
                self.restart_population()
            fitness_vec_train, fitness_vec_test, fitness_vec_train_r2, fitness_vec_test_r2 = self.fitness()
            best_score_train, best_score_test, best_fenotype_test, fittest_individual_test = self.examine_generation(fitness_vec_train, fitness_vec_test,fitness_vec_train_r2, fitness_vec_test_r2)

            if self.prev_top_score < best_score_train:
                if min(self.top_global_score_test, self.top_global_score) < min(best_score_test,best_score_train):
                    self.update_global_best(best_score_test, best_score_train, best_fenotype_test, fittest_individual_test)
                    self.save_results(best_fenotype_test, best_score_test, best_score_train)
                self.prev_top_score = best_score_train
                self.no_imrovment_counter = 1

            # if True:
            #     self.update_global_best(best_score_test, best_score_train, best_fenotype_test)
            #     self.save_results(best_fenotype_test, best_score_test, best_score_train)

            # if self.prev_top_score < best_score_train:
            #     # if best_score_test > self.top_global_score_test:
            #     if min(self.top_global_score_test, self.top_global_score) < min(best_score_test,best_score_train):
            #         self.update_global_best(best_score_test, best_score_train, best_fenotype_test)
            #         self.save_results(best_fenotype_test, best_score_test, best_score_train)
            #     self.prev_top_score = best_score_train
            #     self.no_imrovment_counter = 1

            parents_front, num_parents = self.mating_pool(fitness_vec = fitness_vec_train)
            self.create_new_generation(parents_front = parents_front, num_parents = num_parents)
            self.mutate_population()
            self.no_imrovment_counter += 1
        print('best result: {}, fenotype: {}'.format(self.top_global_score, self.top_fenotype))
            
    def fitness(self):
        population = self.get_population()
        if self.paralal:
            return self.evaluator.evaluate_population_paralal(population)
        return self.evaluator.evaluate_population(population)

    def mating_pool(self, fitness_vec):
        # TODO paralal
        population = self.get_population()
        parents_front, num_parents = self.mating_handler.choose_parents(population, fitness_vec)
        return parents_front, num_parents
        
    def create_new_generation(self, parents_front, num_parents):
        # TODO paralal
        new_generation = self.generation_creator.replicate_parents(parents_front = parents_front, num_parents = num_parents)
        self.population_handler.set_population(new_generation = new_generation)

    def mutate_population(self):
        if self.paralal:
            self.population_handler.mutate_population_paralal()
            return
        self.population_handler.mutate_population()
    
    def crossover_population(self):
        pass
        












