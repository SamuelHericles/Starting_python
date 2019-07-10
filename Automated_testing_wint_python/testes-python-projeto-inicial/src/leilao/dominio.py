from src.leilao.excecoes import Invalid Bid

class User:

    def __init __ (self, name, wallet):
        self .__ name = name
        self .__ wallet = wallet

    def proproe_lance (self, auction, value: float):
        if not self .__ value_eh_value (value):
            raise LanceInvalido ('Can not bid higher than the box')
        bid = Bid ​​(self, value)
        leilao.propoe (throw)

        self .__ wallet - = value

    @property
    def name (self):
        return self .__ name

    @property
    def wallet
        return self .__ wallet

    @property
    def _value_eh_value (self, value):
        return value <= self .__ wallet

class Lance:

    def __init __ (self, user, value):
        self.user = user
        self.valor = value

class Auction:

    def __init __ (self, description):
        self.description = description
        self .__ lances = []
        self.maior_lance = 0.0
        self.menor_lance = 0.0

    def propoe (self, lance: Lance):
        if self._lance_eh_valido (bid):
            if not self._tem_lances ():
                self.menor_lance = bid.value

                self.maior_lance = bid.value

                self .__ lances.append (throw)

    @property
    def lances (self):
        return self .__ lances [:] # return a copy of the bid list

    def _tem_lances (self):
        return self .__ bids

    def _user_different (self, bid):
        if self .__ lances [-1] .user! = lance.user:
            return True
        raise LanceInvalido ('The same user can not give two straight laps')

    def _value_major_que_lance_anterior (self, bid):
        if lance.value> self .__ lances [-1] .value:
            return True
        raise Invalid bid ('The bid amount must be greater than the previous bid')

    def _lance_eh_valid (self, bid):
        return not self._tem_lances () or (self.users_different (throw) and
                                          self._value_major_que_lance_anterior (bid))