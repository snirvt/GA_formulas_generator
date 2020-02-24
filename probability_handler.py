
import constants


class Probability_Handler():

    def __init__(self, max_feature_number):
        self.prob_dict = {}
        self.max_feature_number = max_feature_number

    def create_uniform_probability(self, chance = 0.2):
        self.prob_dict[constants.DNA_SIZE_STR] = chance
        self.prob_dict[constants.DNA_FEATURES_STR] = chance
        self.prob_dict[constants.DNA_WEIGHTS_STR] = chance
        self.prob_dict[constants.DNA_PARENTHESES_STR] = chance
        self.prob_dict[constants.DNA_ACTIONS_STR] = chance
        self.prob_dict[constants.DNA_WL_SCALAR] = chance

    def set_ptobability(self, prob_dict):
        self.prob_dict = prob_dict

    def get_probability_dict(self):
        if len(self.prob_dict) == 0:
            self.create_uniform_probability()
        return self.prob_dict





