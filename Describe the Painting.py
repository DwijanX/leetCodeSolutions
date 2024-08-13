from collections import Counter
class Solution(object):
    def splitPainting(self, segments):
        """
        :type segments: List[List[int]]
        :rtype: List[List[int]]
        """
        events=Counter()
        top=0
        for start,end,val in segments:
            events[start]+=val
            events[end]-=val
            if(end>top):
                top=end

        answer=[]
        currentVal=0
        low=0
        for point in range(top+1):
            if point in events:
                if(currentVal!=0):
                    answer.append([low,point,currentVal])
                currentVal+=events[point]
                low=point
        return answer

        
        

print(Solution().splitPainting([[1,4,5],[4,7,7],[1,7,9]]))
