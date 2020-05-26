'''
Created on Aug 9, 2018

@author: kumarijy
'''
def HCF(x, y):

   # This function implements the Euclidian algorithm to find H.C.F. of two numbers
   while(y):
       x, y = y, x % y

   return x

def gcd(x, y):
   """This function implements the Euclidian algorithm
   to find G.C.D. of two numbers"""

   while(y):
       x, y = y, x % y

   return x

# define lcm function
def lcm(x, y):
   """This function takes two
   integers and returns the L.C.M."""

   lcm = (x*y)//gcd(x,y)
   return lcm

n = int(input())
for i in range(0,n):
    arr = list(map(int, input().rstrip().split()))
    print(lcm(arr[0],arr[1]),HCF(arr[0],arr[1]))