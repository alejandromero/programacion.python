#-*-coding:utf-8 -*-
#Laboratorio 3
#Alejandro Romero Amezcua 
#29 de noviembre de 2016

print "\nEste programa le dira si la primera letra su nombre es vocal o consonante\n"

nombre=raw_input("Introduzca su nombre: ")
if (nombre[0]=='a' or nombre[0]=='e' or nombre[0]=='i' or nombre[0]=='o' or nombre[0]=='u'):
	print "La primera letra su nombre es vocal"
else:
	print "La primera letra su nombre es consonante"