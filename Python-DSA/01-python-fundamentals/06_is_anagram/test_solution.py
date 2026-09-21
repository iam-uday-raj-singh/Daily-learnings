from solution import is_anagram


def test_is_anagram():
    # Standard anagram
    assert is_anagram("anagram", "nagaram") is True

    # Not an anagram
    assert is_anagram("rat", "car") is False

    # Same characters in different order
    assert is_anagram("listen", "silent") is True

    # Same characters in same order
    assert is_anagram("hello", "hello") is True

    # Different lengths
    assert is_anagram("abc", "ab") is False
    assert is_anagram("ab", "abc") is False

    # Empty strings
    assert is_anagram("", "") is True

    # One empty string
    assert is_anagram("", "a") is False
    assert is_anagram("a", "") is False

    # Single character
    assert is_anagram("a", "a") is True
    assert is_anagram("a", "b") is False

    # Repeated characters
    assert is_anagram("aabbcc", "abcabc") is True
    assert is_anagram("aabbcc", "aabbcd") is False

    # Same characters but different frequencies
    assert is_anagram("aab", "abb") is False

    # Character exists in t but not in s
    assert is_anagram("aab", "aac") is False

    # Uppercase and lowercase are treated as different characters
    assert is_anagram("Anagram", "anagram") is False

    # Numbers as characters
    assert is_anagram("112233", "332211") is True
    assert is_anagram("112233", "112234") is False

    # Spaces are treated as characters
    assert is_anagram("a b", "b a") is True
    assert is_anagram("a b", "ab") is False

    # Special characters
    assert is_anagram("a!b@", "@ba!") is True
    assert is_anagram("a!b@", "@bb!") is False


if __name__ == "__main__":
    test_is_anagram()
    print("All tests passed!")