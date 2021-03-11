	### Token class ##
class Token:
	def __init__(self, word, classpart, lineNumber):
		self.word = word
		self.classpart = classpart
		self.lineNumber = lineNumber

	def show(self):
		print(self.word,'---',self.classpart,'---',self.lineNumber)





