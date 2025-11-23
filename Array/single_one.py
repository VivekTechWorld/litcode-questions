# 136. Single Number
# Easy
# Topics
# premium lock icon
# Companies
# Hint
# Given a non-empty array of integers nums, every element appears twice except for one. Find that single one.

# You must implement a solution with a linear runtime complexity and use only constant extra space.

class Solution(object):
    def containsNearbyDuplicate(self, nums, k):

        hash_map = {}

        for i,num in enumerate(nums):
            if num in hash_map and i - hash_map[num] <= k: 
                return True
            else:
                hash_map[num] = i;
        return False        

def main():
    nums = [1,0,1,1]
    k = 1

    s=Solution();
    ans = s.containsNearbyDuplicate(nums,k);
    print(ans)

main();












