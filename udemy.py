#Function exercises from Udemy

# Warmup
# lesser_of_two_events
# def lesser_of_two_events(a,b):
# 	if a % 2 == 0 and b % 2 == 0:
# 		if a < b:
# 			return a
# 		else:
# 			return b
# 	if a % 2 == 0 or b % 2 == 0:
# 		if a < b:
# 			return b
# 		else:
# 			return a

# #print(lesser_of_two_events(5,4))


#print('a','b','c',sep='***')

# s = 'hello world'
# print(s.split())

#---------------------------------------
# def animal_crackers(text):
# 	for word in text.split():
# 		if text.split()[0][0] == text.split()[1][0]:
# 			return True
# 		else:
# 			return False

# print(animal_crackers('Levelheaded Llama'))
# print(animal_crackers('Crazy Kangaroo'))

#---------------------------------------
# def makes_twenty(a,b):
# 	if a == 20 or b == 20 or a + b == 20:
# 		return True
# 	else:
# 		return False

# print(makes_twenty(1,2))

#---------------------------------------
#Level 1 Problems
#---------------------------------------
# def old_macdonald(name):
# 	first_part = name[:3].capitalize()
# 	second_part = name[3:].capitalize()
# 	return first_part + second_part

# print(old_macdonald('macdonald'))

#---------------------------------------
# def master_yoda(text):
# 	text = text.split()
# 	last_word = text[-1] #home
# 	second_rest = ' '.join(text[0:-1]) #I am
# 	new_text = last_word + ' ' + second_rest
# 	return new_text

# yoda = 'I am home'
# ready = 'We are ready'
# carry = 'I am going to carry you'

# print(master_yoda(yoda))
# print(master_yoda(ready))
# print(master_yoda(carry))


#---------------------------------------
# def has_33(nums):
# 	for x in nums:
# 		if nums[x] == 3 and nums[x+1] == 3:
# 			return True
# 		else:
# 			return False

# print(has_33([1,3,3,4]))
#---------------------------------------

# def paper_doll(text):
# 	new_word = ''
# 	for i in text:
# 		new_word += i*3
# 	return new_word

# print(paper_doll('hello'))
#---------------------------------------

# def summer_69(arr):
# 	total = 0
# 	add = True

# 	for num in arr:
# 		while add:
# 			if num != 6:
# 				total += num
# 				break
# 			else:
# 				add = False
# 		while not add:
# 			if num != 9:
# 				break
# 			else:
# 				add = True
# 				break
# 	return total

# print(summer_69([1,3,5]))
# print(summer_69([4, 5, 6, 7, 8, 9]))
# print(summer_69([2, 1, 6, 9, 11]))

#---------------------------------------
#Challenging problems (code along)



# def spy_game(nums):

# 	code = [0,0,7,'x']
# 	#[0,7,'x']
# 	for num in nums:
# 		if num == code[0]:
# 			code.pop(0)
# 	return len(code) == 1

# print(spy_game([1,2,4,0,0,7,5]))
# print(spy_game([1,0,2,4,0,5,7]))
# print(spy_game([1,7,2,0,4,5,0]))

#---------------------------------------

def count_primes(num):

	#check for 0 or 1 input
	if num < 2:
		return 0
	################
	# 2 or greater
	################

	# store our prime numbers
	primes = [2] # start of the prime number is 2
	# Counter going up to the input num
	x = 3 # will start counting @ 3.

	while x <= num:
		for y in range(3,x,2)




print(count_primes(1))



