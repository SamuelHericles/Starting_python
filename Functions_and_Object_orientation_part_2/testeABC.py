# test with abstract classes
from collections.abc import MutableSequence

#python is a dynamically typed language, it is not his duty to warn
#to implement static methods.
# What you can do is validate methods at instantiation time.
class MyMyList (MutableSequence):
	pass

# gives error because you forgot to implement the methods needed to
# make the class a MutableSequence
objatoValidado = MyLanguageMutavel ()
print (objatoValidado)