class Solution(object):
    def containsDuplicate(self, nums):

        nums.sort()
        
        for i in range(1,len(nums)):
            
            if nums[i] == nums[i-1]:
                return True
        return False


def main():
    
    digits = [9,9]

    s = Solution()
    ans = s.containsDuplicate(digits)
    print(ans)

main()