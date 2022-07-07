class Node:

 def __init__(self, nodeName,frequency=0,parentNode=None,lchild=None,rchild=None):

        self.nodeName=nodeName
        self.parentNode=parentNode
        self.lchild=lchild
        self.rchild=rchild
        self.frequency=frequency
        self.childbit=0
        self.code=""

