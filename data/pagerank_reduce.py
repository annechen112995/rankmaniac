#!/usr/bin/env python

import sys

#
# This program simply represents the identity function.
#

'''
Input(s):
outlink, pr of outlink OR
nodeId, content(currPageRank, prevPageRank, outlinks)
'''

for line in sys.stdin:
    tab = line.strip().split('\t')
    content = tab[1].split(',')
    pageRank = 0.0
    outlinkList = []

    if len(content) > 1:
        outlinkList = content[2:] # Input = nodeId, content
    else:
        pageRank += float(content[0]) # Input = outlink, pr of outlink

    #sys.stdout.write(line)
    sys.stdout.write('%s\t%s,%s\n' % (tab[0], pageRank, outlinkList))
