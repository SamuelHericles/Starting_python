'''

  - __init__ functions with two underlines are called constructor functions, they are called automatically
  - The vairavel self is to retrieve the memory endenegment created by the class before calling the function
  - If put limit = 1000.0 this is called the standard declaration of the function, can be edited
  - Python tbm has garbage collector
  - None is the null of python
  - Two underline __ is to leave the attribute private
  - A good code is refactored with time
  - Each class has its responsibility
  - SOLID is:
		S - simple primary responsibility
		O - open / closed principle
		L - Liskov replacement principle
		I - principle of interface segregation
		D - principle of reversal of independence
	Whenever you create a function place on an object

'''
class Account:
	def __init__(self,numero,titular,saldo,limite):
		print("Construindo o objeto...".format(self))
		self .__ number = number
		self .__ holder = holder
		self .__ balance = balance
		self .__ limit = limit

	def extract (self):
		print ("Balance of the holder's {}"). format (self .__ balance, self .__ holder))

	def deposit (self, value):
		self .__ balance + = value

	def __pode_sacar (self, value_a_sacar):
		available_value = self .__ balance + self .__ limit
		return value_a_sacar <= available_value

	def out (self, value):
		if (__ can_sacar (value))
		self .__ balance + = value

	def transfers (self, value, destination):
		self.saca (value)
		destination.deposita (value)

	@property
	def balance (self):
		return self .__ balance

	@property
	def (self):
		return self .__ holder

	@property
	def limit (self):
		return self;

	# static class method, only useful in class, call these functions without an object
	@staticmethod
	def bank_code ():
		return "001"

	@staticmethod
	def bank_code ():
		return {'BB': '001', 'Cash': '104', 'Bradesco': '237'}

	@property
	def get_limite (self):
		return self .__ limit

	@ limit.setter
	def set_limite (self, limit):
		self .__ limit = limit