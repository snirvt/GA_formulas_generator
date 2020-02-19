

import constants

class Tree():
    def __init__(self):
        self.node = Tree_Node()

    def pre_order(self, node_list):
        if self.node.data == None:
            return
        node_list.append(self.node.data)
        self.node.pre_order(self.node.left, node_list)
        self.node.pre_order(self.node.right, node_list)

    def insert(self, new_data):
        self.node.insert(new_data)

    @staticmethod
    def compare_node(input_A, input_B):
        return input_A[0] <= input_B[0]

    def delete_tree(self):
        self.node = Tree_Node()

class Tree_Node():

    def __init__(self):
        self.left = None
        self.right = None
        self.data = None

    def insert(self, new_data):
        if self.data == None:
            self.data = new_data
            return
        if Tree.compare_node(new_data, self.data):
            if self.left == None:
                self.left = Tree_Node()
            self.left.insert(new_data)
        else:
            if self.right == None:
                self.right = Tree_Node()
            self.right.insert(new_data)

    def pre_order(self, node, node_list):
        if node == None:
            return 
        node_list.append(node.data)
        self.pre_order(node.left, node_list)
        self.pre_order(node.right, node_list)
            
