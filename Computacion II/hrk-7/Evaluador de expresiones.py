import re

class Stack():
	def __init__(self):
		self.items = []

	def isEmpty(self):
		return self.items == []

	def push(self, item):
		self.items.append(item)

	def pop(self):
		return self.items.pop()

	def peek(self):
		return self.items[len(self.items)-1]

	def size(self):
		return len(self.items)

def polishCalc(elements):
	p = Stack()
	for element in elements:
		#print ">>>", elemento
		try:
			number = float(element)
			p.push(number)
		except ValueError:
			if element not in "+-*/" or len(element) !=1:
				raise ValueError("Operador no es valido")
			try:
				a1 = p.pop()
				#print ">>>",a1
				a2 = p.pop()
				#print ">>>",a2
			except ValueError:
				raise ValueError("Faltan operandos")

		if element == '+':
			result = a1 + a2
			p.push(result)
		elif element == '-':
			result = a1 - a2
			p.push(result)
		elif element == '*':
			result = a1*a2
			p.push(result)
		elif element == '/':
			result = a2 / a1
			p.push(result)
		elif element == '%':
			result = a1 % a2
			p.push(result)

	res = p.pop()
	if p.isEmpty():
		return res
	else:
		print 'MAL'
		
def parChecker(symbolString):
	symbolString=''.join(filter((lambda x: x if x in '()' else None),(i for i in symbolString)))
	s = Stack()
	balanced = True
	index = 0
	while index < len(symbolString) and balanced:
		symbol = symbolString[index]
		if symbol == "(":
			s.push(symbol)
		else:
			if s.isEmpty():
				balanced = False
			else:
				s.pop()

		index = index + 1

	if balanced and s.isEmpty():
		return True
	else:
		return False

def convertoPolish(string):
	string=filter((lambda x: x if x!='' else None),(i for i in re.split(r'[(|)]',string)))
	print string
	final_string='';expression=False;counter=0;op=''
	for i in range(len(string)):
		actual_string='';actual_op='';count=0
		for j in range(len(string[i])):
			if count<2:
				pass
			else:
				actual_string+=actual_op+' '
				count=0
			
			if string[i][j] in '+-*/%':
				expression=False
				actual_op=string[i][j]+' '
			elif string[i][j].isdigit():
				expression=True
				count+=1
				actual_string+=string[i][j]+' ' #if j!=(len(string[i])-1):
			else:
				raise ('Mal escritura')
		actual_string+=actual_op
		string[i]=actual_string
		
		if counter<2:
			pass
		else:
			final_string+=op+' '
			counter=0
		
		if expression==True:
			final_string+=string[i]
			counter+=1
		else:
			op=string[i]
		
	return final_string		

s=raw_input()
if parChecker(s)==True:
	print(polishCalc(convertoPolish(s).split()))
else:
	print 'Los parentesis estan mal colocados'