# Write a function that computes the volume of a sphere given its radius.

# def vol(rad):
# 	return (4 * 3.14 * (rad ** 3))/3

# print(vol(5))

########
# Write a function that checks whether a number is in a given range (Inclusive of high and low)

# my_list = list(range(0,10))


# def ran_check(num):
# 	return num in my_list

# print(ran_check(3))

##########

# Write a Python function that accepts a string and calculate the number of upper case letters and lower case letters.
# Sample String : 'Hello Mr. Rogers, how are you this fine Tuesday?'
# Expected Output : 
# No. of Upper case characters : 4
# No. of Lower case Characters : 33



# my_string = 'Hello Mr. Rogers, how are you this fine Tuesday?'


# def up_low(string):
# 	upper_case = 0
# 	lower_case = 0
# 	for word in my_string.split():
# 		for i in word:
# 			if i.isupper():
# 				upper_case += 1
# 			elif i.islower():
# 				lower_case += 1
# 			else:
# 				continue

# 	print('No of Upper case characters: ' + str(upper_case))
# 	print('No of Lower case characters: ' + str(lower_case))

# up_low(my_string)

##########

# Write a Python function that takes a list and returns a new list with unique elements of the first list.
# Sample List : [1,1,1,1,2,2,3,3,3,3,4,5]
# Unique List : [1, 2, 3, 4, 5]

# sample_list = [1,1,1,1,2,2,3,3,3,3,4,5]

# def unique_list(l):
# 	my_set = set(l)
# 	return list(my_set)

# print(unique_list(sample_list))

##########

# Write a Python function to multiply all the numbers in a list.
# Sample List : [1, 2, 3, -4]
# Expected Output : -24

# sample_list = [1, 2, 3, -4]

# # print(sample_list[0:])

# def multiply(numbers):
# 	product = numbers[0]
# 	for num in numbers:
# 		product *= numbers[num]
# 	return product
# print(multiply(sample_list))

############

# Write a Python function that checks whether a passed in string is palindrome or not.
# Note: A palindrome is word, phrase, or sequence that reads the same backward as forward, e.g., madam or nurses run.

# palindrom part 1
# my_string = 'helleh'

# def palindrome(string):
# 	first_half = string[0:int(len(my_string)/2)]
# 	second_half = string[int(len(my_string)/2):]
# 	for letter in string:
# 		if first_half == second_half[::-1]:
# 			return True
# 		else:
# 			return False

# print(palindrome(my_string))
# print(palindrome('aasjsdlfjjslk'))

# palindrome part 2

# my_string = 'nurses run'

# def palindrome(string):
# 	no_whitespace = string.replace(' ', '')
# 	if string.replace(' ', '') == no_whitespace[::-1]:
# 		return True

# print(palindrome(my_string))

######################
# import string

# print(string.ascii_lowercase)

# my_string = "The quick brown fox jumps over the lazy dog"

# print(list(my_string.replace(' ', '')))

# def ispangram(str1, alphabet=string.ascii_lowercase):
# 	return set(str1.lower().replace(' ','')) == set(alphabet)

# print(ispangram(my_string))

# check if set a is equal to set b
#print({'a','2','b'} == {'b','2','a'})


# my_list = [1,1,1,1,1,1,1,2,2,2,2,3,3,3,3,3]

# print(list(set(my_list)))


#print('hello %s' %('Noel'))

def ran_check(num, low, high):
	# Check if num is between low and high (including low and high)
	if num in range(low, high):
		print('%s is in the range' %str(num))
	else:
		print('The number is outside the range')

ran_check(4,3,5)























