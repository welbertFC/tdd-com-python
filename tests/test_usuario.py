from leilao.dominio import Usuario, Lance,Leilao
import pytest

from leilao.excecoes import LanceInvalido


@pytest.fixture
def joao():
    return Usuario('joao', 100.0)
@pytest.fixture
def leilao():
    return Leilao('celualr')

def test_deve_subtrair_valor_da_carteira_do_usuario_quando_este_propor_um_lance(joao,leilao):
    joao.propoem_lance(leilao, 50.0)
    assert joao.carteira == 50.0

def test_deve_permitir_propor_lance_quando_o_valor_e_menor_que_o_valor_da_carteira(joao,leilao):
    joao.propoem_lance(leilao, 1.0)
    assert joao.carteira == 99.0

def test_deve_permitir_propor_lance_quando_o_valor_e_igual_ao_da_carteira(joao,leilao):
    joao.propoem_lance(leilao, 100.0)
    assert joao.carteira == 0.0

def test_nao_deve_permitir_propor_lance_com_valor_maior_que_o_da_cateira(joao,leilao):
    with pytest.raises(LanceInvalido):
        joao.propoem_lance(leilao, 200.0)


