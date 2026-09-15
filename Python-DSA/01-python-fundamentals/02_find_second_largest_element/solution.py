def find_second_largest_element(num):
    largest = None
    second_largest = None
    
    for current in num:
        if largest is None:
            largest = current
        elif current > largest:
            second_largest = largest
            largest = current
        elif ((current != largest and second_largest is None) or (current != largest and current > second_largest)):
            second_largest = current
            
    if second_largest is None:
        return "There is no distinctive second largest element"
    else:
        return second_largest
            
            


if __name__== "__main__":
    numbers = list(map(int, input("Enter numbers seperated by spaces: ").split()))
    result = find_second_largest_element(numbers)
    print("Second_Largest Number: ", result)