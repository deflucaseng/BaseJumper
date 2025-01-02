def endnodegenerator():
	return f"\
	\tmov eax, 0x1\n\t\
	mov ebx, 0\n\t\
	int 0x80\n"