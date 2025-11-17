# 14. Longest Common Prefix
# Solved
# Easy
# Topics
# premium lock icon
# Companies
# Write a function to find the longest common prefix string amongst an array of strings.

# If there is no common prefix, return an empty string "".

 

# Example 1:

# Input: strs = ["flower","flow","flight"]
# Output: "fl"
# Example 2:

# Input: strs = ["dog","racecar","car"]
# Output: ""
# Explanation: There is no common prefix among the input strings.


class Solution:
    def longestCommonPrefix(self, strs):

        prefix = strs[0]
        prefix_len = len(prefix)

        for string in strs[1:]:
            print(string,prefix)
            while prefix != string[0:prefix_len]:
                prefix_len  -= 1
                if prefix_len == 0 :
                    return ""
                
                prefix = prefix[0:prefix_len]
        return prefix

            


            
                
                




        




def main():
    strs = ["flower","flow","flight"]

    s=Solution();
    ans = s.longestCommonPrefix(strs);
    print(ans)

main();






