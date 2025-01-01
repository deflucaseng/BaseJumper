def jumpnodegenerator(jumploc, var1, var2):
	return f'or eax, eax\nmov eax, [ebp-{4 * var1}]\ncmp eax, [ebp-{4 * var2}]\nje {jumploc}'

