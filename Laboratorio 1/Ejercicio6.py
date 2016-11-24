#Laboratorio 1
#Alejandro Romero Amezcua
#Ejercicio6
peso=(int(input("Introduzca su peso en kg: ")))
estatura=(float(input("Introduzca su estatura en metros: ")))
def evaluar(a):
	if a<16:
		print "Usted esta en una delgadez severa"
	elif 16.00<a and a<16.99:
		print "Usted esta eb una delgadez moderada"
	elif 17.00<a and a<18.49:
        print "Usted esta en una delgadez leve"
    elif 18.5<a and a<24.99:
        print "Usted esta en un estado optimo"
    elif a<=25:
        print "Usted tiene sobrepeso"
    elif a<=30:
        print "Usted tiene obesidad"
    else:
        print "Usted tiene obesidad morbida"
def imc(a,b):
	imc=float 
	imc=a/(b*b)
	evaluar(imc)
	return imc
print imc(peso,estatura)