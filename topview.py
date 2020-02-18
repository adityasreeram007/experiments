class node:
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None
        self.level=None
class bst:
    def __init__(self):
        self.root=None
    def create(self,data):
        if(self.root==None):
            self.root=node(data)
            self.root.level=0
        else:
            self.insert(self.root,data)
    def insert(self,root,data):
        if(root.data>=data):
            if(root.left==None):
                root.left=node(data)
                
                return
            else:
                self.insert(root.left,data)
        elif(root.data<data):
            if(root.right==None):
                root.right=node(data)
                return
            else:
                self.insert(root.right,data)
    

    def assignlevel(self,root):
        if(root==None):
            return 
        if(root.left!=None and root.left.level==None):
            root.left.level=root.level-1
            
            
        if(root.right!=None and root.right.level==None):
            root.right.level=root.level+1
            
        self.assignlevel(root.left)
        self.assignlevel(root.right)
        
        
        
    
    
        
        
        
if __name__=='__main__':
    b=bst() 
    x = list(map(int, input().split()))
    for i in x:
        b.create(i)
    b.assignlevel(b.root)
    qcont=[]
    qcont.append(b.root)
    queue={}
    queue[0]=b.root.data
    
    while(len(qcont)!=0):
        x=qcont.pop(0)
        if(x.left!=None):
            qcont.append(x.left)
        if(x.right!=None):
            qcont.append(x.right)
        if(x.level not in queue):
            queue[x.level]=x.data        
        
    
    
    
    for i in sorted(queue):
        print(queue[i],end=' ') 
    
        