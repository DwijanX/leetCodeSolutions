
class Solution(object):
    def average(self, salaryList):
        minSoFar=None
        maxSoFar=None
        total=0
        for salary in salaryList:
            if minSoFar==None or salary<minSoFar:
                minSoFar=salary
            if maxSoFar==None or salary>maxSoFar:
                maxSoFar=salary
            total+=salary
        return (total-minSoFar-maxSoFar)/(len(salaryList)-2)



print(Solution().average([48000,59000,99000,13000,78000,45000,31000,17000,39000,37000,93000,77000,33000,28000,4000,54000,67000,6000,1000,11000])) # 2500.00000
        