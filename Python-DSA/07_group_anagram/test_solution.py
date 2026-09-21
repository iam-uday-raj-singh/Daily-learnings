from solution import group_anagram


def normalize(result):
    return sorted([sorted(group) for group in result])


def test_group_anagram():
    # Standard case
    result = group_anagram(["eat", "tea", "tan", "ate", "nat", "bat"])
    expected = [["eat", "tea", "ate"], ["tan", "nat"], ["bat"]]

    assert normalize(result) == normalize(expected)

    # All words are anagrams
    result = group_anagram(["abc", "bca", "cab", "acb"])
    expected = [["abc", "bca", "cab", "acb"]]

    assert normalize(result) == normalize(expected)

    # No anagrams
    result = group_anagram(["dog", "cat", "sun"])
    expected = [["dog"], ["cat"], ["sun"]]

    assert normalize(result) == normalize(expected)

    # Single word
    result = group_anagram(["hello"])
    expected = [["hello"]]

    assert normalize(result) == normalize(expected)

    # Empty input
    result = group_anagram([])
    expected = []

    assert normalize(result) == normalize(expected)

    # Duplicate words
    result = group_anagram(["eat", "eat", "tea", "ate"])
    expected = [["eat", "eat", "tea", "ate"]]

    assert normalize(result) == normalize(expected)

    # Words with repeated characters
    result = group_anagram(["aabb", "baba", "abba", "baab"])
    expected = [["aabb", "baba", "abba", "baab"]]

    assert normalize(result) == normalize(expected)

    # Different word lengths
    result = group_anagram(["a", "ab", "ba", "abc", "cab"])
    expected = [["a"], ["ab", "ba"], ["abc", "cab"]]

    assert normalize(result) == normalize(expected)

    # Single-character words with duplicates
    result = group_anagram(["a", "b", "a", "c", "b"])
    expected = [["a", "a"], ["b", "b"], ["c"]]

    assert normalize(result) == normalize(expected)

    # Uppercase and lowercase are treated as different characters
    result = group_anagram(["Eat", "eat", "ate"])
    expected = [["Eat"], ["eat", "ate"]]

    assert normalize(result) == normalize(expected)
    assert normalize(result) == normalize(expected)


if __name__ == "__main__":
    test_group_anagram()
    print("All tests passed!")