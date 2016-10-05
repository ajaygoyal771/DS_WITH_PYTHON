# Python program for implementation of longest unsorted array in an array after which it will be sorted
def unsorted(list1):
    n=len(list1)
    s=0
    e=n-1
    for s in range(n-1):
        if list1[s]>list1[s+1]:
            break
    if s==n-1:
        print("The array is completely sorted")
        return
    for e in range(n-1,0,-1):
        if list1[e]<list1[e-1]:
            break
    max=list1[s]
    min=list1[s]
    for i in range(s+1,e+1):
        if list1[i]>max:
            max=list1[i]
        if list1[i]<min:
            min=list1[i]
    for i in range(s):
        if list1[i]>min:
            s=i
            break
    for i in range(n-1,e,-1):
        if list1[i]<max:
            e=i
            break
    print("The unsorted array lies in between indexex",s,"and",e,".")
    return
# Driver code to test above
arr = [12, 11, 13, 5, 6, 7]
n = len(arr)
print("Given array is")
for i in range(n):
    print("%d" % arr[i]),

unsorted(arr)
print("\n\nSorted array is")
for i in range(n):
    print("%d" % arr[i]),
