from solution import move_zeroes


def test_move_zeroes():
    # Standard case
    nums = [0, 1, 0, 3, 12]
    assert move_zeroes(nums) == [1, 3, 12, 0, 0]

    # Multiple consecutive zeroes at the beginning
    nums = [0, 0, 1, 0, 3]
    assert move_zeroes(nums) == [1, 3, 0, 0, 0]

    # Multiple consecutive zeroes in the middle
    nums = [1, 0, 0, 2, 0, 3]
    assert move_zeroes(nums) == [1, 2, 3, 0, 0, 0]

    # Multiple consecutive zeroes at the end
    nums = [1, 2, 3, 0, 0]
    assert move_zeroes(nums) == [1, 2, 3, 0, 0]

    # No zeroes
    nums = [1, 2, 3, 4, 5]
    assert move_zeroes(nums) == [1, 2, 3, 4, 5]

    # All zeroes
    nums = [0, 0, 0, 0]
    assert move_zeroes(nums) == [0, 0, 0, 0]

    # Single zero
    nums = [0]
    assert move_zeroes(nums) == [0]

    # Single non-zero element
    nums = [5]
    assert move_zeroes(nums) == [5]

    # Zero at the beginning
    nums = [0, 1, 2, 3]
    assert move_zeroes(nums) == [1, 2, 3, 0]

    # Zero in the middle
    nums = [1, 2, 0, 3, 4]
    assert move_zeroes(nums) == [1, 2, 3, 4, 0]

    # Negative numbers
    nums = [-1, 0, -2, 0, 3]
    assert move_zeroes(nums) == [-1, -2, 3, 0, 0]

    # Duplicate non-zero values
    nums = [0, 2, 2, 0, 3, 2]
    assert move_zeroes(nums) == [2, 2, 3, 2, 0, 0]

    # Already correctly arranged
    nums = [1, 2, 3, 0, 0]
    assert move_zeroes(nums) == [1, 2, 3, 0, 0]


if __name__ == "__main__":
    test_move_zeroes()
    print("All tests passed!")