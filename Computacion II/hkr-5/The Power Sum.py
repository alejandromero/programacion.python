"""The Power Sum"""
#!/bin/python
import time
def all_combinations(x,l,s=[],t=0): #x=numero para llegar a la suma; l=lista de las potencias; s=lista con los numeros que ya tome; t=total de sumas
	if len(s)==0:
		li=l
	else:
		li=l[l.index(s[-1])+1:]
	for i in li:
		if sum(s+[i])<x:
			t+=all_combinations(x,l,s+[i]) #Con s+[i] como parametro, limito que s no se modifique por la siguiente recursion 
		elif sum(s+[i])==x:
			t+=1
			t+=all_combinations(x,l,s+[i])
		elif sum(s+[i])>x:
			break
	return t

x=int(raw_input()); n=int(raw_input()) ;r=int(round(x**(1.0/float(n))))+1
p=[i**n for i in range(1,r)]
start=time.time()
if p[-1]==x:
	print all_combinations(x,p[:-1])+1
else:
	print all_combinations(x,p)
print time.time()-start