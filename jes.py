
    
def find(strr):
    count=0
    if(len(strr)%2==1):
        count= -1
    else:
        mid=int(len(strr)/2)
        first=strr[0:mid]
        second=strr[mid:]
        fcount=counter(first)
        scount=counter(second)
        print(fcount,scount)
        stx=set(strr)
        
        for i in stx:
            if(i in fcount and i in scount):
                count+=abs(fcount[i]-scount[i])
            elif(i in fcount and i not in scount):
                count+=fcount[i]
            else:
                count+=scount[i]
    return count
def counter(st):
    lst=list(st)
    stx=set(st)
    counterc={x:lst.count(x) for x in stx}
    return counterc
    
if __name__=='__main__':        
    n=int(input())
    inputs=[]
    for i in range(n):
        x=find(input()) 
        if(x!=-1):   
            print(int(x/2))
        else:
            print(-1)
    
    
    