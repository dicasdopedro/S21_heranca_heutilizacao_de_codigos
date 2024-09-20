class Pai:
    def mensagem(self):
        return 'Mensagem do pai.'

class Filho(Pai):
    def mensagem(self):
        return 'Mensagem do filho.'

f = Filho()
print(f.mensagem())  # Saída: Mensagem do filho.

