# Adding an element to a dictionary
# my_dict = {'a': 1, 'b': 2}
# my_dict['c'] = 3

# a_dict = {}
# a_dict[1] = "a"
# print(a_dict)

# print(my_dict)

# # dict keys in list
# print(my_dict.keys())

# # dict values in list
# print(my_dict.values())

# # tuples for every key and value, in a list
# print(my_dict.items())

# # add key if it is not in dict:
# if 'd' not in my_dict:
# 	my_dict['d'] = 4

# print(my_dict)

# Picking information from the Dictionary----------------

customer_09 = {"first name": "David", "last name": "Elliott", "address": "4803 Wellesley St."}

for i in customer_09.items():
	print(i)



x = {
  1: 1.1,
  2: 2.2,
  3: 3.3,
}
# print(x[1] + x[2] + x[3])

# Steps to make a dictionary -----------

# 1. start from empty
my_dict = {}

# 2. assign per item:
my_dict["name"] = "Noel"
my_dict[36] = "Noel's age"
my_dict["last name"] = "Fonseca"

# del my_dict[36]

print(my_dict)

# Loop through a dictionary's keys. Add each item—both its key and value—to a second dictionary. Make everything up.

new_dict = {}

for i in x.keys():
  new_dict[i] = x[i]


print(new_dict)


