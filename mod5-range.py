# 202312 - Python 3.12.0
# 5.9 - Range - Gerando valores iteraveis de forma facil


# 1. tipo da classe range
range_numeros = range(5) # 0 ~ 4
print(f'1. {(type(range_numeros))}')

# 2. gerando numeros
for numero in range_numeros:
    print(f'2. {numero}')

# 3. gerando numeros a partir de um numero determinado
for numero in range(10, 15): # 10 ~ 14
    print(f'3. {numero}')

# 4. gerando numeros usando step (pulo)
for numero in range(100, 110, 2): # 100 ~ 108 de 2 em 2
    print(f'4. {numero}')

# 5. gerando lista a partir do range
lista = list(range(0, 100, 10)) # 0 ~ 90 de 10 em 10
print(f'5. {lista}')

