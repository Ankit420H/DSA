class Solution:
    def minimumBoxes(self, apple: List[int], capacity: List[int]) -> int:
        c=k=0
        s=sum(apple)
        w=list(reversed(sorted(capacity)))
        for i in range(len(capacity)):
            k+=w[i]
            c+=1
            if s<=k:
                break
        return c