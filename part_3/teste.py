
def criar_conta(numero,titular,saldo,limte):
	conta = {"numero": numero, "titlular":titular, "saldo":saldo, "limite":limite}
	return conta

def deposita(conta,valor):
	conta["saldo"] += valor

def saca(conta,valor):
	conta["saldo"] -= valor

def extrato(conta):
	print("Saldo é {}".format(conta["saldo"]))

# mundo OO = dado e funcionalidade(comportamentos) andam juntos