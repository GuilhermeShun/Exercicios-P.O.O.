class ContaBancaria:
    def __init__(self, titular, saldo):
        self._saldo = saldo
        self.titular = titular

    def depositar(self, valor):
        if valor >= 0:
            self._saldo += valor
        else:
            print("Impossível depositar valor negativo")

    def sacar(self, valor):
        if valor > self._saldo:
            print("Impossível sacar valor maior que o saldo")
        elif valor < 0:
            print("Impossível sacar valor negativo")
        else:       
            self._saldo -= valor

    def exibir_dados(self):
        print(f'Saldo atual: {self._saldo}\nTitular: {self.titular}\n_________________________\n_________________________')

conta_nova = ContaBancaria(input("Titular: "), 0)
conta_nova.exibir_dados()
while True:
    if input("Deseja continuar? (s/n)") == "s":
        operacao = input("Depósito ou saque? (d/s)")
        if operacao == "d":
            conta_nova.depositar(float(input("Valor para depósito: ")))  
        elif operacao == "s":
            conta_nova.sacar(float(input("Valor para saque: ")))  
        else:
            print("Operação inválida, bebê")
        conta_nova.exibir_dados()    

    else:
        conta_nova.exibir_dados()    
        print("Encerrando o caixa eletrônico... ... ...")
        break

        