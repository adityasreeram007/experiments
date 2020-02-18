completed=[]
competedwords=[]
def goback(crosswords,words):
    if(len(competedwords)>0):
        words.append(competedwords.pop())
    if(len(completed)>0):
        crosswords=completed.pop()
    return crosswords,words

def solve(arr,words):
    completed.append(arr)
    while(True):
        c=findspaces(arr,words[0])
        print(c)
        if(len(c)==1 and len(words)==0):
            break
        elif(len(c)==1 and len(words)!=0):
            print(1)
            arr,words=goback(arr,words)
        else:
            print(1)
            arr=fit(arr,words[0],c[0],c[1],c[2])
            completed.append(arr)
            competedwords.append(words.pop(0))
    print(arr)
    return arr
            
def fit(arr,word,i,j,char):
    if(char=='d'):
        for x in range(len(word)):
            if(i+x<10):
                arr[i+x][j]=word[x]
    else:
        for x in range(len(word)):
            if(j+x<10):
                arr[i][j+x]=word[x]
        
    return arr
            
def findspaces(arr,word):
    for i in range(9):
        for j in range(9):
            if(arr[i+1][j]=='-' or arr[i+1][j]==word[1]):
                d=check(i,j,arr,word,'d')
                if(d==True):
                    return [i,j,'d']
            elif(arr[i][j+1]=='-' or arr[i][j+1]==word[1]):
                d=check(i,j,arr,word,'r')
                if(d==True):
                    return [i,j,'r']
            else:
                continue
    return [False]           
            
def check(i,j,arr,word,char):           
    if(char=='d'):
        for x in range(len(word)):
            if(i+x<10):
                if(arr[i+x][j]!='-' and arr[i+x][j]!=word[x]):
                    return False
            else:
                return False
        return True
    if(char=='r'):
        for x in range(len(word)):
            if(x+j<10):
                if(arr[i][j+x]!='-' and arr[i][j+x]!=word[x]):
                    return False
            else:
                return False
        return True

if __name__=='__main__':
    crosswords=[]
    n=0
    while n<10:
        lst=list(map(str,input()))
        crosswords.append(lst)
        n+=1
    words=list(map(str,input().split(';')))
    print(crosswords)
    print(words)
    arr=solve(crosswords,words)#A B D E F C