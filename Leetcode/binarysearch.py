class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        return self.binary_search(nums, low=0, high=len(nums) - 1, x =target)

    def binary_search(self, arr, low, high, x):
        # Check base case
        if high >= low:

            mid = (high + low) // 2

            # If element is present at the middle itself
            if arr[mid] == x:
                return mid

            # If element is smaller than mid, then it can only
            # be present in left subarray
            elif arr[mid] > x:
                return self.binary_search(arr, low, mid - 1, x)

            # Else the element can only be present in right subarray
            else:
                return self.binary_search(arr, mid + 1, high, x)

        else:
            # Element is not present in the array
            return -1