class Solution(object):
    def arraySign(self, nums):
        answer=1
        for num in nums:
            if(num==0):
                return 0
            if(num<0):
                answer=answer*-1
        return answer
        