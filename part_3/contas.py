#__init__ funções com dois underlines são chamadas de funções construtoras, são chamadas automaticamente
# A vairavel self é para recuperar o endeneço de memoria criado pela classe antes de chamar a função
# Se colocar limite=1000.0 isso se chama declaração padrão da função, pode ser editado
#Python tbm tem garbage coletor
# None é o null do python
# dois underline __ é para deixar o atributo com privado
# um bom código é refatorado com o tempo
# cada classe tem sua responsabilidade
# S - simples responsabilidade principal
# O - principio de open/closed
# L - Liskov principio de substituição
# I - principio de segregação da interface
# D - principio de inversão de independecia
# Sempre que criar uma função coloque em um objeto

class Conta:
	def __init__(self,numero,titular,saldo,limite):
		print("Construindo o objeto...".format(self))
		self.__numero = numero
		self.__titular = titular
		self.__saldo = saldo
		self.__limite = limite

	def extrato(self):
		print("Saldo de {} do titular {}".format(self.__saldo,self.__titular))

	def deposita(self,valor):
		self.__saldo += valor

	def saca(self,valor):
		self.__saldo -= valor

	def transfere(self,valor,destino):
		self.saca(valor)
		destino.deposita(valor)

	def get_saldo(self):
		return self.__saldo

	def get_titular(self):
		return self.__titular


	@property
	def get_limite(self):
		return self.__limite

	@limite.setter
	def set_limite(self,limite):
		self.__limite = limite
