def palindrome(s):
    return s+s[0:len(s)-1][::-1]


if '__main__'==__name__:
    n=int(input())
    alphlist=[chr(x) for x in range(97,97+26)]
  
    striset=[]
    for i in range(n,0,-1):
        stri=''
        for j in range(i):
            stri+=alphlist[j]
        striset.append(palindrome(stri))
  
    for i in range(n-1,-1,-1):
        striset[i]=' '*i+striset[i]
    for i in range(len(striset)-1,-1,-1):
        print(striset[i])
    bark='b'*(n-1)
    barker=[]
    for i in range(0,int(n/2)):
        barker.append(' '*int(n/2)+bark)
    for i in barker:
        print(i)
