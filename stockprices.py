class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        Max_Profit = 0

        while prices:
            Big_Num = max(prices)
            Big_Num_Index = prices.index(Big_Num)

            if Big_Num_Index != 0:
                Profit = prices[Big_Num_Index] - min(prices[:Big_Num_Index])

                #Normal way
                #if Profit > Max_Profit :
                   #Max_Profit = Profit
                #Fucky way
                #Max_Profit = Profit if Profit > Max_Profit else Max_Profit
                #Potentially faster:
                Max_Profit = max(Profit, Max_Profit)

            prices.remove(Big_Num)

        return Max_Profit

prices = [7,2,5,3,9,4,10,1,12,20]
print(Solution().maxProfit(prices))
prices = [1,2,5,3,9,4,10,2,12,20]
print(Solution().maxProfit(prices))