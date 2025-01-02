from engnode import *
from generators import endnodegenerator, evaluatedassigngenerator, jumpnodegenerator, simpleassigngenerator, displaynodegenerator

#NOTES
'''

Space allocated for the base pointer will be done at the end, as I will know how many variables to assign



'''




class EngCodeGenerator:
	def __init__(self, nodelist, filepath):
		self.nodelist = nodelist
		self.symbol_table = {}
		self.currcommand = 0

		with open(filepath + ".asm", "w") as f:

			f.writelines(f"section .data\n\
		true_msg db 'true', 0xA\n\
		true_len equ $ - true_msg\n\
		false_msg db 'false', 0xA\n\
		false_len equ $ - false_msg\n\
		newline db 10\n")



			f.writelines("section .text\n\t\tglobal _start\n\t")

			f.writelines("\n_start:\n")

			for node in nodelist:
				self.currcommand += 1
				f.writelines(f'command{self.currcommand}:\n')
				if(type(node) != EndNode):
					f.writelines(f"\t\tmov dword [lastknownpos], command{self.currcommand + 1}\n")
				f.writelines(f"{self.generatecode(node)}")





			#Writing boolean print support

			f.writelines(f'''
print_true:
		mov ecx, true_msg
		mov edx, true_len
		jmp do_print
print_false:
		mov ecx, false_msg
		mov edx, false_len
do_print:
		mov eax, 4
		mov ebx, 1
		int 0x80
		jmp print_newline
start_num_print:
		mov ecx, buffer
		add ecx, 11
		mov byte [ecx], 0
		dec ecx
		mov ebx, 10
	
convert_loop:
		xor edx, edx
		div ebx
		add dl, \'0\'
		mov [ecx], dl
		dec ecx
		test eax, eax
		jnz convert_loop
		mov eax, [num_to_print]
		test eax, eax
		jns print_number
		mov byte [ecx], \'-\'
		dec ecx
print_number:
		mov edx, buffer
		add edx, 11
		sub edx, ecx
		inc ecx
		mov eax, 4
		mov ebx, 1
		int 0x80
		jmp print_newline
print_newline:
		mov eax, 4
		mov ebx, 1
		mov ecx, newline
		mov edx, 1
		int 0x80
		jmp [lastknownpos]
''')





			f.writelines("section .bss\n\t")
			f.writelines(f"\tnum_to_print resd 1\n\
		lastknownpos resd 1\n\t")
			#Now to define variables 
			f.writelines("\tbuffer resb 12\n\t")
			for variable in self.symbol_table:
				f.writelines(f"\t{variable} resd 1\n\t")

	def gettype(self, assignvalue):
		if assignvalue in self.symbol_table:
			return self.symbol_table[assignvalue]
		elif assignvalue in ["True", "true", "False", "false"]:
			return bool
		else:
			return int

	def generatecode(self, node):
		  
		nodetype = type(node)
		if(nodetype == DisplayNode):
			value = node.displayval if node.displayval not in self.symbol_table else f'[{node.displayval}]'

			if self.symbol_table[node.displayval] == int or node.displayval.isnumeric():
				return displaynodegenerator.displayintnodegenerator(value)
			else:
				return displaynodegenerator.displayboolnodegenerator(value)

		elif(nodetype == SimpleAssignNode):
			print(f'Node Type: {type(node.value)} Node Value: {node.value}')
			if node.value not in self.symbol_table:
				if(node.value == "false" or node.value == "False"):
					value = 0
					typenode = bool
				elif(node.value == "true" or node.value == "True"):
					value = 1
					typenode = bool
				else:
					value = node.value
					typenode = int
				self.symbol_table[node.var] = typenode
			else:
				value = f'[{value}]'

			return simpleassigngenerator.simpleassigngenerator(node.var, value)
		elif(nodetype == EvaluatedAssignNode):
			lhs = node.lhs if node.lhs not in self.symbol_table else f'[{node.lhs}]'
			rhs = node.rhs if node.rhs not in self.symbol_table else f'[{node.rhs}]'
			lefttype, righttype = self.gettype(lhs), self.gettype(rhs)
			if(lefttype != righttype):
				raise ValueError

			self.symbol_table[node.var] = lefttype if node.op not in ["equals", "!equals"] else bool

			return evaluatedassigngenerator.evaluatedassignnodegenerator(node.var, lhs, node.op, rhs)
		elif(nodetype == JumpNode):
			return jumpnodegenerator.jumpnodegenerator(node.jumpto, node.condition)
		elif(nodetype == EndNode):
			return endnodegenerator.endnodegenerator()
		

		













