from unittest import TestCase

from leilao.dominio import Usuario, Lance, Leilao


class TestLeilao(TestCase):

    def setUp(self):
        self.welbert = Usuario('welbert', 500)
        self.lance_do_welbert = Lance(self.welbert, 350.0)
        self.leilao = Leilao('Celular')

    def test_deve_retornar_o_maior_e_o_menor_valor_de_um_lance_quando_adicionados_em_ordem_crescente(self):
        yuri = Usuario('yuri', 500)
        lance_do_yuri = Lance(yuri, 200.0)

        self.leilao.propoe(lance_do_yuri)
        self.leilao.propoe(self.lance_do_welbert)



        menor_valor_esperado = 200.0
        maior_valor_esperado = 350.0

        self.assertEqual(menor_valor_esperado, self.leilao.menor_lance)
        self.assertEqual(maior_valor_esperado, self.leilao.maior_lance)

    def test_nao_deve_permitir_propor_um_lance_em_ordem_descescente(self):
        with self.assertRaises(ValueError):
            yuri = Usuario('yuri', 500)
            lance_do_yuri = Lance(yuri, 100.0)
            self.leilao.propoe(self.lance_do_welbert)
            self.leilao.propoe(lance_do_yuri)

            # yuri = Usuario('yuri')
            # lance_do_yuri = Lance(yuri, 200.0)
            # self.leilao.propoe(self.lance_do_welbert)
            # self.leilao.propoe(lance_do_yuri)
            #
            #
            #
            # menor_valor_esperado = 200.0
            # maior_valor_esperado = 350.0
            #
            # self.assertEqual(menor_valor_esperado,self.leilao.menor_lance)
            # self.assertEqual(maior_valor_esperado,self.leilao.maior_lance)

    def test_deve_retornar_o_mesmo_valor_para_o_maior_e_menor_lance_quando_leilao_tiver_um_lance(self):


        self.leilao.propoe(self.lance_do_welbert)



        self.assertEqual(350.0, self.leilao.maior_lance)
        self.assertEqual(350.0, self.leilao.maior_lance)

    def test_deve_retornar_o_maior_e_o_menor_valor_quando_o_leilao_tiver_tres_lances(self):
        yuri = Usuario('yuri', 500)
        lance_do_yuri = Lance(yuri, 200.0)
        marcos = Usuario('marcos', 500)
        lance_do_marcos = Lance(marcos, 400)
        self.leilao.propoe(lance_do_yuri)
        self.leilao.propoe(self.lance_do_welbert)
        self.leilao.propoe(lance_do_marcos)



        menor_valor_esperado = 200.0
        maior_valor_esperado = 400.0

        self.assertEqual(menor_valor_esperado, self.leilao.menor_lance)
        self.assertEqual(maior_valor_esperado, self.leilao.maior_lance)



    def test_deve_permiti_propor_um_lance_caso_o_leilão_não_tenha_lance(self):
        self.leilao.propoe(self.lance_do_welbert)
        quantiade_de_lances_recebidas = len(self.leilao.lances)
        self.assertEqual(1, quantiade_de_lances_recebidas)

    # se o ultimo usuario for diferene deve permitir propor o lance
    def test_deve_permitir_propor_um_lance_caso_o_ultimo_usuario_seja_diferente(self):
        joao = Usuario('joao', 500)
        lance_do_joao = Lance(joao,200.0)
        self.leilao.propoe(lance_do_joao)
        self.leilao.propoe(self.lance_do_welbert)
        quantidade_de_lances_recebido = len(self.leilao.lances)
        self.assertEqual(2, quantidade_de_lances_recebido)

    # se o ultimo usuariu for o mesmo, não deve permitir propor o lance

    def test_nao_deve_permitir_propor_lance_caso_o_usuario_seja_o_mesmo(self):
        lance_do_welberrt = Lance(self.welbert, 350)

        with self.assertRaises(ValueError):
            self.leilao.propoe(self.lance_do_welbert)
            self.leilao.propoe(lance_do_welberrt)



        # try:
        #     self.leilao.propoe(self.lance_do_welbert)
        #     self.leilao.propoe(lance_do_welberrt)
        #     self.fail(msg='Não Lançou exceção')
        # except ValueError:
        #     quantidade_de_lances_recebidos = len(self.leilao.lances)
        #     self.assertEqual(1, quantidade_de_lances_recebidos)