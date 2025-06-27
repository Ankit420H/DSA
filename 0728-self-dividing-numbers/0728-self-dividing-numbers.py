class Solution:
    def selfDividingNumbers(self, left: int, right: int) -> list[int]:
        result = []
        for i in range(left, right + 1):
            num = i
            T = True
            while num > 0:
                dig = num % 10
                if dig == 0 or i % dig != 0:
                    T = False
                    break
                num = num // 10
            if T:
                result.append(i)
        return result