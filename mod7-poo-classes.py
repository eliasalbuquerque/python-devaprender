# 202312 - Python 3.12.0
# 7.2 - Classes e Intro a POO(Agora você entende!)                  --> ln: 6
# 7.10 - Classes Abstratas - Criando modelos a serem seguidos       --> ln: 59


# 7.2 - Classes e Intro a POO(Agora você entende!)


# código estrutural
marca = 'Asus'
memoria = '8g'
video = 'Nvidia'

print(f'1. estrutural: {marca}')
print(f'1. estrutural: {memoria}')
print(f'1. estrutural: {video}\n')

marca = 'Dell'
memoria = '8g'
video = 'Intel'

print(f'1. estrutural: {marca}')
print(f'1. estrutural: {memoria}')
print(f'1. estrutural: {video}\n')


# função
def dados_computador(marca, memoria, video):
    print(f'2. função: {marca}')
    print(f'2. função: {memoria}')
    print(f'2. função: {video}\n')


dados_computador('Dell', '12gb', 'AMD')
dados_computador('Vaio', '16gb', 'AMD')


# classe
class Computador:
    def __init__(self, marca, memoria, video):
        self.marca = marca
        self.memoria = memoria
        self.video = video


# instancia da classe = objeto
computador1 = Computador('Lenovo', '16gb', 'Intel')
print(f'3. objeto: {computador1.marca}')
print(f'3. objeto: {computador1.memoria}')
print(f'3. objeto: {computador1.video}\n')

computador2 = Computador('Apple', '24gb', 'M2 integrada')
print(f'3. objeto: {computador2.marca}')
print(f'3. objeto: {computador2.memoria}')
print(f'3. objeto: {computador2.video}\n')


# 7.10 - Classes Abstratas - Criando modelos a serem seguidos


# Criar um modelo que implementa na classe que esta herdando
from abc import ABC, abstractmethod

# criando a classe abstrata
class Camera(ABC):

    # metodo obrigatorio para implementacao
    @abstractmethod
    def definir_tamanho_lente(self, tamanho):
        pass


# classe comum herdando classe abstrata
class CameraProfissional(Camera):
    def definir_tamanho_lente(self, tamanho):
        print(f'4. classeAbstrata: {tamanho}mm')


# instanciar classe
camera_profissional = CameraProfissional()
camera_profissional.definir_tamanho_lente(35)


print()


# DESAFIO
# Crie uma classe abstrata chamada `Monitor`, que irá ter 2 métodos abstratos:
# - aumentar_claridade
# - reduzir_claridade
# Os métodos irão receber um número que representa o quanto de claridade deve 
# ser aumentado ou diminuído ao chamar eles.
# Após ter criado a classe abstrata, crie uma nova classe chamada de 
# `MonitorFullHD` e coloque a implementação dos métodos `aumentar_claridade` e 
# `reduzir_claridade` dentro deles.


from abc import ABC, abstractmethod


# classe abstrata
class Monitor(ABC):
    @abstractmethod
    def aumentar_claridade(self, brilho):
        pass

    @abstractmethod
    def diminuir_claridade(self, brilho):
        pass


# classe
class MonitorFullHD(Monitor):    
    def aumentar_claridade(self, brilho):
        print(f'Aumentar claridade em {brilho} pontos')

    def diminuir_claridade(self, brilho):
        print(f'Diminuir claridade em {brilho} pontos')


# objeto
monitor_fhd = MonitorFullHD()
monitor_fhd.aumentar_claridade(5)
monitor_fhd.diminuir_claridade(5)