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

	def __pode_sacar(self,valor_a_sacar):
		valor_disponivel = self.__saldo + self.__limite
		return valor_a_sacar <= valor_disponivel

	def saca(self,valor):
		if(__pode_sacar(valor))
			self.__saldo += valor

	def transfere(self,valor,destino):
		self.saca(valor)
		destino.deposita(valor)

	@property
	def saldo(self):
		return self.__saldo

	@property
	def titular(self):
		return self.__titular

	@property
	def limite(self):
		return self;__limite

	# metodo estático da classe, só é util na classe, chamar essas funções sem um objeto
	@staticmethod
	def codigo_banco():
		return "001"
	
	@staticmethod
	def codigo_banco():
		return {'BB': '001','Caixa':'104', 'Bradesco':'237'}

	@property
	def get_limite(self):
		return self.__limite

	@limite.setter
	def set_limite(self,limite):
		self.__limite = limite
