from collections import deque
from typing import List


class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        queue = deque([0])
        unvisited = set(range(len(rooms)))

        while queue:
            v = queue.popleft()
            if v in unvisited:
                unvisited.remove(v)
                queue.extend(rooms[v])

        return not unvisited


if __name__ == "__main__":
    obj = Solution()
    rooms = [[1], [2], [3], []]
    print(obj.canVisitAllRooms(rooms))
    rooms = [[1, 3], [3, 0, 1], [2], [0]]
    print(obj.canVisitAllRooms(rooms))
