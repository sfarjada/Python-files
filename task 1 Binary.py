def main():
    numbers = input('Enter your numbers seperate by a space: ')
    search = int(input("enter your target number: "))
    
    seperate = numbers.split(' ')

    numberList = [int(element.strip()) for element in seperate if element.strip()] 

    print('Positon of the binary search iteratviley: ',binary(numberList,search))
    print('Positon of the binary search recursively: ',binaryR(numberList,search))
    #print(numberList)

def binary(list,target):
    left = 0
    right = len(list)-1

    while left <= right:
        midpoint = (left + right) // 2
        if list[midpoint] == target:
            return midpoint
        elif list[midpoint] > target:
            right = midpoint - 1
        else:
            left = midpoint + 1
    print(timer())

    return - 1

def binaryR(list ,target, left = 0, right=0):
    if right == 0:
        right = len(list)-1

    midpoint = (left + right) // 2
    
    if left > right:
        return -1
    elif list[midpoint] > target:
        return binaryR(list,target, left, midpoint-1)
    elif list[midpoint] < target:
        return binaryR(list,target, midpoint+1, right)
    else:
        return midpoint
    return timer()

def timer():
    import time
    problemSize = 10
    print("%12s %16s" % ("Problem Size", "Seconds"))
    for count in range(5):
        start =- time.time()
        work = 1
        for x in range (problemSize):
            work+=1
            work-=1
    elasped = time.time() - start
    print("%12d%16.3f" % problemSize, elasped)
    problemSize *=2



if __name__ == "__main__":
    main()