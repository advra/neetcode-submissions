class Solution:
    # build string
    # ignore non-alpha chars
    # case insensitive check
    #
    # time: o(n) space: o(n) due to new string
    def isPalindrome(self, s: str) -> bool:
        newStr=""
        for char in s:
            if char.isalnum():
                newStr+=char.lower()
        return newStr == newStr[::-1]