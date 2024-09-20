class Veiculo:
    def __init__(self, marca, modelo):
        self.marca = marca
        self.modelo = modelo
    
    def info(self):
        return f'Marca: {self.marca}, Modelo: {self.modelo}'

class Carro(Veiculo):
    def __init__(self, marca, modelo, portas):
        super().__init__(marca, modelo)
        self.portas = portas

    def info(self):
        return f'{super().info()}, Portas: {self.portas}'

carro = Carro('Toyota', 'Corolla', 4)
print(carro.info())  # Saída: Marca: Toyota, Modelo: Corolla, Portas: 4

