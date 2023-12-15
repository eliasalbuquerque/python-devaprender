# 202312 - Python 3.12.0
# 5.2  - Criando listas com Python                              --> ln: 9
# 5.3  - Encontre valores e manipulacao de itens de uma lista   --> ln: 92
# 5.4  - Como ordenar listas simples                            --> ln: 145
# 5.5  - Trabalhar com multiplas listas usando o ZIP            --> ln: 172
# 5.12 - Processando itens de uma lista com Map                 --> ln: 217
# 5.13 - Como filtrar dados de uma colecao usando filter        --> ln: 258
# 5.14 - Sets                                                   --> ln: 315


# 5.2 - Criando listas com Python


# 1. listas e indice (index)
from itertools import zip_longest
import random
precos = [10, 20, 30]
print(f'\n1. indice: {precos[2]}')  # 30

# 2. descobrir o index
precos = [10, 20, 30, 50, 50, 60, 70, 90, 90, 100, 150, 200, 250, 300]
print(f'2. descobrir indice: {precos.index(90)}')  # 7
print(f'3. buscar por valor o indice: {precos[precos.index(90)]}')  # 90

# NOTE:
# No item 2, o index irá retornar o index da primeira ocorrencia na lista;
# No item 3, a funcao busca pelo index conforme o parametro passado e tras o
# que tem dentro do index.

# 4. listas sao dinamicas
itens = [1, 2, 3, 'olá', 'café', 'pão', True, False, 10.6, 2.5, 3.3]
print(f'4. dados da lista: {itens[1]}')  # dado inteiro = 2
print(f'5. dados da lista: {itens[4]}')  # dado string = café
print(f'6. dados da lista: {itens[7]}')  # dado booleano = False
print(f'7. dados da lista: {itens[9]}')  # dado float = 2.5


# maneiras diferentes de gerar uma lista

# 8. por multiplicacao:
lista_inteiros = [9] * 10
lista_string = ['teste'] * 5

print(f'\n8. gerar lista: {lista_inteiros}')  # por multiplicacao
print(f'9. gerar lista: {lista_string}')  # por multiplicacao

# 10. por uma faixa de numeros (range)
faixa_de_numeros = list(range(16))  # 1 a 15
print(f'10. gerar lista: {faixa_de_numeros}')

# 11. por string
lista_string = list('Hello World!')
print(f'11. gerar lista: {lista_string}')

# 12. matriz
matriz_de_nomes = [['Carol', 30], ['Marcos', 45]]
print(f'12. matriz: {matriz_de_nomes[0]}')
print(f'13. matriz: {matriz_de_nomes[0][0]}')

# NOTE:
# em 12. acessamos o primeiro elemento da primeira lista;
# em 13. acessamos o primeiro elemento da segunda lista.


# DESAFIOS


# DESAFIO 1:
# Crie uma lista que tenha os nomes dos 3 objetos que você mais usa durante o
# dia e imprima ele na tela
personal_objects = ['Laptop', 'G-Shock DW-5600', 'Cellphone']
print(f'\n14. desafio 1: {personal_objects}')


# DESAFIO 2:
# Usando apenas uma linha de código, crie uma lista de 10 a 131
list_10_to_132 = list(range(10, 132))

# DESAFIO 3:
# Imprima na tela o resultado da combinação da lista do desafio 1 e desafio 2
print(f'15. desafio 3: {personal_objects} {list_10_to_132}')


# DESAFIO 4:
# Crie uma lista de listas(matriz) que tenha os nomes dos 3 objetos que você
# mais usa durante o dia, mas agora dentro de cada item você vai colocar uma
# Informação extra, coloque o valor em reais desse objeto também e imprima ele
# na tela
personal_objects_matrix = [['Laptop', 'R$5500'], [
    'G-Shock DW-5600', 'R$500'], ['Cellphone', 'R$2000']]
print(f'16. desafio 4: {personal_objects_matrix[1][0]}')  # g-shock


# 5.3 - Encontre valores e manipulacao de itens de uma lista


valores = [1, 2, 3, 4, 5, 6, 7, 8, 9]
nomes = ['tiago', 'amanda', 'cintia', 'alexandre']
cargo = ['medico', 'engenheiro', 'arquiteto', 'programador']
anos = [2020, 2030, 2040, 2050]

# 17. adicionar item no final da lista
valores.append(10)
print(f'\n17. adicionar item: {valores}')

# 18. juntar duas listas em uma (unir)
valores.extend(nomes)
print(f'18. unir listas: {valores}')

# 19. juntar dias listas sem alterar as listas originais (concatenar)
nova_lista = nomes + cargo
print(f'19. cancatenar listas: {nova_lista}')

#  20. inserir item em uma lista
print(f'20. inserir item: {anos}')
anos.insert(2, 2035)  # no index 2 inserir valor
print(f'21. inserir item: {anos}')

# 22. extrair item em uma lista
anos_2020 = anos.pop(0)
print(f'22. extrair item: {anos_2020}')
print(f'23. extrair item: {anos}')

# 24. remover item em uma lista:
# por busca de item
anos.remove(2050)
print(f'24. remover item: {anos}')

# por indice
del anos[1]
print(f'25. remover item: {anos}')

# por faixa de itens
print(f'26. remover item: {valores}')
del valores[1:6]
print(f'27. remover item: {valores}')

# 28. contando ocorrencia de itens
print(f'28. ocorrencia: {anos}')
print(f'29. ocorrencia: {anos.count(2040)}')

# 30. resetar lista
anos.clear()
print(f'30. reset lista: {anos}')


# 5.4 - Como ordenar listas simples


# 31. gerar lista aleatoria
def generate_random_list(minimum, maximum, length):
    return [random.randint(minimum, maximum) for _ in range(length)]


valores = generate_random_list(1, 40, 10)
print(f'\n31. ordenar lista: {valores}')

# 32. ordenar lista: ordem crescente
lista_crescente = list(valores)
lista_crescente.sort()
print(f'32. ordenar lista: {lista_crescente}')

# 33. ordenar lista: ordem decrescente
lista_decrescente = list(valores)
lista_decrescente.sort(reverse=True)
print(f'33. ordenar lista: {lista_decrescente}')

# 34. inverter itens da lista
inverter_lista = list(valores)
inverter_lista.reverse()
print(f'34. ordenar lista: {inverter_lista}')


# 5.5 - Trabalhar com multiplas listas usando o ZIP


# 35. Trabalhando com multiplas listas de mesmo tamanho
lista_letras = ['A', 'B', 'C', 'D', 'E']
lista_numeros = [1, 2, 3, 4, 5]

print('\n35. multiplas listas')
for a, b in zip(lista_letras, lista_numeros):
    print(f'    {a} : {b}')

# 36. Trabalhando com multiplas listas de tamanhos diferentes

lista_titulos = ['titulo 1', 'titulo 2', 'titulo 3', 'titulo 4', 'titulo 5']
lista_produtos = ['produto 1', 'produto 2', 'produto 3']

print('36. multiplas listas')
for a, b in zip_longest(lista_titulos, lista_produtos):
    print(f'    para o {a}, entao {b}')


# DESAFIO
'''
Usando as listas abaixo:

produtos = ['Produto 1', 'Produto 2', 'Produto 3', 'Produto 4', 'Produto 5']
precos = ['R$500,00', 'R$1500,00', 'R$2700,00', 'R$5000,00']

Estamos extraindo preços de um site de produtos e queremos armazenar as informações encontradas, porém a pesquisa foi encontrada em momentos diferentes, assim acabamos com duas listas diferentes, favor criar uma mensagem que diz o nome e valor produto, como as mensagens abaixo:

Produto: Produto 1 encontrado no valor de R$500,00
Produto: Produto 2 encontrado no valor de R$1500,00
Produto: Produto 3 encontrado no valor de R$2700,00
Produto: Produto 4 encontrado no valor de R$5000,00
Produto: Produto 5 encontrado no valor de None  
'''
print('\n37. desafio:\n')

produtos = ['Produto 1', 'Produto 2', 'Produto 3', 'Produto 4', 'Produto 5']
precos = ['R$500,00', 'R$1500,00', 'R$2700,00', 'R$5000,00']

for a, b in zip_longest(produtos, precos):
    print(f'Produto: {a} encontrado no valor de {b}')


# 5.12 - Processando itens de uma lista com Map


# 38. criando listas usando loops e range()
numeros = []
for i in range(5):
    numeros.append(i)
print(f'\n38. gerar listas automaticas: {numeros}')

# 39. usando a funcao map
nomes = ['larissa', 'rafael', 'marcos', 'john']


def aprovar_pessoas(nomes):
    return nomes + ' APROVADO'


aprovados = list(map(aprovar_pessoas, nomes))
print(f'39. map: {aprovados}')


# DESAFIO
# Extraia as cores da lista a seguir e coloque as em uma nova lista. Finalmente
# imprima a nova lista na tela.

pinturas = [
    ['Pintura Classica', 'Azul', 1857],
    ['Pintura Medieval', 'Vermelha', 1867],
    ['Pintura Moderna', 'Verde', 1897]
]


def extrair_cores(pinturas):
    return pinturas.pop(1)


cores = list(map(extrair_cores, pinturas))
print(f'40. desafio map: {cores}')


# 5.13 - Como filtrar dados de uma colecao usando filter


nomes = ['larissa', 'rafael', 'marcos', 'john']

# 41. filtrando dados dentro de uma lista
# exemplo 1


def pessoa_aprovada(pessoa):
    if pessoa == 'marcos':
        return True
    else:
        return False


print(f'\n41. filter: {list(filter(pessoa_aprovada, nomes))}')

# exemplo 2
pinturas = [
    ['Pintura Classica', 'Azul', 1857],
    ['Pintura Medieval', 'Vermelha', 1867],
    ['Pintura Moderna', 'Verde', 1897]
]


def eh_antiguidade(pintura):
    if pintura[2] < 1890:  # para o index 2 de cada lista...
        return True
    else:
        return False


# filtra funcao usando o parametro pinturas
pintura_antiga = list(filter(eh_antiguidade, pinturas))
print(f'42. filter: {pintura_antiga}')


# DESAFIO
# Usando a lista abaixo, filtre apenas as vagas com salário acima de R$2500
vagas = [
    ['vaga 1', 1200],
    ['vaga 2', 2550],
    ['vaga 3', 5000]
]


def verificar_salario(salario):
    if salario[1] > 2500:
        return True


salario = list(filter(verificar_salario, vagas))
print(f'43. desafio filter: {salario}')


# 5.14 - Sets --> ln: 315


# 44. removendo itens repetidos de uma lista com set()
numeros = [2, 2, 5, 8]
frutas = ['maca', 'uva', 'banana', 'maca', 'morango']

set_numeros = set(numeros)
set_frutas = set(frutas)

print(f'\n44. set: {set_numeros}')
print(f'45. set: {set_frutas}')

# NOTE:
# a funcao set() transforma a lista em um dicionario{}, cujo valor dos itens 
# contidos nao podem ser duplicados, como no exemplo, numero 2 e maca.

# 46. comparando itens unicos entre listas
numeros_1 = [2, 2, 5, 8]
numeros_2 = [2, 3, 2, 9]

a = set(numeros_1)
b = set(numeros_2)

# comparando . symmetric_difference ( comparado )
print(f'46. set diferença: {a.symmetric_difference(b)}')
