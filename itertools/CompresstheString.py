from itertools import groupby
a=input()
for key,value in groupby(a):
    print(''.join('({}, {})'.format(len(list(value)),key)),end=" ")
