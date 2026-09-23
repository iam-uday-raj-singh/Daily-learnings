# Group Anagrams

**LeetCode #49 — Group Anagrams**

## 1. Problem

Given an array of strings, group the strings that are anagrams of each other.

Anagrams contain the same characters with the same frequencies, but the characters can appear in a different order.

The order of the resulting groups does not matter.

---

## 2. Example

### Example 1

**Input:**

`["eat", "tea", "tan", "ate", "nat", "bat"]`

**Output:**

`[["eat", "tea", "ate"], ["tan", "nat"], ["bat"]]`

The words `eat`, `tea`, and `ate` are anagrams of each other.

Similarly, `tan` and `nat` are anagrams.

`bat` does not have any other anagram in the input.

### Example 2

**Input:**

`["abc", "bca", "cab", "dog"]`

**Output:**

`[["abc", "bca", "cab"], ["dog"]]`

---

## 3. Initial Thinking

The previous problem, **Valid Anagram**, involved finding whether two strings have the same character frequencies.

For this problem, I extended that idea to multiple strings.

The key observation was that anagrams can be converted into the same representation by sorting their characters.

For example:

`eat` → `aet`

`tea` → `aet`

`ate` → `aet`

Since all three words produce the same sorted representation, they can be placed in the same group.

I can therefore use the sorted version of each word as a key in a dictionary.

---

## 4. Approach

Use a dictionary where:

- The **key** is the sorted version of a word.
- The **value** is a list containing all words that have that same sorted representation.

For each word:

1. Sort its characters.
2. Convert the sorted characters back into a string.
3. Use this string as the dictionary key.
4. Add the original word to the corresponding list.

For example:

`eat` → `aet`

`tea` → `aet`

`ate` → `aet`

This produces a dictionary conceptually like:

`aet → ["eat", "tea", "ate"]`

Similarly:

`tan` → `ant`

`nat` → `ant`

which produces:

`ant → ["tan", "nat"]`

Finally, the dictionary values represent the required groups.

A `defaultdict(list)` is used so that a new empty list is automatically created when a sorted key is encountered for the first time.

---

## 5. Complexity

Let:

- `n` = number of strings
- `k` = maximum length of a string

### Time Complexity

For each string, the characters are sorted.

Sorting a string of length `k` takes:

`O(k log k)`

For `n` strings:

**Time Complexity: O(n × k log k)**

### Space Complexity

The dictionary stores the grouped input strings and the sorted keys.

**Space Complexity: O(n × k)**

This includes the space required to store the grouped strings and their keys.

---

## 6. Edge Cases Considered

- **Standard input**

  `["eat", "tea", "tan", "ate", "nat", "bat"]`

- **All words are anagrams**

  `["abc", "bca", "cab", "acb"]`

- **No anagrams**

  `["dog", "cat", "sun"]`

- **Single word**

  `["hello"]`

- **Empty input**

  `[]`

- **Duplicate words**

  `["eat", "eat", "tea", "ate"]`

- **Repeated characters**

  `["aabb", "baba", "abba", "baab"]`

- **Different word lengths**

  `["a", "ab", "ba", "abc", "cab"]`

- **Single-character words**

  `["a", "b", "a", "c", "b"]`

- **Uppercase and lowercase characters**

  `["Eat", "Tea", "eat", "ate"]`

The important property across these cases is that strings are grouped together only when they contain the **same characters with the same frequencies**.