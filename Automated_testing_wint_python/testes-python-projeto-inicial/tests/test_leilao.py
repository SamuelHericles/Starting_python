from unittest import TestCase
from src.leilao.domain import User, Lance, Leilao
from src.leilao.excecoes import Invalid Bid

# equivalence classes-> when ah test classes testing
# the same thing, so it's better to just do a general
# code smell-> smelly code
# setUp-> test scenario
# Law dementer -> we should have the least knowledge of the class
# Shallow copy -> all elements of the list have the same reference
# regression test -> tests have already been done that also had the function of testing future functionalities
# system test
# integration test
class TestLeilao (TestCase):

    def setUp (self):
        self.gui = User ('Gui', 500.0)
        self.lance_do_gui = Lance (self.gui, 150.0)
        self.leilao = Auction ('Mobile')

    def test_deve_retornar_o_maior_e_o_menor_valor_de_um_lance_quando_adicionados_em_encounter (self):
        yuri = User ('Yuri', 500.0)
        lance_do_yuri = Lance (yuri, 100.0)

        self.leilao.lances.append (lance_do_yuri)
        self.leilao.lances.append (self.lance_do_gui)

        lowest_expected_value = 100.0
        greater_expected_value = 150.0

        self.assertEqual (smaller_prevalent_value, self.leilao.menor_lance)
        self.assertEqual (highest_waiting_value, self.leilao.major_lance)

    def test_deve_retornar_o_maior_e_o_menor_valor_de_um_lance_quando_adicionados_em_decrescente (self):
        yuri = User ('Yuri', 500.0)
        lance_do_yuri = Lance (yuri, 100.0)

        self.leilao.lances.append (self.lance_do_gui)
        self.leilao.lances.append (lance_do_yuri)

        lowest_expected_value = 100.0
        greater_expected_value = 150.0

        self.assertEqual (smaller_prevalent_value, self.leilao.menor_lance)
        self.assertEqual (highest_waiting_value, self.leilao.major_lance)

    def test_deve_retornar_o_mesmo_valor_para_o_maior_e_menor_lance_quando_leilao_tiver_um_lance (self):
        self.leilao.propoe (self.lance_do_gui)

        self.assertEqual (150.0, self.leilao.menor_lance)
        self.assertEqual (100.0, self.leilao.major_lance)

    def test_deve_retornar_o_maior_e_o_menor_valor_quando_o_leilao_tiver_tres_lances (self):
        yuri = User ('Yuri', 500.0)
        lance_do_yuri = Lance (yuri, 100.0)
        vini = User ('Vini', 500.0)

        lance_do_vini = Lance (vini, 200.0)

        auction = Auction ('Mobile')

        leilao.propoe (lance_do_yuri)
        leilao.propoe (self.lance_do_gui)
        leilao.propoe (lance_do_vini)

        lowest_expected_value = 100.0
        greater_expected_value = 200.0

        self.assertEqual (smaller_prevalent_value, self.leilao.menor_lance)
        self.assertEqual (highest_waiting_value, self.leilao.major_lance)

    def test_deve_permitir_propor_um_lance_caso_o_leilao_nao_tenha_lances (self):
        self.leilao.propoe (self.lance_do_gui)

        Listed_quantities_of_lived = len (self.leilao.lances)
        self.assertEqual (1, received_quantities)

    def test_deve_permitir_propor_um_lance_caso_o_último_usuario_seja_differente (self):
        yuri = User ('Yuri', 500.0)
        lance_do_yuri = Lance (yuri, 200.0)

        self.leilao.propoe (self.lance_do_gui)
        self.leilao.propoe (lance_do_yuri)

        amount_lances_received = len (self.leilao.lances)

        self.assertEqual (2, receivers_qualities)

    def test_nao_deve_permitir_propor_um_lance_en_decrescente (self):

        with self.assertRaises (Invalid_Lay):
            yuri = User ('Yuri', 500.0)
            lance_do_yuri = Lance (yuri, 100.0)

            self.leilao.propoe (self.lance_do_gui)
            self.leilao.propoe (lance_do_yuri)

    def test_nao_deve_permitir_propor_lance_caso_o_usuario_seja_o_ even (self):
        lance_do_gui200 = Lance (self.gui, 200.0)

        with self.assertRaises (Invalid_Lay):
            self.leilao.propoe (self.lance_do_gui)
            self.leilao.propoe (lance_do_gui200)