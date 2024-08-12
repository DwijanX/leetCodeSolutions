class Solution(object):
    def arraySign(self, nums):
        answer=1
        for num in nums:
            if(num==0):
                return 0
            if(num<0):
                answer=answer*-1
        return answer
        


number = 13  # 1101 in binary
bits=pow(2,2)-1  # 0 0 1 1
amountBits= number & bits      
print(amountBits)
print(bits)
