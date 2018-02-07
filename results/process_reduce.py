#!/usr/bin/env python2

import sys

#
# This function takes the input of the reducer and eiter returns input to
# the next pageRank map function or the final rank
#

'''
Input: (1\tbool, "NodeID:i \t currentRank, preRank, [adj nodes]")
Output: "NodeID:i \t currentRank, preRank, [adj nodes]"
    or  "FinalRank: rank i" of top 20 nodes
'''

nodeString = []
nodes = []
finals = []
nHighest = 20

testLineNum = 0
# Gather all input string and parse
for line in sys.stdin:
    tab = line.strip().split('\t', 1)
    if len(tab) > 1:
        # We dont need the key (1)
        content = tab[1].split(',', 1)
        # This is the boolean denoting convergence of a singular node rank
        finals.append(bool(int(content[0])))
        # This is the string of "NodeID:i\tcurrentRank, preRank, [adg]"
        nodeString.append(content[1])

# If rank converged, output final rank
if all(finals):
    # extract nodeId and nodeRank from node strings
    for i in nodeString:
        tab = i.strip().split('\t')
        if len(tab) > 1:
            nodeId = tab[0][7:]
            content = tab[1].split(',')
            nodeRank = content[1]
            nodes.append([int(nodeId), float(nodeRank)])

    # Calculate final rank by sorting in descending order
    nodes.sort(key=lambda x: float(x[1]), reverse=True)

    # Output final rank
    for i in range(min(nHighest, len(nodes))):
        sys.stdout.write('FinalRank:%s\t%s\n' % (
            str(nodes[i][1]), str(nodes[i][0])))

# Output to PageRank Mapper
else:
    for i in nodeString:
        sys.stdout.write('%s\n' % i)
