from solution import find_second_largest_element


assert find_second_largest_element([10, 5, 8, 20, 15]) == 15

assert find_second_largest_element([10, 20, 20, 5]) == 10

assert find_second_largest_element([5, 5, 4]) == 4

assert find_second_largest_element([10, 8, 8, 5]) == 8

assert find_second_largest_element([-10, -5, -20, -3]) == -5

assert find_second_largest_element([42, 10]) == 10

assert find_second_largest_element([5, 5, 5]) == "There is no distinctive second largest element"

assert find_second_largest_element([5]) == "There is no distinctive second largest element"


print("All tests passed!")