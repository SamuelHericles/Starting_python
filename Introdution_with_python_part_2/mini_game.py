import random
def play():

	print("\n\n*********************")
	print("Divination's game")
	print("*********************",end="\n\n")

'''
	print (type (kick)) -> find the type of the variable, since python has strong typing

	- Parse of python, different from Java that is using valueOf and parseInt, we have:
	- kick = int (kick) -> Reaproveitando variavéis
	- You must pass the correct type to make the comparison because 42 is leaving with str
	- QUALIFYING THE PYTHON3 DIFFERENTIAL FOR PYTHON2:
	  + PRINT CHANGED AND INPUT SEMRPE COMES OUT WITH STRING FOR PYTHON3
	- range is more flexible, and you do not have to use parentheses, but it's advisable
	  
	  round = 1
	  for round in range (1.10):
	  print (round, ":)))")

    detail, only goes to 9, that is, from 1 to 9 if you place 1,10,2 the third 
    parameter will tell the steps to jump the loop, then it would be 1,3,5,7,9 and loop end
	- interger division: 3 // 2, returns an integer without rounding

'''

	# Starting Points
	points = 1000

	# intervalor to generate the numbers from 1 to 100
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

	# while (round <= number_of_tentatives): -> if it was with while
	for roundada in range(0,number_of_attemps):

		#print ("Attempt", rounded, "/", number_of_tentatives) -> without using format
		print("Attempt {} of {}".format(roundada,number_of_attemps)) # String interpolation, mas o valores devem ser str não int
		
		kick = input("Enter the secret numbet ")
		kick = int(kick)

		# Improving code readability, hit, bigger and smaller are type bool
		hit = number_secret == kick
		bigger   = kick > number_secret
		smaller   = kick < number_secret


		if(hit):
			print("You kicked right, you did {}".format(points))
			break #sai do laço
		else:
			if(bigger):
				print("Was the biggest secret number\n")

			# ELIF is used for when you have multiple "if not" in a string of constraints
			elif(smaller):
				print("Was the smallest secret number\n")
				lost_points = abs(number_secret - kick)
				points = points - lost_points


	print("End game")

'''
	- ALL THOSE FUNCTIONS WE STUDY SEE IN BUILD-IN, OR BETTER ARE BASIC FUNCTIONS 
	  FOR PRIMARY CONTACT WITH PYTHON
	- Java libbiotecas are libraries, but in python it's called modules
'''

if(__name__ == "__main__"):# to control execution, if call function, vairavel __name__ is populated by __main__
	#__name__ and __main__ are the engines of python
	play() # With this I can execute the file without needing the file choice.py