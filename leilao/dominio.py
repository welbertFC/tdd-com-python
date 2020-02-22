import sys

class Usuario:

    def __init__(self, nome, carteira):
        self._nome = nome
        self._carteira = carteira

    def propoem_lance(self, leilao, valor):
        if valor > self._carteira:
            raise ValueError('Valor acima da carteira')

        lance = Lance(self, valor)
        leilao.propoe(lance)
        self._carteira -= valor

    @property
    def carteira(self):
        return  self._carteira

    @property
    def nome(self):
        return self._nome

class Lance:

    def __init__(self, usuario, valor):
        self.usuario = usuario
        self.valor = valor

class Leilao:

    def __init__(self, decricao):
        self.descricao = decricao
        self.__lances = []
        self.maior_lance = sys.float_info.min
        self.menor_lance = sys.float_info.max

    def propoe (self, lance: Lance):
        if not self.__lances or self.__lances[-1].usuario != lance.usuario and lance.valor > self.__lances[-1].valor:
            if lance.valor > self.maior_lance:
                self.maior_lance = lance.valor
            if lance.valor < self.menor_lance:
                self.menor_lance = lance.valor
            self.__lances.append(lance)

        else:
            raise ValueError('Erro ao propor lance')

    @property
    def lances(self):
        return self.__lances[:]







