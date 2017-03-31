"""2D Array - DS"""
#!/bin/python
import sys
arr = []; hg=[]
for arr_i in xrange(6):
    arr.append(map(int,raw_input().strip().split(' '))) #strip().split(' ') - Para que
for r in xrange((len(arr)-2)):
    for c in xrange((len(arr[r])-2)):
        hg.append(arr[r][c:c+3]+[arr[r+1][c+1]]+arr[r+2][c:c+3])
print sum(max(hg,key=lambda x: sum(x)))