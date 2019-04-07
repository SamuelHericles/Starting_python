from dominio import Leilao,Usuario,Lance,Avaliador

gui = Usuario('Gui')
yuri = Usuario('Yuri')

lance_do_yuri = Lance(yuri,100.0)
lance_do_gui = Lance(gui,150.0)

leilao = Leilao('Celular')

leilao.lances.append(lance_do_gui)
leilao.lances.append(lance_do_yuri)

for lance in leilao.lances:
	print(f'O usuario {lance.usuario.nome} deu um lance de {lance.valor}')

avaliador = Avaliador()
avaliador.avalia(leilao)

print(f'Maior lance: {avaliador.maior_lance}')
print(f'Menor lance: {avaliador.menor_lance}')