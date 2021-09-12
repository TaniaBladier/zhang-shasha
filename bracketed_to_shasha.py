import sys
import zss
from zss import simple_distance, distance, Node
from discodop.tree import writediscbrackettree
from discodop.treebank import (NegraCorpusReader, BracketCorpusReader, 
                    DiscBracketCorpusReader, incrementaltreereader)
import re

input_bracketed_file_negra = sys.argv[1]
input_bracketed_file_ud2rrg = sys.argv[2]


def negra_to_bracket(negra_file):
    sents = []
    tb = NegraCorpusReader(
    negra_file,
    ensureroot=None,  # add a root label
    functions='add',
    removeempty=True,
    punct='no',
    morphology='no'  # labels are of the form CAT-FUNC, store FUNC separately.
    )

    for n, (key, item) in enumerate(iter(tb.itertrees()),1):
        disctree = writediscbrackettree(item.tree, item.sent)
        sents.append(disctree)

    return sents



def convert_bracketed_to_shasha_node(bracketed_tree_string):
    shasha_tree = bracketed_tree_string.replace('ParentedTree', 'Node')
    shasha_tree = re.sub(r'\[[0-9]+\]', r'[]', shasha_tree)
    #print(shasha_tree)
    return Node(shasha_tree)

bracketed_sentences_gold = negra_to_bracket(input_bracketed_file_negra)

for s in bracketed_sentences_gold:

    l = Node('')
    for q in incrementaltreereader(s):
        parenttree = q[0]
        
        for st in parenttree.subtrees():
            st = Node(str(st.label))
            print(st, type(st))
            l.addkid(st)
    print(distance(l, l, zss.Node.get_children, 
            insert_cost = lambda node: 2, 
            remove_cost= lambda node: 0.5, 
            update_cost= lambda a, b: 0.5,
            return_operations=True))
    print('l', l)
    print(simple_distance(l, l))

"""parenttree = str(q[0:1])[1:-2]

        shasha_tree = convert_bracketed_to_shasha_node(parenttree)
        print('43', type(shasha_tree))
        print()
        print(distance(shasha_tree, shasha_tree, zss.Node.get_children, 
            insert_cost = lambda node: 2, 
            remove_cost= lambda node: 0.5, 
            update_cost= lambda a, b: 1,
            return_operations=True))"""
