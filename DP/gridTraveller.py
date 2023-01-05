dp={}
def gridTraveler(m,n, dp):
    if m==0 or n==0:
        return 0
    if m==1 and n==1:
        return 1
    try:
        return dp[(m,n)]
    except:
        dp[(m,n)]= gridTraveler(m-1,n,dp)+ gridTraveler(m,n-1,dp)
    return dp[(m,n)]

print(gridTraveler(4,3,dp))
print(gridTraveler(2,3,dp))
print(gridTraveler(3,2,dp))
print(gridTraveler(3,3,dp))
print(gridTraveler(18,18,dp))