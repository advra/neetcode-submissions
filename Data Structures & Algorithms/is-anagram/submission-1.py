class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # using built in sort function
        return sorted(s) == sorted(t)