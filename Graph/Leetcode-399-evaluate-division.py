import collections



class Solution:
    def calcEquation(self, equations, values, queries):
        adj = collections.defaultdict(list)
        for i, eq in enumerate(equations):
            a, b = eq
            adj[a].append([b, values[i]])
            adj[b].append([a, 1 / values[i]])

        # a/b ,
        def bfs(src, target):
            if src not in adj or target not in adj:
                return -1
            queue = collections.deque()
            visit = set()
            queue.append([src, 1])
            visit.add(src)
            while queue:
                q, w = queue.popleft()
                if q == target:
                    return w
                for n, weight in adj[q]:
                    if n not in visit:
                        queue.append([n, w * weight])
                        visit.add(n)
            return -1

        return [bfs(q[0], q[1]) for q in queries]


obj = Solution()
equations = [["a", "b"], ["b", "c"]]
values = [2.0, 3.0]
queries = [["a", "c"], ["b", "a"], ["a", "e"], ["a", "a"], ["x", "x"]]
print(obj.calcEquation(equations, values, queries))
