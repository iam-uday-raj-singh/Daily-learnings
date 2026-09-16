# Best Time to Buy and Sell Stock

## Problem

Given an array of stock prices where `prices[i]` represents the price
of a stock on the `i-th` day, find the maximum profit that can be
achieved by buying on one day and selling on a later day.

Only one transaction is allowed.

If no profitable transaction is possible, return `0`.

This problem is based on [LeetCode #121 - Best Time to Buy and Sell Stock](https://leetcode.com/problems/best-time-to-buy-and-sell-stock/).

## Examples

### Example 1

Input:

[7, 1, 5, 3, 6, 4]

Output:

5

The maximum profit is achieved by buying at `1` and selling at `6`.

### Example 2

Input:

[7, 6, 4, 3, 1]

Output:

0

Since the price continuously decreases, no profitable transaction
is possible.

## Initial Thinking

The key question is:

> If today is the selling day, what is the best price at which I could
> have bought the stock before today?

For every price, I only need to remember the lowest price encountered
so far.

This allows the maximum possible profit to be calculated while
traversing the list only once.

## Approach

Maintain two variables:

- `buy` - the lowest stock price encountered so far
- `profit` - the maximum profit found so far

For every price:

1. If the current price is lower than `buy`, update `buy`.
2. Otherwise, calculate the profit from selling at the current price.
3. If the current profit is greater than the previously recorded
   `profit`, update `profit`.

At the end of the traversal, return `profit`.

This avoids checking every possible combination of buying and selling
days.

## Alternative Approach

### Brute Force

A brute-force solution could compare every possible buying day with
every later selling day and calculate the profit for each combination.

This would require nested loops.

- Time: O(n²)
- Space: O(1)

### Optimized One-Pass Approach

The implemented solution keeps track of the minimum price seen so far
and calculates the potential profit for each subsequent price.

- Time: O(n)
- Space: O(1)

## Complexity

For the implemented solution:

- Time: O(n)
- Space: O(1)

The list is traversed only once and only two variables are maintained,
regardless of the input size.

## Edge Cases Considered

The solution handles:

- Empty list
- Single price
- Two prices with a profit
- Two prices with no profit
- Continuously decreasing prices
- Continuously increasing prices
- Equal prices
- Minimum price occurring in the middle
- Maximum profit occurring before the final element
- Multiple possible buy/sell opportunities

## Testing

Test cases are included in `test_solution.py`.

The test suite covers normal cases as well as edge cases, including
empty input, a single price, decreasing prices, equal prices, and
multiple possible transactions.

All test cases passed successfully.

```text
All tests passed!