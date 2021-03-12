# Adding an element to a dictionary ------------------

# my_dict = {'a': 1, 'b': 2}
# my_dict['c'] = 3

# a_dict = {}
# a_dict[1] = "a"
# print(a_dict)

# print(my_dict)

# dict keys in list ----------------------------
# print(my_dict.keys())

# # dict values in list---------------------------
# print(my_dict.values())

# Dict Items --------------------------------------
# print(my_dict.items())

# # add key if it is not in dict: ####################
# if 'd' not in my_dict:
# 	my_dict['d'] = 4

# print(my_dict)

# Picking information from the Dictionary----------------

# customer_09 = {"first name": "David", "last name": "Elliott", "address": "4803 Wellesley St."}
# print(customer_09["first name"])

# 
# for i in customer_09.items():
# 	print(i) # returns tuples

#####################
# x = {
#   1: 1.1,
#   2: 2.2,
#   3: 3.3,
# }
# print(x[1] + x[2] + x[3])

# Steps to make a dictionary -------------------------------

# #1. start from empty
# my_dict = {}

# #2. assign per item:
# my_dict["name"] = "Noel"
# my_dict[36] = "Noel's age"
# my_dict["last name"] = "Fonseca"

# del my_dict[36]

# print(my_dict)

# Loop through a dictionary's keys. Add each item—both its key and value—to a second dictionary. Make everything up.

# new_dict = {}

# for i in x.keys():
#   new_dict[i] = x[i]

# print(new_dict)


#######################

# Dictionary list

dict_1 = {"a": 1, "b": 2}
dict_2 = {"c": 3, "d": 4}
dict_3 = {"e": 5, "f": 6}


# my_list = [dict_1["b"], dict_2["d"], dict_3["e"]]
# print(my_list)

####################### append dictionary to a list of dictionary

my_dict_list = [dict_1, dict_2, dict_3]

dict_x = {"g": 7, "h": 8}

## append
# new_dict = my_dict_list.append(dict_4)

## insert
my_dict_list.insert(0, dict_x)



print(my_dict_list)





























