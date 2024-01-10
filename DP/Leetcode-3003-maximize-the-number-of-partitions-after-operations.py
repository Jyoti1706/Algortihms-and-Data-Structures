from functools import cache


class Solution:
    def maxPartitionsAfterOperations(self, s: str, k: int) -> int:
        @cache
        def dp(index, current_set, can_change):
            if index == len(s):
                return 0
            character_index = ord(s[index]) - ord('a')

            current_set_updated = current_set | (1 << character_index)
            distinct_count = current_set_updated.bit_count()

            if distinct_count > k:
                res = 1 + dp(index + 1, 1 << character_index, can_change)
            else:
                res = dp(index + 1, current_set_updated, can_change)

            if can_change:
                for new_char_index in range(26):
                    new_set = current_set | (1 << new_char_index)
                    new_distinct_count = new_set.bit_count()

                    if new_distinct_count > k:
                        res = max(res, 1 + dp(index + 1, 1 << new_char_index, False))
                    else:
                        res = max(res, dp(index + 1, new_set, False))
            return res

        return dp(0, 0, True) + 1


class Solution2:
    def maxPartitionsAfterOperations(self, s: str, k: int) -> int:

        dp = {}

        def dfs(index, char_bitmask=0, change_used=0):
            nonlocal k
            if index >= len(s):
                return 1

            if (index, char_bitmask, change_used) in dp:
                return dp[(index, char_bitmask, change_used)]

            val = 0
            bitmask_cur_char = 1 << (ord(s[index]) - ord("a"))

            if (char_bitmask | bitmask_cur_char).bit_count() > k:
                val = max(val, 1 + dfs(index + 1, bitmask_cur_char, change_used))
            else:
                val = max(val, dfs(index + 1, char_bitmask | bitmask_cur_char, change_used))

            if change_used == 0:

                for i in range(26):
                    bitmask_brute_char = 1 << i
                    if bitmask_brute_char & char_bitmask:
                        continue
                    if (char_bitmask | bitmask_brute_char).bit_count() > k:
                        val = max(val, 1 + dfs(index + 1, bitmask_brute_char, 1))
                    else:
                        val = max(val, dfs(index + 1, char_bitmask | bitmask_brute_char, 1))

            dp[(index, char_bitmask, change_used)] = val

            return dp[(index, char_bitmask, change_used)]

        return dfs(0)


obj = Solution()
s = "aabaab"
k = 3
print(obj.maxPartitionsAfterOperations(s,k))
s = "xxyz"
k = 1
print(obj.maxPartitionsAfterOperations(s,k))