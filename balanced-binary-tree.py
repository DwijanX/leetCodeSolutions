
class Solution(object):
    length=0
    def checkHeightDiff(self,node):
        if node==None:
            return 0
        l=self.checkHeightDiff(node.left)
        r=self.checkHeightDiff(node.right)
        if abs(l-r)>1:
            raise Exception("Not Balanced")
        return max(l, r)+1


    def isBalanced(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if(root==None):
            return True
        try:
            l=self.checkHeightDiff(root.left)
            r=self.checkHeightDiff(root.right)
        except:
            return False
        if(abs(l-r)>1):
            return False
        return True
        



"""
0
12
 3 4 5 6
7 8 9 10 11 12
"""