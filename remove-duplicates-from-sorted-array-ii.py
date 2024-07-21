from collections import Counter,deque
class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        counter=Counter()
        ans=0
        indexesToRemove=deque()
        for i,num in enumerate(nums):
            if(counter[num]<2):
                ans+=1
                counter[num]+=1
            else:
                indexesToRemove.append(i)
        while(len(indexesToRemove)>0):
            nums.pop(indexesToRemove.pop())
        return ans
        
print(Solution().removeDuplicates([0,0,1,1,1,1,2,3,3]))