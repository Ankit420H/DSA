class Solution:
    def findNumbers(self, nums: List[int]) -> int:
        number = 0
        for i in nums:
            count=0
            while i != 0:
                i//= 10
                count += 1
            if count%2==0:
                number+=1
        return number