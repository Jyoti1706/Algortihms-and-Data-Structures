import math
from typing import List


class Solution:

    def maxBalancedSubsequenceSum_TD(self, nums: List[int]) -> int:
        """
        Top-Down Approach:
        either Skip an element or take that element
        :param nums:
        :return: sum of LIS of nums array on basis of nums[i]-[i] array
        """
        max_ele = max(nums)
        if max_ele<=0:
            return max_ele
        dp={}

        def solve(prev, idx, nums):
            if idx >= len(nums):
                return 0
            if (prev,idx) in dp:
                return dp[(prev,idx)]
            skip = solve(prev, idx + 1, nums)
            take = math.inf * -1
            if (prev == -1) or ((nums[idx] -idx) >= (nums[prev]- prev)) :
                take = nums[idx] + solve(idx, idx + 1, nums)
            dp[(prev, idx)] = max(skip, take)
            return dp[(prev, idx)]
        return solve(-1, 0, nums)

    def maxBalancedSubsequenceSum_BU(self, nums: List[int]) -> int:
        """
                Bottom-Up Approach:
                either Skip an element or take that element
                :param nums:
                :return: sum of LIS of nums array on basis of nums[i]-[i] array
                """
        n = len(nums)
        max_ele = max(nums)
        if max_ele <= 0:
            return max_ele

        dp = [nums[i] for i in range(n)]
        max_sum = math.inf*-1
        for i in range(n):
            for j in range(i):
                if nums[i]-i >= nums[j]-j:
                    dp[i] = max(dp[i], dp[j]+nums[i])
                    max_sum = max(max_sum, dp[i])
        return max(max_sum, max_ele)


"""
1. Sorted Hashmap : Key = nums[i]-i , value = maximum sum till that subsequence
2. if num 
class Solution {
public:
    long long maxBalancedSubsequenceSum(vector<int>& nums) {
        int n = nums.size();
        map<int, long long> mp;

        long long ans = INT_MIN;
        
        for(int i = 0; i < n; i++){
            auto it = mp.upper_bound(nums[i]-i); //Find the element just greater than nums[i]-i;

            long long cur_ans = nums[i];

            if(it != mp.begin()) {
                it--;
                cur_ans += (*it).second;
            }
            mp[nums[i]-i] = max(mp[nums[i]-i], cur_ans);

            it = mp.upper_bound(nums[i]-i);

            while(it != mp.end() && (*it).second <= cur_ans) {
                 mp.erase(it++);
            }

            ans = max(ans, cur_ans);
        }

        return ans;
    }
};

"""