class Program:
	def __init __ (self, name, year):
		self._name = name.title ()
		self.ano = year
		self._likes = 0

	@property
	def likes (self):
		return self._likes

	def dar_likes (self):
		self._likes + = 1

	@property
	def name (self):
		return self._name

	@ name.setter
	def name (self, name):
		self._name = name

	def __str __ (self):
		return f'Name: {self.name} Likes: {self.likes} '

class Movie (Program):
# pass -> passing the statemet, pass up to the top
# _ -> does not protect but the programmer did not want this var to be altered externally
# Supports inheritance from more than one class
# Class is cohesive when it has methods that only do its function, its function is well defined

	def __init __ (self, name, year, duration):
		super () .__ init __ (name, year)
		self = duration = duration

	def __str __ (self):
		return f'Name: {self.name} - {self.duration} min - Likes: {self.likes} '

class Playlist (list):
	def __init __ (self, name, program):
		self.name = name
		self._program = program

# __getitem__ I can leave an iteravel playlist list
# in python, you do not need to inherit from a specific class
# to have polymorphism
# Ducky tiping: if you want an iteravel, you should worry
#to what an iterable thing to do. Very flexible not to
# get stuck to types of objects.
	def __getitem __ (self, item):
		return self._program [item]

# But in some moments you will want to have restrictions, like
# a guarantee that a class implements the methods you
# would you like. ABC's are abstract methods that
# Daughter classes to implement some methods.

	@property
	def listing:
		return self._program

# @property
# def size (self):
# return len (self._program)
# replaces the property size
	def __len __ (self):
		return len (self._program)

class Program:
 def __init __ (self, name, year, season):
	 super () .__ init __ (name, year)
	 self season = season

 def __str __ (self):
	 return f'Name: {self.name} - {self.year} seasons - Likes: {self.likes} '

Avengers = Movie ('Avengers - Infinite War', 2018, 160)
atlanta = Series ('atlanta', 2018, 2)
tmep = Movie ('everybody in plan', 1999, 100)
demolisher = Series ('demolisher', 2016, 2)

avengers.dar_likes ()
avengers.dar_likes ()
avengers.dar_likes ()
atlanta.dar_likes ()
atlanta.dar_likes ()
tmep.dar_likes ()
tmep.dar_likes ()
demolidor.dar_likes ()
demolidor.dar_likes ()

listinha = [atlanta, avengers, tmep, demolidor]
my_playlist = Playlist ('weekend', list)

# only my_playlist is not an iterable one. put a super and init
# because you reuse super class init
for program in my_playlist.liste:
	print (program)
	print (f'tamanho: {len (minha_playlist)} ') # you do this because of __len__