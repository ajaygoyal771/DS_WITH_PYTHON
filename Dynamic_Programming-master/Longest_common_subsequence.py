#Recursive approach for longest common subsequence
def LCS(str1,str2,m,n):
    if n==0 or m==0:
        return 0
    if str1[m-1]==str2[n-1]:
        return 1 + LCS(str1,str2,m-1,n-1)
    else:
        return max(LCS(str1,str2,m-1,n),LCS(str1,str2,m,n-1))
def main():
    print("Enter the string 1")
    str1=input()
    m=len(str1)
    print("Enter the string 2")
    str2=input()
    n=len(str2)
    print(LCS(str1,str2,m,n))
main()
