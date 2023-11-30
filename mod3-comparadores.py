# 202311 - Python 3.12.0
# 3 - Aprenda a controlar o fluxo de seus programas
# 3.3 - Lógica de comparação c Operadores lógicos

# OPERADORES DE COMPARAÇÃO
# Exemplo com operadores de comparação
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

print("Igual:", igual) #false
print("Diferente:", diferente) #true
print("Menor que:", menor_que) #true
print("Maior que:", maior_que) #false
print("Menor ou igual a:", menor_igual) #true
print("Maior ou igual a:", maior_igual) #false


# OPERADORES LÓGICOS
# Exemplo de operadores lógicos com strings operador 'and'
# Verifica se a linguagem é Python E sua popularidade é alta
linguagem = "Python"
popularidade = "alta"

linguagem_popular = (linguagem == "Python") and (popularidade == "alta")
print("Linguagem Popular:", linguagem_popular) #true


# Exemplo de operador 'or'
# Verifica se a cor é azul OU verde
cor = "azul"

cor_azul_ou_verde = (cor == "azul") or (cor == "verde")
print("Cor é Azul ou Verde:", cor_azul_ou_verde) #true


# Exemplo de operadores lógicos com números
# Verifica se a nota está entre 60 e 90 OU é igual a 100
nota = 75

condicao_nota = (60 <= nota <= 90) or (nota == 100)
print("Condição da Nota:", condicao_nota) #true


# Exemplo de operador 'not'
# Verifica se a pessoa NÃO é idosa (idade não é superior a 60)
idade = 25

nao_idoso = not (idade > 60)
print("Não Idoso:", nao_idoso) #true


# Exemplo de operadores lógicos com datas
# Verifica se a pessoa tem mais de 18 anos E nasceu antes de 2000
from datetime import datetime

hoje = datetime.now()
nascimento = datetime(1990, 5, 15)

condicao_idade_data = (hoje.year - nascimento.year > 18) and (nascimento.year < 2000)
print("Condição de Idade e Data:", condicao_idade_data) #true


# Exemplo de combinação de operadores lógicos
# Verifica se a temperatura está entre 20 e 30 graus E a umidade está entre 40 e 60
temperatura = 28
umidade = 70

condicoes_ideais = (temperatura >= 20 and temperatura <= 30) and (umidade >= 40 and umidade <= 60)
print("Condições Ideais:", condicoes_ideais) #false
