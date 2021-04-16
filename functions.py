
## HOW TO DEFINE AND CALL KEYWORD ARGUMENTS IN FUNCTIONS
# define the function and parameters

# def calc_tax(sales_total, tax_rate):
# 	print(sales_total * tax_rate)

# calc_tax(sales_total=101.37, tax_rate=.05)

## DEFINING FUNCTIONS WITH A DEFAULT VALUES
# parameter value is set during function definition
# parameter without default shoudl come first
def calc_tax(sales_total, tax_rate=.05):
	return sales_total * tax_rate

calc_tax(101.37) # 2nd parameter can be skipped when calling the function

calc_tax(tax_rate=.075, sales_total=101.37)

###

# EMPTY DEFAULT VALUE
def print_order(product_name, color, size, engraving_text=""):
	return product_name, color, size, engraving_text

print_order("Giordanno", "red", "large")

# MIXING POSITIONAL ARGUMENTS WITH ARGUMENTS WITH DEFAULT VALUES
def give_greeting(greeting, first_name = "Al", flattering_greeting = " the wonder boy "):
	return greeting + " " + flattering_greeting + first_name

x = give_greeting("Hello", first_name = "Noel")

# Args and Kwargs
def display_result(winner, score, **kwargs):
	print("The winner was " + winner)
	print("The score was " + score)
	print(kwargs["overtime"])
	print(kwargs["injuries"])

#display_result(winner="Real Madrid", score="1-0", overtime="yes", injuries="none")

#returns
# The winner was Real Madrid
# The score was 1-0
# yes
# none

def display_nums(a, b, *args):
	print(a)
	print(b)
	print(args[0])
	print(args[1])
	print(args)

# display_nums("hello", "world", "you", "are", "awesome")

def myfunc(*a):
	for i in a:
		print(i)
# myfunc(1,2,3,4,5)

list_to_be_filled = []

def myfunc(*b):
  for i in b:
    list_to_be_filled.append(i)
  print(list_to_be_filled)
# myfunc(1,2,3,4)

##########

# using RETURN

def calc_tax(sales_total = 101.37, tax_rate = .05):
	tax = sales_total * tax_rate
	return tax

# print(calc_tax())

##

def myfunc(a, b):
  return a + b
  
# print(myfunc(1, 2))

###

creatures = {
  "cat": "meow",
  "dog": "bow-wow",
  "fish": "glug",
}

def myfunc2(mydict, key, value):
	mydict[key] = value
	return mydict

# print(myfunc2(creatures, "cat", "meew meew"))

#########################
# Args and Kwargs

###


def myfunc3(*args):
	print("sum", sum(args))

# myfunc3(1,2,3)

###


def adder(*args):
	sum = 0
	for num in args:
		sum += num
	print("The sum is:", sum)

# adder(1,2,3,4,5,6)

###

fruit_list = ["banana", "apple", "mango"]
veggie_list = ["broccoli", "zuchinni", "spinach"]
meat_list = ("chicken", "pork", "beef")
dairy_list = {"milk", "butter", "yougurt"}

def myfunc4(**kwargs):
	for food_type in kwargs.values():
		for food in food_type:
			print(food)

# myfunc4(fruit=fruit_list, vegetable=veggie_list, meat=meat_list, dairy=dairy_list)

###

def myfunc5(*args):
	print(args)

# myfunc5(fruit_list, veggie_list, meat_list, dairy_list)

###

def addition(a, b, *args, option=True):
	result = 0
	if option:
		for i in args:
			result += i
		return a + b + result
	else:
		print("The option is not True")
		return result

# print(addition(1,2,3,5,6, option="hello"))
# would return the total
# print(addition(1,2,3,5,6, option=False))
# skips the if statement, will return 0 (result)

###


def arg_printer(a, b, option=True, **kwargs):
	print(a, b)
	print(option)
	print(kwargs)

# arg_printer(1,2, my_kwarg="hello")
# will retyurn:
# 1 2
# True
# {'my_kwarg': 'hello'}

###

mylist = ["hello", 1, 2, "world!"]

def myfunc5(*args):
	print(args)

# myfunc5(mylist)

def myfunc6(a, b):
	total = a + b
	return total
# print(myfunc6(1, 2))

###

def whatever():
	y = 2
	print(y)
	
# whatever()
y = 1
# print(y)

###


def now_say_it(x):
	print(x)

def say_something():
	what_to_say = "hi"
	now_say_it(what_to_say)

say_something()





























