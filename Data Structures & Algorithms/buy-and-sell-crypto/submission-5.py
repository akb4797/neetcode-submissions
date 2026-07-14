class Solution:
    def maxProfit(self, prices: List[int]) -> int:
                
        maxProfit = 0
        buyPrice = prices[0]
        sellPrice = 0

        for i in range(0, len(prices)-1):
            if (prices[i] < prices[i+1]):
                profit = prices[i+1]-buyPrice
                if(profit > maxProfit):
                    maxProfit = profit

            elif (prices[i] > prices[i+1]):
                    if(prices[i+1] < buyPrice):
                        buyPrice = prices[i+1]
                
            
            else:
                print ("skip")
        
        return maxProfit