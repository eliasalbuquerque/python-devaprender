# 202312 - Python 3.12.0
# 5.15.1 - O que são e como ler arquivos JSON   --> ln: 6
# 5.15.2 - Como criar e ler arquivos JSON       --> ln: 93


# 5.15.1 - O que são e como ler arquivos JSON


import os
import json


# JSON = Javascript Object Notation
usuarios1 = 'json-files/usuarios1.json'
usuarios2 = 'json-files/usuarios2.json'
usuarios3 = 'json-files/usuarios3.json'
usuarios4 = 'json-files/usuarios4.json'
usuarios5 = 'json-files/usuarios5.json'


# usuarios1.json: nome da carol
# abrir arquivo json e utf-8 para caracteres especiais
with open(usuarios1, encoding='utf-8') as arquivo_json:

    # importa os dados do arquivo json em uma string
    data = json.load(arquivo_json)

    # 1. lista todos as chaves do dicionario json
    keys = list(data.keys())
    print(f'\narquivo usuarios1.json\n1. chaves: {keys}')

    # 3. imprime o valor contido na chave 'nome'
    print(f'2. item: {data['nome']}')


# usuarios2.json: permissao intermediaria
with open(usuarios2, encoding='utf-8') as arquivo_json:
    data = json.load(arquivo_json)
    keys = list(data.keys())
    print(f'\narquivo usuarios2.json\n3. chaves: {keys}')

    # 4. acessando elemento da lista dentro do dicionario (chave, indice)
    item_lista = data['permissões'][1]
    print(f'4. item: {item_lista}')


# usuarios3.json:
with open(usuarios3, encoding='utf-8') as arquivo_json:
    data = json.load(arquivo_json)

    # 5. telefone da carol
    print(f'\narquivo usuarios3.json')
    print(f'5. item: {data['usuários'][0]['telefone']}')

    # 6. douglas é admin?
    print(f'6. item: {data['usuários'][1]['admin']}')

    # 7. permissoes de douglas
    print(f'7. item: {data['usuários'][1]['permissões']}')


# usuarios4.json:
with open(usuarios4, encoding='utf-8') as arquivo_json:
    data = json.load(arquivo_json)

    # 8. preco do plano da carol
    print(f'\narquivo usuarios4.json')
    print(f'8. item: {data['usuários'][0]['plano']['preco']}')


# usuarios5.json:
with open(usuarios5, encoding='utf-8') as arquivo_json:
    data = json.load(arquivo_json)

    # 9. carol é admin?
    print(f'\narquivo usuarios5.json')
    print(f'9. item: {data[0]['admin']}\n')


# DESAFIO
# Imprimir o e-mail do usuário com id 2
# imprimir a city do usuário com id 1
# Imprimir o total do pedido do usuário com id 2

print('DESAFIO 1')

desafio = 'json-files/desafio.json'

with open(desafio, encoding='utf-8') as arquivo_json:
    data = json.load(arquivo_json)
    print(data['user'][1]['email'])
    print(data['user'][0]['address']['city'])
    print(data['user'][1]['orders'][0]['total'])



# 5.15.2 - Como criar e ler arquivos JSON



def caminho_arquivo_json(file_name):
    folder_path = 'json-files'
    return os.path.join(folder_path, f'{file_name}.json')


def criando_arquivo_json():
    arquivo = caminho_arquivo_json(nome_arquivo_json)
    with open(arquivo, 'w', encoding='utf-8') as arquivo_json:
        return json.dump(data, arquivo_json, indent=4, ensure_ascii=False)


def lendo_arquivo_json():
    arquivo = caminho_arquivo_json(nome_arquivo_json)
    with open(arquivo, encoding='utf-8') as arquivo_json:
        return json.load(arquivo_json)  # json -> dicionario


# 1. JSON A PARTIR DE UM DICIONARIO:
notebook = {"marca": "Dell", "preço": "15000"}
data = notebook
nome_arquivo_json = 'notebook-dell'
criando_arquivo_json()


# 2. JSON A PARTIR DE UMA STRING
notebook2 = '{"marca":"Lenovo", "preço":"17000"}'
nome_arquivo_json = 'notebook-lenovo'

# converter string para dicionario
data = json.loads(notebook2)
criando_arquivo_json()


# 3. LENDO OS ARQUIVOS JSON
nome_arquivo_json = 'notebook-dell'
dicionario_json = lendo_arquivo_json()

print(f'\n10. lendo json: {dicionario_json['marca']}')

nome_arquivo_json = 'notebook-lenovo'
dicionario_json = lendo_arquivo_json()

print(f'11. lendo json: {dicionario_json['marca']}')


# DESAFIO 2


def local_arquivo_json(nome_arquivo):
    nome_da_pasta = 'json-files'
    return os.path.join(nome_da_pasta, f'{nome_arquivo}.json')


def gerando_arquivo_json(dicionario, nome_arquivo_json):
    arquivo = local_arquivo_json(nome_arquivo_json)
    with open(arquivo, 'w', encoding='utf-8') as arquivo_json:
        return json.dump(data, arquivo_json, indent=4, ensure_ascii=False)


def lendo_arquivo(nome_arquivo_json):
    arquivo = local_arquivo_json(nome_arquivo_json)
    with open(arquivo, encoding='utf-8') as arquivo_json:
        return json.load(arquivo_json)


# string para conversao em json
string_para_json = '{"name" : "John Smith", "age" : 30, "city" : "New York", "isStudent" : true, "gpa" : 3.5}'

# converter string para dicionario
data = json.loads(string_para_json)

# argumentos:
# 1. conversao da string para o dicionario, ou o dicionario direto
# 2. nome do arquivo json a ser salvo em formato string
gerando_arquivo_json(data, 'desafio2')

# argumentos:
# 1. nome do arquivo a ser lido sem a extensão (.json)
arquivo = lendo_arquivo('desafio2')
print('\nDESAFIO 2')
print(f'12. lendo json: {arquivo['isStudent']}')