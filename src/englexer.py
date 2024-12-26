from engtoken import EngToken


class EngLexer:
	def __init__(self, path):
		self.path = path

	def lex(self):
		with open(self.path, 'r') as file:
			content = [line.strip() for line in file.readlines() if line != '\n']
			return [EngToken(line) for line in content]