def cria_conta(numero, titular, saldo, limite):
    conta = {"numero": numero, "titular": titular, "saldo": saldo, "limite": limite}
    return conta

def deposita(conta, valor_deposito):
    conta["saldo"] += valor_deposito

def saca(conta, valor_saque):
    conta["saldo"] -= valor_saque

def extrato(conta):
    print("O saldo na conta é de {}".format(conta["saldo"]))




