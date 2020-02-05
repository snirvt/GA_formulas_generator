

class Probability_Handler():

    def __init__(self):
        self.prob_list = []
        self.prob_list.append(0.1) # set individual size prob
        self.prob_list.append(0.1) # set feature indices prob
        self.prob_list.append(0.1) # set tree values prob
        self.prob_list.append(0.1) # set parentheses binary vec prob
        self.prob_list.append(0.1) # set action_vector prob
        self.prob_list.append(0.1) # set crossover prob

    def set_ptobability(self,prob_list):
        self.prob_list = prob_list

    def get_probability_list(self):
        return self.prob_list

    # set_individual_size_prob
    # set_feature_indices_prob
    # set_tree_values_prob
    # set_parentheses_binary_vec_prob
    # set_action_vector_prob
    # set_crossover_prob

    #     self.individual_size = ng.generate_gaussian_integers(mu=3, sigma=1, lower_limit=1, upper_limit=5)[0]
    #     self.feature_indices = ng.generate_n_uniform_random_integers(min_val=0, max_val = num_features, size = max_individual_size)
    #     self.tree_values = ng.generate_n_unique_random_integers(self.individual_size)
    #     self.parentheses_binary_vec = ng.generate_n_uniform_random_integers(min_val=0 , max_val=2 , size=self.individual_size)
    #     self.action_vector = ng.generate_n_uniform_random_integers(min_val=0 , max_val = num_actions , size = self.individual_size)
    #     self.probability_handler = probability_handler




