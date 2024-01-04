from typing import List


class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int):
        price = [float("inf")] * n
        price[src] = 0
        for i in range(k + 1):
            tmpPrices = price.copy()
            for s, d, p in flights:
                if price[s] == float("inf"):
                    continue
                if price[s] + p < tmpPrices[d]:
                    tmpPrices[d] = price[s] + p
            price = tmpPrices
        return -1 if price[dst] == float("inf") else price[dst]


if __name__ == "__main__":
    obj = Solution()
    n = 4
    flights = [[0, 1, 100], [1, 2, 100], [2, 0, 100], [1, 3, 600], [2, 3, 200]]
    src = 0
    dst = 3
    k = 1
    print(obj.findCheapestPrice(n,flights, src, dst, k))
    n = 3
    flights = [[0, 1, 100], [1, 2, 100], [0, 2, 500]]
    src = 0
    dst = 2
    k = 1
    print(obj.findCheapestPrice(n,flights, src, dst, k))
