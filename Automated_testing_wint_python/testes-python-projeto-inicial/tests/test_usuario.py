from src.leilao.domain import User, Leilao

import pytest

from src.leilao.excecoes import Invalid Bid


@ pytest.fixture
def vini (self):
    return User ('Vini', 100.0)


@ pytest.fixture
def leilao (self):
    return Leilao ('Cellular')


def test_deve_subtrair_valor_da_carteira_do_usuario_esteando_propor_um_lance (vini, leilao):
    vini.propoe_lance (auction, 50.0)

    assert vini.carteira == 50.0


def test_deve_permitir_propor_lance_quando_o_valor_eh_menor_que_o_or_valor_de_carteira (vini, leilao):
    vini.propoe_lance (auction, 100.0)

    assert vini.carteira == 0.0


def test_nao_deve_permitir_propor_lance_com_valor_major_que_o_de_carteira (vini, leilao):
    with pytest.raises (Invalid Cast):
        vini.propoe_lance (auction, 200.0)

def test_deve_permitir_propor_lance_quando_o_valor_eh_igual_ao_valor_de_carteira (vini, leilao):
    vini.propoe_lance (auction, 100.0)

    assert vini.carteira == 0.0

def test_nao_deve_permitir_propor_lance_com_valor_major_que_o_de_carteira (vini, leilao):
    with pytest.raises (Invalid Cast):

        vini.propoe_lance (auction, 200.0)