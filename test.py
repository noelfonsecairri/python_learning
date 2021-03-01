# import os

# my_file_path = 'hello world'

# class fileHelper:

# 	def getFileExtension(fileName):
# 		basename = os.path.basename(fileName)
# 		dn, dext = os.path.splitext(basename)
# 		if dext == "." or dext == "":
# 			return dext
# 		else:
# 			return dext[1:]
# 		# return dn, dext

# ext = fileHelper.getFileExtension(my_file_path)

# print(type(ext))
# if(ext and ext in ["jpg", "jpeg", "png", "pdf", ".", " "]):
# 	print('it is true')

ext = ''

if(ext in ["jpg", "jpeg", "png", "pdf", ".", ""]):
	print(True)

