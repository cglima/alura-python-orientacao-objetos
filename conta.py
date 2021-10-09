class Conta:

    def __init__(self, numero, titular, saldo, limite):
        print(f"Construindo o objeto ... {self}")
        self.__numero = numero
        self.__titular = titular
        self.__saldo = saldo
        self.__limite = limite

    def extrato(self):
        print(f"O saldo da conta do titular {self.__titular} é {self.__saldo}")

    def deposita(self, valor):
        self.__saldo += valor

    def saca(self, valor):
        self.__saldo -= valor

    def transfere(self,valor, destino):
        self.saca(valor)
        destino.deposita(valor)
