class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade
    def exibir(self):
        print(f"Nome: {self.nome} Idade {self.idade}")

shun = Pessoa(input("Nome: "), int(input("Idade: ")))
shun.exibir()