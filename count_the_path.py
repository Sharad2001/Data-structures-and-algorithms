from collections import defaultdict, deque
class Solution:
    def possible_paths(self, edges, n, s, d):
        adj = defaultdict(list)
        cnt = 0
        for i, j in edges:
            adj[i].append(j)
        q = deque()
        q.append(s)
        while (q):
            node = q.popleft()
            if node == d:
                cnt += 1
            for m in adj[node]:
                q.append(m)
        return cnt

if __name__ == '__main__':
    n, m, s, d = input().split()
    n = int(n); m = int(m); s = int(s); d = int(d);
    edges = []
    for _ in range(m):
        x,y = input().split()
        x = int(x); y = int(y);
        edges.append([x,y])
    obj = Solution()
    ans = obj.possible_paths(edges, n, s, d)
    print(ans)