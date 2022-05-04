from src.banco.banco_list import BancoLista
from src.conta.conta import Conta


class CriarBanco:
    if __name__ == '__main__':
        banco = BancoLista()
        conta1 = Conta('21.324-7')
        conta2 = Conta('20.342-6')
        banco.cadastrar(conta)
        banco.creditar(conta.get_numero(), 100)
        banco.debitar(conta.get_numero(), 50)
        banco.procurar_conta(conta.get_numero())
        banco.saldo(conta.get_numero())
        banco.transferir(conta.get_numero())