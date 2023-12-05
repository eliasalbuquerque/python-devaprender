# 202311 - Python 3.12.0
# 3 - Aprenda a controlar o fluxo de seus programas
# 3.3 - Lógica de comparação c Operadores lógicos
# 3.4 - Comparações c/ Operadores Booleanos
# 3.5 - Operadores de Igualdade


# ==============================================================================
# OPERADORES                                    SIGNIFICADO
# ==============================================================================
# ()                                            Parenteses
# **                                            Expoente
# *                                             Multiplicação
# /                                             Divisão
# //                                            Divisão por inteiros
# %                                             Modulus
# +, -                                          Adição, subtração
# ==, !=, >, <, >=, <=, is, is not, in, not in  Compadores lógicos, identidade,
#                                               pertencimento em conjuntos
# not                                           NOT booleano
# and                                           AND booleano
# or                                            OR boolean
# ==============================================================================


# OPERADORES DE COMPARAÇÃO
# Exemplo com operadores de comparação
import random
from datetime import datetime

a = 5
b = 10

# Verifica se a é igual a b
igual = (a == b)

# Verifica se a é diferente de b
diferente = (a != b)

# Verifica se a é menor que b
menor_que = (a < b)

# Verifica se a é maior que b
maior_que = (a > b)

# Verifica se a é menor ou igual a b
menor_igual = (a <= b)

# Verifica se a é maior ou igual a b
maior_igual = (a >= b)

print("Igual:", igual)  # false
print("Diferente:", diferente)  # true
print("Menor que:", menor_que)  # true
print("Maior que:", maior_que)  # false
print("Menor ou igual a:", menor_igual)  # true
print("Maior ou igual a:", maior_igual)  # false

# Comparadores de igualdade
a = 10E7 * 5
b = 10E7 * 5

print('Igual:', a == b) # compara o valor
print('Is:', id(a) is id(b)) # compara a identidade


# OPERADORES LÓGICOS
# Exemplo de operadores lógicos com strings operador 'and'
# Verifica se a linguagem é Python E sua popularidade é alta
linguagem = "Python"
popularidade = "alta"

linguagem_popular = (linguagem == "Python") and (popularidade == "alta")
print("Linguagem Popular:", linguagem_popular)  # true


# Exemplo de operador 'or'
# Verifica se a cor é azul OU verde
cor = "azul"

cor_azul_ou_verde = (cor == "azul") or (cor == "verde")
print("Cor é Azul ou Verde:", cor_azul_ou_verde)  # true


# Exemplo de operadores lógicos com números
# Verifica se a nota está entre 60 e 90 OU é igual a 100
nota = 75

condicao_nota = (60 <= nota <= 90) or (nota == 100)
print("Condição da Nota:", condicao_nota)  # true


# Exemplo de operador 'not'
# Verifica se a pessoa NÃO é idosa (idade não é superior a 60)
idade = 25

nao_idoso = not (idade > 60)
print("Não Idoso:", nao_idoso)  # true


# Exemplo de operadores lógicos com datas
# Verifica se a pessoa tem mais de 18 anos E nasceu antes de 2000

hoje = datetime.now()
nascimento = datetime(1990, 5, 15)

condicao_idade_data = (hoje.year - nascimento.year >
                       18) and (nascimento.year < 2000)
print("Condição de Idade e Data:", condicao_idade_data)  # true


# Exemplo de combinação de operadores lógicos
# Verifica se a temperatura está entre 20 e 30 graus E a umidade está entre 40 e 60
temperatura = 28
umidade = 70

condicoes_ideais = (
    temperatura >= 20 and temperatura <= 30) and (umidade >= 40 and umidade <= 60)
print("Condições Ideais:", condicoes_ideais)  # false


# Testes e aplicacoes proprias
fulano = ['Maria', 'Paula', 'Carla', 'Renata',
          'João', 'Ricardo', 'Pedro', 'Jean']
idade = [21, 32, 17, 15, 44, 65, 70, 35]
convite = [True, False]
acompanhado = [True, False]

dados = [random.choice(fulano), random.choice(idade), random.choice(convite), random.choice(acompanhado)]
print(dados)

entrada = (dados[1] >= 21 or dados[3]) and dados[2]

if entrada == True:
    print('Entrada liberada.')
else:
    print('Entrada negada.')

if dados[2] == False:
    print(f'{dados[0]} não possui convite e não pode entrar.')
elif dados[1] >= 21:
    print(f'{dados[0]} é maior de idade e possui convite, pode entrar.')
elif dados[3] == True:
    print(f'{dados[0]} esta acompanhada e possui convite, pode entrar.')
else:
    print(f'{dados[0]} tem convite mas é menor de idade e esta sem acompanhante, não pode entrar.')


# ​DESAFIO
'''
1. Quero que você defina as seguintes variáveis, inicialmente todas como False, a 
   ideia aqui não é de se importar com os valores dentro dessas variáveis, mas sim 
   como montar condicionais.

    - possui_passaporte = False;
    - passagem_comprada = False;
    - menor_de_idade = False;

2. E Crie as seguintes condições usando o que acabou de ver e imprima o resultado 
   na tela. Tente fazer cada condição e depois veja a solução no final deste aula.

    - Uma pessoa só pode viajar se possuir  passaporte e tiver a passagem comprada 
      e não for menor de idade;
    - Uma pessoa só pode viajar se possuir passaporte ou tiver a passagem comprada 
      e não for menor de idade;
    - Uma pessoa só pode viajar se não possuir passaporte ou tiver a passagem 
      comprada e não for menor de idade;
    - Uma pessoa não pode viajar se não possuir passaporte ou não tiver a passagem 
      comprada e for menor de idade;
'''

possui_passaporte = False
passagem_comprada = False
menor_de_idade = False

print('---- DESAFIO: 4 - Comparações c/ Operadores Booleanos ----')

# Uma pessoa só pode viajar se possuir passaporte e tiver a passagem comprada 
# e não for menor de idade;
print('1)', possui_passaporte and passagem_comprada and not menor_de_idade) #false
    
# Uma pessoa só pode viajar se possuir passaporte ou tiver a passagem comprada 
# e não for menor de idade;
print('2)', (possui_passaporte or passagem_comprada) and not menor_de_idade) #false

# Uma pessoa só pode viajar se não possuir passaporte ou tiver a passagem 
# comprada e não for menor de idade;
print('3)', (not possui_passaporte or passagem_comprada) and not menor_de_idade) #true

# Uma pessoa não pode viajar se não possuir passaporte ou não tiver a passagem 
# comprada e for menor de idade;
print('4)', not (not possui_passaporte or not passagem_comprada) and menor_de_idade) #false
