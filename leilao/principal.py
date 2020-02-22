from leilao.dominio import Usuario, Lance, Leilao


welbert = Usuario('welbert')
yuri = Usuario('yuri')

lance_do_yuri = Lance(yuri,200.0)
lance_do_welbert = Lance(welbert, 350.0)

leilao = Leilao('Celular')

leilao.lances.append(lance_do_yuri)
leilao.lances.append(lance_do_welbert)


for lance in leilao.lances:
    print(f'O Usuario {lance.usuario.nome}  deu um lançe de {lance.valor}')

avaliador = Avaliador()

avaliador.avalia(leilao)

print(f'o menor lance foi de {avaliador.menor_lance} o maior lance foi de {avaliador.maior_lance}')