
class node:
    def __init__(self,char):
        self.char=char
        self.child=[None]*26
        self.isend=False
        self.counter=0

class trie:
    def __init__(self):
        self.root=node('#')
    def insert(self,key):
        p=self.root
        for i in range(len(key)):
            index=ord(key[i])-ord('a')
            if not p.child[index]:
                p.child[index]=node(key[i])
                
                
            p.counter+=1
            print(p.counter)
            p=p.child[index]
        
        p.isend=True

    def search(self,strr):
        p=self.root
        for i in range(len(strr)):
            index=ord(strr[i])-ord('a')
            if not p.child[index]:
                return 0
            
            p=p.child[index]
        
        
       
        
        return p.counter
    
            

if __name__=='__main__':
    
    t=trie()
    n=int(input())
    for i in range(n):
        x=list(map(str,input().split()))
        if(x[0]=='add'):
            t.insert(x[1])
        else:
            
            print(t.search(x[1]))
    