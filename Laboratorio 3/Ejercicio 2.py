#-*-coding:utf-8 -*-
#Laboratorio 3
#Alejandro Romero Amezcua 
#29 de noviembre de 2016

numero=int(input("Ingrese el numero del cual quiera la suma de sus digitos: "))
digitos=str(numero)
digitos=map(int,digitos) #Sin usar if :)

def suma(a):
	s=0
	for i in range(0,len(a)):
		s=s+a[i]
	return s
	
print suma(digitos)