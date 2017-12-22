def binomial(m,n):
    L = [[0] * (n + 1) for i in range(m + 1)]
    for i in range(m+1):
        for j in range(min(i,n)+1):
            if j==0 or j==i:
                L[i][j]=1
            else:
                L[i][j]=L[i-1][j-1]+L[i-1][j]
    return L[m][n]

print("Enter the value of m")
m=int(input())
print("Enter the value of n")
n=int(input())
print("The value is",binomial(m,n))
