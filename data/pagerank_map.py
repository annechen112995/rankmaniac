#!/usr/bin/env python2

import sys

#
# This program simply represents the identity function.
#

'''
Example Input: NodeId:0	1.0,0.0,1,2
Format: NodeId:<IDNumber>\t<currPageRank>,<prevPageRank>,<outlinks>\n
'''

alpha = 0.85;

for line in sys.stdin:
    tab = line.strip().split('\t')
    content = tab[1].split(',')
    nodeId = tab[0][7:] # get nodeID number
    currPageRank = float(content[0])
    outlinkList = ''

    # Check for outlinks
    if len(content) > 2:
        outlinks = content[2:]
        outlinkValue = alpha * currPageRank / len(outlinks)
        newPageRank = (1 - alpha) * currPageRank

        # Emit outlink and value of outlink "NodeID:i \t rank"
        for i in outlinks:
            outlinkList = outlinkList + ',' + i
            sys.stdout.write('NodeId:%s\t%s\n' % (i, outlinkValue))
        sys.stdout.write('NodeId:%s\t%s,%s%s\n' % (nodeId, newPageRank, currPageRank, outlinkList))

    else:
        newPageRank = currPageRank
        outlinks = []
        # Emit current node and it's pr
        sys.stdout.write('NodeId:%s\t%s,%s%s\n' % (nodeId, newPageRank, currPageRank, outlinkList))
