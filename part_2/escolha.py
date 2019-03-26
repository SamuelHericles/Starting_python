import forca
import mini_game

# PYTHON É INTERPRETADO E C É COMPILADO
# NO PYTHON É DIRETO EXECUTADO, PODE RODAR EM QUALQUER SO, COMPILA AO VIVO, MAS É UMA HIBRIDA DE COMPILAÇÃO E INTERPRETAÇÃO
# NO C PRECISO CRIAR UM EXECUTAVEL POIS JÁ FOI COMPILADO, ENTÃO É PRECISO RECOMPILAR EM OUTRO SO



def escolha_jogo():
	print("***************************")
	print("Escolha seu jogo!")
	print("***************************")

	print("\n (1)Forca \n (2)Adivinhação")
	jogo = int(input("Qual você quer?\n>>>"))

	if(jogo == 1):
		forca.jogar()
	elif(jogo == 2):
		mini_game.jogar()

if(__name__ == "__main__"):# saber se é o arquivo prinicipal ou não
	escolha_jogo()