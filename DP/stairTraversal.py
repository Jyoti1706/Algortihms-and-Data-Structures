def staircaseTraversal(heights, maxstep):
    # Write your code here.
    arr = [0, ] * (heights+1)
    arr[0] = 1
    arr[1] = 1
    i = 2
    curr_sum = 2
    while i <= maxstep:
        arr[i] = curr_sum
        curr_sum = curr_sum + arr[i]
        i = i + 1

    while i <= heights:
        step_sum = 0
        j = 1
        while j <= maxstep:
            step_sum = step_sum + arr[i - j]
            j = j + 1
        arr[i] = step_sum
        i = i + 1
    print(arr)
    return arr[-1]

height = 6
maxstep = 3

print(staircaseTraversal(height,maxstep))
height = 6
maxstep = 3

print(staircaseTraversal(4,2))

