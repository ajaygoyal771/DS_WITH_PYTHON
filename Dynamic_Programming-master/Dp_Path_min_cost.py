def mincost(L,m,n):
    # find the length of the strings
    # declaring the array for storing the dp values

    """Following steps build L[m+1][n+1] in bottom up fashion
    Note: L[i][j] contains length of LCS of X[0..i-1]
    and Y[0..j-1]"""
    tc = [[0]*(n + 1) for i in range(m + 1)]
    tc[0][0]=L[0][0]
    for i in range(1,m + 1):
        tc[i][0]=tc[i-1][0]+L[i][0]
    for j in range(1,n + 1):
        tc[0][j]=tc[0][j-1]+L[0][j]
    for i in range(1,m+1):
        for j in range(1,n+1):
            tc[i][j]=min(tc[i-1][j-1],tc[i-1][j],tc[i][j-1])+L[i][j]


    # L[m][n] contains the length of LCS of X[0..n-1] & Y[0..m-1]
    return tc[m][n]


# end of function lcs


# Driver program to test the above function
print("Enter the value of m")
m=int(input())
print("Enter the value of n")
n=int(input())
L= [[None]*(n) for i in range(m)]
print("Enter the elements of matrix")
for i in range(m):
    for j in range(n):
        x=int(input())
        L[i][j]=x
print("Minimum Cost is",mincost(L,2,2))


