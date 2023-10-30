class Conta:
    def __init__(self, saldo_inicial):
        self.saldo = saldo_inicial

    def consultar_saldo(self):
        return self.saldo

    def depositar(self, valor):
        self.saldo += valor
        return f'Depósito de R${valor:.2f} realizado com sucesso. Saldo total: R${self.saldo:.2f}'

    def sacar(self, valor):
        if self.saldo >= valor:
            self.saldo -= valor
            return f'Saque de R${valor:.2f} realizado com sucesso. Saldo restante: R${self.saldo:.2f}'
        else:
            return 'Saldo insuficiente. Saque não realizado.'

def main():
    saldo_inicial = 0 
    conta = Conta(saldo_inicial)

    while True:
        print("\nEscolha uma opção:")
        print("1. Consultar saldo")
        print("2. Depositar dinheiro")
        print("3. Sacar dinheiro")
        print("4. Sair")

        opcao = input("Digite o número da opção desejada: ")

        if opcao == "1":
            print(f"Saldo disponível: R${conta.consultar_saldo():.2f}")
        elif opcao == "2":
            valor = float(input("Digite o valor a ser depositado: R$"))
            print(conta.depositar(valor))
        elif opcao == "3":
            valor = float(input("Digite o valor a ser sacado: R$"))
            print(conta.sacar(valor))
        elif opcao == "4":
            print("Obrigado por usar nosso caixa eletrônico. Volte sempre!")
            break
        else:
            print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    main()
