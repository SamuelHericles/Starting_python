import forca
import mini_game

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