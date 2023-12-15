# 202312 - Python 3.12.0
# 5.17 - Como salvar informações em um arquivo [Pesquisar, Salvar, Editar, 
# Excluir]


'''
'w'  -> escreve         write
'a'  -> acrescenta      append
'r'  -> lê              read
'r+' -> lê e escreve    read add
'''

import os


# criando arquivo
with open('assets/test.txt', 'w') as arquivo:
    # arquivo.write('test 1')
    pass


# adicionando conteudo em arquivo existente
with open('assets/test.txt', 'a') as arquivo:
    # arquivo.write('usando ammend')
    pass


# adicionando conteudo com quebra de linha
nomes = ['lucas', 'carol', 'jeff', 'douglas']

with open('assets/test-nomes.txt', 'a', newline='') as arquivo:
    for nome in nomes:
        # arquivo.write(nome + os.linesep)
        pass

# NOTE:
# newline='' = serve para pular para linha posterior, sem isso o programa 
#              escreve jincluindo uma linha vazia entre os valores. 


# adicionando numeros -> converter para string
numeros = [1, 2, 3, 4, 5, 6]

with open('assets/test-numeros.txt', 'a', newline='') as arquivo:
    for numero in numeros:
        # arquivo.write(str(numero) + os.linesep)
        pass


# lendo arquivos
with open('assets/test-nomes.txt', 'r') as arquivo:
    for linha in arquivo:
        # print(linha.strip())
        pass

# NOTE:
# .strip() = serve para remover linha vazia entre cada leitura feita, 
#            automaticamente o Python adiciona \n em cada leitura em linha.


# DESAFIO 
# Manipulação de Arquivos
import os


# 3 listas
frutas = ['maçã', 'laranja', 'melancia', 'uva', 'banana']
cores = ['vermelho', 'amarelo', 'verde', 'azul', 'preto']
linguagens = ['python', 'java', 'rust', 'php', 'c']


# Desafio 1 - Crie um novo arquivo chamado frutas.txt e insira dentro dele
# todos as 5 frutas que estão na lista de frutas
nome_arquivo = 'frutas.txt'
local_arquivo = 'assets'
arquivo_txt = os.path.join(local_arquivo, nome_arquivo)

with open(arquivo_txt, 'w', encoding='utf-8', newline='') as arquivo:
    for i in frutas:
        arquivo.write(i + os.linesep)


# Desafio 2 - Imprima na tela todas as linhas que estao dentro do arquivo 
# frutas.txt
with open(arquivo_txt, 'r', encoding='utf-8') as arquivo:
    for linha in arquivo:
        print(linha.strip())


# Desafio 3 - Sem apagar os dados que já estão dentro de frutas.txt, adicione 
# todas as cores que estão dentro da sua lista de cores ao arquivos frutas.txt
with open(arquivo_txt, 'a', encoding='utf-8', newline='') as arquivo:
    for i in cores:
        arquivo.write(i + os.linesep)


# Desafio 4 - Crie um novo arquivo chamado 'Top 5 Linguagens.txt' e popule o 
# arquivo, de forma com que cada linuguagem ocupe apenas uma linha.
nome_arquivo = 'Top 5 Linguagens.txt'
local_arquivo = 'assets'
arquivo_txt = os.path.join(local_arquivo, nome_arquivo)

with open(arquivo_txt, 'w', encoding='utf-8', newline='') as arquivo:
    for i in linguagens:
        arquivo.write(i + os.linesep)


# BONUS - Como você poderia criar vários arquivos diferentes usando um laço for 
# e strings dinâmicos(f'{}'), e também não escrever nada dentro deles?
for i in range(5):
    arquivo_txt = os.path.join(local_arquivo, 'bonus')
    with open(f'{arquivo_txt}{i}.txt', 'w') as arquivo:
        pass
