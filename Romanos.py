import unittest
class NumerosRomanos(object):

    equivalencias = {
        1: "I",
        4: "IV",
        5: "V",
        9: "IX",
        10: "X",
        40: "XL",
        50: "L"
      }
    def convertir(self, n):
        keys = list(self.equivalencias.keys())
        subLista = []
        for i in keys:
            if n >= i:
                subLista.append(i)
        subLista.reverse()
        numero = n
        resultado = ""
        for j in subLista:
            resultado, numero = self.concatenarNumero(numero, j, resultado, self.equivalencias[j])

        return resultado

    def concatenarNumero(self, pNumero, pAux, pResultado, pSimbolo):
        resto = pNumero
        while resto >= pAux:
            pResultado += pSimbolo
            resto -= pAux
        return pResultado, resto

class NumerosRomanosTest(unittest.TestCase):
    def setUp(self):
        self.numeroRomano = NumerosRomanos()
    def test_diez(self):
        resultado = self.numeroRomano.convertir(10)
        self.assertEqual("X", resultado)
    def test_setentayocho(self):
        resultado = self.numeroRomano.convertir(78)
        self.assertEqual("LXXVIII", resultado)

    def test_uno(self):
         resultado = self.numeroRomano.convertir(1)
         self.assertEqual("I", resultado)
    def test_dos(self):
        resultado = self.numeroRomano.convertir(2)
        self.assertEqual("II", resultado)
    def test_tres(self):
        resultado = self.numeroRomano.convertir(3)
        self.assertEqual("III", resultado)
    def test_cuatro(self):
        resultado = self.numeroRomano.convertir(4)
        self.assertEqual("IV", resultado)
    def test_cinco(self):
        resultado = self.numeroRomano.convertir(5)
        self.assertEqual("V", resultado)
    def test_seis(self):
        resultado = self.numeroRomano.convertir(6)
        self.assertEqual("VI", resultado)
    def test_siete(self):
        resultado = self.numeroRomano.convertir(7)
        self.assertEqual("VII", resultado)
    def test_ocho(self):
        resultado = self.numeroRomano.convertir(8)
        self.assertEqual("VIII", resultado)
    def test_nueve(self):
        resultado = self.numeroRomano.convertir(9)
        self.assertEqual("IX", resultado)
    def test_once(self):
        resultado = self.numeroRomano.convertir(11)
        self.assertEqual("XI", resultado)
    def test_doce(self):
        resultado = self.numeroRomano.convertir(12)
        self.assertEqual("XII", resultado)
    def test_trece(self):
        resultado = self.numeroRomano.convertir(13)
        self.assertEqual("XIII", resultado)

if __name__ == '__main__':
    unittest.main()
'''
    1 -> I
    5 -> V
    10 -> X
    50 -> L
    100 -> C
    500 -> D
    1000 -> M
'''