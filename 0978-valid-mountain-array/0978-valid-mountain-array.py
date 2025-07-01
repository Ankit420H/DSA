class Solution:
    def validMountainArray(self, arr: List[int]) -> bool:
        m=arr.index(max(arr))
        if len(arr)<3:
            return False

        if m==0 or m==len(arr)-1:
            return False

        for i in range(m):
            if arr[i]>=arr[i+1]:
                return False

        for i in range(m,len(arr)-1):
            if arr[i]<=arr[i+1]:
                return False

        return True