class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s)!=len(t):
            return False
        # anagram same letters,numbers (use hashmap and compare?)
        # hashmap will sort for us
        sMap={}
        tMap={}
        for c in s:
            if c in sMap:
                sMap[c]=sMap[c]+1
            else:
                sMap[c]=1
        for c in t:
            if c in tMap:
                tMap[c]=tMap[c]+1
            else:
                tMap[c]=1
        if sMap == tMap:
            return True
        return False

# r,1
# r,1 a,1
# r,1 a,1 c,1
# r,1 a,1 c,1 e,1
# r,1 a,1 c,2 e,1
# r,1 a,2 c,2 e,1
# r,2 a,2 c,2 e,1

# c,1 
# c,1 a,1 
# c,1 a,1 r,1
# c,1 a,1 r,2
# c,1 a,2 r,2
# c,2 a,2 r,2
# c,2 a,2 r,2 e,1