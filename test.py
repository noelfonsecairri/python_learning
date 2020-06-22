import os

my_file_path = 'hello world.'

class fileHelper:
	def getFileExtension(fileName):
		basename = os.path.basename(fileName)
		dn, dext = os.path.splitext(basename)
		if dext == "." or dext == "":
			return "@" + dext + "@"
		else:
			return dext[1:]
		# return dn, dext

print(fileHelper.getFileExtension(my_file_path))


