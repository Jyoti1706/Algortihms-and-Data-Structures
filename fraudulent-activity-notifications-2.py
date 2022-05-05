'''Count friquency approach
https://www.hackerrank.com/challenges/fraudulent-activity-notifications/problem?h_l=interview&playlist_slugs%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D=sorting
'''

def activityNotifications(expenditure, d):
    arr = expenditure[:d]
    max_ele = max(arr)
    count_arr = [0] * (max_ele+1)
    j =0
    for a in arr:
        count_arr[a] += 1
    if d%2 == 1:
        median = [(d // 2 + 1)-1,]
    else:
        median = [(d // 2)-1,((d // 2)+1)-1]
    sum = 0
    for i in range(d,len(expenditure))
        if len(median) == 1:
            k=0
            while sum < d:
                sum = sum+count_arr[k]
                k = k+1




