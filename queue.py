a,b=map(int,input().split())
arr=list(map(int,input().split()))    
queries=[]
for i in range(b):
    queries.append(int(input()))
table=[[99999999999 for x in range(a)]for v in range(a)]

for i in range(len(arr)):
    table[0][i]=arr[i] 
#print(table)
j=1
for i in range(a):
    x=j
    while(x<a):
        table[j][x]=max(table[j-1][x-1],table[j-1][x])
        x+=1
    j+=1
#print(table)
for i in queries:
    print(min(table[i-1]))
    
    