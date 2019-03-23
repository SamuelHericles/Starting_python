print("Olá mundo")
print("REComeçando")
print("************")

numero_secreto = 42

# print(type(chute)) -> descobrir o tipo da variavel, já o python tem tipagem forte

#Parse do python, diferente do Java que é usando valueOf e parseInt, temos:
#chute = int(chute) -> Reaproveitando variavéis

# Deve-se passar o tipo correto para haver a comparação, pois 42 está saindo com str

# O usuário vai escolhar quantas vezes quer tentar adivinhar o código
numero_de_tentativas = input("Quantas vezes você quer tentar?\n>>> ")
numero_de_tentativas = int(numero_de_tentativas) # no python3, o input sempre sai uma str
rodada = 1

while( rodada <= numero_de_tentativas):

	print("Tentativa ",rodada,"/",numero_de_tentativas)

	chute = input("Digite o número secreto:")
	chute = int(chute)

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
	rodada = rodada + 1	


print("Fim de jogo")
"""#QUAL A DIFERENLA DO PYTHON3 PARA O PYTHON2: 
	+O PRINT MUDOU E O INPUT SEMRPE SAI COM STRING PARA O PYTHON3
"""

