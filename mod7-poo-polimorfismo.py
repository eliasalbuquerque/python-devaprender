# 202312 - Python 3.12.0
# 7.11 - Polimorfismo - Seja flexível


# NOTE:
# Algo só pode ser considerado polimorfico quando ele se adapta dinamicamente
# ao que ele recebe.


class Carro:
    def ligar(self):
        print(f'1. Ligando o carro')


class Moto:
    def ligar(self):
        print(f'1. Ligando a moto')

# funcao polimorfica, se adapta ao metodo das duas classes


def iniciar(veiculo):
    veiculo.ligar()


# objetos
carro = Carro()
moto = Moto()

# usando funcao polimorfica
iniciar(carro)
iniciar(moto)


print()


class Pessoa:
    # funcao polimorfica, que se adapta aos argumentos passados
    def apresentar(self, nome, idade=None, profissao=None):
        caracteristicas_pessoa = nome
        if idade != None:
            caracteristicas_pessoa += f', {idade}'
        if profissao != None:
            caracteristicas_pessoa += f', {profissao}'
        print(f'2. {caracteristicas_pessoa}')


pessoa = Pessoa()
pessoa.apresentar('Amanda', 18, 'Programadora')
pessoa.apresentar('Amanda', 18)
pessoa.apresentar('Amanda', None, 'Programadora')
pessoa.apresentar('Amanda')
