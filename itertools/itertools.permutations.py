from itertools import permutations
a,n=input().split(" ")
li=[]
for i in list(permutations(a,int(n))):
    li.append("".join(map(str,i)))

print("\n".join(map(str,sorted(li))))
