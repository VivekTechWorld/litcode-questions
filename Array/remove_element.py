class Solution(object):
    def removeElement(self, nums, val):
        k=0
        for i in range(len(nums)):

            if nums[i] != val:
                nums[k]=nums[i];
                k += 1;
        return k;

def main():
    nums =[3,2,2,3]
    val = 2;
    s=Solution();
    ans = s.removeElement(nums,val);
    print(ans)

main();
















