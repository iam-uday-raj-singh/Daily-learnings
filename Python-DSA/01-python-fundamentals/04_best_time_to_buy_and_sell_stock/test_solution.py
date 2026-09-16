from solution import best_time_to_buy_and_sell_stock


# 1. Normal case
assert best_time_to_buy_and_sell_stock([7, 1, 5, 3, 6, 4]) == 5

# 2. Prices continuously decrease
assert best_time_to_buy_and_sell_stock([7, 6, 4, 3, 1]) == 0

# 3. Empty list
assert best_time_to_buy_and_sell_stock([]) == 0

# 4. Only one price
assert best_time_to_buy_and_sell_stock([5]) == 0

# 5. Two prices - profitable
assert best_time_to_buy_and_sell_stock([1, 5]) == 4

# 6. Two prices - no profit
assert best_time_to_buy_and_sell_stock([5, 1]) == 0

# 7. Lowest price occurs in the middle
assert best_time_to_buy_and_sell_stock([7, 6, 1, 5, 3, 6]) == 5

# 8. Best profit occurs before the final element
assert best_time_to_buy_and_sell_stock([1, 5, 3, 2, 4]) == 4

# 9. Prices remain constant
assert best_time_to_buy_and_sell_stock([5, 5, 5, 5]) == 0

# 10. Multiple possible transactions - only one transaction is allowed
assert best_time_to_buy_and_sell_stock([3, 2, 6, 5, 0, 3]) == 4


print("All tests passed!")