import random
def play():

	print("\n\n*********************")
	print("Divination's game")
	print("*********************",end="\n\n")

	points = 1000

	number_secret = random.randrange(1,101)
	print(number_secret)

	print("What is the level of difficulty?")
	level = int(input(("\n (1) Easy \n (2) Normal \n (3) Hard \n>>>")))

	if(level == 1):
		number_of_attemps = 20
	elif(level == 2):
		number_of_attemps = 10
	elif(level == 3):
		number_of_attemps = 5

	roundada = 1

	for roundada in range(0,number_of_attemps):

		print("Attempt {} of {}".format(roundada,number_of_attemps)) # String interpolation, mas o valores devem ser str não int
		
		kick = input("Enter the secret numbet ")
		kick = int(kick)

		hit = number_secret == kick
		bigger   = kick > number_secret
		smaller   = kick < number_secret


		if(hit):
			print("You kicked right, you did {}".format(points))
			break
		else:
			if(bigger):
				print("Was the biggest secret number\n")
			elif(smaller): 
				print("Was the smallest secret number\n")
				lost_points = abs(number_secret - kick)
				points = points - lost_points

	print("End game")

if(__name__ == "__main__"):
	play()