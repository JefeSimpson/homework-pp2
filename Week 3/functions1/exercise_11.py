'''
Write a Python function that checks whether a word or phrase is palindrome or not. 
Note: A palindrome is word, phrase, or sequence that reads the same backward as forward, e.g., madam
'''

def isPalindrome(s): 
    if s == s[len(s)::-1]:
        return True
    else: 
        return False

s = input() 
print(isPalindrome(s))