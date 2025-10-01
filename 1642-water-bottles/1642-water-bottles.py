class Solution:
    def numWaterBottles(self, numBottles: int, numExchange: int) -> int:
        s=numBottles
        while numBottles>=numExchange:
            a=numBottles//numExchange
            s+=a
            numBottles=a+(numBottles%numExchange)
        return s

