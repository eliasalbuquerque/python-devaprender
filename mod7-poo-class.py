# 202312 - Python 3.12.0
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

computador1 = Computador('Lenovo', '16gb', 'Intel')
print(f'3. objeto: {computador1.marca}')
print(f'3. objeto: {computador1.memoria}')
print(f'3. objeto: {computador1.video}\n')

computador2 = Computador('Apple', '24gb', 'M2 integrada')
print(f'3. objeto: {computador2.marca}')
print(f'3. objeto: {computador2.memoria}')
print(f'3. objeto: {computador2.video}\n')
