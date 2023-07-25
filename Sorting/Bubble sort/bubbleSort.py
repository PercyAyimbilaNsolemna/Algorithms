'''
    A program that experiments bubble sort 
    
    The time complexity of bubble sort is Big O(n^2) that is quadratic
    
    The space complexity of bubble sort is Big O(1) that is constant time
    
'''

def main():
    numbers = [99, 44, 6, 2, 1, 5, 63, 87, 283, 4, 0]
    
    print(bubbleSort(numbers))

def bubbleSort(array):
    array_length = len(array)
    for i in range(0, array_length):
        for j in range(0, array_length-1):
            if array[j] > array[j+1]:
                array[j], array[j+1] = array[j+1], array[j]
    return f'The sorted array is {array}'

if __name__ == '__main__':
    main()