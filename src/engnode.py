class DisplayNode:
	def __init__(self, displayval):
		self.displayval = displayval
	
	def __repr__(self):
		return f'printing: {self.displayval}'


class SimpleAssignNode:
	def __init__(self, var, value):
		self.var = var
		self.value = value

	def __repr__(self):
		return f'assigning {self.value} to {self.var}'

class EvaluatedAssignNode:
	def __init__(self, var, lhs, op, rhs):
		self.var = var
		self.lhs = lhs
		self.op = op
		self.rhs = rhs

	def __repr__(self):
		return f'{self.lhs} {self.op} {self.rhs} are now assigned to {self.var}'

class JumpNode:
	def __init__(self, jumpto, condition):
		self.jumpto = int(jumpto)
		self.condition = condition
	
	def __repr__(self):
		return f'jumping to line {self.jumpto} if {self.condition}'

class EndNode:
	def __init__(self):
		pass

	def __repr__(self):
		return "ending program"

