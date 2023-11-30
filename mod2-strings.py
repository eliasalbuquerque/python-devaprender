# 202311 - Python 3.12.0
# 2 - Como receber e trabalhar com dados

# 2.4 - Strings
# DESAFIO
print('Vamos codar!')
print("Vamos 'codar!'")
print("Vamos \n'codar!'")


# 2.5 - Strings dinamicas = f'{}'
# String dinamica
nome = 'rafael'
email = 'rafael@gmail.com'
print(f'Ola {nome}, voce cadastrou o email {email}, essa informacao esta correta?')

# ​Desafio 1
## Crie os seguinte strings dinâmicos
nome = 'Carol'
hobby = 'ouvir Música'
# Resultado
# 'Olá sou a Carol e gosto de ouvir musica'
print(f'Olá sou a {nome} e gosto de {hobby}')

# Desafio 2
## Monte a seguintes palavras, usando as sílabas como base
b = 'ba'
parte2 = 'nica'
a = 'a'
r = 'ri'
parte1 = 'eletrô'
t = 'te'
# Resultado
# 'bateria eletrônica'
print(f'{b}{t}{r}{a} {parte1}{parte2}')


# 2.6 - Métodos comuns de um string
nome_curso = '  Edição de Vídeo  '
print('a', nome_curso.upper())
print('b', nome_curso.lower())
print('c', nome_curso.strip())
print('d', nome_curso.lstrip())
print('e', nome_curso.rstrip())
print('f', nome_curso.find('ção'))
print('g', nome_curso.replace('Vídeo', 'Música'))
print('h', 'https://www.olx.com.br/estado-sp?q=relogios'.replace('relogios', 'carros'))

# DESAFIO 
# Através da criação de string dinâmicos e os métodos de um string que acabou de aprender, use como base as variáveis a seguir para criar as seguintes frases
a = 'é'
b = 'MELHOR'
c = 'QUE'
d = 'feito'
e = 'perfeito'
# Resultado
# 'É melhor FEITO que PERFEITO'
print(f'{a.upper()} {b.lower()} {d.upper()} {c.lower()} {e.upper()}')


# 2.7 - Slice (extraindo partes de um string)
a = 'Teclado'
print(a[2]) #c
print(a[4]) #a

b = 'Acessar o último caractere de uma string'
print(b[-1]) #g

c = 'Index'
print(c.index('d')) #2

link = 'facebook.com/devaprender'
print('a)', link[0]) #f
print('b)', link[-1]) #r
print('c)', link[0:5]) #faceb --> exclude last
print('d)', link[0:]) #facebook.com/devaprender
print('e)', link[-5:]) #ender
print('f)', link[5:]) #ook.com/devaprender
print('g)', link[:-5]) #facebook.com/devapr

frase = 'Clean Code'
print(frase.rindex('C')) #6 --> right to left

# DESAFIO 1
# Desafio 1 Encontre o índice de 'o' dentro da variável biblioteca
biblioteca = 'Biblioteca'
print(biblioteca.index('o')) #5

# Desafio 2
# Usando a frase
frase = 'Desenvolvimento De Aplicações'
# Imprima apenas a palavra 'De Aplicações'
print(frase[frase.rindex('D'):])


# 2.8 - Split e Join
frase = 'Olá, bem-vindo a este treinamento!'
print(frase.split()) #separa por espacos
print(frase.split(',')) #separa por caractere
print(frase.split('-')) #separa por caractere

nomes = 'jhonatan, rafael, carol, amanda, jefferson'
print(nomes.split()) 
print(nomes.split(','))

hashtags = '#music #guitar #gamer #coder #python'
print(hashtags.split())
print(hashtags.split('#'))
print(hashtags.split('#', 2)) #separa por caractere do index 0 ao 1, o 2 é o resto da string

# Concatenacao
# Separar string
hashtags_separadas = hashtags.split(' ')
print(hashtags_separadas)
# Concatenar strings
print(','.join(hashtags_separadas))
print('.'.join(hashtags_separadas))
print(' '.join(hashtags_separadas))

# ​Desafio 1: Transforme a frase1 em uma lista de palavras e guarde o resultado 
# em uma variável chamada palavras1
# Desafio 2: Transforme a frase2 em uma lista de palavras e guarde o resultado 
# em uma variável chamada palavras2
# Desafio 3: Pegue o palavras1 e transforme elas no seguinte string: 
# "Desafio,manipulação,de,strings". Imprima o resultado no console.
# Desafio 4: Pegue o palavras2 e transforme elas no seguinte string: 
# frase2 = "jhonatan & rafael & carol & camilla". Imprima o resultado no 
# console.

frase1 = 'Desafio manipulação de strings'
frase2 = 'jhonatan,rafael,carol,camilla'

palavras1 = frase1.split()
palavras2 = frase2.split(',')
print(','.join(palavras1))
print(' & '.join(palavras2))
