class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # brute w/ 2 pointer
        # i start at 0
        # j go to next
        # compare and store max
        # return max
        i=j=0
        maxProfit=0
        for i in range(len(prices)):
            for j in range(i+1,len(prices)):
                maxProfit = max(maxProfit, prices[j]-prices[i])
        return maxProfit