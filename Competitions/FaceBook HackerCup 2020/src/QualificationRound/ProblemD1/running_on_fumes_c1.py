from collections import deque

def running_on_fumes_chapter_1():
    N, M = map(int, input().strip().split())
    C = [input() for _ in range(N)]
    dq = deque([(0, 0)])
    for i in range(1, len(C)):
        count = 0
        if dq and i-dq[0][0] > M:
            count += 1
            dq.popleft()
        if not dq:
            return -1
        if not C[i]:
            continue
        d = dq[0][1]+C[i]
        while dq and dq[-1][1] >= d:
            dq.pop()
        dq.append((i, d))   
    return dq[0][1]

for case in range(input()):
    print ('Case #%d: %s' % (case+1, running_on_fumes_chapter_1()))