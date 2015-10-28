import decimal as dec
 
 
class Coinpurse:
    def __init__(self, usd, q, d, n, p):
        self._usd = usd
        self._q = q
        self._d = d
        self._n = n
        self._p = p
 
    @property
    def total(self):
        self._total = dec.Decimal(self._usd +
                                  .25 * self._q +
                                  .1 * self._d +
                                  .05 * self._n +
                                  .01 * self._p).quantize(dec.Decimal('.01'))
        return self._total
 

class Bank:
    def __init__(self, name):
        self._name = name
        self._accounts = {}

    @property
    def largest(self):
        return "Largest account"

    @property
    def grand_total(self):
        gt = 0
        for key in self._accounts:
            gt += self._accounts[key].balance
        return gt



