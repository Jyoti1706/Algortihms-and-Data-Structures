"""
https://leetcode.com/problems/rotting-oranges/description/
"""
import collections


class Solution:
    def orangesRotting(self, grid):
        ROWS = len(grid)
        COLUMNS = len(grid[0])
        queue = collections.deque()
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        marked = [[False for _ in range(COLUMNS)] for _ in range(ROWS)]
        count = 0
        for r in range(ROWS):
            for c in range(COLUMNS):
                if grid[r][c] == 2:
                    queue.append((r,c))
                    marked[r][c] = True
        if not queue:
            return -1

        while queue:
            flag = 0
            for c in range(len(queue)):
                r, c = queue.popleft()
                for d in directions:
                    row = r + d[0]
                    col = c + d[1]
                    if (0 <= row < ROWS) and (0 <= col < COLUMNS) and grid[row][col] == 1 and marked[row][col] == False:
                        queue.append((row, col))
                        marked[row][col] = True
                        grid[row][col] = 2
                        if flag == 0:
                            count += 1
                            flag=1

        for r in range(ROWS):
            for c in range(COLUMNS):
                if marked[r][c] == False and grid[r][c] == 1:
                    return -1
        return count


obj = Solution()
# grid = [[2,1,1],[1,1,0],[0,1,1]]
# print(obj.orangesRotting(grid))
#
# grid = [[2,1,1],[0,1,1],[1,0,1]]
# print(obj.orangesRotting(grid))
#
# grid = [[0,2]]
# print(obj.orangesRotting(grid))
#
# grid = [[1]]
# print(obj.orangesRotting(grid))
#
# grid = [[1, 2]]
# print(obj.orangesRotting(grid))

grid = [[1]]
print(obj.orangesRotting(grid))
