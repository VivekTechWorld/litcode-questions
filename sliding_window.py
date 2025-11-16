# class Solutoin(object):
#     def sliding_window(self,nums,w):
#         curr=0
#         for i in range(0,w):
#             curr+=nums[i]

#         maxx=curr
#         for i in range(1,len(nums)-w+1):
#             curr=curr-nums[i-1]+nums[i+w-1]

#             if curr > maxx:
#                 maxx=curr
        
#         return maxx




# def main():

#     arr=[3,8,2,5,7,6,12]

#     w=4

#     s1=Solutoin()
#     ans=s1.sliding_window(arr,w)
#     print(ans)

# main()

class Solution(object):
    def sliding_window(self,nums,w):
        curr=0
        for i in range(0,w):
            curr+=nums[i]
        
        maxx=curr
        for i in range(1,len(nums)-w+1):
            curr=curr-nums[i-1]+nums[i+w-1]

            if curr > maxx:
                maxx=curr
        return maxx

def main():
    
    arr=[3,8,2,5,7,6,12]

    w=4

    s1=Solution()
    ans=s1.sliding_window(arr,w)
    print(ans)

main()