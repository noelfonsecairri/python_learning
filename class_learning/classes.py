class Animal():
	def __init__(self, Animal):
		self.Animal = Animal
		print(Animal + " is an animal.")

class Mammal(Animal):
	def __init__(self, mammal_name):
		print(mammal_name + " is a mammal")
		super().__init__(mammal_name)


my_instance = Mammal("Cat")
