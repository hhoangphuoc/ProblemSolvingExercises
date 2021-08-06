#
# Time:  O(N^2)
# Space: O(1), excluding the space of output
#

def travel_restrictions():
    N = input()
    I, O = [input().strip() for _ in range(2)]
    result = []
    left, right = -1, -1
    for i in range(N):
        if not (i-1 >= 0 and O[i] == I[i-1] == 'Y'):
            left = i
        if right < i:
            right = i
            while right+1 < N and O[right] == I[right+1] == 'Y':
                right += 1
        result.append('N'*left + 'Y'*(right-left+1) + 'N'*(N-1-right))
    return "\n" + "\n".join(result)

for case in range(input()):
    print('Case #%d: %s' % (case+1, travel_restrictions()))