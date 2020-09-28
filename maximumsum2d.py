def findmax(mat):
    for i in range(mat):
        for j in range(mat[0]):
            for k in range(0,len(mat)-i):
                
t=int(input())
for i in range(t):
    r,c=map(int,input().split(' '))
    arr=list(map(int,input().split(' ')))
    mat=[]
    samp=[]
    x=0
    while x<len(arr):
        if len(samp)==c:
            mat.append(samp)
            # print(samp)
            samp=[]
            # print(samp)
        samp.append(arr[x])
        x+=1
    mat.append(samp)
    print(mat)
    print(findmax(mat))    
    