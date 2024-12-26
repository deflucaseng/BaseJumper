from engnode import *




class EngParser:

	def parsetokens(self, tokens):
		nodelst = []


		for token in tokens:
			if(token.type == "display"):
				nodelst.append(self.parseDisplay(token.val[0]))
			elif(token.type == "simpleassign"):
				nodelst.append(self.parseSimpleAssign(token.var, token.val[0]))
			elif(token.type == "numericcomparativeassign"):
				nodelst.append(self.parseNumericComparativeAssign(token.var, token.val))
			elif(token.type == "evaluatedassign"):
				nodelst.append(self.parseEvaluatedAssign(token.var, token.val))
			elif(token.type == "jump"):
				nodelst.append(self.parseJump(token.val))
			elif(token.type == "end"):
				nodelst.append(EndNode())
			else:
				print("Error unknown Type Parser")
				raise ValueError
		return nodelst
	
	def parseDisplay(self, displayval):
		return DisplayNode(displayval)

	def parseSimpleAssign(self, var, value):
		return SimpleAssignNode(var, value)
	
	def parseNumericComparativeAssign(self, var, value):
		if(len(value) == 5): #Is equal to
			return EvaluatedAssignNode(var, value[0], "equals", value[-1])
		
		else: #is not equal to 
			return EvaluatedAssignNode(var, value[0], "!equals", value[-1])

	def parseEvaluatedAssign(self, var, value):
		return EvaluatedAssignNode(var, value[0], value[1], value[2])

	def parseJump(self, value):
		return JumpNode(value[0], value[-1])
	
