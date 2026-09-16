def contains_duplicate(num):
    return  len(num) != len(set(num))

if __name__ == "__main__":
        numbers = list(map(int, input("Enter numbers seperated by space: ").split()))
        result = contains_duplicate(numbers)
        print("Duplicates presemt: ", result)