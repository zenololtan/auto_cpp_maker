#Automate c++ header and files
#Use: cppmake name1 name2 name3 name4
#Makes an hpp and cpp file containing class in coplienform and funcs with given name

import sys

class	Template:
	def	__init__(self, name):
		self.name = name
		hpp_template = "/Users/zenotan/automate/auto_cpp_maker/templates/hpp_template.txt"
		cpp_template = "/Users/zenotan/automate/auto_cpp_maker/templates/cpp_template.txt"
		self.create_file(name + ".hpp", hpp_template)
		self.create_file(name + ".cpp", cpp_template)

	def	create_file(self, name, template):
		fd_new = open(name, "w")
		fd_tmpl = open(template, "r")
		for line in fd_tmpl:
			if "ifndef" in line or "define" in line:
				fd_new.write(line.replace("*NAME*", name.upper()))
			else:
				fd_new.write(line.replace("*NAME*", name))
		fd_new.close()
		fd_tmpl.close()
	
def create_makefile(name, files):
	template = "/Users/zenotan/automate/auto_cpp_maker/templates/makefile_template.txt"
	fd_new = open("Makefile", "w")
	fd_tmpl = open(template, "r")
	for line in fd_tmpl:
		if "*FILES*" in line:
			replace = ""
			for file in files:
				replace += "	" + file.name + ".cpp \\\n"
			fd_new.write(line.replace("*FILES*", replace))
		else:
			fd_new.write(line.replace("*NAME*", name))
	fd_new.close()
	fd_tmpl.close()
	
def	main():
	templates = []
	makefile = False

	for arg in sys.argv[1:]:
		if "--makefile=" in arg:
			makefile = arg
		else:
			templates.append(Template(arg))
	if makefile:
		create_makefile(makefile[11:], templates)


main()
