from collections import deque 
class Solution(object):
    def longestBeautifulSubstring(self, word):
        """
        :type word: str
        :rtype: int
        """
        stack=deque()
        vowelVals={"a":1,"e":2,"i":3,"o":4,"u":5}
        maxSubString=0
        letterIndex=-1
        while(letterIndex<len(word)-1):
            letterIndex+=1
            if(len(stack)==0):
                if(word[letterIndex]=="a"):
                    stack.append(word[letterIndex])
                continue
            
            if( vowelVals[word[letterIndex]]-vowelVals[stack[-1]]==1 or word[letterIndex]==stack[-1]):
                stack.append(word[letterIndex])
                if(word[letterIndex]=="u" and len(stack)>maxSubString):
                    maxSubString=len(stack)
            else:
                stack.clear()
                letterIndex-=1
            
        return maxSubString


print(Solution().longestBeautifulSubstring("aeiaaioaaaaeiiiiouuuooaauuaeiu"))
#print(ord("e")-ord("a"))
        


