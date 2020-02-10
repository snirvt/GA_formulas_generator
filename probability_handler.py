
import constants


class Probability_Handler():

    def __init__(self):
        self.prob_dict = {}
        self.prob_dict[constants.DNA_SIZE_STR] = 0.2
        self.prob_dict[constants.DNA_FEATURES_STR] = 0.2
        self.prob_dict[constants.DNA_WEIGHTS_STR] = 0.2
        self.prob_dict[constants.DNA_PARENTHESES_STR] = 0.2
        self.prob_dict[constants.DNA_ACTIONS_STR] = 0.2

    def set_ptobability(self, prob_dict):
        self.prob_dict = prob_dict

    def get_probability_dict(self):
        return self.prob_dict





