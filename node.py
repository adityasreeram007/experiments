class node:
    def __init__(self,val):
        self.data=val
        self.left=None
        self.right=None
class bst:
    def __init__(self):
        self.root=None
    def add(self,val):
        if(self.root==None):
            self.root=node(val)
        else:
            x=node(val)
            self.root=self.insert(self.root,x)
        return
    def insert(self,root,x):
        if(root==None):
            root=x
            
        elif(root.data>x.data):
            root.left=self.insert(root.left,x)
        else:
            root.right=self.insert(root.right,x)
        return root
        
    def inorder(self,root):
        if(root==None):
            return  
        self.inorder(root.left)
        print(root.data)
        self.inorder(root.right)
if __name__=='__main__':
    b=bst()
    arr=[3,2,4,5,7]
    for i in arr:
        b.add(i)
        
    b.inorder(b.root)
    
        
        