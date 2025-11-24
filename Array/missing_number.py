class Solution(object):
    def missingNumber(self, nums):

        nums.sort();
        target= 0;
        for i in range(0,len(nums)):
            if target != nums[i]:
                return target
            target += 1;
        return target;

def main():
    nums = [1]

    s=Solution();
    ans = s.missingNumber(nums);
    print(ans)

main();







