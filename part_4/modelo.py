class Programa:
	@property
	def likes(self):
		return self. __likes
	
	def dar_likes(self):
		self.__likes += 1

	@property
	def nome(self):
		return self.__nome

	@nome.setter
	def nome(self,nome):
		self.__nome = nome
	

class Filme(Programa):
	#pass ->passando o statemet, passadno pro cima
	# _ -> não protege mas o programador perebe que essa var não poed ser alterada externamente
	def __init__(self,nome,ano,duracao):
		self._nome = nome.title()
		self.ano = ano
		self.duracao = duracao
		self._likes = 0

class Serie(Programa):
	def __init__(self,nome,ano,temporada):
		self._nome = nome.title()
		self.ano = ano
		self.temporada = temporada
		self._likes = 0

	vingadores = Filme("Vingadores - guerra infinita",2018,160)
	vingadores.dar_like()
	print(f'Nome: {vingadores.nome} - Ano:{vingadores.ano}'
		  f'- Duracao: {vingadores.duracao} - Likes {vingadores.likes}')

	
	atlanta = Serie("atlanta",2018,2)
	print(f'Nome:{atlanta.nome} - Ano: {atlanta.ano}' 
		  f'-Tempordas:{atlanta.temporada} - Likes {atlanta.likes}')