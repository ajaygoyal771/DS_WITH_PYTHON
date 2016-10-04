# Python program for implementation of QuickSort
def part(arr,low,high):
    i=low-1
    pivot=arr[high]
    for j in range(low,high):
        if arr[j]<=pivot:
            i=i+1
            arr[i],arr[j]=arr[j],arr[i]
    arr[i+1],arr[high]=arr[high],arr[i+1]
    return i+1

def quicksort(arr,low,high):
    if low < high :
        pi=part(arr,low,high)
        quicksort(arr,low,pi-1)
        quicksort(arr,pi+1,high)
# Driver code to test above
arr = [12, 11, 13, 5, 6, 7]
n = len(arr)
print("Given array is")
for i in range(n):
    print("%d" % arr[i]),

quicksort(arr,0,n-1)
print("\n\nSorted array is")
for i in range(n):
    print("%d" % arr[i]),
