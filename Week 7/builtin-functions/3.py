'''
Write a Python program with builtin function that checks whether a passed string is palindrome or not.
'''

word = "madam"
if word == word[::-1]: 
    print("It is palindrome")
else:
    print("It is not palindrome") 

reversed_word = reversed(word)
if list(reversed_word) == list(word): 
    print("It is palindrome")
else:
    print("It is not palindrome") 
