#-*-coding:utf-8 -*-
#Alejandro Romero Amezcua
#20 de diciembre de 2016

"""Este programa brinda informacion acerca de los elementos de la tabla periodica dependiendo de lo que se necesite y lo que se conozca"""

import csv
import os

def isint(x):
	try:
		int(x)
		return True
	except:
		return False

def cons_l(t):
	e=[]
	for fila in t:
		dic={"Numero atomico":None,"Simbolo":None,"Nombre":None,"Masa atomica":None,"Configuracion":None}
		dic["Numero atomico"]=fila[0]
		dic["Simbolo"]=fila[1]
		dic["Nombre"]=fila[2]
		dic["Masa atomica"]=fila[3]
		dic["Configuracion"]=fila[4]
		e.append(dic)
	return e

def buscar(b,t):
	for i in range(0,len(t)):
		for prop,val in t[i].items():
			if b==val:
				for prop,val in t[i].items():
					print prop,'\t',val
			else:
				pass

f=open('tp.csv')
try:
    tp=csv.reader(f)
except:
	print "Error: El archivo tp.csv no esta en el directorio"
	raw_input("\nPresione la tecla enter para terminar con la ejecucion del programa")
	quit()

elementos=cons_l(tp)

r=False
while r==False:
	os.system('cls')
	print "Bienvenido"
	print "\nLa finalidad de este programa es ayudarle a encontrar informacion relevante\nsobre algun elemento de la tabla periodica."
	print "La informacion que se le brinde,dependera de su busqueda; si usted introduce el numero atomico, los datos que el programa le devolvera seran los del ejemplos\nsiguiente con el numero atomico 1:"
	buscar('1',elementos)
	print "\nEn cambio si introduce el simbolo del elemento le devolvera:"
	buscar('h',elementos)
	print "\nSi intoduce el nombre de elemento (en ingles) en lugar del nombre, le regresara el simbolo"
	e=raw_input("\n\n¿Cual será el parametro que le gustaria ingresar?\n")
	if isint(e)==True:
		while int(e)>118:
			e=raw_input("\nPor favor introduzca un valor menor a 118:\n")
	else:
		e=e[0].upper()+e[1:]
	buscar(e,elementos)
	if (raw_input("\n\n¿Quiere efectuar otra busqueda? [Si=1,No=0] "))=='1':
		pass
	else:
		r=True

raw_input("\nPresione la tecla enter para terminar con la ejecucion del programa\n")
