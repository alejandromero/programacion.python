#Laboratorio 3
#Alejandro Romero Amezcua 
#29 de noviembre de 2016

print "\nPrograma que recibe nombre y da el verso a cantar\n"

def nombresc(a): #Si el nombre comienza con consonante 
	b=''
	for i in range(0,len(a)-1):
		b=b+a[i+1]
	return b

def evaluarc(a):
	j=0
	while j==0:
		if (a[0]=='a' or a[0]=='e' or a[0]=='i' or a[0]=='o' or a[0]=='u'):
			pass
			j=1
		else:
			a=nombresc(a)
	return a

def verso(a):
	print a,a
	if (a[0]=='a' or a[0]=='e' or a[0]=='i' or a[0]=='o' or a[0]=='u'):
		print "bob"+a
	else:
		print "bob"+evaluarc(a)
	print "banana bana"
	if (a[0]=='a' or a[0]=='e' or a[0]=='i' or a[0]=='o' or a[0]=='u'):
		print "fof"+a
	else:
		print "fof"+evaluarc(a)
	print "fi fai mo"
	if (a[0]=='a' or a[0]=='e' or a[0]=='i' or a[0]=='o' or a[0]=='u'):
		print "m"+a
	else:
		print "m"+evaluarc(a)
	print a
	
nombre=raw_input("Ingrese un nombre corto: ")
verso(nombre)
