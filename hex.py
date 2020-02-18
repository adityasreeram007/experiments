#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the poisonousPlants function below.
def poisonousPlants(p):
    count=0
    
    while(True):
        p,flag=check(p)    
        if(flag==1):
            break
        count+=1
    return count
def check(arr):
    d=len(arr)
    stack=[]
    flag=0
    stack.append(arr[0])
    top=arr[0]
    a=1
    while(a<d):
        if(top>=arr[a]):
            stack.append(arr[a])

        top=arr[a]
        a+=1
    print(stack)
    if(len(arr)==len(stack)):
        flag=1
    arr=stack.copy()
    

            
            
        
            


    return arr,flag
if __name__ == '__main__':
   
    n = int(input())

    p = list(map(int, input().rstrip().split()))

    result = poisonousPlants(p)
    print(result)


