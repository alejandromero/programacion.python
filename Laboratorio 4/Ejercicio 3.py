#-*-coding:utf-8 -*-
#Ejercicio 3
#Alejandro Romero Amezcua
#12 de diciembre de 2016
"""Programa que  dados el nombre de un archivo de texto y un nombre para un nuevo archivo, permita crear un archivo que sea el mismo que el pero con las lineas enumeradas"""
import os

def readfile(nombre):
	if os.path.isfile(nombre):
		file=open(nombre,"U")
		c=file.readlines()
	else:
		print "El archivo no está en ésta carpeta o el nombre está mal ecrito"
	return c

def newfile(l,nombre):
	newf=open(nombre,"w")
	for i in range(0,len(l),1):
		newf.write(str(i)+')'+' '+l[i])

archivo=raw_input("\n¿Cual es el nombre del archivo de .txt?\n")
archivo=archivo+".txt"		
if input("\n¿El arcivho está en la carpeta del arvhivo .py? [si=1,no=0] ")==1:
	pass
else:
	dir=raw_input("Ingrese la direccion del archivo:\n")
	archivo=dir+'\\'+archivo

lineas=readfile(archivo)
nombre=raw_input("\n¿Cual sera el nombre del nuevo archivo?\n")
while nombre==archivo:
	if input("El nuevo archivo sustituira al anterior [si=1,no=0] ")==0:
		nombre=raw_input("\n¿Cual sera el nombre del nuevo archivo?\n")
	elif input("El nuevo archivo sustituira al anterior [si=1,no=0] ")==1:
		break
	else:
		print "Introdusca un valor valido\n"
nombre=nombre+'.txt'
newfile(lineas,nombre)

raw_input("\nPresione la tecla intro para terminar la ejecucion")