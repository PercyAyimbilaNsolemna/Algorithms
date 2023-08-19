'''
    Write a function that adds two numbers in a sorted array. Return the real indexes of the two numbers
    
    Space complexity should be constant
     
'''

class Sum:
    def ___str___(self):
        return 'This class sums two numbers and checks it with a target number'
    
    def check(self, numbers, target):
        i = 0
        j = len(numbers) - 1
        
        while i < j:
            if numbers[i] + numbers[j] == target:
                return [i+1, j+1]
            elif numbers[i] + numbers[j] < target:
                i += 1
            else:
                j -= 1
        return 'No match'
    
def main():
    sum = Sum()
    print(sum.check([0, 3, 4, 5, 7, 8], 9))
    
if __name__ == '__main__':
    main()