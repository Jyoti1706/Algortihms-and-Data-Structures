'''
You are given an integer array height of length n. There are n vertical lines drawn such that the two endpoints of the ith line are (i, 0) and (i, height[i]).

Find two lines that together with the x-axis form a container, such that the container contains the most water.

Return the maximum amount of water a container can store.

Notice that you may not slant the container.
'''
from typing import List



class Solution:
    def maxArea_bruteForce(self, height: List[int]) -> int:
        n = len(height)
        max_area = 0
        for p1 in range(n):
            for p2 in range(p1+1, n):
                area = min(height[p1], height[p2])*(p2-p1)
                max_area = max(max_area, area)
        return max_area

    def maxArea(self, height: List[int]) -> int:
        '''
        :param height array
        :return: max area
        :technique: used 2 pointer technique,
        1. find min of 2 element at p1 and p2, find width i.e p2-p1
        2. move min of 2 element at p1 and p2 as our result will be affected by minimum element, so move minimum element pointer
        3. set max_area = max(max_area, new_calculated_area)
        '''
        n = len(height)
        p1 = 0
        p2 = n-1
        max_area = 0
        while p1<p2:
            area = min(height[p1], height[p2])*(p2-p1)
            max_area = max(max_area, area)
            if height[p1]<= height[p2]:
                p1 += 1
            else:
                p2 -= 1
        return max_area





solution = Solution()
def test_solution():
    inp = [1, 8, 6, 2, 5, 4, 8, 3, 7]
    result = solution.maxArea(inp)
    assert result == 49

def test_solution_zerosize_array():
    inp = [1]
    result = solution.maxArea(inp)
    assert result == 0

def test_solution_samelength():
    inp = [5,5,5,5,5,5,5,5]
    result = solution.maxArea(inp)
    assert result == 35
