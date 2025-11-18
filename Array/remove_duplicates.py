class Solution(object):
    def removeDuplicates(self, nums):
        
        k=1
        for i in range(1,len(nums)):
            
            if nums[k] != nums[i]:
                nums[k]= nums[i]
                k += 1;
        return k,nums;  

def main():
    nums = [1,1,2]

    s=Solution();
    ans = s.removeDuplicates(nums);
    print(ans)

main();