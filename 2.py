class Carro:
    def __init__(self, marca, modelo, ano):
        self.marca = marca
        self.modelo = modelo
        self.ano = ano

    def exibir_detalhes(self):
        print(f'Marca: {self.marca} \nModelo: {self.modelo} \nAno: {self.ano}\n')

bruno = Carro("Fiat", "Uno", "1997")
carlos = Carro("Volkswagen", "Fusca", "1564")
diego = Carro("Hyundai", "HB20", "2016")
rafael = Carro("Ford", "Corsa", "1997")
paula = Carro("BMW", "118I", "2021")
renata = Carro("Rolls-Royce", "Phantom", "1985")

carros = [bruno, carlos, diego, rafael, paula, renata]
for carro in carros:
    carro.exibir_detalhes()
