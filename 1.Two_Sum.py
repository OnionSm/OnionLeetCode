def binary_search(arr, n, x, i):
    left = i+1
    right = n - 1
    while left <= right:
        mid = left + (right - left) // 2
        print(mid)
        if arr[mid] == x:
            return mid
        elif arr[mid] < x:
            left = mid + 1
        else:
            right = mid - 1
    return -1
arr = [0,4,3,0]
print(binary_search(arr, 4, 0, 0))