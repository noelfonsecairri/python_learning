cat_names = []

while True:
	name = input('Enter the name of the cat ' + str(len(cat_names) + 1) + ' (Or enter nothing to stop): ')
	if name == '':
		break
	cat_names = cat_names + [name]

print('The cat names are: ')
for cat in cat_names:
	print(cat)