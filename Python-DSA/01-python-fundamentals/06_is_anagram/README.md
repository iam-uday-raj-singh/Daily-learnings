# Valid Anagram

**LeetCode #242 — Valid Anagram**

## 1. Problem

Given two strings `s` and `t`, determine whether `t` is an anagram of `s`.

An anagram contains the same characters with the same frequency, but the characters can appear in a different order.

Return `True` if the two strings are anagrams; otherwise, return `False`.

---

## 2. Example

### Example 1

**Input:**

`s = "anagram"`

`t = "nagaram"`

**Output:**

`True`

Both strings contain the same characters with the same frequencies.

### Example 2

**Input:**

`s = "rat"`

`t = "car"`

**Output:**

`False`

The strings do not contain the same characters.

---

## 3. Initial Thinking

The first thought was to capture each character and its frequency.

A hash map is suitable for this because Python dictionaries can store a character as a key and its frequency as the corresponding value.

For example:

`"anagram"`

can be represented as:

`{"a": 3, "n": 1, "g": 1, "r": 1, "m": 1}`

The idea is to build the frequency of the characters in `s` and then use `t` to reduce those frequencies.

If both strings are anagrams, every character frequency should eventually become `0`.

An important edge case is that the two strings must have the same length. If their lengths are different, they cannot be anagrams.

---

## 4. Approach

The solution uses a single frequency dictionary.

### Step 1: Check Length

First, compare the lengths of `s` and `t`.

If the lengths are different, immediately return `False`.

### Step 2: Build Character Frequency

Traverse `s` and store the frequency of every character in a dictionary.

For example:

`s = "aab"`

produces:

`{"a": 2, "b": 1}`

### Step 3: Subtract Frequencies

Traverse `t`.

For every character that exists in the frequency dictionary, decrease its frequency by `1`.

For example:

`s = "aab"`

`t = "baa"`

After processing `t`, all frequencies become:

`{"a": 0, "b": 0}`

### Step 4: Check Frequencies

If every frequency is `0`, the two strings contain exactly the same characters with exactly the same frequencies.

Therefore, they are anagrams.

Python's `all()` function can be used to check whether every frequency is equal to `0`.

---

## 5. Complexity

### Time Complexity

**O(n)**

The string `s` is traversed once to build the frequency dictionary, and `t` is traversed once to subtract the frequencies.

Therefore:

`O(n) + O(n) = O(n)`

Overall time complexity:

**O(n)**

where `n` is the length of the strings.

### Space Complexity

**O(k)**

The frequency dictionary stores each distinct character.

Here, `k` represents the number of distinct characters.

For a fixed character set, this can effectively be considered **O(1)** auxiliary space.

---

## 6. Edge Cases Considered

- **Standard anagram**

  `"anagram"` → `"nagaram"` → `True`

- **Not an anagram**

  `"rat"` → `"car"` → `False`

- **Same characters in different order**

  `"listen"` → `"silent"` → `True`

- **Same string**

  `"hello"` → `"hello"` → `True`

- **Different lengths**

  `"abc"` → `"ab"` → `False`

- **Both strings empty**

  `""` → `""` → `True`

- **One empty string**

  `""` → `"a"` → `False`

- **Single character**

  `"a"` → `"a"` → `True`

- **Different single characters**

  `"a"` → `"b"` → `False`

- **Repeated characters**

  `"aabbcc"` → `"abcabc"` → `True`

- **Different character frequencies**

  `"aab"` → `"abb"` → `False`

- **Character exists in `t` but not in `s`**

  `"aab"` → `"aac"` → `False`

- **Uppercase and lowercase characters**

  `"Anagram"` → `"anagram"` → `False`

- **Numbers as characters**

  `"112233"` → `"332211"` → `True`

- **Spaces**

  `"a b"` → `"b a"` → `True`

- **Special characters**

  `"a!b@"` → `"@ba!"` → `True`

The important property across these cases is that the two strings must contain **exactly the same characters with exactly the same frequencies**.