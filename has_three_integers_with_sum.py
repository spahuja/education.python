def has_three_integers_with_sum(arr, target):
    arr.sort()
    n = len(arr)
    for i in range(n - 2):
        left = i + 1
        right = n - 1
        while left < right:
            curr_sum = arr[i] + arr[left] + arr[right]
            if curr_sum == target:
                return True
            elif curr_sum < target:
                left += 1
            else:
                right -= 1
    return False

arr1 = [13,51,524,11,533,11,5,13,1,1]
val1 = 40

def test_has_three_integers_with_sum():
    arr1 = [1,3,5,9,11,1,3,5,6]
    val1 = 9
    assert has_three_integers_with_sum(arr1, val1) == True

    arr2 = [1,3,2,5,9,15,10]
    val2 = 100
    assert has_three_integers_with_sum(arr2, val2) == False

test_has_three_integers_with_sum()