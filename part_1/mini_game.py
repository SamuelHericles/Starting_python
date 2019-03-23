print("Olá mundo")
print("REComeçando")
print("************")

numero_secreto = 42

# print(type(chute)) -> descobrir o tipo da variavel, já o python tem tipagem forte

#Parse do python, diferente do Java que é usando valueOf e parseInt, temos:
#chute = int(chute) -> Reaproveitando variavéis

# Deve-se passar o tipo correto para haver a comparação, pois 42 está saindo com str
"""
#QUAL A DIFERENLA DO PYTHON3 PARA O PYTHON2: 
	+O PRINT MUDOU E O INPUT SEMRPE SAI COM STRING PARA O PYTHON3

 #range é mais flexivel, e no for você não precisa usar parenteses , mas é aconselhavel
	rodada = 1
	for rodada in range(1,10):
		print(rodada,":)))")
	
	detalhe, só vai até o 9, ou seja, de 1 até 9
	caso coloque 1,10,2 o terceiro parâmetro vai dizer os passo para pular o laço, então seria 1,3,5,7,9 e fim do laço

"""



# O usuário vai escolhar quantas vezes quer tentar adivinhar o código
numero_de_tentativas = input("Quantas vezes você quer tentar?\n>>> ")
numero_de_tentativas = int(numero_de_tentativas) # no python3, o input sempre sai uma str
rodada = 1

# while( rodada <= numero_de_tentativas): -> caso fosse com while
for rodada in range(0,numero_de_tentativas):

	#print("Tentativa ",rodada,"/",numero_de_tentativas) ->  sem usar o format
	print("Tentativa {} de {}".format(rodada,numero_de_tentativas)) # String interpolation, mas o valores devem ser str não int
	print("Tentativa {1} de {0}".format(rodada,numero_de_tentativas)) # inverter os valores
	print("Tentativa {:.2f}".format(1.99)) #Pergar apenas duas casas decimais
	print("Tentativa {:44.2f}".format(21.99)) #Pegar apenas duas casas deciamis e 44 espaços de início
	print("Tentativa {:5.2f}".format(311.99)) #5.2 quer dizer que são 5 número e 2 decimais
	
	chute = input("Digite o número secreto:")
	chute = int(chute)

	# Melhorando a legibilidade do código, acertou, maior e menor são type bool
	acertou = numero_secreto==chute
	maior   = chute > numero_secreto
	menor   = chute < numero_secreto


	if(acertou):
		print("Você chutou certo")
		break #sai do laço
	else:
		if(maior):
			print("Foi maior que o número secreto")
		elif(menor): # ELIF é usado para quando tiver vários "se não" em uma cadeia de restrições
			print("Foi menor que o número secreto")
		print("Que pena, não foi")
	rodada = rodada + 1	


print("Fim de jogo")
