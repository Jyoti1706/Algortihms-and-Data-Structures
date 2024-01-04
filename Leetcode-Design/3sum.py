nums = [-2,0,0,2,2]

#bruteForce

def bruteforce(nums):
    i=0
    results=set()
    while i< len(nums):
        j=i+1
        while j<len(nums):
            k=j+1
            while k <len(nums):
                if nums[i]+nums[j]+nums[k] == 0:
                    pair = tuple(sorted((nums[i],nums[j],nums[k])))
                    #print(pair)
                    results.add(pair)
                k=k+1
            j=j+1
        i=i+1
    return list(results)


def triplesum2zeros(arr):
    visited=set()
    arr.sort()
    results=set()
    for i in range(len(arr)):
        if arr[i] in visited:
            continue
        else:
            visited.add(arr[i])
            j=i+1
            k=len(arr)-1
            required_sum = 0 - arr[i]
            while j<k:
                curr_sum = arr[j]+arr[k]
                if curr_sum<required_sum:
                    j=j+1
                elif curr_sum > required_sum:
                    k=k-1
                else:
                    results.add(tuple(sorted((arr[i], arr[j], arr[k]))))
                    j=j+1
                    k=k-1
    return results
print(nums)
print(triplesum2zeros(nums))