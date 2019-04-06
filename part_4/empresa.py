# Arquivo onde vai ter herança de duas classes
class Funcionario:
	def __init__(self,nome):
		self.nome =  nome

	def registra_horas(self, horas):
		print('Horas registradas')

	def mostrar_tarefas(self):
		print('Fez muita coisa...')

class Caelum(Funcionario):
	def mostrar_tarefas(self):
		print('Fez muita coisa,Caelumer')

	def busca_cursos_do_mes(self, mes=None):
		print(f'Monstrando cursos - {mes}' if mes else'Mostrando cursos desse mês')

class Alura(Funcionario):
	def mostrar_tarefas(self):
		print('Fez muita coisa, Alurete!')

	def busca_perguntas_sem_respostas(self):
		print('Mostrnado perguntas não respondidas do fórum')

#Mixins, é quando você tem aspectos não-funcionais usados por 
# multiplas classes.
class Hipster:
	def __str__(self):
		return f'Hipster, {self.nome}'


class Junior(Alura,Hipster):
	pass

class Pleno(Alura, Caelum,Hipster):
	pass

jose = Junior('José')
jose.busca_perguntas_sem_respostas()
print(jose)

luan = Pleno('Luan')
luan.busca_perguntas_sem_respostas()
luan.busca_cursos_do_mes()
luan.mostrar_tarefas()
print(luan)