import operator
def summer(arr):
    summ=0
    for x in arr:
        summ+=abs(x)
    return summ
if __name__=='__main__':
    n=int(input())
    arr=list(map(int,input().split()))
    q=int(input())
    que=list(map(int,input().split()))
    # print(arr)
    # print(que)
    summ=summer(arr)
    for i in que:
        listx=[i] * n
        arr=list(map(operator.add,arr,listx))
        print(summer(arr))
        
        
        
            

