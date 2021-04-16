# cleanest_cities = ["city1", "city2", "city3"]

# user_input = ""
# while user_input != "q":
# 	user_input = input("Enter a city, or q to quit: ")
# 	if user_input != "q":
# 		for a_clean_city in cleanest_cities:
# 			if a_clean_city == user_input:
# 				print(a_clean_city + " is one of the cleanest cities")
# 				break
# 		else:
# 			print("your city is not clean")
# 			break
			
###

# x = ""
# while x != "hello":
# 	my_input = input("Enter the value of 'x': ")
# 	if my_input != "hello":
# 		print("x is still not 'hello'")
# 	else:
# 		print("x is now 'hello'!")
# 		break

###

# Setting a flag


# Try: while True after this code along:

# my_nums = [1,2,3,4,5]

# keep_loopping = True
# while keep_loopping == True:
# 	user_input = input("Enter a number or q to quit: ")
# 	if user_input != "q":
# 		for num in my_nums:
# 			if int(user_input) == num:
# 				print("The number is within range")
# 		break
# 	else:
# 		keep_loopping = False


###

# x = True
# y = False
# z = 0

# while x != y:
# 	z += 1
# 	x = y
# 	print(z)

###

mydict = {1: True, 4: True, 10: True, 100: False, 200: True}

for x in mydict.items():
	if x[1] != True:
		print(x[0])





















