from collections import Counter
n=int(input())

for i in range(n):
    lst=list(map(int,input().split()))
    count=0
    for j in range(lst[0],lst[1]+1):
        if(j<0):
            s='{:033b}'.format(j)[1:]
            
            sdash=''
            flag=0
            for x in range(len(s)-1,-1,-1):
                if(flag==0 and s[x]=='1'):
                    sdash+=s[x]
                    flag=1
                elif(flag==0):
                    sdash+=s[x]
                else:
                    if(s[x]=='1'):
                        sdash+='1'
                    else:
                        sdash+='0'
                                    
     
        else:
            s='{:032b}'.format(j)
            count+=Counter(s)['1']
    print(count)
            
            