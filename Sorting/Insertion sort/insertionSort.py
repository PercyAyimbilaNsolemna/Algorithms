'''
    Implementation of insertion sort
    
    The time complexity will be checked after the implementation
    
    The space complexity will be checked after the implementation
    
'''

def main():
    numbers = [3, 2, 1, 8, 4]
    
    print(insertionSort(numbers))

def insertionSort(array):
    array_length = len(array)
    for i in range(0, array_length):
        while i > 0 and array[i] < array[i-1]:
            array[i-1], array[i] = array[i], array[i-1]
            i -= 1
    return f'The sorted array is {array}'
        

if __name__ == '__main__':
    main()