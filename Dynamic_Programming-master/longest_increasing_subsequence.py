def LIS(arr):
    length = len(arr)
    if length == 1:
        return 1
    res_arr = [int(1)] * length
    ans = 1
    for i in range(length):
        for j in range(i):
            if arr[j] < arr[i]:
                res_arr[i] = max(res_arr[i], res_arr[j] + 1)
        ans = max(ans,res_arr[i])
    print(res_arr)
    return ans

arr = [10, 22, 9, 33, 21, 50, 41, 60]
print(LIS(arr))
