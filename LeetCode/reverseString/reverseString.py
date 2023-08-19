'''
    Write a function that reverses a string 
    
    Space complexity should be constant time 
    
    Space complexity is Big O(1)
    
    Time complexity is Big O(N)
    
    TODO: Write a test for the reverse method
    
'''

class String:
    def __str__(self):
        return 'This is the string class'
    
    def reverse(self, word):
        i = 0
        j = len(word) - 1
        
        while i < j:
            word[i], word[j] = word[j], word[i]
            i += 1
            j -= 1
        return word
    
def main():
    string = String()
    print(string.reverse(['h', 'e', 'l', 'l', 'o']))
    
if __name__ == '__main__':
    main()
    