def minSubArrayLen(target, nums):
    i=0
    j=0
    sum=0
    output=len(nums)+1
    while i < len(nums):
        while j < len(nums) and sum < target:
            sum = nums[j]+sum
            j=j+1
        if sum >= target:
            array_len = j-i
            output=min(array_len,output)
        sum=sum-nums[i]
        i=i+1
    if output == len(nums)+1:
        return 0
    return output

# target = 7
# nums = [2,3,1,2,4,3]
# print(minSubArrayLen(target,nums))
#
# target = 4
# nums = [1,4,4]
# print(minSubArrayLen(target,nums))

target = 11
nums = [1,2,3,4,5]
print(minSubArrayLen(target,nums))