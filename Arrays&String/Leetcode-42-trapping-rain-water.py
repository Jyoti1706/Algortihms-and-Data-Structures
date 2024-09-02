class Solution:
    def trap(self, height):
        l, r = 0, len(height)
        leftMax = height[0]
        rightMax = height[1]
        res = 0
        while l < r:
            if leftMax < rightMax:
                l += 1
                leftMax = max(leftMax, height[l])
                res += leftMax - height[l]
            else:
                r -= 1
                rightMax = max(rightMax, height[r])
                res += rightMax - height[r]
        return res


height = [0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]
obj = Solution()
print(obj.trap(height))
height = [4, 2, 0, 3, 2, 5]
print(obj.trap(height))
