# Move Zeroes

**LeetCode #283 — Move Zeroes**

## 1. Problem

Given an integer array `nums`, move all `0`s to the end of the array while maintaining the relative order of the non-zero elements.

The operation must be performed **in-place**.

---

## 2. Example

### Example 1

**Input:**

`[0, 1, 0, 3, 12]`

**Output:**

`[1, 3, 12, 0, 0]`

### Example 2

**Input:**

`[0, 0, 1, 0, 3]`

**Output:**

`[1, 3, 0, 0, 0]`

The relative order of the non-zero elements should remain unchanged.

---

## 3. Initial Thinking

My initial approach was to compare adjacent elements.

If the current element was `0`, I would take the next element and move it into the current position while setting the next position to `0`.

However, this approach becomes problematic when there are multiple consecutive zeroes.

For example:

`[0, 0, 1]`

The `1` needs to move across multiple zeroes. This can result in repeatedly shifting elements and makes the approach more complicated.

Because of this, I changed the approach to use a separate `position` variable.

---

## 4. Approach

Use a variable `position` to keep track of where the next non-zero element should be placed.

The array is processed in two steps:

### Step 1: Move Non-Zero Elements

Traverse the array and place every non-zero element at the current `position`.

- `i` is used to scan the array.
- `position` determines where the next non-zero element should be placed.
- `position` is incremented only when a non-zero element is found.

This places all non-zero elements at the beginning of the array while preserving their relative order.

### Step 2: Fill Remaining Positions with Zeroes

After all non-zero elements have been placed, `position` points to the first position that should contain a zero.

Fill all remaining positions with zeroes.

For example:

`[0, 0, 1, 0, 3]`

After placing the non-zero elements, the relevant portion is:

`[1, 3, ...]`

Since there are two non-zero elements, the remaining positions are filled with zeroes:

`[1, 3, 0, 0, 0]`

This approach modifies the original array in-place and preserves the order of the non-zero elements.

---

## 5. Complexity

### Time Complexity

**O(n)**

The array is traversed twice:

- First pass: Place all non-zero elements.
- Second pass: Fill the remaining positions with zeroes.

Therefore:

`O(n) + O(n) = O(n)`

Overall time complexity:

**O(n)**

### Space Complexity

**O(1)**

No additional array or data structure is created.

The original array is modified in-place.

---

## 6. Edge Cases Considered

- **No zeroes**

  `[1, 2, 3, 4]` → `[1, 2, 3, 4]`

- **All zeroes**

  `[0, 0, 0, 0]` → `[0, 0, 0, 0]`

- **Zeroes at the beginning**

  `[0, 0, 1, 2]` → `[1, 2, 0, 0]`

- **Zeroes in the middle**

  `[1, 0, 0, 2, 3]` → `[1, 2, 3, 0, 0]`

- **Zeroes at the end**

  `[1, 2, 3, 0, 0]` → `[1, 2, 3, 0, 0]`

- **Single zero**

  `[0]` → `[0]`

- **Single non-zero element**

  `[5]` → `[5]`

- **Negative numbers**

  `[-1, 0, -2, 0, 3]` → `[-1, -2, 3, 0, 0]`

- **Duplicate non-zero elements**

  `[0, 2, 2, 0, 3, 2]` → `[2, 2, 3, 2, 0, 0]`

- **Multiple consecutive zeroes**

  `[0, 0, 1, 0, 0, 2]` → `[1, 2, 0, 0, 0, 0]`

The important property across all cases is that the **relative order of the non-zero elements is preserved**.