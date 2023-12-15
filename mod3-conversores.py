# 202311 - Python 3.12.0
# 3 - Aprenda a controlar o fluxo de seus programas
# 3.6 - Convertendo entre tipos                 --> ln: 7
# 5.16 - Conversão entre tipos (coleções)       --> ln: 32


# 3.6 - Convertendo entre tipos


# 1. convertendo e indentificando os tipos
a = 5
print(f'1. int: {a} {type(a)}')  # 5 <class 'int'>

a = float(a)
print(f'2. float: {a} {type(a)}')  # 5.0 <class 'float'>

a = str(a)
print(f'3. str: {a} {type(a)}')  # '5.0' <class 'str'>


# 4. convertendo float em lista
str_list = list(a)
print(f'\n4. list: {str_list}  {type(str_list)}')

# 5. convertendo float em tupla
str_tuple = tuple(a)
print(f'5. tuple: {str_tuple}  {type(str_tuple)}')

# 6. convertendo dados em um dicionario
b = 20
c = 2.5

str_dict = {'string': a, 'inteiro': b, 'float': c}
print(f'dictionary: {str_dict}  {type(str_dict)}')


# 5.16 - Conversão entre tipos (coleções)


# 7. convertendo lista em:
numeros = [10, 20, 30, 40, 50]
print(f'\n7. dicionario: {set(numeros)}')
print(f'8. tupla: {tuple(numeros)}')

# 9. incluindo chaves no dicionario:
dicionario = {
    i: num for i, num in enumerate(numeros, 1)}
print(f'\n9. dicionario (keys): {dicionario}')
