#
# Time:  O(N)
# Space: O(1)
#

from collections import Counter

def alchemy():
    N = input()
    count = Counter(input().strip())
    return "NY"[int(abs(count['A']-count['B']) == 1)]

for case in range(input()):
    print('Case #%d: %s' % (case+1, alchemy()))