class Solution:
    # but if we dont need to iterate like first solution then
    # time: O(n)
    # space: O(n) building new string
    def getConcatenation(self, nums: List[int]) -> List[int]:
        return nums + nums