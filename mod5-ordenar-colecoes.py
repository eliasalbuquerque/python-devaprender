# 202312 - Python 3.12.0
# 5.11 - Como ordenadar coleções através de propriedades


# 1. ordenando uma lista de dicionarios
pessoas = [
    {'nome': 'John',
     'idade': 32,
     'nivel_acesso': 2},
    {'nome': 'Carol',
     'idade': 18,
     'nivel_acesso': 3},
    {'nome': 'Thomas',
     'idade': 45,
     'nivel_acesso': 5},
    {'nome': 'Amanda',
     'idade': 23,
     'nivel_acesso': 1},
]

from operator import itemgetter

pessoas.sort(key=itemgetter('nome'))
print(f'\n1. ordenar dicionario por chave "nome": \n{pessoas}') # Amanda, Carol, ...

pessoas.sort(key=itemgetter('nivel_acesso'))
print(f'\n2. ordenar dicionario por chave "nivel_acesso": \n{pessoas}') # Amanda, John, ...

# 3. ordenar uma lista de tuplas
produtos = [
    ('celular', 750),
    ('bicicleta', 1500),
    ('microfone', 550),
]
produtos.sort(key=itemgetter(1))
print(f'\n3. ordenar tupla por "index": \n{produtos}') # celular, microfone, ...

# 4. ordenar em ordem reversa
pessoas.sort(key=itemgetter('nome'), reverse=True)
produtos.sort(key=itemgetter(1), reverse=True)

print(f'\n4. ordem reversa dicionario: \n{pessoas}') # Thomas, John, ...
print(f'\n5. ordem reversa tupla: \n{produtos}') # bicicleta, celular, ...

# 6. ordenar matriz
matriz = [[5, 10], [15, 21], [1, 5]]
matriz.sort(key=itemgetter(1)) 
print(f'\n6. ordenar matriz por "index": \n{matriz}') # [1, 5], [5, 10], ...


# DESAFIOS
# D1. Ordene a lista de produtos abaixo pelo preço em ordem crescente
produtos = [
    {'nome': 'Celular',
     'preco': 1500},
    {'nome': 'Monitor',
     'preco': 500},
    {'nome': 'Microfone',
     'preco': 300}
]

produtos.sort(key=itemgetter('preco'))
print(f'\n{produtos}')


# D2. Ordene em ordem descrescente a lista de equipamento_filmagem por valor do equipamento
equipamento_filmagem = [
    ('Tripé', 300),
    ('Câmera', 1700),
    ('Iluminação', 200),
]

equipamento_filmagem.sort(key=itemgetter(1), reverse=True)
print(f'\n{equipamento_filmagem}')


# D3. Ordene em ordem crescente a cotacao_moedas com base no valor da moeda
cotacao_moedas = [['usd', 5.25], ['brl', 1.56], ['eur', 6.47]]

cotacao_moedas.sort(key=itemgetter(1))
print(f'\n{cotacao_moedas}')