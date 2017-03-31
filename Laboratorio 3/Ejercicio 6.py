#-*-coding:utf-8 -*-
#Laboratorio 3
#Alejandro Romero Amezcua 
#29 de noviembre de 2016

print "\nPrograma que transforma la longevidad humana en perruna\n" #Una disculpa por la sustitucion de la n en donde no va, python no me deja trabajar con la otra letra ni acetos

anospersona=int(raw_input("Ingrese la cantidad de anos persona: "))
if anospersona<0:
	anospersona=int(raw_input("Ingrese un numero positivo: "))
else:
	pass

def conversion(a):
	ap=0 #anos perro
	for i in range(1,a+1):
		if i<=2:
			ap=ap+10.5
		else:
			ap=ap+4
	return ap

print conversion(anospersona)