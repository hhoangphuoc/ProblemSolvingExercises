#
# Time:  O(NlogN)
# Space: O(N)
#

from collections import defaultdict

def timber():
    #get the number of trees in the lines
    N = input()
    # store Pi,Hi value of input in array
    P = [map(int, input().strip().split()) for _ in xrange(N)]

    #sort all the tree in increasing order of position.
    P.sort()
    lookup = defaultdict(lambda:defaultdict(int))
    result = 0
    # iterate the array to only the right direction
    for d, direction in ((1, lambda x:x), (-1, reversed)):
        # p is position of the tree
        # l is the height of the tree.
        for p, l in direction(P):

            # find the max length between 2 tree positions when cutting down.
            lookup[d][p+d*l] = max(lookup[d][p+d*l], lookup[d][p]+l)

        for p, l in lookup[d].iteritems():
            result = max(result, lookup[-d][p]+l)
    return result

for case in xrange(input()):
    print('Case #%d: %s' % (case+1, timber()))