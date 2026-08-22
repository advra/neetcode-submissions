class Solution:
    # ignore non-alpha chars
    # case insensitive check
    # build string, reverse and compare
    def isPalindrome(self, s: str) -> bool:
        newStr=""
        for char in s:
            if char.isalnum():
                newStr+=char.lower()
        return newStr == newStr[::-1]