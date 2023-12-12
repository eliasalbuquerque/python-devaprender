# 202312 - Python 3.12.0
# 5.8 - Arrays


from array import array


# 1. typecode: inteiros, decimais e caracteres
numeros = array('i', [1, 2, 3, 4, 5, 6])
print(f'1. {numeros}')

# NOTE:
# link de todos os typecodes disponíveis
# https://docs.python.org/3/library/array.html

# 2. adiciona valor no final da lista
numeros.append(10)
print(f'2. {numeros}')

# 3. adiciona valor em uma posicao da lista
numeros.insert(-1, 7)
print(f'3. {numeros}')

# 4. extrair, remover e deletar item da lista
numeros.pop(0)  # extrai item index 0
numeros.remove(5)  # remove o valor 5
del numeros[1]  # deleta item index 1
print(f'4. {numeros}')
