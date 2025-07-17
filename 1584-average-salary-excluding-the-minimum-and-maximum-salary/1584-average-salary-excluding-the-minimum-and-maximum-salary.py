class Solution:
    def average(self, salary: List[int]) -> float:
        # ma=float('-inf')
        # mi=float('inf')
        # a=b=0
        # for i in range(len(salary)):
        #     if salary[i]>ma:
        #         ma=salary[i]
        #         a=i
        #     if salary[i]<mi:
        #         mi=salary[i]
        #         b=i
        # salary.pop(a)
        # salary.pop(b)
        # print(salary)
        salary=sorted(salary)
        print(salary)
        salary.pop(0)
        salary.pop(-1)
        return round(sum(salary)/len(salary),5)
        