from bisect import bisect_left, bisect_right


def binary_search(arr, target):
    l, r = 0, len(arr) - 1

    # RI: 
    # 1. target is not in slices outside of arr[l:r+1], i.e. -arr[l:r+1]
    # 2. [l:r+1] must shrink
    while l <= r:
        m = (l + r) // 2
        if arr[m] == target:
            return m
        if arr[m] < target:
            l = m + 1
        else:
            r = m - 1
    # l > r, arr[l:r+1] is empty. -arr[l:r+1] == arr. 
    # => target is not found in arr
    return -1


a = binary_search([1, 2, 3], 3)
print(a)
b = binary_search([1, 2, 3], 0)
print(b)
c = binary_search([1, 2, 3], 1)
print(c)
d = bisect_left([1, 2, 3], 3)
print(d)
d = bisect_right([1, 2, 3], 3)
print(d)
