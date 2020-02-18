strr=input()
n=len(strr)
import math
row=int(math.sqrt(n))
col=row+1
if(row*row==n):
    col=row
x=[]
i=0
j=col
count=0
while(count<row):
    if(j>=len(strr)-1):
        j=len(strr)
    x.append(strr[i:j])
    i=j
    j+=col
    count+=1
#print(x)

for i in range(len(x[0])):
    pri=''
    for j in x:
        if(len(j)>i):
            pri+=j[i]
    print(pri,end=' ')
