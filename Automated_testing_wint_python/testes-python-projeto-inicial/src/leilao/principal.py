from src.leilao.dominio import User, Bid, Auction, Appraiser

gui = User ('Gui')
yuri = User ('Yuri')

lance_do_yuri = Lance (yuri, 100.0)
lance_do_gui = Bid (gui, 150.0)

auction = Auction ('Mobile')

leilao.lances.append (lance_do_yuri)
leilao.lances.append (lance_do_gui)

for lance in leilao.lances:
     print (f'The user {lance.user.name} gave a bid of {lance.value} ')

appraiser = Appraiser ()
appraiser.avalia (auction)

print (f'The lowest bid was {appraiser.menor_lance} and the highest bid was {appraiser.major_lance})