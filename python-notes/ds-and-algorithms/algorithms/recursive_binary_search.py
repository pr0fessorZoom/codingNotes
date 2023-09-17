'''
    # Recursive binary search
    # A recursive function is a function that calls himself 
'''

def recursive_binay_search(numberList,target):
    
    if len(numberList) == 0: # Looks if the number is higher than list size (in this case)
        return False
    else:
        midpoint = (len(numberList))//2

        if numberList[midpoint] == target: # Best case, just in the middle
            return numberList[midpoint]
        else:
            if numberList[midpoint] < target:
                return recursive_binay_search(numberList[midpoint+1:], target) # Recursive case A
            else:
                return recursive_binay_search(numberList[:midpoint], target) # Recursive case 

def verify(result):
    print("Target found: ", result)

if __name__ == '__main__':

    numberList = []
    for i in range(1,100001): # List comprehension
        numberList.append(i)

    result = recursive_binay_search(numberList, 105)
    verify(result)