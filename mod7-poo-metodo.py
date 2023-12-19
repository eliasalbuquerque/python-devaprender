# 202312 - Python 3.12.0
# 7.3 - Métodos de uma classe                       --> ln: 6
# 7.5 - Métodos comuns VS Instância VS Classe       --> ln: 41


# 7.3 - Métodos de uma classe


class Computador:
    def __init__(self, marca, memoria, video):
        self.marca = marca
        self.memoria = memoria
        self.video = video

    def ligar(self):
        print(f'1. Ligando computador {self.marca}')

    def desligar(self):
        print(f'1. Desligando computador {self.marca}')

    def dados_computador(self):
        print(f'1. Computador {self.marca}, com {
              self.memoria}, e placa de video {self.video}')


computador1 = Computador('Asus', '16gb', 'AMD')
computador1.ligar()
computador1.dados_computador()
computador1.desligar()

print()

computador2 = Computador('Dell', '16gb', 'Intel')
computador2.dados_computador()
computador2.ligar()
computador2.desligar()

print()


# 7.5 - Métodos comuns VS Instância VS Classe


# métodos comuns
# métodos de classe
# métodos estáticos

class Computador:
    so = 'Windows 11'

    def __init__(self, marca, memoria, video):
        self.marca = marca
        self.memoria = memoria
        self.video = video

    # medodo comum
    def exibir_dados_computador(self):
        print(f'2. {self.marca, self.memoria, self.video, self.so}')

    # metodo de classe
    @classmethod
    def computador_escritorio(cls, memoria):
        return cls('Dell', memoria, 'Intel integrada')

    @classmethod
    def computador_alto_rendimento(cls, memoria):
        return cls('Dell', memoria, 'Nvidia')

    # metodo estatico
    def roda_programas_pesados(memoria):
        if memoria >= 12:
            return True
        else:
            return False


# configuracao de computador para escritorio
computador1 = Computador.computador_escritorio('8gb')
computador1.exibir_dados_computador()

# configuracao de computador para alto desempenho
computador2 = Computador.computador_alto_rendimento('24gb')
computador2.exibir_dados_computador()

# verificar se computador aguenta rodar programas que com muito processamento
print(f'2. {Computador.roda_programas_pesados(16)}')

print()
