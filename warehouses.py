from bisect import bisect_left


def warehouses(centers, d):
    n = len(centers)
    centers.sort()  # n*log(n)
    prefix_sums = [0] * (n + 1)
    for i, c in enumerate(centers):
        prefix_sums[i + 1] = prefix_sums[i] + c

    # log(n)
    def distance(x):
        i = bisect_left(centers, x)
        left = x * i - prefix_sums[i]
        right = prefix_sums[-1] - prefix_sums[i] - x * (n - i)
        return left + right

    median = centers[n // 2]
    # left most x <= d
    i, j = -(10**9), median
    while i < j:
        m = (i + j) // 2
        if distance(m) > d:
            i = m + 1
        else:
            j = m
    left = i

    # right most x <= d
    i, j = median, 10**9
    while i < j:
        m = (i + j + 1) // 2
        if distance(m) > d:
            j = m - 1
        else:
            i = m

    return i - left + 1


print(warehouses([-2, 1, 0], 4))
print(warehouses([0], 0))