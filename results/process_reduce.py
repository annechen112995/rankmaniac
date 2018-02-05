#!/usr/bin/env python

import sys

#
# This program simply represents the identity function.
#

for line in sys.stdin:
    tab = line.strip().split('\t')
    nodeId = tab[0]
    rank = tab[1]
    sys.stdout.write('FinalRank:%s\t%s\n' % (float(rank), nodeId))

 