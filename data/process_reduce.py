#!/usr/bin/env python2

import sys

#
# This function takes the input of the reducer and eiter returns input to
# the next pageRank map function or the final rank
#

'''
Input: "1\tbool,NodeID:i \t currentRank, preRank, [adj nodes \t iter"
Output: "NodeID:i \t currentRank, preRank, [adj nodes \t iter"
    or  "FinalRank: rank i" of top 20 nodes
'''


def process_input(line):
    # Remove key
    preprocess = line.strip().split('\t', 1)

    # Obtain value "bool, NodeID:i \t cRank, pRank, nodes \t iter"
    value = preprocess[1]

    # We get [bool, "NodeID..... \t iter"]
    first_comma = value.split(',', 1)
    converged_tag = bool(int(first_comma[0]))

    # Separate iter with node --> ['NodeId...', iter]
    last_tab = first_comma[1].rsplit('\t', 1)
    node_string = last_tab[0]
    iter_ID = last_tab[1]

    return converged_tag, node_string, iter_ID


def process_nodes(node_strings):
    '''
    We get a list of "NodeID:i \t c_rank, p_rank, adj nodes..."
    output: lists of (nodeID, c_rank) sorted by c_rank in reverse
    '''
    nodes = []

    # Organize into pairs of (nodeID, c_rank)
    for i in node_strings:
        tab = i.strip().split('\t')
        if len(tab) > 1:
            node_Id = tab[0][7:]
            content = tab[1].split(',')
            node_rank = content[1]
            nodes.append([int(node_Id), float(node_rank)])

    # Calculate final rank by sorting in descending order
    nodes.sort(key=lambda x: float(x[1]), reverse=True)

    return nodes


node_strings = []
converged_tags = []
num_top_pages = 20
max_iter = 50
iter_ID = 0
test_line_num = 0

# Gather all input string and parse
for line in sys.stdin:
    if len(line) > 1:
        converged_tag, node_string, iter_ID = process_input(line)

        # Store
        converged_tags.append(converged_tag)
        node_strings.append(node_string)

# If rank converged, output final rank
if all(converged_tags) or iter_ID >= max_iter - 1:
    nodes = process_nodes(node_strings)

    # Output final rank
    for i in range(min(num_top_pages, len(nodes))):
        sys.stdout.write('FinalRank:%s\t%s\n' % (
            str(nodes[i][1]), str(nodes[i][0])))

# Output to PageRank Mapper
else:
    for i in node_strings:
        sys.stdout.write('%s\t%s\n' % i, iter_ID + 1)
