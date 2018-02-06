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
# 1. NodeId: n_id\tr_contr, p_rank, adj_list
# or
# 2. NodeId: n_id\tr_contr
#
# Where:
#           n_id is the Node id
#           \t is a tab character
#           r_contr is the portion of the node's pageRank
#           p_rank is the previous pagerank of the node
#           adj_list is the node's neighbors, comma delineated
#
#
# Output:
# Each output line is formatted as NodeId: n_id\tc_rank, p_rank, adj_list
# Where:
#           c_rank is the current pagerank of the node
#


for line in sys.stdin:
    # split the line to get our key and values
    tab = line.strip().split('\t')
    content = tab[1].split(',')
    c_pageRank = 0.0
    outlink_string = ''

    if len(content) > 1:
        c_pageRank += float(content[0])
        p_pageRank = content[1]    # the previous pageRank
        outlink_list = content[2:] # the list of neighbors
        for i in outlink_list:
            outlink_string = outlink_string + ',' + i
    else:
        c_pageRank += float(content[0]) # We sum the contributions to pageRank


sys.stdout.write('%s\t%s,%s%s\n' % (tab[0], c_pageRank, p_pageRank, outlink_string))
