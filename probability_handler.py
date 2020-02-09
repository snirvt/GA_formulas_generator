

class Probability_Handler():

    def __init__(self):
        self.prob_dict = {}
        self.prob_dict['size'] = 0.2
        self.prob_dict['feature_indices'] = 0.2
        self.prob_dict['weights'] = 0.2
        self.prob_dict['parentheses_binary_vec'] = 0.2
        self.prob_dict['actions'] = 0.2

    def set_ptobability(self, prob_dict):
        self.prob_dict = prob_dict

    def get_probability_dict(self):
        return self.prob_dict





