# 202312 - Python 3.12.0
# 3 - Aprenda a controlar o fluxo de seus programas
# 3.8 - If elif else
# 3.9 - Compare MAIS com menos código! Operador ternário

import random

# 3.8 - If elif else
# condicoes simples
a = random.choice([True, False])
print(f'{a}')

if a == True:
    print('a é verdadeiro')
else:
    print('a é falso')


# condicoes encadeadas
numero_atrasos = random.randint(0, 3)
print(f'{numero_atrasos} faltas')

if numero_atrasos >= 3:
    print('vá para a diretoria')
elif numero_atrasos == 2:
    print('essa é sua segunda falta')
elif numero_atrasos == 1:
    print('essa é sua primeira falta')
else:
    print('pode entrar')

'''
A velocidade maxima da via e 50km/h
- cruzou entre 51 e 60: multa 2 pontos;
- cruzou entre 61 e 75: multa 4 pontos;
- cruzou acima 75: multa 7 pontos;
'''
velocidade = random.randint(45, 80)

if velocidade > 75:
    print(f'velocidade {velocidade}km/h: multa de 7 pontos')
elif velocidade > 60:
    print(f'velocidade {velocidade}km/h: multa de 4 pontos')
elif velocidade > 50:
    print(f'velocidade {velocidade}km/h: multa de 2 pontos')
else:
    print(f'velocidade {velocidade}km/h: dentro do limite de velocidade (50km/h)')


# DESAFIO
# Monte o seguinte cenário usando condicionais:
'''
Você está montando um sistema para um salão de beleza para calcular o preço do 
corte de cabelos grandes que irá seguir as seguinte regras:

- Se seu cabelo estiver com ou abaixo de 20cm você paga o valor de R$50,00
- Se seu cabelo estiver entre 21cm a 30cm você paga o valor de R$70,00
- Se seu cabelo estiver entre 31cm a 50cm você paga o valor de R$100,00
- Acima de 50cm Favor consultar na recepção
'''
# Declare uma variável que represente o tamanho atual do cabelo
# Apenas imprima na tela a mensagem apropriada, nada além disso é necesário

tamanho_cabelo = 20

print('---- DESAFIO: 8 - If elif else ----')

if tamanho_cabelo > 50:
    print('valor do corte consultar na recepção')
elif tamanho_cabelo > 30:
    print('valor do corte é R$100,00')
elif tamanho_cabelo > 20:
    print('valor do corte é R$70,00')
else:
    print('valor do corte é R$50,00')


# 3.9 - Compare MAIS com menos código! Operador ternário
idade = random.randint(13, 23)

print(f'{idade}: maior de idade') if idade >= 18 else print(f'{idade}: menor de idade')
# --> expressao --> if condicao --> else expressao

# DESAFIO
# Use expressão condicional (operador ternário) para criar a seguinte condição:
# - se velocidade estiver acima de 100 exibir, você foi multado, caso contrário
#   exiba siga em frente.
# Declare uma variável com o calor de 80.

velocidade = random.randint(80, 120)
print(f'{velocidade}: Voce foi multado') if velocidade >= 100 else print(f'{velocidade}: Siga em frente')
