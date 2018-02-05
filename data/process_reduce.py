#!/usr/bin/env python

import sys

#
# This program simply represents the identity function.
#

'''
Input: NodeId, PageRank, List of Outlinks
'''

alpha = 0.85

for line in sys.stdin:
    tab = line.strip().split('\t')
    content = tab[1].split(',')
    nodeId = tab[0]
    rank = float(content[0])
    rank = 1.0 - (alpha) + (alpha * rank)

    sys.stdout.write('FinalRank:%s\t%s\n' % (rank, nodeId))
    #sys.stdout.write(line)
