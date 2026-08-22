class Solution:
    # 2 pointer
    # compare to target return any valid index pair
    # no repeats so skip i and j for check
    # otherwise increment j
    # return empty if none found
    #
    # time: o(n) while loop
    # space: o(1): inplace checking with pointers 
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        i=0
        j=1
        while i<len(nums):
            if  i!=j and nums[i]+nums[j]==target:
                return [i,j]
            if j==len(nums)-1:
                i=i+1
                j=0
                continue
            j=j+1
        return []
