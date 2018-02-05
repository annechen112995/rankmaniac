#!/usr/bin/env python

import sys

#
# This program simply represents the identity function.
#

'''
Example Input: NodeId:0	1.0,0.0,1,2
Format: NodeId:<IDNumber>\t<currPageRank>,<prevPageRank>,<outlinks>\n
'''

for line in sys.stdin:
    tab = line.strip().split('\t')
    content = tab[1].split(',')
    nodeId = tab[0][7:] # get nodeID number
    currPageRank = float(content[0])

    # check for outlinks
    if len(content) > 2:
        outlinks = content[2:]
        outlinkValue = str(currPageRank / len(outlinks))

        # print outlinks and value of outlinks
        for i in outlinks:
            sys.stdout.write('%s\t%s\n' % (i, outlinkValue))
        sys.stdout.write('%s\t0\n' % nodeId)

    else:
        sys.stdout.write('%s\t%s\n' % (nodeId, currPageRank))

    sys.stdout.write('%s\tp,%s\n' % (nodeId, tab[1]))
