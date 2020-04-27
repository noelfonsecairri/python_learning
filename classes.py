# class Patient():
# 	def __init__(self, last_name, first_name, age):
# 		self.last_name = last_name
# 		self.first_name = first_name
# 		self.age = age

# pid4343 = Patient("Taleb", "Sue", 61)
# pid4344 = Patient("Anand", "Punya", 29)
# pid4345 = Patient("Oppenheimer", "Douglas", 15)
# pid4346 = Patient("Lin", "Lily", 48)
# pid12902 = Patient("Nilsson", "Rhonda", 48)

# print(pid12902.age)

#########
# l = [1,2,3,1,1,1,1,1,2,2,2,2,3,3,3,3]
# myset = set(l)


# class Dog():

# 	# This is called Class Object Attribute
# 	# Same for any instance of a class
# 	species = 'mammal'

# 	def __init__(self, breed, name):
# 		self.breed = breed
# 		self.name = name

# 		# expect boolean from this:
# 		#self.spots = spots

# 	# THIS IS A METHOD (looks like functions inside of a class.)
# 	def bark(self, number):
# 		print(f"WOOF! My name is {self.name}, and the number is {number}")


# my_dog = Dog('doberman', 'bruno')

# print(my_dog.name)
# print(my_dog.breed)
# print(my_dog.species)

# my_dog.bark('asd')

# class Circle():

# 	# Class object attribute
# 	pi = 3.14

# 	def __init__(self, radius=1):

# 		self.radius = radius
# 		self.area = self.pi * self.radius * self.radius

# 	# Method
# 	def get_circumference(self):
# 		return 2 * self.pi * self.radius

# my_circle = Circle(2)

# print(my_circle.get_circumference())
# print(my_circle.area)

# class Animal():
# 	def __init__(self, temperance, size):
# 		self.temperance = temperance
# 		self.size = size

# 	def who_am_i(self):
# 		print('I am an animal')

# 	def eat(self):
# 		print('I am eating')

# class Dog(Animal):
# 	def __init__(self, kingdom):
# 		Animal.__init__(self, "I'm a happy dog", "humongous")
# 		self.kingdom = kingdom

# 	def bark():
# 		print('I am barking')




# my_animal = Animal()
# my_animal.eat()

# my_animal = Animal('happy', 'big')

# my_dog = Dog('Animalia')


# print(my_dog.size)
# print(my_dog.kingdom)

#################

# POLYMORPHISM

# class Animal():
# 	def __init__(self, name):
# 		self.name = name

# 	def speak(self):
# 		raise NotImplementedError('Subclass must implement abstract method')

# class Dog(Animal):
# 	def __init__(self, name):
# 		self.name = name

# 	def speak(self):
# 		return self.name + ' says Woof!'

# class Cat(Animal):
# 	def __init__(self, name):
# 		self.name = name

# 	def speak(self):
# 		return self.name + ' says Meow!'





# fido = Dog('Fido')
# isis = Cat('Isis')
# #gats = Animal('Gats')

# print(fido.speak())
# print(isis.speak())
# print(gats.speak())

# for pet in [fido, isis]:
# 	print(pet.speak())

# def speak(pet):
# 	print(pet.speak())

# speak(fido)

################

# Unassisted POLYMORPHISM

# class Dog():
# 	def __init__(self, name):
# 		self.name = name

# 	def print_name(self):
# 		print(self.name)

# 	def speak(self):
# 		print self.name + ' says'



# bruno = Dog('Bruno')

# bruno.print_name()

###################

# class Book():
# 	def __init__(self, title, author, pages):
# 		self.title = title
# 		self.author = author
# 		self.pages = pages

# 	def __len__(self):
# 		return self.pages

# 	def __str__(self):
# 		return "yes, we have a string method for this one. title is: " + self.title + " and the author is " + self.author

# 	# def __del__(self):
# 	# 	print('A book is destroyed')


# my_book1 = Book('My amazing life', 'Noel', 200)
# my_book2 = Book('The good earth', 'Pearl', 300)
# my_book3 = Book('Red horse', 'Michael', 500)

# my_books = (my_book1, my_book2, my_book3)

# for i in my_books:
# 	print(str(i) + ' and their pages are ' + str(len(i)) + ', respectively')




# print(len(my_book))

#print(str(my_book))

# class Bag():

# 	def __init__(self, style):
# 		self.style = style

# 	def __len__(self):
# 		return len(self.style)

# 	def __del__(self):
# 		print('A bag has been destroyed')

# my_bag_1 = Bag('Gucci')
# my_bag_2 = Bag('Canvass')
# my_bag_3 = Bag('Target Special')

# my_bags = (my_bag_1, my_bag_2, my_bag_3)

# for i in my_bags:
# 	print(len(i))

#del my_bag_1

# for i in my_bags:
# 	print(i)

################

###########
# Objec Oriented Programming 
# Homework Assignment - My own solutions

# import math

# class Line():
# 	def __init__(self, coor1, coor2):
# 		self.coor1 = coor1
# 		self.coor2 = coor2

# 	def distance(self):
# 		return math.sqrt(((self.coor2[0] - self.coor1[0])**2)+((self.coor2[1] - self.coor1[1])**2))

# 	def slope(self):
# 		return (self.coor2[1]-self.coor1[1]) / (self.coor2[0]-self.coor1[0])

# coordinate1 = (3,2)
# coordinate2 = (8,10)

# my_line = Line(coordinate1, coordinate2)

# print(my_line.distance())

# print(my_line.slope())

##############

# class Cylinder():

# 	pi = 3.14

# 	def __init__(self, height=1, radius=1):
# 		self.height = height
# 		self.radius = radius

# 	def volume(self):
# 		return Cylinder.pi * (self.radius**2) * self.height

# 	def surface_area(self):
# 		return (2 * Cylinder.pi * self.radius * self.height) + (2 * Cylinder.pi * (self.radius**2))

# my_cylinder = Cylinder(2,3)

# print(my_cylinder.volume())

# print(my_cylinder.surface_area())

###########
# Objec Oriented Programming Solutions
# Homework Assignment

# Problem 1

# class Line(object):
# 	def __init__(self, coor1, coor2):
# 		self.coor1 = coor1
# 		self.coor2 = coor2

# 	def distance(self):
# 		x1,y1 = self.coor1
# 		x2,y2 = self.coor2
# 		return((x2-x1)**2 + (y2-y1)**2)**0.5

# 	def slope(self):
# 		x1,y1 = self.coor1
# 		x2,y2 = self.coor2
# 		return (y2-y1)/(x2-x1)

# coordinate1 = (3,2)
# coordinate2 = (8,10)
# li = Line(coordinate1, coordinate2)

# print(li.distance())
# print(li.slope())

###############

# Problem 2

# same as my solution

##############

# Object Oriented Programming Challenge
# My solution:

# class Account():
# 	def __init__(self, owner, balance):
# 		self.owner = owner
# 		self.balance = balance

# 	def __str__(self):
# 		return 'Account owner: ' + self.owner + '\nAccount balance: ' + str(self.balance)

# 	def deposit(self, amount):
# 		return self.balance + amount

# 	def withdraw(self, amount):
# 		if amount > self.balance:
# 			return 'Insufficient funds'
# 		else:
# 			return self.balance - amount

# acct1 = Account('Jose', 100)

# print(acct1)

# print(acct1.owner)

# print(acct1.balance)

# print(acct1.deposit(50))

# print(acct1.withdraw(75))

# print(acct1.withdraw(500))
















