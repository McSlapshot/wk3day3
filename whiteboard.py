#Find Palindrom Given a string of lowercase letters, write a function to see if the word is a palindrome (the same word spelled forward and backwards).	Example Input: ‘racecar’ Example Output: True

from audioop import reverse
import math
def find_palindrome(name):
    if name == name[::-1] :
        return True
    else:
        return False
print(find_palindrome('racecar'))

def reverse_words(text):
    left = 0 
    right = len(text)-1
    while left < right:
        if text[left] == text[right]:
            left += 1
            right -= 1
        else:
            return False
    return True
reverse_words("moom")
    
def cal():
    l = input('Enter the length of a Rectangle: ')
    b = input('Enter the breadth of a Rectangle: ')
    Area = l * b
    print(Area)
cal( )

def circumference():
    r = input('What is the radius: ')
    c = 2*math.pi*r
    print(c)
circumference()