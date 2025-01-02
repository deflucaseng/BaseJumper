def displayboolnodegenerator(value):
	return f'\
	\tmov eax, {value}\n\t\
	cmp eax, 1\n\t\
	jne print_false\n\t\
	jmp print_true\n'
	

def displayintnodegenerator(value):
	return f'\
	\tmov eax, {value}\n\t\
	mov dword [num_to_print], eax\n\t\
	jmp start_num_print\n'