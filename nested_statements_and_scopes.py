# x = 25
# def printer():
# 	x = 50
# 	return x

# print(printer())
# print(x)

# LEGB Rule for variables:

# L: Local - Names assigned in any way within a function (def or lambda), and not declared global in that function


# E: Enclosing function locals - Names in the local scope of any and all enclosing funtions (def or lambda), from inner to outer


# G: Global (module) - Names assigned at the top-level of a module file, or declared global in a def within the file.


# Built-in (Python) - Names preassigned in the built-in names module: openm range, SyntaxError,...

# Global
name = 'THIS IS A GLOBAL STRING'
def greet():
	# Enclosing
	#name = 'Sammy'

	def hello():
		# Local
		name = "I'm a local"
		print('Hello ' + name)
	hello()

print(name)
greet()

print(help(filter))

