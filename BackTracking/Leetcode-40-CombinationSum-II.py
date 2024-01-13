from typing import List


class Solution:
    def f(self, i, arr, target, ds, ans):
        # BASE CASE
        if target == 0:
            ans.append(ds.copy())
            return
        if i >= len(arr):
            return
        # RECURENCE RELATION
        if target >= arr[i]:
            ds.append(arr[i])
            self.f(i + 1, arr, target - arr[i], ds, ans)  # PICK
            ds.pop()
        j = i + 1  ## Move pointer till next non duplicate element
        while (j < len(arr) and arr[j] == arr[j - 1]):
            j += 1
        self.f(j, arr, target, ds, ans)  # NOT PICK

    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        ds = []
        ans = []
        candidates.sort()
        self.f(0, candidates, target, ds, ans)
        return ans


if __name__ == "__main__":
    obj = Solution()
    candidates = [10, 1, 2, 7, 6, 1, 5]
    target = 8
    print(obj.combinationSum2(candidates, target))
