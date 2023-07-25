'''
    A program that experiments bubble sort 
    
    The time complexity of bubble sort is Big O(n^2)
    
    The space complexity is yet to be determined depending on how I implement the code 
    
'''

def main():
    array = [2, 3, 1, 8, 4]
    
    print(bubbleSort(array))

def bubbleSort(array):
    array_length = len(array)
    for i in range(0, array_length):
        for j in range(0, array_length-1):
            if array[j] > array[j+1]:
                array[j], array[j+1] = array[j+1], array[j]
    return array

if __name__ == '__main__':
    main()