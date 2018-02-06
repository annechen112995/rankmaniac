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
    if len(line) > 0:
    # sys.stdout.write("\n\n\n")
    # sys.stdout.write("line {}".format(testLineNum))
    # sys.stdout.write(line)
    # tab = line.strip().split('\t',1)
    # idx = len(tab) - 1;
    # # idx = 1;
    # sys.stdout.write("tab length is {}\n".format(len(tab)));
    # sys.stdout.write("last index in tab is {}\n".format(len(tab) - 1));
    # sys.stdout.write("last element in tab is {}\n".format(tab[len(tab) - 1]));
    # sys.stdout.write("last element in tab is using placeholder{}\n".format(tab[idx]));
    # # sys.stdout.write("tab is {}".format(tab[1]));
    # # print "tab is: " + str(tab)
    # # for i in range(len(tab)):
    # #     sys.stdout.write(str(i) + '\n')
    # #     sys.stdout.write(str(tab[i]) + '\n')
    # testLineNum = testLineNum + 1

        # We dont need the key (1)
        content = tab[1].split(',',1)
        # This is the boolean denoting convergence of a singular node rank
        finals.append(bool(int(content[0])))
        # This is the string of "NodeID:i\tcurrentRank, preRank, [adg]"
        nodeString.append(content[1])

# If rank converged, output final rank
if all(finals):
    # extract nodeId and nodeRank from node strings
    for i in nodeString:
        tab = i.strip().split('t')
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
        sys.stdout.write(i)'''
