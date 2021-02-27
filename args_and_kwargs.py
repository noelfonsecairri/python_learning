def myfunc(*args):
	print(sum(args) * .05)

#ca

def myfunc2(**kwargs):
	print(kwargs)
	if 'fruit' in kwargs:
		print('My fruit of choice is {}'.format(kwargs['fruit']))
	else:
		print('I did not find any fruit here')

#myfunc2(fruit='apple', vegetable='lettuce')

def myfunc3(*args, **kwargs):
	print(args)
	print(kwargs)
	print('I would like to have {} {}'.format(args[0], kwargs['fruit']))

myfunc3(3,4,5,fruit='banana', vegetable='cabbage')