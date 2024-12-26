class SymbolTable:
	def __init__(self):
		self.table = {}

	def __contains__(self, value):
		return value in self.table

	def updateval(self, var, value):
		self.table[var] = value

	def getval(self, var):
		return self.table[var]
	
