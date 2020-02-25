from individual import Individual
from tree import Tree
import utils

class Genom_Translator():
    def __init__(self, column_names):
        self.column_names = column_names
        self.tree = Tree()
        self.expression_str = ''

    def translate_genotype(self, individual):
        fenotype = ''
        broken_fenotype = self.get_raw_fenotype(individual).split('_')
        for split in broken_fenotype:
            if split.isnumeric():
                fenotype += 'R' + str(self.column_names[int(split)])
            else:
                fenotype += split
        return fenotype  

    def get_raw_fenotype(self, individual):
        self.build_individual_binary_tree(individual)
        self.expression_str = ''
        self.extract_tree_expression(self.tree.node, index_mark = '_')
        return self.fix_expression(self.expression_str)

    def build_individual_binary_tree(self, individual):
        merged_values = Individual.merge_dna_data(individual)
        self.tree.delete_tree()
        for value in merged_values:
            self.tree.insert(value)

    def extract_tree_expression(self, node, index_mark = '_'):
        if node == None or node.data == None:
            return self.expression_str
        feature, parentheses, action, wl_scalar, wl_power, parentheses_bias = Individual.get_all_merged_values(node.data)
        
        if parentheses == 1:
            self.expression_str += '('
        self.expression_str += '({}'.format(wl_scalar) + '*' ## add wl scalar
        self.expression_str += '{}{}{}'.format(index_mark, feature, index_mark)
        self.expression_str += '**{}'.format(wl_power)
        self.expression_str += ')'
        self.expression_str += utils.get_action(action)

        self.expression_str = self.extract_tree_expression(node.left, index_mark)
        self.expression_str = self.extract_tree_expression(node.right, index_mark)

        if parentheses == 1:
            self.expression_str = self.expression_str[:-1] + '+{})'.format(parentheses_bias) + self.expression_str[-1] ## put closing parentesis before action
        return self.expression_str

    def fix_expression(self, expression):
        expression = expression[:-1] ## remove the last action X[:,0]+X[:,1]+ -> X[:,0]+X[:,1]
        expression = expression.replace('^','**')
        return expression