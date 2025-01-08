def three_sum(arr: list, target):
    arr += [-10_000, 10_000]
    arr.sort()
    res = []
    # RI:
    # 1. res contains triples where the 1st value is in arr[:i]
    for i, iv in enumerate(arr):
        if i == 0 or iv == arr[i - 1]:
            continue
        tar_2 = target - iv

        j, k = i + 1, len(arr) - 2
        # RI:
        # 1. if tar_2 == arr[l] + arr[r], then j <= l < r <= k
        while j < k:
            if arr[j] == arr[j - 1]:
                j += 1
                continue
            if arr[k] == arr[k + 1]:
                k -= 1
                continue
            sum_jk = arr[j] + arr[k]
            if sum_jk == tar_2:
                res.append((i, j, k))
                j += 1
                k -= 1
            elif sum_jk < tar_2:
                j += 1
            else:
                k -= 1
    # RI:
    # 1. i == len(arr), res continas triples where the 1st value is in arr
    return res


print(three_sum([1, 2, 3], 0))
print(three_sum([1, 2, 3], 6))
print(three_sum([1, 1, 2, 2, 3, 3], 6))
