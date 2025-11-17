class Solution:
    def evalRPN(self, t: List[str]) -> int:
        s=[]
        for x in t:
            if x not in '+-*/':
                s.append(int(x))
            else:
                b=s.pop()
                a=s.pop()
                if x=='+': s.append(a+b)
                elif x=='-': s.append(a-b)
                elif x=='*': s.append(a*b)
                else: s.append(int(a/b))
        return s.pop()