class Animal:
    def __init__(self, nome):
        self.nome = nome

class Mamifero(Animal):
    pass

class Cachorro(Mamifero):
    def emitir_som(self):
        return f'{self.nome} faz au au!'

class Gato(Mamifero):
    def emitir_som(self):
        return f'{self.nome} faz miau!'

rex = Cachorro('Rex')
felix = Gato('Felix')

print(rex.emitir_som())  # Saída: Rex faz au au!
print(felix.emitir_som())  # Saída: Felix faz miau!

