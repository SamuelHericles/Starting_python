# File where you will have inheritance of two classes
class Officer:
	def __init __ (self, name):
		self.name = name

	def register_hours (self, hours):
		print ('Registered Hours')

	def show_tasks (self):
		print ('Did a lot ...')

class Caelum (Official):
	def show_tasks (self):
	print ('Did a lot, Caelumer')

	def search_paths (self, month = None):
		print (f'Monstrando courses - {mes} 'if mes else'Mostrando courses of this month')

class Alura (Official):
	def show_tasks (self):
		print ('You did a lot, Alurete!')

	def search_questions_in_responses (self):
		print ('Display unanswered questions from the forum')

#Mixins, is when you have non-functional aspects used by
# multiple classes.
class Hipster:
	def __str __ (self):
		return f'Hipster, {self.name} '

class Junior (Alura, Hipster):
	pass

class Full (Alura, Caelum, Hipster):
	pass

jose = Junior ('José')
jose.busca_preferred_questions ()
print (jose)

luan = Full ('Luan')
luan.busca_preferred_questions ()
luan.busca_cursos_do_mes ()
luan.astrar_tasks ()
print (luan)