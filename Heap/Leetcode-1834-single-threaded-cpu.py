import heapq
from typing import List


class Solution:
    def getOrder(self, tasks: List[List[int]]) -> List[int]:
        n = len(tasks)
        ind = 0
        result = []
        for i in tasks:
            i.append(ind)
            ind += 1
        tasks.sort()
        #tasks = sorted(tasks, key=lambda x: (x[0], x[2]))
        # print(tasks)
        heap = []
        heapq.heapify(heap)
        current = tasks[0][0]
        i = 0
        while i < n and tasks[i][0] == current:
            heapq.heappush(heap, [tasks[i][1], tasks[i][2]])
            i += 1

        while heap or (i < n):

            while i < n and tasks[i][0] <= current:
                heapq.heappush(heap, [tasks[i][1], tasks[i][2]])
                i += 1
            # add tasks when heap is empty as current processed time < next task start time
            while not heap and i < n:
                # take only 1 start time and add all task to heap which start at same start time
                current_temp = tasks[i][0]
                current += tasks[i][0]   # way to add idle time
                while i < n and tasks[i][0] == current_temp:
                    heapq.heappush(heap, [tasks[i][1], tasks[i][2]])
                    i += 1
            process_time, idx = heapq.heappop(heap)
            result.append(idx)
            current += process_time
        print(result)
        return result


if __name__ == "__main__":
    obj = Solution()
    tasks = [[1, 2], [2, 4], [3, 2], [4, 1]]
    print(obj.getOrder(tasks) == [0,2,3,1])  # [0,2,3,1]
    tasks = [[7, 10], [7, 12], [7, 5], [7, 4], [7, 2]]
    print(obj.getOrder(tasks) == [4,3,2,0,1])
    tasks = [[5, 2], [7, 2], [9, 4], [6, 3], [5, 10], [1, 1]]
    print(obj.getOrder(tasks) == [5,0,1,3,2,4])
    tasks = [[7,1],[6,3],[1,3]]
    print(obj.getOrder(tasks) == [2,1,0])
    tasks = [[5, 6], [9, 4], [3, 9], [3, 7], [1, 1], [6, 9], [9, 1]]
    print(f"Expected : {[4,3,6,1,0,2,5]}")
    print(obj.getOrder(tasks))
