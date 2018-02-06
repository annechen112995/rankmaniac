#!/usr/bin/env python2

import sys

#
# This program simply represents the identity function.
#

'''
Input: NodeId, PageRank, List of Outlinks
'''

alpha = 0.85
highestNodes = []
highestRanks = []
nodeCount = 0

for line in sys.stdin:
    tab = line.strip().split('\t')
    content = tab[1].split(',')
    nodeId = tab[0]
    rank = float(content[0])

    sys.stdout.write('FinalRank:%s\t%s\n' % (rank, nodeId))

    '''
    if nodeId not in highestNodes and nodeCount < 20:
        highestNodes.append(nodeId)
        highestRanks.append(rank)
        nodeCount += 1
    else:
        if (nodeCount == 20) and rank > max(highestRanks):
            sys.stdout.write('higher rank %s, %s' % (rank, max(highestRanks)))

    #sys.stdout.write(line)
for i in range(len(highestNodes)):
    sys.stdout.write('FinalRank:%s\t%s\n' % (highestNodes[i], highestRanks[i]))
    '''
