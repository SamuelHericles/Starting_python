class Programa:
	def __init__(self, nome, ano):
		self._nome = nome.title()
		self.ano = ano
		self._likes = 0

	@property
	def likes(self):
		return self._likes
	
	def dar_likes(self):
		self._likes += 1

	@property
	def nome(self):
		return self._nome

	@nome.setter
	def nome(self, nome):
		self._nome = nome
	
	def __str__(self):
		return f'Nome: {self.nome} Likes: {self.likes}'

class Filme(Programa):
	# pass ->passando o statemet, passadno pro cima
	# _ -> não protege mas o programador perebe que essa var não poed ser alterada externamente
	# Suporta herança de mais de uma classe
	# Classe é coesa quando tem métodos que apenas fazem sua função, é bem definida sua função

	def __init__(self,nome,ano,duracao):
		super().__init__(nome,ano)
		self.duracao = duracao

	def __str__(self):
		return f'Nome: {self.nome} - {self.duracao} min - Likes: {self.likes}'

class Playlist(list):
	def __init__(self, nome, programa):
		self.nome = nome
		self._programa = programa

	# __getitem__ posso deixar uma lista da playlist iteravel
	# no python, não é preciso herdar de uma classe específica
	# para ter polimorfismo
	# Ducky tiping: se você quer um iteravel, deve-se preocupar
	#com o que um iterável deve fazer. Muito flexivel para não
	# ficar preso a tipos dos objetos.
	def __getitem__(self, item):
		return self._programa[item]

	# Mas em alguns momentos você vai querer ter restrições, como
	# uma garantia que uma classe implemente os métodos que você
	# quer. Para isso as ABC's, são métodos abstratos, que forçam
	# as classes filhas a implementar alguns métodos.



	@property	
	def listagem(self):
		return self._programa

	# @property
	# def tamanho(self):
	# 	return len(self._programa)
	# substitui o property tamanho
	def __len__(self):
		return len(self._programa)

class Serie(Programa):
 	def __init__(self, nome, ano, temporada):
 		super().__init__(nome, ano)
 		self.temporada = temporada

 	def __str__(self):
 	 	return f'Nome: {self.nome} - {self.temporada} temporadas - Likes:{self.likes}'



vingadores = Filme('vingadores - guerra infinita', 2018, 160)
atlanta = Serie('atlanta', 2018, 2)
tmep = Filme('todo mundo em planico', 1999, 100)
demolidor = Serie('demolidor', 2016, 2)

vingadores.dar_likes()
vingadores.dar_likes()
vingadores.dar_likes()
atlanta.dar_likes()
atlanta.dar_likes()
tmep.dar_likes()
tmep.dar_likes()
demolidor.dar_likes()
demolidor.dar_likes()

listinha = [atlanta,vingadores,tmep,demolidor]
minha_playlist = Playlist('fim de semana', listinha )
# apenas a minha_playlist não é uma iterable. coloque um super e init
# pois você reutiliza o init da super classe
for programa in minha_playlist.listagem:
	print(programa)
print(f'tamanho: {len(minha_playlist)}') # você fazer isso por causa do __len__