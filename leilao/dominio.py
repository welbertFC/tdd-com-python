
class Usuario:

    def __init__(self, nome, carteira):
        self._nome = nome
        self._carteira = carteira

    def propoem_lance(self, leilao, valor):
        if self._valor_eh_valido(valor):
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

    def _valor_eh_valido(self, valor):
        return valor > self._carteira


class Lance:

    def __init__(self, usuario, valor):
        self.usuario = usuario
        self.valor = valor

class Leilao:

    def __init__(self, decricao):
        self.descricao = decricao
        self.__lances = []
        self.maior_lance = 0.0
        self.menor_lance = 0.0

    def propoe (self, lance: Lance):
        if self._lance_eh_valido(lance):
            if not self._tem_lances():
                self.menor_lance = lance.valor
            self.maior_lance = lance.valor
            self.__lances.append(lance)

        else:
            raise ValueError('Erro ao propor lance')

    @property
    def lances(self):
        return self.__lances[:]

    def _tem_lances(self):
        return self.__lances

    def _usuarios_diferentes(self, lance):
        return self.__lances[-1].usuario != lance.usuario

    def _valor_maior_que_lance_anterior(self, lance):
        return lance.valor > self.__lances[-1].valor

    def _lance_eh_valido(self,lance):
        return not self._tem_lances() or (self._usuarios_diferentes(lance) and
                                          self._valor_maior_que_lance_anterior(lance))







