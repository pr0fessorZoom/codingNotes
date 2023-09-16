def binarySearch(numberList,target):
    '''
    # Binary search splits the array looking until finds the target
    '''
    first = 0
    last = len(numberList) - 1
    steps = 0

    while first <= last:
        midpoint = (first+last)//2
        steps = steps + 1
        
        if numberList[midpoint] == target:
            print("took ", steps)
            return midpoint
        elif numberList[midpoint] < target:
            first = midpoint + 1
        else:
            last = midpoint - 1

def verify(index):
    '''
    # Verify if the number is find
    '''
    if index != None:
        print("Target found at index: ", index)
    else:
        print("Target not found in list")

if __name__ == '__main__':
    
    numberList = []
    for i in range(1,1000001): # List comprehension
        numberList.append(i)
    giveNumber = int(input("Give a number "))
    
result = binarySearch(numberList, giveNumber)
verify(result)