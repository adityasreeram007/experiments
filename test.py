n=int(input())
inp=input()
check=input()
table=[[0 for i in range(len(inp)+1)]for j in range(len(check)+1)]
#print(table)
for i in range(1,len(inp)+1):
    table[0][i]=inp[i-1]
for i in range(1,len(check)+1):
    table[i][0]=check[i-1]
print(table)
j=0
for i in range(len(check)):
    while(j<len(inp)):
        if(table[i][0]==table[0][j]):
            table[i+1][j]=1+sum(table[i+1][])
        j+=1
print(table)
        
    
    




