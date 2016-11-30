#Laboratorio 3
#Alejandro Romero Amezcua 
#29 de noviembre de 2016

print "Programa que ordena de forma ascendente los numeros"
largo=int(input("Cuantos numeros desea ordenar: "))
numeros=[]
for i in range(0,largo):
	print "Ingrese el numero ",i+1,": "
	numeros.append(int(input()))
numeros.sort()
print "Los numeros ordenados de forma ascendente son: ",numeros