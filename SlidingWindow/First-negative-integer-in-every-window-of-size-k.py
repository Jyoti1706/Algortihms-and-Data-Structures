"""
https://www.youtube.com/watch?v=-uc7OCrjp8g&list=PLpIkg8OmuX-J2Ivo9YdY7bRDstPPTVGvN
"""
import collections


def firstNegativeElement(array, window):
    i = 0
    j = 0
    queue = collections.deque()
    res=[]
    while j <len(array):
        if array[j]<0:
            queue.append(array[j])
        if j-i+1 == window:
            if queue:
                res.append(queue[0])
                if array[i] == queue[0]:
                    queue.popleft()
            else:
                res.append(0)
            i += 1
        j += 1
    return res


array = [8, 1, -2, 2, -3, 6, 8, -1,5,4,6]
k=3
print(firstNegativeElement(array,k))
