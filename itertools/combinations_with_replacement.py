from itertools import combinations_with_replacement
a,n=input().split(" ")
for l in list(combinations_with_replacement(sorted(a),int(n))):
    print("".join(map(str,l)))
