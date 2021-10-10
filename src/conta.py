class Conta:

    numero_contas = 0
    limite_transferencia = 10000.0

    def __init__(self, numero, titular, saldo, limite):
        #print(f"Construindo o objeto ... {self}")
        self.__numero = numero
        self.__titular = titular
        self.__saldo = saldo
        self.__limite = limite
        Conta.numero_contas += 1

    def __repr__(self):
        """ Representação do objeto """
        return f"Conta({self.__numero}, '{self.__titular}, {self.__saldo}, {self.__limite}')"

    def extrato(self):
        print(f"O saldo da conta do titular {self.__titular} é {self.__saldo}")

    def deposita(self, valor):
        if valor < 0:
            raise ValueError("o valor a depositar nao pode ser negativo!")
        else:
            self.__saldo += valor


    def __pode_sacar(self, valor_a_sacar):
        valor_disponivel_a_sacar = self.saldo + self.limite
        return valor_a_sacar <= valor_disponivel_a_sacar

    def saca(self, valor):
        if valor < 0:
            raise ValueError(" o valor para saque nao pode ser negativo!")

        # se nao pode sacar
        if not self.__pode_sacar(valor):
            raise ValueError(f"O valor {valor} ultrapassou o limite para saque!")

        self.__saldo -= valor

    def transfere(self, valor, destino):
        if valor > 10000.0:
            raise ValueError("O valor para transferencia é maior que o limite permitido (10000.0)")
        else:
            self.saca(valor)
            destino.deposita(valor)

    @property
    def saldo(self):
        return self.__saldo

    @property
    def titular(self):
        return self.__titular

    @property
    def limite(self):
        print('Obtendo valor do limite..')
        return self.__limite

    @limite.setter
    def limite(self, limite):
        print('Alterando o valor do limite')
        self.__limite = limite

    #método de escopo de classe - executado pela classe e não pelo objeto
    @staticmethod
    def codigo_banco():
        return '001'

    @staticmethod
    def codigos_banco():
        return {'BB':'001', 'CAIXA': '104', 'Bradesco':'237'}

