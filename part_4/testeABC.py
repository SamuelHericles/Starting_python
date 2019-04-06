# teste com classes abstratas
from collections.abc import MutableSequence

#python é uma lingaguem com tipagem dinamica, não é dever dele de avisar
#para implementar os métodos estáticos.
#o que se pode fazer é validar métodos em tempo de instanciação.
class MinhaListinhaMutavel(MutableSequence):
	pass

# dá erro porque esqueceu de implementar os métodos necessários para
# tornar a classe uma MutableSequence
objatoValidado = MinhaListinhaMutavel()
print(objatoValidado)

