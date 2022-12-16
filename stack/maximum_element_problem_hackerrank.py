'''

You have an empty sequence, and you will be given N queries. Each query is one of these three types:

1 x  -Push the element x into the stack.
2    -Delete the element present at the top of the stack.
3    -Print the maximum element in the stack.
Function Description

Complete the getMax function in the editor below.

getMax has the following parameters:
- string operations[n]: operations as strings

Returns
- int[]: the answers to each type 3 query

sampletest case: STDIN   Function
-----   --------
10      operations[] size n = 10
1 97    operations = ['1 97', '2', '1 20', ....]
2
1 20
2
1 26
1 20
2
3
1 91
3

Sample Output
------------------
26
91

'''


import os


max_stack = []
stack = []
output = []


def getMax(operations):
    # Write your code here

    for ops in operations:
        ops = ops.split()
        ops = list(map(int, ops))
        if ops[0] == 1:
            stack.append(ops[1])
            if max_stack:
                max_stack.append(max(ops[1], max_stack[-1]))
            else:
                max_stack.append(ops[1])
        elif ops[0] == 2:
            stack.pop()
            max_stack.pop()
        else:
            if max_stack:
                output.append(max_stack[-1])
    return output


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    ops = []

    for _ in range(n):
        ops_item = input()
        ops.append(ops_item)

    res = getMax(ops)

    fptr.write('\n'.join(map(str, res)))
    fptr.write('\n')

    fptr.close()
