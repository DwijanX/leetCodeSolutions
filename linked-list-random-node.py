import random
class Solution(object):

    root=None
    length=0
    def countDepth(self,node):
        if(node!=None):
            return self.countDepth(node.next)+1
        else:
            return 0

    def __init__(self, head):
        """
        :type head: Optional[ListNode]
        """
        self.root=head
        self.length=self.countDepth(self.root)

        
    def pickNode(self,node,index):
        if(index==0):
            return node.val
        else:
            return self.pickNode(node.next,index-1)
    def getRandom(self):
        """
        :rtype: int
        """
        randNode=random.randint(0,self.length-1)
        return self.pickNode(self.root,randNode)