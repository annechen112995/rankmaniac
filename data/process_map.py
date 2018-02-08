#!/usr/bin/env python

import sys
import math

'''
This mapper is used to determine when the MapReduce algorithm
terminates.
We consider our algorithm to have converged when the change in
pageRank for all nodes between iterations is less than the
variable t.
'''


# Input:
# Each input line is formatted as NodeId: n_id\tc_rank, p_rank, adj_list\titerations
# Where:
#           n_id is the Node id
#           \t is a tab character
#           c_rank is the current pagerank of the node
#           p_rank is the previous pagerank of the node
#			adj_list is the node's neighbors, comma delineated
#           iterations is the current number of iterations performed
#
# Output:
# Each output line is formatted as 1\tconverged, NodeId: n_id\tc_rank, p_rank, adj_list\titerations
# Where:
#			\t is a tab character
#			converged is 0 if |c_rank-p_rank| > t and 1 otherwise
#			n_id is the Node id
#           c_rank is the current pagerank of the node
#           p_rank is the previous pagerank of the node
# 			adj_list is the node's neighbors, comma delineated
#           iterations is the number of iterations performed

for line in sys.stdin:
    t = 0.002
    tab = line.strip().split('\t')
    prevContent = str(tab[0]) + str(tab[1])
    content = tab[1].split(',')
    iterations = int(tab[2]) + 1

    c_pageRank = float(content[0])
    p_pageRank = float(content[1])
    converged = 0

    # Return 0 as the value for converged if the change in pageRank is
    # larger than t
    if (abs(c_pageRank-p_pageRank) < t):
    	converged = 1
    sys.stdout.write(('1\t%s,%s\t%s\n' % (converged, prevContent, iterations)))
