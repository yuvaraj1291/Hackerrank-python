m,n=map(int,input().split())
a=[]
for i in range(m):
    a.append(input())

for j in range(n):
    b=input()
    flag=False
    for k,x in enumerate(a):
        if(x==b):
            flag=True
            print(k+1,end=" ")
    if(not(flag)):
        print("-1",end=" ")
    print()
