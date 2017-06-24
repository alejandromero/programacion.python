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
		
class Task():
	def __init__(self,id):
		self.area=raw_input('Area solicitante de la tarea: ')
		self.description=raw_input('Descipcion de la tarea: ')
		self.id=id
	def __repr__(self):
		return self.description
		
class Employee():
	def __init__(self,id):
		self.id=id
		self.tasks_number=0
		self.tasks=Stack()
	def add_task(self):
		self.tasks_number+=1
		self.tasks.push(Task(self.tasks_number))
	def __repr__(self):
		return 'Empleado '+str(self.id)

class Employee_list():
	def __init__(self):
		self.em_list=[]
		self.employee_id=1
	def add_employee(self):
		self.em_list.append(Employee(self.employee_id))
		self.employee_id+=1
	def task(self):
		id=int(raw_input('Codigo de empleado: '))
		for i in self.em_list:
			if i.id==id:
				i.add_task()
				break
			else:
				pass
	def task_min(self):
		sorted(self.em_list,key=lambda x: x.tasks_number)[0].add_task()
	def process_tasks(self):
		id1=int(raw_input('Desde el id: '))
		id2=int(raw_input('Hasta el id: '))
		for i in self.em_list:
			if id1<=i.id<=id2:
				while i.tasks.isEmpty()!=True:
					print 'Empleado ',i.id,' ',i.tasks.pop()