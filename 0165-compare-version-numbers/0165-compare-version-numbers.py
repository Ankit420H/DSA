class Solution:
    def compareVersion(self, v1: str, v2: str) -> int:
        a=v1.split('.')
        b=v2.split('.')
        for i in range(max(len(a),len(b))):
            x=int(a[i]) if i<len(a) else 0
            y=int(b[i]) if i<len(b) else 0
            if x!=y: return 1 if x>y else -1
        return 0
