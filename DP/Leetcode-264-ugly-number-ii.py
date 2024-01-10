import heapq


class Solution:
    def nthUglyNumber(self, n: int) -> int:
        arr = [0 for _ in range(n + 1)]
        i2 = 1
        i3 = 1
        i5 = 1
        arr[1] = 1
        for i in range(2, n + 1):
            i2Ugly = arr[i2] * 2
            i3Ugly = arr[i3] * 3
            i5Ugly = arr[i5] * 5
            minUgly = min(i2Ugly, i3Ugly, i5Ugly)
            arr[i] = minUgly
            if minUgly == i2Ugly:
                i2 += 1
            if minUgly == i3Ugly:
                i3 += 1
            if minUgly == i5Ugly:
                i5 += 1
        return arr[n]


if __name__ == "__main__":

    obj = Solution()
    print(obj.nthUglyNumber(10))
