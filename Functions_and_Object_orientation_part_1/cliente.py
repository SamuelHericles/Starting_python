# PROPERTY @ form so you do not need to put (), make it readable

class Client:
	def __init__(self,name):
		self.name = name

	@property
	def name(self):
		print("Calling @property name()")
		return self.__name.title()

	@name.setter
	def name(self,name):
		print("Calling setter name()")
		self.__name = name