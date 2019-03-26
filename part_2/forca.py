import random
def jogar():

	print("***************************")
	print("Bem vindo ao jogo da Forca!")
	print("***************************")


	arquivo = open("palavras.txt","r")
	palavras = []

	for linha in arquivo:
		linha = linha.strip()
		palavras.append(linha)
	
	arquivo.close()

	numero = random.randrange(0,len(palavras))
	palavra_secreta = palavras[numero].upper()

	letras_acertadas = ["_" for letra in palavra_secreta] # list compreenshions
	enforcou = False
	acertou = False 
	tentativas = 0

	print(letras_acertadas)

	#enquanto não acertou ou enforcou
	#enquanto (TRUE E TRUE)
	while(not acertou and not enforcou):
			chute = input('Digite uma letra\n>>> ')
			chute = chute.strip().upper()

			if(chute in palavra_secreta):
				index = 0
				for letra in palavra_secreta:				
					if(chute == letra):
						#print("Econtrei a letra {} a posição {}".format(letra,index))
						letras_acertadas[index] = letra # colcoar index para add ao indice e mostrar ele no print
					index = index + 1
			else:
				tentativas = tentativas + 1

			enforcou = tentativas == 6
			acertou = "_" not in letras_acertadas
			print(letras_acertadas)
	if(acertou):
		print("Você ganhou!")
	else:
		print("Você perdeu! a palavra era {}".format(palavra_secreta))
	print("Fim de jogo!")

if(__name__ == "__main__"):
	jogar()