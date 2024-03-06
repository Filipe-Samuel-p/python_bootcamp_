# Exercicio do livro "introdução ao python"

class ContaEspecial(conta):
    def __init__(self,clientes,numero,saldo = 0,limite = 0):
        conta.__init__(self,clientes,numero,saldo)
        self.limite = limite

    def saque(self,valor):
        if self.saldo + self.limite >= valor:
            self.saldo -= valor
            self.operacoes.append(["SAQUE", valor])
