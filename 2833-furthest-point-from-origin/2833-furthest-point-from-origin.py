class Solution:
    def furthestDistanceFromOrigin(self, moves: str) -> int:
        l=r=d=0
        for i in moves:
            if i=="L":
                l+=1
            elif i=="R":
                r+=1
            else:
                d+=1
        if l>r:
            return l+d-r
        else:
            return r+d-l