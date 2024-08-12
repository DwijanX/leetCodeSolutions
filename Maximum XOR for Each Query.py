class Solution(object):
    def calculateArrXOR(self,nums):
        ans=nums[0]
        for num in nums[1:]:
            ans=ans ^ num
        return ans
    def getMaximumXor(self, nums, maximumBit):
        answer=[]
        qs=len(nums)
        maxOnesBits= (1 << maximumBit) - 1
        xorVal=self.calculateArrXOR(nums)
        for i in range(qs):
            
            answer.append(maxOnesBits ^ xorVal)
            xorVal ^= nums[qs - 1 - i]
        return answer


        

print(Solution().getMaximumXor([0,1,1,3],2))