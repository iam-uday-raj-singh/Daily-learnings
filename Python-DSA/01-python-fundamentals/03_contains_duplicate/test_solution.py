from solution import contains_duplicate


assert contains_duplicate([1, 2, 3, 1]) == True
assert contains_duplicate([1, 2, 3, 4]) == False
assert contains_duplicate([1, 1, 2, 2, 3, 3]) == True
assert contains_duplicate([5, 5, 5, 5]) == True
assert contains_duplicate([42]) == False
assert contains_duplicate([]) == False
assert contains_duplicate([-1, -2, -3, -1]) == True
assert contains_duplicate([-1, -2, -3, -4]) == False
assert contains_duplicate([1, 2, 3, 4, 5, 5]) == True
assert contains_duplicate([10, 20, 30, 40, 50, 60, 70, 80, 90, 100]) == False


print("All tests passed!")