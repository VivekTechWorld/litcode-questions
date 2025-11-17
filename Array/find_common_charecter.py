class Solution:
    def longestCommonPrefix(self, strs):

        prefix = strs[0]
        pre_len  = len(prefix)
        ans = []
        for string in strs[1:]:
            
            for char in string:

                if char in prefix:  
                    ans.append(char)

        return prefix






def main():
    strs = ["bella","label","roller"]

    s=Solution();
    ans = s.longestCommonPrefix(strs);
    print(ans)

main();