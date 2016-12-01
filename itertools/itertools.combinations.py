from itertools import combinations
a,n=input().split(" ")
for i in range(int(n)):
    for l in list(combinations(sorted(a),i+1)):
        print("".join(map(str,l)))
    
