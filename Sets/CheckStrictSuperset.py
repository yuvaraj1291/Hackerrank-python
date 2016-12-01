A=set(map(int,input().split(" ")))
result=True
for i in range(int(input())):
    B=set(map(int,input().split(" ")))
    if(A==B):
        result=False
    elif(not(A.intersection(B)==B)):
        result=False
print(result)
