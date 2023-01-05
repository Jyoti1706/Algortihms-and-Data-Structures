def si_clockwise_rotation_of_array(nums,k):
    return nums[k+1:]+nums[:k+1]

tc = int(input())
for _ in range(tc):
    arr_size, k = list(map(int, input().rstrip().split()))
    nums = list(map(int, input().rstrip().split()))
    print(si_clockwise_rotation_of_array(nums,k))

