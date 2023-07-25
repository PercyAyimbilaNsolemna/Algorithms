'''
    Implementation of selection sort
    
    The time complexity of selection sort is Big O(n^2) that is quadratic
    
    The space complexity of selection sort is Big O()
    
'''

def main():
    numbers = [5, 2, 3, 1, 6, 0]
    
    print(selectionSort(numbers))

def selectionSort(array):
    array_length = len(array)
    for i in range(0, array_length):
        #Comparing the ith element with all elements greater than the ith element 
        for j in range(i+1, array_length):
            smallest_number = array[i]
            if smallest_number > array[j]:
                array[i], array[j] = array[j], array[i]
    return f'The sorted array {array}'
        
        

if __name__ == '__main__':
    main()