import itertools
s=input()
slist=[x for x in range(len(s))]
arr=list(itertools.combinations(slist,4))

count=0
for i in arr:
    if(s[i[0]]==s[i[3]] and s[i[1]]==s[i[2]]):
        count+=1

print(count)