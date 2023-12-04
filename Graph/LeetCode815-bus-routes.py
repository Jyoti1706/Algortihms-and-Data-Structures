import collections

from Graph.DisjointTest import DisjointSet


class Solution:
    def numBusesToDestination(self, routes, source, target):
        if source == target:
            return 0

        idx = 0
        stops = set()
        for route in routes:
            for i in route:
                stops.add(i)

        if source not in stops or target not in stops:
            return -1
        unordered_map = {i: set() for i in stops}

        for route in routes:
            for i in route:
                unordered_map[i].add(idx)
            idx += 1
        # print( unordered_map)
        queue = collections.deque()
        visited = set()
        for i in unordered_map[source]:
            queue.append(i)
            visited.add(i)
        count = 0
        while queue:
            flag = 0
            for i in range(len(queue)):
                c = queue.popleft()

                if flag == 0:
                    count += 1
                    flag = 1
                for r in routes[c]:
                    if r == target:
                        return count

                    for idx in unordered_map[r]:
                        if idx not in visited:
                            visited.add(idx)
                            queue.append(idx)

        return -1

if __name__ == "__main__":


    obj = Solution()
    #
    # routes = [[1, 2, 7], [3, 6, 7]]
    # source = 1
    # target = 6
    # print(obj.numBusesToDestination(routes, source, target))
    #
    # routes = [[7,12],[4,5,15],[6],[15,19],[9,12,13]]
    # source = 15
    # target = 12
    # print(obj.numBusesToDestination(routes, source, target))
    #
    # routes = [[2],[2,8]]
    # source = 8
    # target = 2
    # print(obj.numBusesToDestination(routes, source, target))
    routes = [[1,2,7],[3,6,7]]
    source = 8
    target = 6
    print(obj.numBusesToDestination(routes, source, target))
