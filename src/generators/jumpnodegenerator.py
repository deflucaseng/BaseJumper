def jumpnodegenerator(jumploc, condition):
	return f'\
	\tmov eax, [{condition}]\n\
	\tcmp eax, 1\n\
	\tjne command{jumploc}\n'

