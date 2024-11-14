class Animal:
    def __init__(self):
        print("Animal criado")
class Cachorro(Animal):
    def emitir_som(self):
        print("AUAU DOGDOG AUAU\n")

class Gato(Animal):
    def emitir_som(self):
        print("MIAU QUAL FOI MIAU MIAU\n")

cachorro1 = Cachorro()
cachorro1.emitir_som()
gatinho1 = Gato()
gatinho1.emitir_som()