import datetime,copy

class Queue:
  def __init__(self):
    self.items = []

  def isEmpty(self):
    return self.items == []

  def enqueue(self, item):
    self.items.insert(0,item)
    
  def dequeue(self):
    return self.items.pop()

  def size(self):
    return len(self.items)

class Super_market():
  def __init__(self):
    self.products_list=[]
    self.actl_date=datetime.date(*map(int,raw_input('Fecha: ').split()))
  def add_product(self):
    self.actl_date=datetime.date(*map(int,raw_input('Fecha: ').split()))
    self.products_list.append(Product(self.actl_date))
  def change_price(self):
    cod=raw_input('Codigo de producto: ')
    for j in self.products_list:
      if j.prod_cod==cod:
        j.change_price()
        break 
  def more_rem(self,n):
    more=[]
    for i in self.products_list:
      if i.rem_number>n:
        print i.prod_cod,i.rem_number,i.average()
  def __repr__(self):
    return 'Lista de productos'#self.actl_date,'','Productos: ',','.join(self.products_list)

class Product():
  def __init__(self,date):
    self.prod_cod=raw_input('Codigo de producto: ')
    self.price=Price(int(raw_input('Precio del producto: ')),date)
    self.name=raw_input('Nombre del producto: ')
    self.rem_list=Queue()
    self.rem_number=0
  def change_price(self):
    self.rem_list.enqueue(self.price)
    self.price=Price(int(raw_input('Precio del producto: ')),datetime.date(*map(int,raw_input('Fecha: ').split())))
    self.rem_number+=1
  def average(self):
    average=0; prices=copy.deepcopy(self.rem_list)
    for i in range(self.rem_number):
      p=prices.dequeue()
      average+=p.amount
    average+=self.price.amount
    #average=sum([i.amount for i in self.rem_list]) + self.price.amount
    average=float(average)/float(self.rem_number+1)
    return average
  def __repr__(self):
    return self.name#self.prod_cod+''+self.price+'$'

class Price():
  def __init__(self,amount,actl_date,coin='Peso'):
    self.amount=amount
    self.actl_date=actl_date
    self.coin_type=coin
  def __repr__(self):
    return str(self.amount)