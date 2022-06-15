"""
Author: Sahil Gogna
Date: 6-15-22
Description: Remove Duplicates from Sorted Array
"""

"""
Description: removes duplicates from an integer array
Input: Integer Array
Output: Number of unique elements and array without duplicates
"""
def removeDuplicates(nums):
    i = 0
    cnt = 0
    lst_size = len(nums) - 1
    if not nums:
        print("nums is empty")
    if len(nums) == 1:
        print("Only one element in array")
    while i < lst_size:
        i1 = nums[i]
        if i1 == '_':
            break
        i2 = nums[i+1]
        if i1 == i2:
            cnt = cnt + 1
            nums.remove(i2)
            nums.append('_')
        i = i + 1
    print(cnt)
    print(nums)
        
