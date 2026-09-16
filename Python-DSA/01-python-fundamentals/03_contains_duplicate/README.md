# Contains Duplicate

## Problem

Given a list of integers, determine whether any value appears at least
twice.

Return `True` if a duplicate exists and `False` if all elements are distinct.

This problem is based on [LeetCode #217 - Contains Duplicate](https://leetcode.com/problems/contains-duplicate/).

## Examples

### Example 1

Input:

[1, 2, 3, 1]

Output:

True

### Example 2

Input:

[1, 2, 3, 4]

Output:

False

## Initial Approach

The first approach that came to mind was to use Python's built-in `set()`.

Since a set only stores unique values, we can compare the length of the
original list with the length of the set.

If the lengths are different, at least one duplicate was removed while
creating the set.

```python
len(num) != len(set(num))