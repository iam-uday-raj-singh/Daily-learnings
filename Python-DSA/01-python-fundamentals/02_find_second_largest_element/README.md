# Find the Second Largest Number

## Problem

Given a list of integers, find the second largest distinct number
without using Python's built-in `max()` function.

## Example

Input:

[10, 5, 8, 20, 15]

Output:

15

## Approach

### Initial approach

The initial idea was to first find the largest element, remove it,
and then find the largest element again. This would give the second
largest element.

Although this works, it requires modifying the list and performing
another search.

### Optimized approach

Maintain two variables while traversing the list:

- `largest` — the largest value encountered so far
- `second_largest` — the second largest distinct value encountered so far

For each number:

1. If it is larger than `largest`, the previous `largest` becomes
   `second_largest`.
2. If it is smaller than `largest` but larger than `second_largest`,
   it becomes the new `second_largest`.
3. Duplicate values of `largest` are ignored.

This allows the problem to be solved in a single traversal.

## Complexity

- Time: O(n)
- Space: O(1)

## Key Learning

My initial approach was to initialize the first two elements as
`largest` and `second_largest` and then handle several edge cases
separately. This made the code increasingly complicated, especially
when dealing with duplicate values.

I then reconsidered the problem and simplified the approach by
maintaining `largest` and `second_largest` while traversing the list.

The overall time complexity remains O(n), but the final solution
requires only a single traversal and handles the edge cases more cleanly.

## Testing

Test cases are included in `test_solution.py` covering:

- Normal input
- Duplicate largest values
- Duplicate second-largest values
- Negative numbers
- Two-element lists
- No distinct second-largest element
- Single-element input