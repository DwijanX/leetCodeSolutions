import heapq


def mostFrequentIDs( nums, freq):
    heap=[]
    counter={}
    heapq.heapify(heap)
    ans=[]
    for i in range(len(nums)):
        if nums[i] not in counter:
            counter[nums[i]]=0
        else:
            heap.remove((counter[nums[i]],nums[i]))
        counter[nums[i]]+=freq[i]
        heapq.heappush(heap, (counter[nums[i]],nums[i]))
        if(len(heap)==0):
            ans.append(0)
        else:
            ans.append(heap[-1][0])
    return ans
    
    #for i in range(len(nums)):
        

print(mostFrequentIDs([2,3,2,1],[3,2,-3,1]))
