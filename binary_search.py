def binary_search(arr, target):
    l, r = 0, len(arr)-1

    # RI: if target is in arr, it is within [l, r]
    while l <= r:
        m = (l+r)//2
        if arr[m] == target:
            return m
        if arr[m] < target:
            l = m+1
        else:
            r = m-1
    # l > r, [l, r] is empty. target is not found
    return -1


a = binary_search([1, 2, 3], 3)
print(a)
b = binary_search([1, 2, 3], 0)
print(b)
c = binary_search([1, 2, 3], 1)
print(c)