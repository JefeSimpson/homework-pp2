'''
Given a list of ints, return True if the array contains a 3 next to a 3 somewhere.

def has_33(nums):
    pass

has_33([1, 3, 3]) → True
has_33([1, 3, 1, 3]) → False
has_33([3, 1, 3]) → False 
'''

def has_33(nums): 
    nums_in_str = ""
    for i in nums: 
        nums_in_str += str(i)

    if nums_in_str.find("33") != -1: 
        return True
    else: 
        return False


l = list(map(int, input().split()))
print(has_33(l))
