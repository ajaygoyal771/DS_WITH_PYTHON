import math
def mincost(L,m,n):
    if n < 0 or m < 0:
        return math.inf
    if n==0 and m==0:
        return L[m][n]
    else:
        return L[m][n]+min(mincost(L,m-1,n-1),mincost(L,m-1,n),mincost(L,m,n-1))


# end of function mincost


# Driver program to test the above function
print("Enter the value of m")
m=int(input())
print("Enter the value of n")
n=int(input())
L = [[None] * (n + 1) for i in range(m + 1)]
for i in range(m):
    for j in range(n):
        x=int(input())
        L[i][j]=x
print("Minimum cost is:",mincost(L,2,2))

