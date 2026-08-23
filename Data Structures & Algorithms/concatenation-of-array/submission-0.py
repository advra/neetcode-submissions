class Solution:
    # create string
    # copy contents twice using 2 pointer
    # nums:1,2,3
    # ans:1,2,3,

    # time: O(n) while n loop
    # space: O(n) building new string 2n size
    def getConcatenation(self, nums: List[int]) -> List[int]:
        ans=[]
        i=0
        j=0
        newLength=2*len(nums)
        while i < newLength:
            if i>=len(nums):
                ans.append(nums[j])
                j=j+1
            else:
                ans.append(nums[i])
            i=i+1
        return ans

        