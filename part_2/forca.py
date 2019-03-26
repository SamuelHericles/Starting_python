import random
def jogar():

	abertura()
	palavra_secreta = escolhe_a_palavra_secreta()
	letras_acertadas =cria_lista_lacuna(palavra_secreta) 

	enforcou = False
	acertou = False 
	tentativas = 0

	print(letras_acertadas)
	#enquanto não acertou ou enforcou
	#enquanto (TRUE E TRUE)
	while(not acertou and not enforcou):

			chute = pede_chute()

			if(chute in palavra_secreta):
				marca_chute_correto(chute,palavra_secreta,letras_acertadas)
			else:
				tentativas += 1
				desenha_forca(tentativas)

			enforcou = tentativas == 7
			acertou = "_" not in letras_acertadas
			print(letras_acertadas)
	if(acertou):
		imprime_mensagem_vencedor()
	else:
		imprime_mensagem_perdedor(palavra_secreta)


def imprime_mensagem_perdedor(palavra_secreta):
    print("Puxa, você foi enforcado!")
    print("A palavra era {}".format(palavra_secreta))
    print("    _______________         ")
    print("   /               \       ")
    print("  /                 \      ")
    print("//                   \/\  ")
    print("\|   XXXX     XXXX   | /   ")
    print(" |   XXXX     XXXX   |/     ")
    print(" |   XXX       XXX   |      ")
    print(" |                   |      ")
    print(" \__      XXX      __/     ")
    print("   |\     XXX     /|       ")
    print("   | |           | |        ")
    print("   | I I I I I I I |        ")
    print("   |  I I I I I I  |        ")
    print("   \_             _/       ")
    print("     \_         _/         ")
    print("       \_______/           ")



def imprime_mensagem_vencedor():
    print("Parabéns, você ganhou!")
    print("       ___________      ")
    print("      '._==_==_=_.'     ")
    print("      .-\\:      /-.    ")
    print("     | (|:.     |) |    ")
    print("      '-|:.     |-'     ")
    print("        \\::.    /      ")
    print("         '::. .'        ")
    print("           ) (          ")
    print("         _.' '._        ")
    print("        '-------'       ")

def desenha_forca(erros):
    print("  _______     ")
    print(" |/      |    ")

    if(erros == 1):
        print(" |      (_)   ")
        print(" |            ")
        print(" |            ")
        print(" |            ")

    if(erros == 2):
        print(" |      (_)   ")
        print(" |      \     ")
        print(" |            ")
        print(" |            ")

    if(erros == 3):
        print(" |      (_)   ")
        print(" |      \|    ")
        print(" |            ")
        print(" |            ")

    if(erros == 4):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |            ")
        print(" |            ")

    if(erros == 5):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |            ")

    if(erros == 6):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |      /     ")

    if (erros == 7):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |      / \   ")

    print(" |            ")
    print("_|___         ")
    print()

def marca_chute_correto(chute,palavra_secreta,letras_acertadas):
	index = 0
	for letra in palavra_secreta:				
		if(chute == letra):
			#print("Econtrei a letra {} a posição {}".format(letra,index))
			letras_acertadas[index] = letra # colcoar index para add ao indice e mostrar ele no print
		index +=1
	

def pede_chute():
	chute = input('Digite uma letra\n>>> ')
	return chute.strip().upper()

def abertura():
	print("*************************************")
	print("*****Bem vindo ao jogo da Forca!*****")
	print("*************************************")

def escolhe_a_palavra_secreta():
	arquivo = open("palavras.txt","r")
	palavras = []

	for linha in arquivo:
		linha = linha.strip()
		palavras.append(linha)
	
	arquivo.close()

	numero = random.randrange(0,len(palavras))
	return palavras[numero].upper()

def cria_lista_lacuna(palavra):
	return ["_" for letra in palavra] # list compreenshions

if(__name__ == "__main__"):
	jogar()