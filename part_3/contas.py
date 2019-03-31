#__init__ funções com dois underlines são chamadas de funções construtoras, são chamadas automaticamente
# A vairavel self é para recuperar o endeneço de memoria criado pela classe antes de chamar a função
# Se colocar limite=1000.0 isso se chama declaração padrão da função, pode ser editado
#Python tbm tem garbage coletor
# None é o null do python
class Conta:
	def __init__(self,numero,titular,saldo,limite):
		print("Construindo o objeto...".format(self))
		self.numero = numero
		self.titular = titular
		self.saldo = saldo
		self.limite = limite

	def extrato(self):
		print("Saldo de {} do titular {}".format(self.saldo,self.titular))

	def deposita(self,valor):
		self.saldo += valor

	def saca(self,valor):
		self.saldo += valor