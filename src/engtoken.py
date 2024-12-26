class EngToken:
	def __init__(self, line):
		self.linelst = line.split()
		if(self.linelst[0] == "end"):
			self.type = "end"
			self.var = None
			self.val = []
		elif(self.linelst[0] == "jump"):
			self.type = "jump"
			self.var = None
			self.val = [val for val in self.linelst[2:]]

		elif(self.linelst[0] == "display"):
			self.type = "display"
			self.var = None
			self.val = [self.linelst[1]]
		elif(self.linelst[1] == "isnow" and len(self.linelst) == 3):
			self.type = "simpleassign"
			self.var = self.linelst[0]
			self.val = [self.linelst[2]]
		elif(len(self.linelst) > 6):
			self.type = "numericcomparativeassign"
			self.var = self.linelst[0]
			self.val = [val for val in self.linelst[2:]]
		else:
			self.type = "evaluatedassign"
			self.var = self.linelst[0]
			self.val = [val for val in self.linelst[2:]]
	
	def __repr__(self):
		return " ".join(self.linelst)

	
	
