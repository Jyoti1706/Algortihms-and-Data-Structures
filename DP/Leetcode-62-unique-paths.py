"""
Top-Down Dynamic Programming:
Step 1: Initialize the Memoization Table

Create a memoization table (an auxiliary 2D array) of size m x n to store computed results. Initialize all entries to -1 to indicate that no results have been computed yet.
Step 2: Recursive Function

Implement a recursive function, say uniquePathsRecursive(x, y, m, n, memo), which calculates the number of unique paths to reach cell (x, y) from the top-left corner.
In this function:
Check if (x, y) is the destination cell (m - 1, n - 1). If yes, return 1 since there is one way to reach the destination.

Check if the result for (x, y) is already computed in the memoization table (memo[x][y] != -1). If yes, return the stored result.

Otherwise, calculate the number of unique paths by recursively moving right and down (if valid) and adding the results. Use the following logic:
➡If (x, y) can move right (i.e., x < m - 1), calculate rightPaths = uniquePathsRecursive(x + 1, y, m, n, memo).
➡ If (x, y) can move down (i.e., y < n - 1), calculate downPaths = uniquePathsRecursive(x, y + 1, m, n, memo).
➡ The total unique paths to (x, y) are rightPaths + downPaths.
➡** Store the result** in the memoization table (memo[x][y]) and return it.

Step 3: Invoke the Recursive Function

Call the recursive function with the initial arguments (0, 0, m, n, memo) to find the number of unique paths.
Step 4: Return the Result

The result obtained from the recursive function call represents the number of unique paths from the top-left corner to the bottom-right corner.

Top-Down Dynamic Programming (with Memoization):
Time Complexity (TC): O(m * n).
Space Complexity (SC): O(m + n).

"""

class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        # Create a memoization table to store computed results
        memo = [[-1 for _ in range(n)] for _ in range(m)]

        # Call the recursive function to compute unique paths
        return self.uniquePathsRecursive(0, 0, m, n, memo)

    def uniquePathsRecursive(self, x: int, y: int, m: int, n: int, memo) -> int:
        # If we reach the destination (bottom-right corner), return 1
        if x == m - 1 and y == n - 1:
            return 1

        # If we have already computed the result for this cell, return it from the memo table
        if memo[x][y] != -1:
            return memo[x][y]

        # Calculate the number of unique paths by moving right and down
        rightPaths = 0
        downPaths = 0

        # Check if it's valid to move right
        if x < m - 1:
            rightPaths = self.uniquePathsRecursive(x + 1, y, m, n, memo)

        # Check if it's valid to move down
        if y < n - 1:
            downPaths = self.uniquePathsRecursive(x, y + 1, m, n, memo)

        # Store the result in the memo table and return it
        memo[x][y] = rightPaths + downPaths
        return memo[x][y]


if __name__ == "__main__":
    obj = Solution()
    m = 3
    n = 7
    print(obj.uniquePaths(m,n))