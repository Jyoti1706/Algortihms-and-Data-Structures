"""
https://leetcode.com/problems/task-scheduler/

Given a characters array tasks, representing the tasks a CPU needs to do, where each letter represents a different task. Tasks could be done in any order. Each task is done in one unit of time. For each unit of time, the CPU could complete either one task or just be idle.

However, there is a non-negative integer n that represents the cooldown period between two same tasks (the same letter in the array), that is that there must be at least n units of time between any two same tasks.

Return the least number of units of times that the CPU will take to finish all the given tasks.



Example 1:

Input: tasks = ["A","A","A","B","B","B"], n = 2
Output: 8
Explanation:
A -> B -> idle -> A -> B -> idle -> A -> B
There is at least 2 units of time between any two same tasks.
Example 2:

Input: tasks = ["A","A","A","B","B","B"], n = 0
Output: 6
Explanation: On this case any permutation of size 6 would work since n = 0.
["A","A","A","B","B","B"]
["A","B","A","B","A","B"]
["B","B","B","A","A","A"]
...
And so on.
Example 3:

Input: tasks = ["A","A","A","A","A","A","B","C","D","E","F","G"], n = 2
Output: 16
Explanation:
One possible solution is
A -> B -> C -> A -> D -> E -> A -> F -> G -> A -> idle -> idle -> A -> idle -> idle -> A

"""
import heapq
from collections import Counter
class Solution:
    def leastInterval(self, tasks, n ):
        maxheap =[]
        task = dict(Counter(tasks))
        time = 0
        print(task)
        for v in task.values():
            heapq.heappush(maxheap, -1*v)
        queue = []
        while maxheap or queue:
            time += 1
            if maxheap:
                cur = heapq.heappop(maxheap)+1
                if cur:
                    queue.append([cur, time+n])
            if queue and queue[0][1] == time:
                heapq.heappush(maxheap,queue.pop(0)[0])
        return time

    def scheduler(self, task,n ):
        count = Counter(task)
        maxheap = [-c for c in count.values()]
        heapq.heapify(maxheap)
        time = 0
        queue = []
        while maxheap or queue:
            time += 1
            if maxheap:
                curr = heapq.heappop(maxheap)+1
                if curr != 0:
                    queue.append([curr, time + n])
            if queue and queue[0][1]== time:
                heapq.heappush(maxheap, queue.pop(0)[0])

        return time


tasks = ["A","A","A","A","A","A","B","C","D","E","F","G"]
n = 2

obj = Solution()
print(obj.leastInterval(tasks,n))
print(obj.scheduler(tasks,n))



