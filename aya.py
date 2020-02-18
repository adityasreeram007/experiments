class Node:
    def __init__(self,data):
        self.key=data
        self.left=None
        self.right=None
        self.level=None
       
    def __str__(self):
        return str(self.key)
       
def assignlevel(root):
    if root is None:
        return
    if root.left!=None and root.left.level==None:
        root.left.level=root.level-1
    if root.right!=None and root.right.level==None:
        root.right.level=root.level+1
    assignlevel(root.left)
    assignlevel(root.right)
   
def topview(root):
    root.level=0
    queue={}
    queue[0]=root.key
   
    assignlevel(root)
       
    qcont=[]
    qcont.append(root)
    queue={}
    queue[0]=root.key
   
    while(len(qcont)!=0):
        x=qcont.pop(0)
        if(x.left!=None):
            qcont.append(x.left)
        if(x.right!=None):
            qcont.append(x.right)
        if(x.level not in queue):
            queue[x.level]=x.key    
   
    for i in sorted(queue):
        print(queue[i],end=' ')  
       
if __name__=='__main__':
    root=Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.left = Node(4)
    root.left.right = Node(5)
    root.right.left = Node(6)
    root.right.right = Node(7)
    root.right.left.right = Node(8)
    root.right.right.right = Node(9)
    topview(root)