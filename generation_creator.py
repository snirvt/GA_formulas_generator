
import copy
class Generation_Creator():

    def __init__(self):
        pass

    def replicate_parents(self, parents_front, num_parents):
        for i in range(num_parents, len(parents_front)):
            parents_front[i] = copy.deepcopy(parents_front[i % num_parents])
        return parents_front


