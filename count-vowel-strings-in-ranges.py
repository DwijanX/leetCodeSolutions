class Solution(object):
    vowels=('a','e','i','o','u')
    def checkIfWordVowelCondition(self,word):
        if(word[0] in self.vowels and word[-1] in self.vowels):
            return True
        return False
    def vowelStrings(self, words, queries):
        prefixes=[]
        ans=[]
        for i,word in enumerate(words):
            if(self.checkIfWordVowelCondition(word)):
                if( i==0):
                    prefixes.append(1)
                else:
                    prefixes.append(prefixes[i-1]+1)
            else:
                if( i==0):
                    prefixes.append(0)
                else:
                    prefixes.append(prefixes[i-1])
        for query in queries:
            ans.append(prefixes[query[1]]- (prefixes[query[0]-1] if query[0]>0 else 0))
        return ans
        
print(Solution().vowelStrings(["aba","bcb","ece","aa","e"],[[0,2],[1,4],[1,1]]))