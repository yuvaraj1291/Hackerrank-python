n=int(input())
li=list(map(int,input().split(" ")))
s=set(li)
a=sum(li)
b=sum(s)*n
print(int((b-a)/(n-1)))
