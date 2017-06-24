import datetime

class trans():
	def __init__(self,id,date,acnt,amount,type):
		self.id=id
		self.date=date
		self.acnt=acnt
		self.amount=amount
		self.type=type
	def __repr__(self):
		return 'Transaction '+str(self.id)

class trans_list():
	def __init__(self):
		self.transactions=[]
		self.id=1
	def add(self):
		date=datetime.date(*map(int,raw_input("Date: ").split()))
		acnt=int(raw_input("Account number: "))
		amount=int(raw_input("Amount: "))
		type=raw_input("Transaction type: ").lower()
		self.transactions.append(trans(self.id,date,acnt,amount,type))
		self.id+=1
	def calc_deposits(self):
		total=0
		date1=datetime.date(*map(int,raw_input("Desde el: ").split()))
		date2=datetime.date(*map(int,raw_input("Hasta el: ").split()))
		for i in self.transactions:
			if date1<i.date<date2:
				if i.type=='deposito':
					total+=i.amount
				else:
					pass
		return total
	def calc_year(self):
		total_dep=0
		total_ext=0
		year=int(raw_input("Year: "))
		for i in self.transactions:
			if i.date.year==year:
				if i.type=='deposito':
					total_dep+=i.amount
				elif i.type=='extraccion':
					total_ext+=i.amount
		
		return total_dep,total_ext
	def calc_account(self):
		total=0
		account=int(raw_input('Account number: '))
		year=int(raw_input('Year: '))
		for i in self.transactions:
			if i.acnt==account:
				if i.type=='deposito':
					total+=i.amount
				elif i.type=='extraccion':
					total-=i.amount
		return total