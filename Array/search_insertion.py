class Solution:
    def searchInsert(self,nums,target):
        if nums[len(nums)-1] < target :
            return len(nums)+1;
        i=0;
        while nums[i] <= target:
        
            if target == nums[i]:
                return i
            else:
                i +=1;
        return i;

def main():
    nums = [1,3,5,6]
    target = 5
    s = Solution()
    ans = s.searchInsert(nums,target)
    print(ans)

main()