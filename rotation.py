r,c,t=map(int,input().split())
mat=[]
for i in range(r):
    mat.append(list(map(int,input().split())))
layers=[]
x=0
y=0
while(x<int(r/2) and y<int(c/2)):
    layer1=[]
    for i in range(y,c-y-1):
        layer1.append(mat[x][i])
    for i in range(x,r-x-1):
        layer1.append(mat[i][c-y-1])
    for i in range(c-x-1,x,-1):
        layer1.append(mat[r-x-1][i])
    for i in range(r-x-1,x,-1):
        layer1.append(mat[i][y])
    layers.append(layer1)
    x+=1
    y+=1
    
print(layers)
for i in range(len(layers)):
    for j in range(t):
        w=layers[i].pop(0)
        layers[i].append(w)
print(layers)
x=0
y=0
for k in layers:
    
    for i in range(y,c-y-1):
        mat[x][i]=k.pop(0)
    for i in range(x,r-x-1):
        mat[i][c-y-1]=k.pop(0)
    for i in range(c-x-1,x,-1):
        mat[r-x-1][i]=k.pop(0)
    for i in range(r-x-1,x,-1):
        mat[i][y]=k.pop(0)
    x+=1
    y+=1
   
print(mat)