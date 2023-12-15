class Solution:
    """
    Loop through all pair of vertex via path and calculate the distance , update the minimum distance at cell[i][j]
    say vertex are 0,1,2,3,4
    0-->3
    calc 0->0->3, 0->1->3, 0->2->3,0->3->3,0->4->3 and update the lowest value at matrix[0][3]

    after Shortest distance calculation loop, matrix will be updated by shortest distance from i to j.

    THIS IS FLOYD WARSHALL ALGORITHM --> COMPLEXITY: O(N^3)
    """

    def shortest_distance(self, matrix):
        # Code here
        n = len(matrix)
        # marking no edge as high value
        for i in range(n):
            for j in range(n):
                if matrix[i][j] == -1:
                    matrix[i][j] = 100000000
        # Shortest distance calculation loop
        for via in range(n):
            for i in range(n):
                for j in range(n):
                    matrix[i][j] = min(matrix[i][j], matrix[i][via] + matrix[via][j])

        for i in range(n):
            for j in range(n):
                if matrix[i][j] == 100000000:
                    matrix[i][j] = -1


matrix = [[0, 1, 43], [1, 0, 6], [-1, -1, 0]]  # Output: {{0,1,7},{1,0,6},{-1,-1,0}}
obj = Solution()
obj.shortest_distance(matrix)
print(matrix)
