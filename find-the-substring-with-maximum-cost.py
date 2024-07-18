class Solution(object):
    def getMaxCostOfArray(self, s,costs):
        maxCost=-10000
        currentCost=0
        for char in s:
            currentCost+=costs[char]
            if(currentCost>maxCost):
                maxCost=currentCost
            if(currentCost<0):
                currentCost=0
        if(maxCost<0):
            return 0
        return maxCost


    def maximumCostSubstring(self, s, chars, vals):
        costs={}
        for i in range(len(chars)):
            costs[chars[i]]=vals[i]
        for i in range(0,len(s)):
            if s[i] not in costs:
                costs[s[i]]=ord(s[i])-ord('a')+1
        return self.getMaxCostOfArray(s,costs)
        

print(Solution().maximumCostSubstring("okyytyj", "uafndmokwztrjphgle", [189,-229,860,782,-194,-582,-743,966,777,90,526,-806,-992,845,-997,340,80,705]))  # 2


