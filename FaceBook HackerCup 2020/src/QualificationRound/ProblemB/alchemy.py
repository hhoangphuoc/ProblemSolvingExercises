#
# Time:  O(N)
# Space: O(1)
#

from collections import Counter

def alchemy():
    N = input()
    count = Counter(raw_input().strip())
    return "NY"[int(abs(count['A']-count['B']) == 1)]

for case in xrange(input()):
    print('Case #%d: %s' % (case+1, alchemy()))