def find_largest(num):
    if len(num)!= 0:
        largest = num[0]
        for i in range(1,len(num)):
            if num[i] > largest:
                largest = num[i]
        return largest    
    else:
        return "Put at least one number inside the array"
                
        
if __name__== "__main__":
    numbers = list(map(int, input("Enter numbers seperated by spaces: ").split()))
    result = find_largest(numbers)
    print("Largest Number: ", result)