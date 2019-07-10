import random
def play():

	abertura()
	secret_word = choose_word_secret()
	right_lyrics =create_list_gap(secret_word) 

	hanged = False
	hit = False 
	attmeps = 0

	print(right_lyrics)
	#while not right or hanged
	#while (TRUE and TRUE)
	while(not hit and not hanged):

			kick = ask_kick()

			if(kick in secret_word):
				correct_kick(kick,secret_word,right_lyrics)
			else:
				attempts += 1
				draws_hangman(attempts)

			hanged = attempts == 7
			hit = "_" not in right_lyrics
			print(right_lyrics)
	if(hit):
		print_winning_message()
	else:
		print_lost_message(secret_word)


def print_lost_message(secret_word):
    print("Sorry, you was hanged!")
    print("The word was {}".format(secret_word))
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



def print_winning_message():
    print("Congratulations, you are winner!")
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

def draws_hangman(erros):
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

def correct_kick(kick,secret_word,right_lyrics):
	index = 0
	for letter in secret_word:				
		if(kick == letter):
            # put index to add to index and show it in print
			right_lyrics[index] = letter
		index +=1
	

def ask_kick():
	kick = input('Digite uma letter\n>>> ')
	return kick.strip().upper()

def opening():

    print("***************************")
    print("Welcome to the hangman game")
    print("***************************")

def choose_word_secret():
	file = open("words.txt","r")
	words = []

	for line in file:
		line = line.strip()
		words.append(line)
	
	file.close()

	number = random.randrange(0,len(words))
	return words[number].upper()

def create_list_gap(word):
	return ["_" for letter in word] # list compreenshions

if(__name__ == "__main__"):
	play()