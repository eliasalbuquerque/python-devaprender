# 202312 - Python 3.12.0
# 5.10 - Enumerate


# 1. descobrindo e usando o index da iteracao
lista = range(1, 5) # 1 ~ 4

# lista normal:
for numero in lista:
    print(f'1. {numero}')

# inserir mensagem de acordo com o index escolhido
for indice, numero in enumerate(lista, 0):
    print(f'2. {indice, numero}')
    if indice == 1:
        print(f'2. estamos na metade da lista')

# NOTE:
# no loop, o 0 é o numero que será inserido como indice do conjunto. Pode ser 
# usado qualquer valor para iniciar, porém, é recomendável a inicialização em 0.


# DESAFIO
# Itere sobre a lista abaixo exibindo o número do índice + nome da fruta. Porém
# quando o índice for 3 exiba 'Nº índice + nome da fruta EM PROMOÇÃO'

frutas = ['maça', 'laranja', 'morango', 'limao']

for indice, fruta in enumerate(frutas, 0):
    if indice < 3:
        print(f'{indice}: {fruta}')
    else:
        print(f'{indice}: {fruta} EM PROMOÇÃO')
