"""Sumatoria"""
c=[[i] for i in map(int,raw_input().split())]
for j in range(len(c)):
    row=map(int,raw_input().split())
    for z in range(len(c)):
        c[z].append(row[z])
for k in range(len(c)): print sum(c[k]),