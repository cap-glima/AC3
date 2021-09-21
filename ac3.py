import abc
from unittest import TestCase, main, result


class Calculator (object):
    def calcula(self, numero1, numero2, operador):
        operacaocria = OperacaoCria()
        operacao = operacaocria.criar(operador)
        if (operacao == None):
            return 0
        else:
            resultado = operacao.executar(numero1, numero2)
            return resultado

class OperacaoCria(object):
    def cria (self, operador):
        if (operador == 'somar'):
            return Somar()
        elif (operador == 'subtrair'):
            return Subtrair()
        elif (operador == 'dividir'):
            return Dividir()

class Operacao(metaclass=abc.ABCMeta):
    @abc.abstractclassmethod
    def executar (self, numero1, numero2):
        pass

class Somar(Operacao):
    def executar(self, numero1, numero2):
        resultado = numero1 + numero2
        return resultado

class Subtrair(Operacao):
    def executar(self, numero1, numero2):
        resultado = numero1 - numero2
        return resultado

class Dividir(Operacao):
    def executar(self, numero1, numero2):
        resultado = numero1 / numero2
        return resultado


class Testes(TestCase):
    
    def test_somar(self):
        calculador = Calculator()
        result = calculador.calcular(3,3, 'somar')
        self.assertEqual(result, 6)

    def test_subtrair(self):
        calculador2 = Calculator()
        self.assertEqual(calculador2.calcular(4,4, 'subtrair'), 0)

    def test_subtrair(self):
        calculadorS = Calculator()
        result = calculadorS.calcular(2,6, 'subtrair')
        print (result)
        self.assertEqual(result, 2)

    def test_dividir(self):
        calculadorD = Calculator()
        self.assertEqual(calculadorD.calcular(4,2, 'dividir'), 2)
    
calculador = Calculator()
x = calculador.calcular(3,3, 'somar')
print(x)

if __name__ == '__main__':
    main()