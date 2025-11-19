class Solution(object):
    def plusOne(self, digits):

        i = len(digits) -1;
        
        while(i >= 0):
            if digits[i]  < 9:
                digits[i] += 1
                return digits
            digits[i] = 0;
            i -= 1
        
        return [1] + digits;


def main():
    
    digits = [9,9]

    s = Solution()
    ans = s.plusOne(digits)
    print(ans)

main()