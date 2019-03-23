print("Olá mundo")
print("REComeçando")
print("************")

numero_secreto = 42
chute = input("Digite o número secreto:")

# print(type(chute)) -> descobrir o tipo da variavel, já o python tem tipagem forte

#Parse do python, diferente do Java que é usando valueOf e parseInt, temos:
chute = int(chute) #Reaproveitando variavéis

# Deve-se passar o tipo correto para haver a comparação, pois 42 está saindo com str
# Melhorando a legibilidade do código, acertou, maior e menor são type bool
acertou = numero_secreto==chute
maior   = chute > numero_secreto
menor   = chute < numero_secreto
if(acertou):
	print("Você chutou certo")
else:
	if(maior):
		print("Foi maior que o número secreto")
	elif(menor): # ELIF é usado para quando tiver vários "se não" em uma cadeia de restrições
		print("Foi menor que o número secreto")
	print("Que pena, não foi")


print("Fim de jogo")
"""#QUAL A DIFERENLA DO PYTHON3 PARA O PYTHON2: 
	+O PRINT MUDOU E O INPUT SEMRPE SAI COM STRING PARA O PYTHON3
"""

