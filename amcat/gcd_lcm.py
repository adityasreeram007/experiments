def find_gcd(n,m):
    if n%m==0:
        return m
    n,m=m,n%m
    return find_gcd(n,m)
n,m=map(int,input().split())
if m>n:
    n,m=m,n
x=find_gcd(n,m)
print(x)
print(int((n*m)/x))

    