from tree_node import *

class Tree():
    def __init__(self):
        self.root = TreeNode('1', 'root', None, [], None, 0)
        self.tree_map = dict()

    #def construct_tree(self):
        # create tree structure
        self.root.set_root(self.root)
        a = TreeNode('2', 'a', self.root, [], self.root, 1)
        b = TreeNode('3', 'b', self.root, [], self.root, 1)
        c = TreeNode('4', 'c', a, [], self.root, 2)
        self.root.set_children([a, b])
        a.set_children([c])

        # create tree hashmap
        self.tree_map = {
            '1': self.root,
            '2': a,
            '3': b,
            '4': c
        }


