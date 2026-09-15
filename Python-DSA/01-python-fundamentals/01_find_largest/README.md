# Find the Largest Number

## Problem

Given a list of integers, find the largest number without using the in-built max() function in python.

## Examples

#Input:
[4,7,9,1,3]

#Output:
9

## Approach
First, brute force approach:
 
## Complexity
Time :  O(n)
Space : O(1)

## Key Learning
Earlier, I jumped directly to brute force approach and started comparing each element with the other element.
But, when put my mind, I realised that if we initialise the first variable as largest and then just compare each variable one by one across array, it would give the same result but in much more efficient way. 
Time complexity reduced from O(n square) to O(n).

Have added the edge cases inside the test_solution.py

##
Feel free to add additional edge cases if you think of any inside the test solution.

