def merge_intervals(intervals):
    if not intervals:
        return []

    intervals.sort()
    merged = [intervals[0]]

    for interval in intervals:
        if interval[0] <= merged[-1][1]:
            merged[-1] = (merged[-1][0], max(merged[-1][1], interval[1]))
        else:
            merged.append(interval)

    return merged

def test_merge_intervals():
    # Test 1
    intervals1 = [(1, 3), (2, 6), (8, 10), (15, 18)]
    expected1 = [(1, 6), (8, 10), (15, 18)]
    assert merge_intervals(intervals1) == expected1

    # Test 2
    intervals2 = [(1, 4), (4, 5)]
    expected2 = [(1, 5)]
    assert merge_intervals(intervals2) == expected2

test_merge_intervals()