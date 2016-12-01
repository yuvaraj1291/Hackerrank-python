from collections import Counter

n=int(input())
l=list(map(int,input().split(' ')))
a=Counter(l)
n=int(input())
sum=0
for i in range(n):
    size,prize=map(int,input().split())
    if(a[size]>0):
        a[size]-=1
        sum+=prize
print(sum)        
