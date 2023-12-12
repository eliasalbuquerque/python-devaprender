# 202312 - Python 3.12.0
# 4.2 - Function, Agora você entende! --> ln: 9
# 4.3 - Processar VS retornar(O que é e como usar return) --> ln: 60
# 4.4 - Argumentos posicionais VS Argumentos nomeados --> ln: 85
# 4.5 - Args - Funções com n° de argumentos dinâmicos --> ln: 132
# 4.6 - Kwargs - Funções com n° de argumentos nomeados dinâmicos --> 148



# 4.2 - Function, Agora você entende!



# 1. funcao sem parametros
def hello_world():
    print('1. Hello World!')

hello_world()


# 2. funcao com argumento (recebe um parametro)
def hello_personal(nome):
    print(f'2. Bem-vindo(a) {nome}')

hello_personal('Elias')
# nome = input('2. Qual é o seu nome: ')
# hello_personal(nome)


# 3. funcao com valor padrao definido
# com mais de um argumento, o padrao deve estar por ultimo
def apresentar_lugar(lugar='nossa loja'):
    print(f'3. Conheça {lugar}')

apresentar_lugar()
apresentar_lugar('Disney')


# DESAFIO 1
# Crie uma função chamada gerar_nome_completo que recebe como 
# parâmetro o nome e sobrenome de alguém e dá boas vindas para essa pessoa
def gerar_nome_completo(nome, sobrenome):
    print(f'4. Boas vindas {nome} {sobrenome}')

gerar_nome_completo('Elias', 'Albuquerque')


# DESAFIO 2
# Crie uma função chamada calcular_valores que recebe 2 parâmetros o primeiro o 
# preco de um produto e o segundo parâmetro é a quantidade, porém a quantidade 
# deve haver um valor padrão de 1. Sua função deve exibir o resultado do preço 
# do produto, multiplicado a quantidade escolhida.
def calcular_valores(preco, quantidade=1):
    produto = float(preco * quantidade)
    print(f'5. O valor do preço total para {quantidade} unidades é R${produto:.2f}')

calcular_valores(50,3)



# 4.3 - Processar VS retornar (O que é e como usar return)



# vai precisar usar essa informacao no programa ou soh preciso processar esse 
# dado nesse momento e nao utilizarei mais?

# 6. processar
def exibir_cotacao(moeda='usd'):
    if moeda == 'usd':
        print('6. Processar: 5.47')

exibir_cotacao()

# 7. retornar
def exibir_cotacao(moeda='usd'):
    if moeda == 'usd':
        return '7. Retorna: 5.47'

cotacao = exibir_cotacao()

print(cotacao)



# 4.4 - Argumentos posicionais VS Argumentos nomeados



def exibir_preco(sequencia, nome_produto, preco):
    print(f'{sequencia}. {nome_produto} está no valor de: ${preco}')

# 8. argumentos posicionais
exibir_preco(8, 'Iphone 15 pro', 999) # 8.
exibir_preco(9, 999, 'Iphone 15 pro') # 9.

# 10. argumentos nomeados
exibir_preco(sequencia=10, nome_produto='Iphone 15 pro', preco=999)  # 10.
exibir_preco(nome_produto='Iphone 15 pro', preco=999, sequencia=11)  # 11.

# NOTE:
# * Argumentos nomeados direciona o valor do parametro direto para o argumento;
# * Argumentos posicionais dependem da sequencia certa de parametros/argumentos
#   para funcionar adequadamente;
# * Para argumentos nomeados, ha a possibilidade de obrigar o uso usando '*'  
#   antes do argumento obrigatorio;

# 12. argumentos nomeados obrigatorios
def exibir_preco(sequencia, nome_produto, *, preco):
    print(f'{sequencia}. {nome_produto} está no valor de: ${preco}')

# exibir_preco(12, 'Iphone 15 pro', 999) # 12. --> Traceback
exibir_preco(12, 'Iphone 15 pro', preco=999) # 12.


# DESAFIO

# Crie uma função chamado gerar_objeto_personalizado que irá receber 3 
# parâmetros, cor, altura, formato.
# A sua função deve apenas imprimir na tela o que foi passado para ela, nada 
# mais, nada menos.
# Porém ela deve seguir as seguintes regras:
# 1 - O primeiro argumento deve ser posicional
# 2 - Os argumentos altura e formato precisam OBRIGATORIAMENTE serem nomeados

def gerar_objeto_personalizado(cor, *, altura, formato):
    print(f'13. {cor}, {altura}, {formato}')

gerar_objeto_personalizado('vermelho', altura=50, formato='quadrado')



# 4.5 - Args - Funções com n° de argumentos dinâmicos



# 15. *args = Tupla
# quantidade ilimitada de argumentos posicionais
def somar(*valores, b):
    print(f'14. {valores}')
    for valor in valores:
        b += valor
    print(f'15. {b}')

somar(10, 20, 5, b=5)



# 4.6 - Kwargs - Funções com n° de argumentos nomeados dinâmicos



# 16. **kwargs (keyword arguments)
# quantidade ilimitada de argumentos nomeados
def concatenar(**palavras):
    frase = ''
    for palavra in palavras.values():
        frase += palavra + ' '
    print(f'16. {frase}')

concatenar(a='Eu', b='sou', c='desenvolvedor', d='de', e='software')

# posicional, ilimitado posicional, ilimitado nomeado
def fazer_calculo(nome, *args, **kwargs):
    print(f'17. arg pos: {nome}')
    print(f'18. arg ilim pos: {args}')
    print(f'19. arg ilim nom: {kwargs}')

    for arg in args:
        print(f'*args: {arg}')

    for kwarg in kwargs:
        print(f'**kwargs: {kwarg}')
    
    for kwarg in kwargs.values():
        print(f'**kwargs-value: {kwarg}')

fazer_calculo('Elias', 10, 9, 8, a=1, b=2, c=3)
