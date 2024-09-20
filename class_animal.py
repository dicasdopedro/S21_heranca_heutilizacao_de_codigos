class Animal:
    def __init__(self, nome):
        self.nome = nome
    
    def emitir_som(self):
        pass

class Cachorro(Animal):
    def emitir_som(self):
        return f'{self.nome} faz au au!'

c = Cachorro('Rex')
print(c.emitir_som())  # Saída: Rex faz au au!
