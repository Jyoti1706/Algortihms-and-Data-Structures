import heapq


class Solution:
    def longestDiverseString1(self, a: int, b: int, c: int) -> str:
        maxheap = []
        if a:
            maxheap.append((-a,"a"))
        if b:
            maxheap.append((-b,"b"))
        if c:
            maxheap.append((-c,"c"))
        heapq.heapify(maxheap)
        prev = None

        res = ""
        while maxheap or prev:
            print(prev)
            if not maxheap and prev:
                if prev[0]==-1 and res[-2] != res[-1]:
                    res +=prev[0]
                break
            cnt, chr = heapq.heappop(maxheap)
            if abs(cnt)>1:
                res += (chr*2)
                cnt += 2
            elif abs(cnt)==1:
                res += chr
                cnt += 1
            else:
                pass
            if prev:
                heapq.heappush(maxheap, prev)
                prev = None
            if cnt != 0:
                prev = (cnt, chr)
        return res

    def longestDiverseString(self, a: int, b: int, c: int) -> str:
        res,maxheap = "",[]
        for count, char in [(-a,"a"),(-b,"b"),(-c,"c")]:
            #print(count, char)
            if count != 0:
                heapq.heappush(maxheap,(count,char))
        while maxheap:
            cnt, chr = heapq.heappop(maxheap)
            #print(cnt, chr)
            if len(res)>1 and res[-1]==res[-2]==chr:
                if not maxheap:
                    break
                cnt2, chr2 = heapq.heappop(maxheap)
                res += chr2
                cnt2 += 1
                if cnt2:
                    heapq.heappush(maxheap,(cnt2,chr2))
            else:
                res += chr
                cnt += 1
            if cnt:
                heapq.heappush(maxheap, (cnt, chr))
        return res



a=0
b=9
c=12
obj = Solution()
print(obj.longestDiverseString(a,b,c))
