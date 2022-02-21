from collections import defaultdict

mod = 10 ** 9 + 7


# runnning dfs go through entire tree
# return - the adjacency list
def dfs(node):
    ch = defaultdict(lambda: 1)
    stack = [node]
    visited = [0 for i in range(n+1)]
    visited[node] = 1
    for i in stack:
        for j in tree[i]:
            if not visited[j]:
                visited[j] = i
                stack.append(j)
    while len(stack) > 1:
        nextNode = stack.pop()
        ch[visited[nextNode]] += ch[nextNode]
    return sorted(ch.values())


for _ in range(int(input())):

    n = int(input())

    # create distributed tree and fill in the nodes
    tree = defaultdict(list)
    for i in range(n-1):
        u, v = map(int, input().split())
        tree[u].append(v)
        tree[v].append(u)

    # running dfs starting from root is node 1
    children = dfs(1)

    k = int(input())
    # read the given list of primes numbers, sort in ascending order
    primes = sorted(map(int, input().split()))
    for i in range(k-(n-1)):
        current = primes.pop()
        primes[-1] = (current*primes[-1]) % mod
    primes = [1]*max(n-1-k, 0) + primes

    # number of times a path is includes
    passage = []
    for i in range(n-1):
        passage.append((children[i])*(n-children[i]))  # multiple u and v
    passage.sort()

    ans = 0
    for i, j in zip(primes, passage):
        ans += i*j
        ans = ans % mod
    print(ans % mod)
