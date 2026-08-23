class Solution:
    # two pointer
    # l,r, check 
    # find valid char for l (skip)
    # find valid char for r (skip)
    # compare
    # increment with l-> and <=r
    # skipping problem therefore middle is no half of length
    def isPalindrome(self, s: str) -> bool:
        l=0
        r=len(s)-1
        charL=charR=""
        while l<r:
            if s[l].isalnum():
                charL = s[l].lower()
            else:
                l=l+1
                continue
            if s[r].isalnum():
                charR = s[r].lower()
            else:
                r=r-1
                continue
            if charR != charL:
                return False
            else:
                l=l+1
                r=r-1
        return True

