# Binary search is the basic algorithm for search values, looking 1 and 1 to find the solve.

def linearSearch(targetList,target):
    '''
    # Returns the index position of the target if found, else return None
    '''
    steps = 0
    for i in range(len(targetList)):
        steps += 1
        if targetList[i] == target:
            print("took ", steps)
            return i

def verify(index):
    '''
    # Verify if the number is find
    '''
    if index != None:
        print("Target found at index: ", index)
    else:
        print("Target not found in list")

if __name__ == '__main__':
    
    # Ask for a number and call the function to solve
    giveNumber = int(input("Please give a number: "))
    numberList = []
    for i in range(1,1000001): # List comprehension
        numberList.append(i)

    result = linearSearch(numberList, giveNumber)
    verify(result)