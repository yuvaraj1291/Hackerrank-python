n=input()
setA=set(map(int,input().split(" ")))
t=int(input())
for i in range(t):
    op=input().split(" ")
    setB=set(map(int,input().split(" ")))
    if(op[0]=='intersection_update'):
        setA.intersection_update(setB)
    elif(op[0]=='update'):
        setA.update(setB)
    elif(op[0]=='symmetric_difference_update'):
        setA.symmetric_difference_update(setB)
    elif(op[0]=='difference_update'):
        setA.difference_update(setB)

print(sum(setA))

        
