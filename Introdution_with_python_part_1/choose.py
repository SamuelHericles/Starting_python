import forca
import mini_game

'''
 - PYTHON IS INTERPRETED AND C IS COMPILED
 - NO PYTHON IS DIRECT EXECUTED, CAN ROTATE ON ANY SO, COMPILATES LIVE, BUT IT 
   IS A HYBRID OF COMPILATION AND INTERPRETATION
 - DO NOT C CREATE AN EXECUTABLE SINCE IT HAS BEEN COMPILED, THEN YOU NEED TO RECOMPILATE ON
   ANOTHER SO
'''

def choose_game():
	print("***************************")
	print("Chose your game!")
	print("***************************")

	print("\n (1)Hangman \n (2)Divination")
	jogo = int(input("What do you want?\n>>>"))

	if(jogo == 1):
		forca.play()
	elif(jogo == 2):
		mini_game.play()

if(__name__ == "__main__"):#Like this you know if this file is main
	choose_game()