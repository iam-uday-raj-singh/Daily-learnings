def move_zeroes(nums):
    position = 0
    for i in range(len(nums)):
        if nums[i] != 0:
            nums[position] = nums[i]
            position +=1
     
    for i in range(position, len(nums)):
        nums[i] = 0   
    return nums

if __name__== "__main__":
    number = list(map(int, input("Enter number in array separated by spaces: ").split()))
    result = move_zeroes(number)
    print("After moving zeroes in array: ", result)
    
            