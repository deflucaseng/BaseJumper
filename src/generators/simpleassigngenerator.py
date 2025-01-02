def simpleassigngenerator(var, value):
	return f"\
	\tmov eax, {value}\n\t\
	mov dword [{var}], eax\n"

