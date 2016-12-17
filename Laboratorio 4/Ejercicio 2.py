#-*-coding:utf-8 -*-
#Ejercicio 3
#Alejandro Romero Amezcua
#16 de diciembre de 2016
"""Programa que que regresa un nuevo archivo con nombres cocatenados en base a nombres de archivos"""

import os,glob

def nombres(dir):
	n=''
	os.chdir(dir)
	for file in glob.glob("*.txt"):
		n=n+(file)
	return n

def nuevoa(dir,n,nom):
	os.chdir(dir)
	newf=open(nom,"w")
	newf.write(n)

pdir=os.getcwd()

nombre=raw_input("¿Cual sera el nombre del nuevo archivo?")
nombre=nombre+".txt"

if (int(raw_input("¿Su archivo se guardara en este directorio[Si=1,No=0]? ")))==1:
	dir2=pdir
else:
	dir2=raw_input("Ingrese el directorio en el cual se guardara el archivo:\n")

if (int(raw_input("¿Los nombres de los archivos .txt estan en el directorio en el que se guardara el archivo[Si=1,No=0]? ")))==1:
	dirn=dir2
else:
	dirn=raw_input("Ingrese el directorio del cual se extraeran los nombres de los archivos .txt:\n")

nom=nombres(dirn)
nuevoa(dir2,nom,nombre)

raw_input("\nPresione la tecla intro para terminar la ejecucion")
