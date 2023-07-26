'''
    Implementation od merge sort
    
    Time complexity is Big O(nlog(n)) that is logarithmic time 
    
    Space complexity with be termined by the code
    
'''

def main():
    numbers = [5, 3, 1, 0, 7, 2, 9]
    
    print(mergeSort(numbers))

def mergeSort(array):
    # Condition to stop the recursion and return the array when it's only one element
    array_length = len(array)
    if array_length == 1:
        return array
    
    # Divide the array into two halves
    mid = array_length // 2
    
    left_array = array[:mid]
    right_array = array[mid:] 
    
    '''
    To clearly understand how recursive sorting is done uncomment out this
    
    print(f'Sorted Left:  {left_array}')
    print(f'Sorted Right: {right_array}')
    
    Recursively sort the left and right halves
     
    '''
    sorted_left = mergeSort(left_array)
    sorted_right = mergeSort(right_array)
    
    '''
    
    To clearly understand the actaul left and right values passed to the merge sort function uncomment this 
    
    print(f'Left sorted: {sorted_left}' )
    print(f'Right sorted: {sorted_right}' )
    
    print(f'Left: {sorted_left}')
    print(f'Right: {sorted_right}')
    
    Merge the sorted halves using the merge function
    
    '''
    return merge(sorted_left, sorted_right)
    
 #Work on the merge function to be able to compare and combine the divided array   
def merge(left, right):
    # Create an empty list to store the sorted elements
    sorted_array = []
    left_index = 0
    right_index = 0
    
    # Compare elements from the left and right arrays and merge them in sorted order
    while left_index < len(left) and right_index < len(right):
        if left[left_index] < right[right_index]:
            sorted_array.append(left[left_index])
            left_index += 1
        else: 
            sorted_array.append(right[right_index])
            right_index += 1
            
    # Append any remaining elements from the left and right arrays (if any)       
    sorted_array.extend(left[left_index:])
    sorted_array.extend(right[right_index:])
    
    #print(sorted_array)
    
    return sorted_array

if __name__ == '__main__':
    main()