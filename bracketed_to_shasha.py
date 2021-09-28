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



def convert_bracketed_to_shasha_node(bracketed_tree):
    l = Node('a')

    for st in bracketed_tree:
        print('36', l)
        print(st, type(st))
        st = Node(str(st.label))
        print(st, type(st))
        l.addkid(st)
        print('40', l)
    return l

bracketed_sentences_gold = negra_to_bracket(input_bracketed_file_negra)

B = (
    Node("f")
        .addkid(Node("a")
            .addkid(Node("l"))
            .addkid(Node("c")
                .addkid(Node("b"))))
        .addkid(Node("e"))
    )

for s in bracketed_sentences_gold:

    
    for q in incrementaltreereader(s):
        parenttree = q[0]
        
        print(distance(B, B, zss.Node.get_children, 
                insert_cost = lambda node: 1, 
                remove_cost= lambda node: 1, 
                update_cost= lambda a, b: 1,
                return_operations=True))
        print('simple distance: ', simple_distance(parenttree,parenttree, return_operations=True))
