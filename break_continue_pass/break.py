# from https://www.youtube.com/watch?v=yCZBnjF4_tU
av = 5
x = int(input('How many candies do you want?'))

i = 1
while i <= x:
	if i > av:
		print('out of stock')
		break # as soon as the while loop reaches a certain number, BREAK from the code.

	print('candy')
	i += 1

print('bye')