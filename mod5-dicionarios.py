# 202312 - Python 3.12.0
# 5. 6 - Dicionarios


'''
Pessoa
    nome
    idade
    altura
'''

# 1. criando dicionario usando {chave: valor}
pessoas = [{'nome': 'Carol', 'idade': 18, 'altura': 1.52}, {'nome': 'Tulio', 'idade': 26, 'altura': 1.85}]
print(f'1. {pessoas}')

# 2. criando dicionario usando construtor
pessoas_2 = dict(nome='Lucia', idade=58, altura=1.50)
print(f'2. {pessoas_2}')

# 3. acessando dados do dicionario
print(f'3. {pessoas_2['nome']}')

# 4. mostrando todas as chaves disponiveis
print(f'4. {pessoas_2.keys()}')

# 5. mostrando todos os valores disponiveis
print(f'5. {pessoas_2.values()}')

# 6. mostrando todos os itens (chave, valor)
print(f'6. {pessoas_2.items()}')

# 7. iterar sobre um dicionario
for item in pessoas_2.items():
    print(f'7. {item[1]}')
