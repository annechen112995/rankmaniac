#!/usr/bin/env python2

import sys

'''
This reducer computes one step of the pageRank algorithm,
and updates the pageRank of all nodes once.
It does so by summing all pageRank contributions that come in
from the mapper program.

'''

# Input:
# Each input line is formatted as either:
# 1. NodeId: n_id\tr_contr, p_rank, adj_list\titerations
# or
# 2. NodeId: n_id\tr_contr
#
# Where:
#           n_id is the Node id
#           \t is a tab character
#           r_contr is the portion of the node's pageRank
#           p_rank is the previous pagerank of the node
#           adj_list is the node's neighbors, comma delineated
#           iterations is the current number of iterations performed
#
#
# Output:
# Each output line is formatted as NodeId: n_id\tc_rank, p_rank, adj_list
# Where:
#           c_rank is the current pagerank of the node
#


c_pageRank = 0.0
prev_key = None
p_pageRank = None
outlink_string = ''
iterations = None

for line in sys.stdin:
    # split the line to get our key and values
    tab = line.strip().split('\t')
    curr_key = tab[0]


    if (curr_key != prev_key and prev_key is not None):
        sys.stdout.write('%s\t%s,%s%s\t%s\n' % (prev_key, c_pageRank, p_pageRank, outlink_string, iterations))
        c_pageRank = 0.0
        p_pageRank = None
        prev_key = curr_key
        outlink_string = ''
        
    if (prev_key is None):
        prev_key = curr_key

    content = tab[1].split(',')
    
    if len(content) > 1:
        iterations = tab[2]
        if iterations > 3:
            c_pageRank += 2 * float(content[0])
        else:
            c_pageRank += float(content[0])
        p_pageRank = content[1]    # the previous pageRank
        outlink_list = content[2:] # the list of neighbors
        for i in outlink_list:
            outlink_string = outlink_string + ',' + i
    else:
        c_pageRank += float(content[0]) # We sum the contributions to pageRank

sys.stdout.write('%s\t%s,%s%s\t%s\n' % (prev_key, c_pageRank, p_pageRank, outlink_string, iterations))



