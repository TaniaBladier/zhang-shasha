from zss import simple_distance, distance, Node

A = (
    Node("f")
        .addkid(Node("a")
            .addkid(Node("h"))
            .addkid(Node("c")
                .addkid(Node("l"))))
        .addkid(Node("e"))
    )
B = (
    Node("f")
        .addkid(Node("a")
            .addkid(Node("l"))
            .addkid(Node("c")
                .addkid(Node("b"))))
        .addkid(Node("e"))
    )
print(simple_distance(A, B))
print()

import zss

try:
    from editdist import distance as strdist
except ImportError:
    def strdist(a, b):
        if a == b:
            return 0
        else:
            return 1

def weird_dist(A, B):
    return 1*strdist(A, B)

class WeirdNode(object):

    def __init__(self, label):
        self.my_label = label
        self.my_children = list()

    @staticmethod
    def get_children(node):
        return node.my_children

    @staticmethod
    def get_label(node):
        return node.my_label

    def addkid(self, node, before=False):
        if before:  self.my_children.insert(0, node)
        else:   self.my_children.append(node)
        return self

#dist = zss.simple_distance(
#    A, B, WeirdNode.get_children, WeirdNode.get_label, weird_dist)

#print (dist)
#assert dist == 20

# Node(label, children)
# a---> b
#  \--> c
c = Node('c', [])
b = Node('b', [])
a = Node('a', [Node('b', []), Node('c', [])])

# a---> c
a2 = Node('a', [Node('d', [Node('c', [])])])

b = Node('ROOT', [Node('SENTENCE', [Node('CLAUSE', [Node('CORE', [Node('NP', [Node('CORE_N', [Node('NUC_N', [Node('N-PROP', [])])])]), Node('NUC', [Node('V', []), Node('ADV', [])]), Node('NP', [Node('OP-DEF', []), Node('CORE_N', [Node('NUC_N', [Node('N', [])])])]), Node('.', [])])])])])
print(type(b))
print(simple_distance(b, b))
print(distance(b, b, zss.Node.get_children, 
    insert_cost = lambda node: 2, 
    remove_cost= lambda node: 0.5, 
    update_cost= lambda a, b: 1,
    return_operations=True))
