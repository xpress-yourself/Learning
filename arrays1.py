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
            nums.remove(i2)
            nums.append('_') 
            while i1 == nums[i+1]: # check for more than 2 duplicates of a number
                nums.remove(nums[i+1])
                nums.append('_')   
        i = i + 1
    return nums

def counter(nums):
    cnt = 0
    # Determine actual number
    for x in nums:
        if x == '_':
            break
        cnt = cnt + 1

    print(cnt,", nums = ",nums)

def main():
    nums = [0,1,2]
    nums_new = removeDuplicates(nums)
    counter(nums_new)


main()

        
