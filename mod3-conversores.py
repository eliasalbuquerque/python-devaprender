# 202311 - Python 3.12.0
# 3 - Aprenda a controlar o fluxo de seus programas
# 3.6 - Convertendo entre tipos


a = 5
print(f'int: {a} {type(a)}') #5 <class 'int'>

a = float(a)
print(f'float: {a} {type(a)}') #5.0 <class 'float'>

a = str(a)
print(f'str: {a} {type(a)}') #'5.0' <class 'str'>

b = 20
c = 2.5

str_list = list(a)
print(f'list: {str_list}  {type(str_list)}')

str_tuple = tuple(a)
print(f'tuple: {str_tuple}  {type(str_tuple)}')

str_dict = {'string': a, 'inteiro': b, 'float': c}
print(f'dictionary: {str_dict}  {type(str_dict)}')
