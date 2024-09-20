class Veiculo:
    def __init__(self, marca, modelo):
        self.marca = marca
        self.modelo = modelo
    
    def info(self):
        return f'{self.marca} {self.modelo}'

class Carro(Veiculo):
    def __init__(self, marca, modelo, cor):
        super().__init__(marca, modelo)
        self.cor = cor

    def info(self):
        return f'{super().info()} de cor {self.cor}'

meu_carro = Carro('Honda', 'Civic', 'Preto')
print(meu_carro.info())  # Saída: Honda Civic de cor Preto

