class Caminhante:
    def andar(self):
        return 'Está andando'

class Nadador:
    def nadar(self):
        return 'Está nadando'

class Triatleta(Caminhante, Nadador):
    pass

tri = Triatleta()
print(tri.andar())  # Saída: Está andando
print(tri.nadar())  # Saída: Está nadando

