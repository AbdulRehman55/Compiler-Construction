from lib import *

class SyntaxAnalyzer:

	def __init__(self,tokens):
		self.tokens=tokens
		self.len=len(tokens)
		self.limit=5
		self.currentLim=0
		self.current=0
		self.S()



	def S(self):
		if self.tokens[self.current].word == '$':
			return False
		self.defs()

		# if self.tokens[self.current].word != 'public':
		# 	print(self.tokens[self.current].word)
		# 	print(f"invalid syntax public expected at line {self.tokens[self.current].lineNumber}")
		# else:
		# 	self.current+=1

		# if self.tokens[self.current].word != 'class':
		# 	print(f"invalid syntax class expected at line {self.tokens[self.current].lineNumber}")
			
		# else:
		# 	self.current+=1

		# if self.tokens[self.current].classpart != 'Identifier':
		# 	print(f"invalid syntax identifier expected at line {self.tokens[self.current].lineNumber}")
			
		# else:
		# 	self.current+=1

		# self.INH()

		# if self.tokens[self.current].word != '{':
		# 	print(f" {'{'} expected at line {self.tokens[self.current].lineNumber}")
		# else:
		# 	self.current+=1

		self.CLASS_BODY()


		# if self.tokens[self.current].word != 'fun' and self.tokens[self.current].word != '$':
		# 	print(f"invalid syntax function declaration expected at line {self.tokens[self.current].lineNumber}")
		# else:
		# 	self.current+=1

		# if self.tokens[self.current].word != 'main' and self.tokens[self.current].word != '$':
		# 	print(f"invalid syntax main expected at line {self.tokens[self.current].lineNumber}")
		# else:
		# 	self.current+=1


		# if self.tokens[self.current].word != '(' and self.tokens[self.current].word != '$':
		# 	print(f"invalid syntax ( expected at line {self.tokens[self.current].lineNumber}")
		# else:
		# 	self.current+=1

		# if self.tokens[self.current].word != ')' and self.tokens[self.current].word != '$':
		# 	print(f"invalid syntax ) expected at line {self.tokens[self.current].lineNumber}")
		# else:
		# 	self.current+=1

		# if self.tokens[self.current].word != ':' and self.tokens[self.current].word != '$':
		# 	print(f"invalid syntax : expected at line {self.tokens[self.current].lineNumber}")
		# else:
		# 	self.current+=1

		# if not self.DT2():
		# 	print(f"invalid syntax void expected at line {self.tokens[self.current].lineNumber}")
		# else:
		# 	self.current+=1

		# if self.tokens[self.current].word != '{' and self.tokens[self.current].word != '$':
		# 	print(f" {'{'} expected at line {self.tokens[self.current].lineNumber}")
		# else:
		# 	self.current+=1

		#self.MST()

		# if self.tokens[self.current].word != '}' and self.tokens[self.current].word != '$':
		# 	print(f" {'}'} expected at line {self.tokens[self.current].lineNumber}")
		# else:
		# 	self.current+=1


		if self.tokens[self.current].word != '}' and self.tokens[self.current].word != '$':
			print(f" {'}'} expected at line {self.tokens[self.current].lineNumber}")
		else:
			self.current+=1

		self.defs()
		return


	def INH(self):
		if self.tokens[self.current].word == '$':
			return False
		if self.tokens[self.current].word == 'extends' and self.tokens[self.current].word != '$':
			self.current+=1
			if self.tokens[self.current].classpart == 'Identifier' and self.tokens[self.current].word != '$':
				self.current+=1
				return True
			elif self.tokens[self.current].classpart == 'Invalid Lexeme' and self.tokens[self.current].word != '$':
				self.current+=1
				print(f" identifier expected {self.tokens[self.current].lineNumber}")
			else:
				print(f" parent class expected at line {self.tokens[self.current].lineNumber}")
		else:
			return False


	def defs(self):
		if self.tokens[self.current].word == '$':
			return False
		self.currentLim+=1
		if self.CLASS_DEF():
			if self.tokens[self.current].classpart == 'acc_mod' and self.tokens[self.current].word != '$':
				if self.currentLim<self.limit:
					if self.defs():
						return True
				else:
					return False
			return True
		else:
			return False
		

	def CLASS_DEF(self):
		if self.tokens[self.current].word == '$':
			return False
		if self.AM():
			if self.tokens[self.current].word == 'class' and self.tokens[self.current].word != '$':
				self.current+=1
				# else:
				# 	print(f" class expected at line{self.tokens[self.current].lineNumber} ")
				if self.tokens[self.current].classpart == 'Identifier' and self.tokens[self.current].word != '$':
					self.current+=1
				# else:
				# 	print(f" Identifier expected at line{self.tokens[self.current].lineNumber} "
		else:
			return False
			print(f"class expected {self.tokens[self.current].classpart}")
		self.INH()

		if self.tokens[self.current].word == '{' and self.tokens[self.current].word != '$':
			self.current+=1
			self.CLASS_BODY()
			if self.tokens[self.current].word == '}' and self.tokens[self.current].word != '$':
				#print(self.tokens[self.current].word)
				self.current+=1
				return True
		else:
			print(f" {'{'} expected at line {self.tokens[self.current].lineNumber}")
			return False

		
			

		# else:
		# 	print(self.tokens[self.current].word)
		# 	print(f" {'}'} expected at line {self.tokens[self.current].lineNumber}")
		# 	return False
		return True

	def AM(self):
		if self.tokens[self.current].word == '$':
			return False
		if self.tokens[self.current].classpart == 'acc_mod' and self.tokens[self.current].word != '$':
			self.current+=1
			return True
		else:
			return True
			print(f"Access Modeifier expected at {self.tokens[self.current].lineNumber}")
			


	def CLASS_BODY(self):
		if self.tokens[self.current].word == '$':
			return False
		if self.DEC():
			if self.CLASS_BODY():
				return False
		elif self.FUN_DEF():
			if self.CLASS_BODY():
				return False
		return False
			

	def MST(self):
		if self.tokens[self.current].word == '$':
			return False
		if  self.SST():
			if self.MST():
				return True
		return False

	def SST(self):
		if not self.DEC():
			if not self.FOR():
				if not self.UNTIL():
					if not self.DO_UNTIL():
						if not self.IF():
							return False
		return True
	def O_Static(self):
		if self.tokens[self.current].word == 'static' and self.tokens[self.current].word != '$':
			self.current+=1
			return True
		else:
			return False

	def FUN_DEF(self):
		if self.tokens[self.current].word == '$':
			return False
		kw = self.tokens[self.current]
		if kw.word == 'fun' and self.tokens[self.current].word != '$':
			self.current += 1
			kw = self.tokens[self.current]
			if kw.classpart in ['Identifier','main'] and self.tokens[self.current].word != '$':
				self.current += 1
				kw = self.tokens[self.current]
				if kw.word == '(' and self.tokens[self.current].word != '$':
					self.current += 1
					kw = self.tokens[self.current]
					self.LIST()
					kw = self.tokens[self.current]
					if kw.word == ')' and self.tokens[self.current].word != '$':
						self.current += 1
						kw = self.tokens[self.current]
						if kw.word == ':' and self.tokens[self.current].word != '$':
							self.current += 1
							kw = self.tokens[self.current]
							if self.DT2():
								kw = self.tokens[self.current]
								if kw.word == '{' and self.tokens[self.current].word != '$':
									self.current += 1
									kw = self.tokens[self.current]
									if self.MST():
										if kw.word == '}' and self.tokens[self.current].word != '$':
											self.current += 1
											kw = self.tokens[self.current]
											return True
										else:
											print(f"{'}'} expected at line {self.tokens[self.current].lineNumber}")
								else:
									print(f"{'{'} expected at line {self.tokens[self.current].lineNumber}")
							else:
								print(f" return type expected at line {self.tokens[self.current].lineNumber}")
						else:
							print(f" : expected at line {self.tokens[self.current].lineNumber}")
					else:
							print(f") expected at line{self.tokens[self.current].lineNumber}")
				else:
					print(f"( expected at line{self.tokens[self.current].lineNumber}")
			else:
				print(f"identifier expected at line{self.tokens[self.current].lineNumber}")

		return False


	def LIST(self):
		if self.tokens[self.current].word == '$':
			return False
		kw = self.tokens[self.current]
		if self.DT():
			kw = self.tokens[self.current]
			if kw.word==',' and self.tokens[self.current].word != '$':
				self.current+=1
				self.LIST()
		else:
			return False
		if (kw.classpart == 'INC_DEC' and self.tokens[self.current].word != '$'):
			self.current += 1
			kw = self.tokens[self.current]
			if (kw.classpart == 'Identifier' and self.tokens[self.current].word != '$'):
				self.current+=1
				kw = self.tokens[self.current]
				if self.X():
					if self.LIST():
						return True
		return 

	def CONST(self):
		if self.tokens[self.current].word == '$':
			return False
		kw = self.tokens[self.current]
		if kw.classpart == 'Integer Constant' and self.tokens[self.current].word != '$':
			self.current += 1
			kw = self.tokens[self.current]
			return True
		elif kw.classpart == 'Float Constant' and self.tokens[self.current].word != '$':
			self.current += 1
			kw = self.tokens[self.current]
			return True
		elif kw.classpart == 'String Constant' and self.tokens[self.current].word != '$':
			self.current += 1
			kw = self.tokens[self.current]
			return True
		elif kw.classpart == 'Character Constanst' and self.tokens[self.current].word != '$':
			self.current += 1
			kw = self.tokens[self.current]
			return True
		else:
			print(f"invalid token at line {self.tokens[self.current].lineNumber}")
		return False

	def DT(self):
		if self.tokens[self.current].word == '$':
			return False
		kw = self.tokens[self.current]
		if kw.classpart == 'Int_DT' or kw.classpart == 'Boolean_DT' or kw.classpart == 'Char_DT' or kw.classpart == 'String_DT' or kw.classpart == 'Float_DT' and self.tokens[self.current].word != '$':
			self.current+=1
			kw=self.tokens[self.current]
			if kw.classpart == 'Identifier' and self.tokens[self.current].word != '$':
				self.current+=1
				return True
			else:
				print(f"Identifier expected at line {kw.lineNumber}")
				return False
		else:
			#print(f"type expected at line {kw.lineNumber}")
			return False
		return True

	def DT2(self):
		if self.tokens[self.current].word == '$':
			return False
		kw = self.tokens[self.current]
		if kw.classpart in ['Int_DT','Boolean_DT','Char_DT','String_DT','Float_DT','void'] and self.tokens[self.current].word != '$':
			self.current+=1
			return True
		else:
			return False


	def FOR(self):
		if self.tokens[self.current].word == '$':
			return False
		kw=self.tokens[self.current]
		if kw.word == 'for' and self.tokens[self.current].word != '$':
			self.current+=1
			kw=self.tokens[self.current]
			if kw.word == '(' and self.tokens[self.current].word != '$':
				self.current+=1
				kw=self.tokens[self.current]
				if kw.classpart == 'Identifier' and self.tokens[self.current].word != '$':
					self.current+=1
					kw=self.tokens[self.current]
					if kw.word == 'in' and self.tokens[self.current].word != '$':
						self.current+=1
						kw=self.tokens[self.current]
						if kw.classpart == 'Integer Constant' and self.tokens[self.current].word != '$':
							self.current+=1
							kw=self.tokens[self.current]
							if kw.word == '..' and self.tokens[self.current].word != '$':
								self.current+=1
								kw=self.tokens[self.current]
								if kw.classpart == 'Integer Constant' and self.tokens[self.current].word != '$':
									self.current+=1
									kw=self.tokens[self.current]
									if kw.word == ')' and self.tokens[self.current].word != '$':
										self.current+=1
										kw=self.tokens[self.current]
										if kw.word == '{' and self.tokens[self.current].word != '$':
											self.current+=1
											kw=self.tokens[self.current]
											self.MST()
											kw=self.tokens[self.current]
											if kw.word == '}' and self.tokens[self.current].word != '$':
												self.current+=1
												kw=self.tokens[self.current]
												return True
											else:
												print(f"{'}'} expected at line {self.tokens[self.current].lineNumber}")
										else:
											print(f"{'{'} expected at line {self.tokens[self.current].lineNumber}")
									else:
										print(f") expected at line {self.tokens[self.current].lineNumber}")
								else:
									print(f"Integer expected at line {self.tokens[self.current].lineNumber}")
							else:
								print(f".. expected at line {self.tokens[self.current].lineNumber}")
						else:
							print(f"integer expected at line {self.tokens[self.current].lineNumber}")
					else:
						print(f"in expected at line {self.tokens[self.current].lineNumber}")
				else:
					print(f"Identifier expected at line {self.tokens[self.current].lineNumber}")
			else:
				print(f"( expected at line {self.tokens[self.current].lineNumber}")
		else:
			return False

	def IF(self):
		if self.tokens[self.current].word == '$':
			return False
		kw=self.tokens[self.current]
		if kw.word in ['if'] and self.tokens[self.current].word != '$':
			self.current+=1
			kw=self.tokens[self.current]
			if kw.word == '(' and self.tokens[self.current].word != '$':
				self.current+=1
				kw=self.tokens[self.current]
				if self.OE():
					kw=self.tokens[self.current]
					if kw.word == ')' and self.tokens[self.current].word != '$':
						self.current+=1
						kw=self.tokens[self.current]
						if kw.word == '{' and self.tokens[self.current].word != '$':
							self.current+=1
							kw=self.tokens[self.current]
							self.MST()
							kw=self.tokens[self.current]
							if kw.word == '}' and self.tokens[self.current].word != '$':
								self.current+=1
								self.ELIF()
								self.ELSE()
								return True
							else:
								print(f"{'}'} expected at line {kw.lineNumber}")
						else:
							print(f"{'{'} expected at line {kw.lineNumber}")
					else:
						print(f") expected at line {kw.lineNumber}")
				else:
					print(f"expression expected at line {kw.lineNumber}")
			else:
				print(f"( expected at line {kw.lineNumber}")
		else:
			return False


	def ELIF(self):
		if self.tokens[self.current].word == '$':
			return False
		kw=self.tokens[self.current]
		if kw.word in ['elif'] and self.tokens[self.current].word != '$':
			self.current+=1
			kw=self.tokens[self.current]
			if kw.word == '(' and self.tokens[self.current].word != '$':
				self.current+=1
				kw=self.tokens[self.current]
				if self.OE():
					kw=self.tokens[self.current]
					if kw.word == ')' and self.tokens[self.current].word != '$':
						self.current+=1
						kw=self.tokens[self.current]
						if kw.word == '{' and self.tokens[self.current].word != '$':
							self.current+=1
							kw=self.tokens[self.current]
							self.MST()
							kw=self.tokens[self.current]
							if kw.word == '}' and self.tokens[self.current].word != '$':
								self.current+=1
								return True
							else:
								print(f"{'}'} expected at line {kw.lineNumber}")
						else:
							print(f"{'{'} expected at line {kw.lineNumber}")
					else:
						print(f") expected at line {kw.lineNumber}")
				else:
					print(f"expression expected at line {kw.lineNumber}")
			else:
				print(f"( expected at line {kw.lineNumber}")
		else:
			return False

	def ELSE(self):
		if self.tokens[self.current].word == '$':
			return False
		kw=self.tokens[self.current]
		if kw.word == 'else' and self.tokens[self.current].word != '$':
			self.current+=1
			kw=self.tokens[self.current]
			if kw.word == '{' and self.tokens[self.current].word != '$':
				self.current+=1
				kw=self.tokens[self.current]
				self.MST()
				kw=self.tokens[self.current]
				if kw.word == '}' and self.tokens[self.current].word != '$':
					self.current+=1
					return True
				else:
					print(f"{'}'} expected at line {kw.lineNumber}")
			else:
				print(f"{'{'} expected at line {kw.lineNumber}")
		else:
			print(f") expected at line {kw.lineNumber}")


	def UNTIL(self):
		if self.tokens[self.current].word == '$':
			return False
		kw=self.tokens[self.current]
		if kw.word in ['until'] and self.tokens[self.current].word != '$':
			self.current+=1
			kw=self.tokens[self.current]
			if kw.word == '(' and self.tokens[self.current].word != '$':
				self.current+=1
				kw=self.tokens[self.current]
				if self.OE():
					kw=self.tokens[self.current]
					if kw.word == ')' and self.tokens[self.current].word != '$':
						self.current+=1
						kw=self.tokens[self.current]
						if kw.word == '{' and self.tokens[self.current].word != '$':
							self.current+=1
							kw=self.tokens[self.current]
							self.MST()
							kw=self.tokens[self.current]
							
							if kw.word == '}' and self.tokens[self.current].word != '$':
								self.current+=1
								return True
							else:
								print(f"{'}'} expected at line {kw.lineNumber}")
						else:
							print(f"{'{'} expected at line {kw.lineNumber}")
					else:
						print(f") expected at line {kw.lineNumber}")
				else:
					print(f"expression expected at line {kw.lineNumber}")
			else:
				print(f"( expected at line {kw.lineNumber}")
		else:
			return False


	def DO_UNTIL(self):
		if self.tokens[self.current].word == '$':
			return False
		kw=self.tokens[self.current]
		if kw.word == 'do' and self.tokens[self.current].word != '$':
			self.current+=1
			kw=self.tokens[self.current]
			if kw.word == '{' and self.tokens[self.current].word != '$':
				self.MST()
				self.current+=1
				kw=self.tokens[self.current]
				if kw.word == '}' and self.tokens[self.current].word != '$':
					self.current+=1
					kw=self.tokens[self.current]
					if kw.word == 'until' and self.tokens[self.current].word != '$':
						self.current+=1
						kw=self.tokens[self.current]
						if kw.word == '(' and self.tokens[self.current].word != '$':
							self.current+=1
							self.OE()
							kw=self.tokens[self.current]
							if kw.word == ')' and self.tokens[self.current].word != '$':
								self.current+=1
								return True
							else:
								print(f") expected at line {kw.lineNumber}")
						else:
							print(f"( expected at line {kw.lineNumber}")
					else:
						print(f"until expected at line {kw.lineNumber}")
				else:
					print(f"{'}'} expected at line {kw.lineNumber}")
			else:
				print(f"{'{'} expected at line {kw.lineNumber}")
		else:
			return False

	def DEC(self):
		kw=self.tokens[self.current]
		self.AM()
		self.O_Static()

		if self.DT2():
			kw=self.tokens[self.current]
			if kw.classpart == 'Identifier':
				self.current+=1
				if self.M():
					self.current+=1
					kw=self.tokens[self.current]
					if kw.word == ';':
						self.current+=1
						return True
					else:
						print(f"; expected at line {kw.lineNumber}")
				kw=self.tokens[self.current]
				if kw.word == ';':
					self.current+=1
					return True
						
				kw=self.tokens[self.current]
				if kw.word == ';':
					self.current+=1
					return True
				else:
					print(f"; expected at line {kw.lineNumber}")
			else:
				print(f"Identifier expected at line {kw.lineNumber}")
					
		else:
			return False
			print(f"type expectedd at line {kw.lineNumber}")


	def M(self):
		kw=self.tokens[self.current]
		if kw.word == '=' and self.tokens[self.current].word != '$':
			self.current+=1
			if self.OE():
				if self._M():
					return True
			else:
				if kw.word == ',' and self.tokens[self.current].word != '$':
					self.current+=1
					kw=self.tokens[self.current]
					if kw.classpart == 'Identifier' and self.tokens[self.current].word != '$':
						self.current+=1
						self.M()
						return True
		else:
			return False

	def _M(self):
		kw=self.tokens[self.current]
		if kw.word == ',' and self.tokens[self.current].word != '$':
			self.current+=1
			kw=self.tokens[self.current]
			if kw.classpart == 'Identifier' and self.tokens[self.current].word != '$':
				self.current+=1
				if self.M():
					return True
		else:
			return False




	def OE(self):
		if self.tokens[self.current].word == '$':
			return False
		elif self.AE():
			if self.O_E():
				return True
			else:
				return True
		else:
			return False

	def O_E(self):
		if self.tokens[self.current].word == '||' and self.tokens[self.current].word != '$':
			self.current+=1
			self.AE()
			self.O_E()
			return True
		else:
			return False


	def AE(self):
		if self.RE():
			if self.A_E():
				return True
			else:
				return True
		else:
			return False


	def A_E(self):
		if self.tokens[self.current].word == '&&':
			self.current+=1
			self.RE()
			self.O_E()
			return True
		else:
			return False

	def RE(self):
		if self.E():
			if self.R_E():
				return True
			else:
				return True
		else:
			return False

	def R_E(self):
		if self.tokens[self.current].classpart == 'ROP':
			self.current+=1
			if self.tokens[self.current].classpart == 'ROP':
				print(f"invalid syntax at line{self.tokens[self.current].lineNumber}")
			self.RE()
			self.O_E()
			return True
		else:
			return False


	def E(self):
		if self.T():
			if self.X():
				return True
			else:
				return True
		else:
			return False

	def X(self):
		if self.tokens[self.current].classpart == 'PM':
			self.current+=1
			self.T()
			self.X()
			return True
		else:
			return False


	def T(self):
		if self.F():
			if self._T():
				return True
			else:
				return True
		else:
			return False


	def _T(self):
		if self.tokens[self.current].classpart == 'MDR':
			self.current+=1
			self.F()
			self._T()
			return True
		else:
			return False

	def F(self):
		if self.tokens[self.current].word in ['true','false']:
			self.current+=1
			return True
		elif self.tokens[self.current].classpart == 'Identifier':
			self.current+=1
			return True
		elif self.tokens[self.current].classpart =='INC_DEC':
			self.current+=1
			return True
		elif self.CONST():
			return True
		elif self.tokens[self.current].word =='(' and self.tokens[self.current].word !='$':
			self.current+=1
			if self.OE():
				if self.tokens[self.current].word ==')' and self.tokens[self.current].word !='$':
					self.current+=1
					return True
		elif self.tokens[self.current].word == '!':
			self.current+=1
			if self.F():
				return True
			else:
				return False
		elif self.tokens[self.current].word == 'this':
			self.current+=1
			if self.tokens[self.current].word == '.':
				if self._THIS():
					return True
		elif self.tokens[self.current].word == 'super':
			self.current+=1
			if self.tokens[self.current].word == '.':
				if self._SUPER():
					return True
		else:
			return False


	def _THIS(self):
		kw=self.tokens[self.current]
		if kw.classpart == 'Identifier':
			self.current+=1
			if self.THIS_SUPER():
				return True
		return False
		

	def THIS_SUPER(self):
		if self.tokens[self.current]!= '$':
			if self.X():
				return True
			elif self.tokens[self.current]== '(':
				if self.ARGS2():
					if self.tokens[self.current]== ')':
						if self.tokens[self.current]== ';':
							if self.X():
								return True
					else:
						print(f") expected at line {self.tokens[self.current].lineNumber}")
			else:
				return False

	def _SUPER(self):
		kw=self.tokens[self.current]
		if kw.classpart == 'Identifier':
			self.current+=1
			if self.THIS_SUPER():
				return True
		return False

	def _F(self):
		return

	def _F_(self):
		return

	def __F_(self):
		pass


