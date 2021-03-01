class Patient():
	def __init__(self, last_name, first_name):
		self.last_name = last_name
		self.first_name = first_name

patient1 = Patient('Fonseca', 'Noel')

print(patient1.last_name)