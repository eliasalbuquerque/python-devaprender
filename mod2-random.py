# 202311 - Python 3.12.0
# 2 - Como receber e trabalhar com dados
# 2.12 - Valores aleatórios com Random

import random

# valor de 0.0 a 1.0
print(random.random())

# valor decimal entre valores conhecidos
print(random.uniform(4, 10))

# valor inteiro entre valores conhecidos
print(random.randint(4, 10))

# escolher opcao aleatorio
cores = ['verde','vermelho','azul']
print(random.choice(cores))

# escolher quantidade de opcao aleatoria
print(random.choices(cores, k=2))

# embaralhar opcoes
baralho = ['ás de paus','ás de dama','ás de espada','ás de ouro']
print(random.shuffle(baralho))
print(baralho)


# ​​DESAFIO

# 1. Você quer simular a opção de jogar uma moeda e resultar em cara ou coroa. 
# Jogue as opções dentro de uma variável e depois crie um programa que imprimir 
# 'cara' ou 'coroa' na tela.
moeda = ['cara','coroa']
print('### Desafio ramdon 1:')
while True:
    user_input = input('Aperte a letra "c" e "Enter" para jogar cara ou coroa: ')
    if user_input == 'c':
        print(random.choice(moeda))
    else:
        break

# 2. Você quer fazer um sorteio entre 5 nomes em uma lista de nomes. Crie uma 
# lista de 5 nomes e sorteie um nome de dentro dessa lista e exiba na tela.
nomes = ['Elias','Jhonantan','Natalia','Juliana','Creusa']
print('### Desafio ramdon 2:')
print(random.choice(nomes))

# 3. você quer escolher aleatóriamente um número de 10-100. Imprima na tela um 
# valor aleatório entre 10 e 100.
print('### Desafio ramdon 3:')
print(random.randint(10, 100))
