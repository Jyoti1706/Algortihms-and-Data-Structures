import math


class MedianFinder:

    def __init__(self):
        self.nums = []
        self.count = 0

    def addNum(self, num: int) -> None:
        appended = False
        if not self.nums:
            self.nums.append(num)
            appended = True
        else:
            #print(self.count)
            for i in range(self.count):
                #print(i)
                if num <= self.nums[i]:
                    self.nums = self.nums[:i]+[num,]+self.nums[i:]
                    appended = True
                    break
        if not appended:
            self.nums.append(num)

        self.count += 1


    def findMedian(self) -> float:
        mid = math.ceil(self.count / 2) -1
        print(f"self.nums:: {self.nums}, self.count:: {self.count}, mid: {mid}")
        if self.count % 2 == 0:
            return (self.nums[mid] + self.nums[mid - 1]) / 2
        else:
            return self.nums[mid]

input1 = ["MedianFinder","addNum","findMedian","addNum","findMedian","addNum","findMedian","addNum","findMedian","addNum","findMedian","addNum","findMedian","addNum","findMedian","addNum","findMedian","addNum","findMedian","addNum","findMedian","addNum","findMedian","addNum","findMedian","addNum","findMedian","addNum","findMedian","addNum","findMedian","addNum","findMedian","addNum","findMedian","addNum","findMedian","addNum","findMedian","addNum","findMedian","addNum","findMedian"]
input2 = [[],[12],[],[10],[],[13],[],[11],[],[5],[],[15],[],[1],[],[11],[],[6],[],[17],[],[14],[],[8],[],[17],[],[6],[],[4],[],[16],[],[8],[],[10],[],[2],[],[12],[],[0],[]]
obj = MedianFinder()
i = 1
for action in input1[1:]:
    if action == "addNum":
        obj.addNum(input2[i][0])
    if action == "findMedian":
        print(obj.findMedian())
    i += 1

