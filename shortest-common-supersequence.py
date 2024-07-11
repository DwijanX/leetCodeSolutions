def findLCS(str1,str2):
        m=len(str1)
        n=len(str2)
        matrix=[[0 for column in range(n+1)] for row in range(m+1)]
        for i in range(0,m+1):
                
                for j in range(0,n+1):
                        if(i==0 or j==0):
                                matrix[i][j]=0
                        elif(str1[i-1]==str2[j-1]):
                                matrix[i][j]=matrix[i-1][j-1]+1
                        else:
                                matrix[i][j]=max(matrix[i-1][j],matrix[i][j-1])
        lcs=""
        indexRow=m
        indexCol=n
        
        while True:
                if(matrix[indexRow][indexCol]==0):
                        break
                if(matrix[indexRow][indexCol]>matrix[indexRow-1][indexCol] and matrix[indexRow][indexCol]>matrix[indexRow][indexCol-1]):
                        lcs=str1[indexRow-1]+lcs
                        indexRow-=1
                        indexCol-=1
                        continue
                if(matrix[indexRow][indexCol]==matrix[indexRow-1][indexCol] ):
                        indexRow-=1
                        continue
                if(matrix[indexRow][indexCol]==matrix[indexRow][indexCol-1] ):
                        indexCol-=1
                        continue
        print(len(lcs))
        return lcs
        

def shortestCommonSupersequence( str1, str2):
        lcs=findLCS(str1,str2)
        scs=""
        indexStr1=0
        indexStr2=0
        for char in lcs:
                
                while(indexStr1<len(str1) and str1[indexStr1]!=char):
                        scs+=str1[indexStr1]
                        indexStr1+=1

                while(indexStr2<len(str2) and str2[indexStr2]!=char):
                        scs+=str2[indexStr2]
                        indexStr2+=1
                scs+=char
                indexStr2+=1
                indexStr1+=1
        scs+=str1[indexStr1:]+str2[indexStr2:]

        return scs
        
        

print(shortestCommonSupersequence("bcaaacbbbcbdcaddadcacbdddcdcccdadadcbabaccbccdcdcbcaccacbbdcbabb", "dddbbdcbccaccbababaacbcbacdddcdabadcacddbacadabdabcdbaaabaccbdaa")) # 


