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
			for node in nodelist:
				f.writelines(f"command{self.currcommand}:\n\t{self.generatecode(node)}\n")
				self.currcommand += 1


	def generatecode(self, node):
		  
		nodetype = type(node)
		if(nodetype == DisplayNode):
			return displaynodegenerator.displaynodegenerator()
		elif(nodetype == SimpleAssignNode):
			self.symbol_table[node.var] = len(self.symbol_table) * 4		
			value = node.value if node.value not in self.symbol_table else self.symbol_table[node.value]
			return simpleassigngenerator.simpleassigngenerator(self.symbol_table[node.var], value)
		elif(nodetype == EvaluatedAssignNode):
			self.symbol_table[node.var] = len(self.symbol_table) * 4
			lhs = node.lhs if node.lhs not in self.symbol_table else self.symbol_table[node.lhs]
			rhs = node.rhs if node.rhs not in self.symbol_table else self.symbol_table[node.rhs]
			return evaluatedassigngenerator.evaluatedassignnodegenerator(self.symbol_table[node.var], lhs, node.op, rhs)
		elif(nodetype == JumpNode):
			condition = node.condition if node.condition not in self.symbol_table else self.symbol_table[node.condition]
			return jumpnodegenerator.jumpnodegenerator(f"command{node.jumpto}", condition)
		elif(nodetype == EndNode):
			return endnodegenerator.endnodegenerator()
		

		













