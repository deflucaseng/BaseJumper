from engnode import *
from symboltable import SymbolTable


class EngEvaluator:
	def __init__(self, nodes):
		self.nodes = nodes
		self.end = False
		self.counter = 0
		self.st = SymbolTable()

		while(not self.end):
			self.runcycle()

	
	def runcycle(self):
		currenttype = type(self.nodes[self.counter])
		if(currenttype == DisplayNode):
			print(self.gettrueval(self.nodes[self.counter].displayval))
		elif(currenttype == SimpleAssignNode):
			self.st.updateval(self.nodes[self.counter].var, self.gettrueval(self.nodes[self.counter].value))

		elif(currenttype == EvaluatedAssignNode):
			var, lhs, op, rhs = self.nodes[self.counter].var, self.nodes[self.counter].lhs, self.nodes[self.counter].op, self.nodes[self.counter].rhs
			lhs, rhs, = self.gettrueval(lhs), self.gettrueval(rhs)

			if(op == "equals"):
				self.st.updateval(var, lhs == rhs)
			elif(op == "!equals"):
				self.st.updateval(var, lhs != rhs)
			elif(op == "or"):
				self.st.updateval(var, lhs or rhs)
			elif(op == "and"):
				self.st.updateval(var, lhs and rhs)
			elif(op == "xnor"):
				self.st.updateval(var, (not lhs and not rhs) or (lhs and rhs))
			elif(op == "nor"):
				self.st.updateval(var, (not lhs and not rhs))
			elif(op == "xor"):
				self.st.updateval(var, not ((not lhs and not rhs) or (lhs and rhs)))
			elif(op == "nand"):
				self.st.updateval(var, not(lhs and rhs))
			elif(op == "plus"):
				self.st.updateval(var, lhs + rhs)
			elif(op == "minus"):
				self.st.updateval(var, lhs - rhs)
			elif(op == "times"):
				self.st.updateval(var, lhs * rhs)
			elif(op == "divided"):
				self.st.updateval(var, lhs / rhs)
			else:
				raise ValueError

		elif(currenttype == JumpNode):
			if(self.gettrueval(self.nodes[self.counter].condition)):
				self.counter = self.nodes[self.counter].jumpto - 2

		elif(currenttype == EndNode):
			self.end = True
		else:
			raise ValueError
		
		self.counter += 1



	def gettrueval(self, var):
		if(var in self.st):
			return self.st.getval(var)
		elif(var.isalpha()):
			return bool(var)
		else:
			return int(var)
