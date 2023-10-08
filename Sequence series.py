def count_changes_to_make_series(arr):
    n = len(arr)
    if n < 2:
        return 0
    changes = 0
    expected_series = [2, 1]
    for i in range(2, n):
        expected_next = expected_series[-1] + expected_series[-2]
        if arr[i] != expected_next:
            changes += 1
            arr[i] = expected_next
        expected_series.append(expected_next)
    return changes
n = int(input())
arr = list(map(int, input().split()))
changes_needed = count_changes_to_make_series(arr)
print(changes_needed)
