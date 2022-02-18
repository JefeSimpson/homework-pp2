'''
Write a function that takes in a list of integers and returns True if it contains 007 in order

def spy_game(nums):
    pass

spy_game([1,2,4,0,0,7,5]) --> True
spy_game([1,0,2,4,0,5,7]) --> True
spy_game([1,7,2,0,4,5,0]) --> False
'''

def spy_game(nums): 
    nums_in_str = ""
    for i in nums: 
        nums_in_str += str(i)
    part_str = ""
    for i in range(len(nums_in_str)): 
        if nums_in_str[i] == '0' or nums_in_str[i] == '7': 
            part_str += nums_in_str[i]
    
    if part_str.find("007") != -1: 
        return True
    else:
        return False

l = list(map(int, input().split()))
print(spy_game(l))
