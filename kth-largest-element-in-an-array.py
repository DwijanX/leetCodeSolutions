class Solution(object):
    def findKthLargest(self, nums, k):
        nums.sort()
        return nums[-k]
        
print(Solution().findKthLargest([3,2,1,5,6,4], 2))  # 5