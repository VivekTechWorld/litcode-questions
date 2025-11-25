# 283. Move Zeroes
# Easy
# Topics
# premium lock icon
# Companies
# Hint
# Given an integer array nums, move all 0's to the end of it while maintaining the relative order of the non-zero elements.

# Note that you must do this in-place without making a copy of the array.

 

# Example 1:

# Input: nums = [0,1,0,3,12]
# Output: [1,3,12,0,0]
# Example 2:

# Input: nums = [0]
# Output: [0]

class Solution(object):
    def moveZeroes(self, nums):

        nums.sort(reverse=True);
        j = 0 
        n = len(nums)
        print(nums)
        while j < n - 1:
            print(nums[j],nums[j+1])
            if nums[j] == 0:    
                break;
            elif nums[j] > nums[j + 1]: 
                nums[j], nums[j + 1] = nums[j + 1], nums[j]
                j = 0
            j += 1
        return nums;

def main():

    nums = [0,1,0,3,12]

    s=Solution();
    ans = s.moveZeroes(nums);
    print(ans)

main();










def main():
    nums = [1]

    s=Solution();
    ans = s.moveZeroes(nums);
    print(ans)

main();
